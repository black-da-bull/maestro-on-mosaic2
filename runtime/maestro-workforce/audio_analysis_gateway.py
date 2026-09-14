"""Fail-closed gateway for Maestro v0.5 audio-analysis workers.

This module deliberately contains no MIR/model dependencies. Vercel validates provenance
and authority boundaries, then hands work to an external durable worker. Experimental
results remain evidence and cannot mutate Technical UST or promote renderer policy.
"""
from __future__ import annotations

import json
import os
import re
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, quote, urlparse
from urllib.request import Request, urlopen

SCHEMA_VERSION = "maestro.audio.gateway.v0.5"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
JOB_ID_RE = re.compile(r"^[A-Za-z0-9._:-]{1,200}$")
MAX_REQUEST_BYTES = 64 * 1024
MAX_CONTEXT_BYTES = 16 * 1024
MAX_WORKER_RESPONSE_BYTES = 2 * 1024 * 1024

ADAPTERS: dict[str, dict[str, Any]] = {
    "beat_this": {"role": "beat_downbeat_tempo", "execution": "external_worker", "evidence_class": "model_inference"},
    "songformer": {"role": "structure_sections", "execution": "external_worker", "evidence_class": "model_inference"},
    "chordmini": {"role": "harmony_chords", "execution": "external_worker", "evidence_class": "model_inference"},
    "basic_pitch": {"role": "lightweight_amt", "execution": "external_worker", "evidence_class": "model_inference"},
    "advanced_amt": {"role": "instrument_agnostic_amt", "execution": "external_worker", "evidence_class": "model_inference"},
    "clap": {"role": "text_audio_embedding", "execution": "external_worker", "evidence_class": "model_inference"},
    "audio_language": {"role": "evidence_reasoning", "execution": "external_worker", "evidence_class": "advisory_inference"},
    "statistical_embedding": {"role": "non_semantic_descriptor_baseline", "execution": "external_worker", "evidence_class": "derived_measurement"},
}

AUTHORITY = {
    "technical_ust_mutation": False,
    "canon_promotion": False,
    "renderer_policy_promotion": False,
    "keeper_or_release_approval": False,
    "operator_decision_required": True,
}

JOB_STATUSES = {"queued", "running", "completed", "failed"}
RESULT_STATUSES = {"completed", "failed", "not_configured", "unavailable"}


class GatewayValidationError(ValueError):
    pass


class WorkerUnavailable(RuntimeError):
    pass


class WorkerProtocolError(RuntimeError):
    pass


def _strict_object(value: Any, *, allowed: set[str], required: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise GatewayValidationError(f"{label}_must_be_object")
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise GatewayValidationError(f"{label}_unknown_fields:{','.join(unknown)}")
    missing = sorted(k for k in required if k not in value)
    if missing:
        raise GatewayValidationError(f"{label}_missing_fields:{','.join(missing)}")
    return value


def _require_text(value: Any, name: str, *, max_len: int = 12000, allow_empty: bool = False) -> str:
    if not isinstance(value, str):
        raise GatewayValidationError(f"{name}_must_be_string")
    text = value.strip()
    if not allow_empty and not text:
        raise GatewayValidationError(f"{name}_required")
    if len(value) > max_len:
        raise GatewayValidationError(f"{name}_too_long")
    return value


def _require_sha(value: Any, name: str = "source_sha256") -> str:
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise GatewayValidationError(f"{name}_must_be_lowercase_sha256")
    return value


def _logical_ref(value: Any, name: str, *, max_len: int) -> str:
    ref = _require_text(value, name, max_len=max_len)
    lower = ref.lower()
    if "://" in lower or lower.startswith(("file:", "data:")) or ".." in ref or "\\" in ref or ref.startswith("/"):
        raise GatewayValidationError(f"{name}_must_be_logical_artifact_reference")
    return ref


def _bounded_json_object(value: Any, name: str, *, max_bytes: int) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise GatewayValidationError(f"{name}_must_be_object")
    try:
        encoded = json.dumps(value, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise GatewayValidationError(f"{name}_must_be_json_serializable") from exc
    if len(encoded) > max_bytes:
        raise GatewayValidationError(f"{name}_too_large")
    return value


def _worker_base_url() -> str:
    base = os.environ.get("MAESTRO_AUDIO_WORKER_URL", "").strip().rstrip("/")
    if not base:
        raise WorkerUnavailable("audio_worker_not_configured")
    parsed = urlparse(base)
    local_http = parsed.scheme == "http" and parsed.hostname in {"localhost", "127.0.0.1", "::1"}
    if parsed.scheme != "https" and not local_http:
        raise WorkerUnavailable("audio_worker_url_must_use_https")
    if not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise WorkerUnavailable("audio_worker_url_invalid")
    return base


def capabilities() -> dict[str, Any]:
    configured = bool(os.environ.get("MAESTRO_AUDIO_WORKER_URL", "").strip())
    return {
        "schema": SCHEMA_VERSION,
        "authority": AUTHORITY.copy(),
        "worker": {
            "configured": configured,
            "transport": "external_durable_job_worker",
            "inline_heavy_inference": False,
        },
        "adapters": [{"id": key, **value} for key, value in ADAPTERS.items()],
        "learning_lifecycle": ["observation", "candidate_heuristic", "validated_heuristic", "renderer_policy"],
        "auto_promotion": False,
    }


def validate_job_request(payload: Any) -> dict[str, Any]:
    data = _strict_object(
        payload,
        allowed={"project_id", "source_ref", "source_sha256", "deterministic_analysis_id", "adapters", "context"},
        required={"project_id", "source_ref", "source_sha256", "deterministic_analysis_id", "adapters"},
        label="audio_job",
    )
    project_id = _logical_ref(data["project_id"], "project_id", max_len=300)
    source_ref = _logical_ref(data["source_ref"], "source_ref", max_len=1000)
    source_sha = _require_sha(data["source_sha256"])
    deterministic_id = _logical_ref(data["deterministic_analysis_id"], "deterministic_analysis_id", max_len=500)
    adapters = data["adapters"]
    if not isinstance(adapters, list) or not adapters:
        raise GatewayValidationError("adapters_must_be_nonempty_list")
    clean: list[str] = []
    for item in adapters:
        if not isinstance(item, str) or item not in ADAPTERS:
            raise GatewayValidationError(f"unknown_adapter:{item}")
        if item not in clean:
            clean.append(item)
    context = _bounded_json_object(data.get("context") or {}, "context", max_bytes=MAX_CONTEXT_BYTES)
    return {
        "schema": SCHEMA_VERSION,
        "project_id": project_id,
        "source_ref": source_ref,
        "source_sha256": source_sha,
        "deterministic_analysis_id": deterministic_id,
        "adapters": clean,
        "context": context,
        "authority": AUTHORITY.copy(),
    }


def validate_renderer_record(kind: str, record: Any) -> dict[str, Any]:
    if kind == "renderer_experiment":
        allowed = {
            "objective", "starting_state", "lyric_prompt", "style_prompt", "studio_instruction", "suno_response",
            "generation_settings", "reference_artifact_ids", "generated_artifact_ids", "analysis_ids",
            "controlled_variables", "held_constant", "lesson_candidate", "causal_claim_authorized",
        }
        data = _strict_object(record, allowed=allowed, required={"objective", "generation_settings"}, label=kind)
        _require_text(data["objective"], "objective")
        _bounded_json_object(data["generation_settings"], "generation_settings", max_bytes=MAX_CONTEXT_BYTES)
        if data.get("causal_claim_authorized", False) is not False:
            raise GatewayValidationError("causal_claim_authorized_must_be_false")
        surfaces = [data.get("lyric_prompt", ""), data.get("style_prompt", ""), data.get("studio_instruction", "")]
        if not any(isinstance(x, str) and x.strip() for x in surfaces):
            raise GatewayValidationError("experiment_requires_renderer_input_surface")
    elif kind == "operator_assessment":
        allowed = {"experiment_artifact_id", "decision", "notes", "blind_listening", "loudness_matched", "preferred_artifact_id", "criteria"}
        data = _strict_object(record, allowed=allowed, required={"experiment_artifact_id", "decision", "notes"}, label=kind)
        _logical_ref(data["experiment_artifact_id"], "experiment_artifact_id", max_len=500)
        if data["decision"] not in {"keep", "reject", "redirect", "neutral"}:
            raise GatewayValidationError("invalid_operator_decision")
        _require_text(data["notes"], "notes")
    elif kind == "renderer_heuristic":
        allowed = {"statement", "status", "model_version_scope", "experiment_artifact_ids", "rationale", "operator_confirmed", "reversible", "supersedes_artifact_id"}
        data = _strict_object(record, allowed=allowed, required={"statement", "status", "model_version_scope", "experiment_artifact_ids", "rationale"}, label=kind)
        _require_text(data["statement"], "statement")
        _require_text(data["model_version_scope"], "model_version_scope", max_len=500)
        _require_text(data["rationale"], "rationale")
        if data["status"] not in {"observation", "candidate_heuristic", "validated_heuristic", "renderer_policy"}:
            raise GatewayValidationError("invalid_heuristic_status")
        ids = data["experiment_artifact_ids"]
        if not isinstance(ids, list) or not ids:
            raise GatewayValidationError("experiment_artifact_ids_must_be_nonempty_string_list")
        for artifact_id in ids:
            _logical_ref(artifact_id, "experiment_artifact_id", max_len=500)
        operator_confirmed = data.get("operator_confirmed", False)
        if data["status"] != "observation" and operator_confirmed is not True:
            raise GatewayValidationError("heuristic_promotion_requires_operator_confirmation")
        if data["status"] == "renderer_policy" and data.get("reversible", True) is not True:
            raise GatewayValidationError("renderer_policy_must_be_reversible")
    else:
        raise GatewayValidationError("unknown_renderer_record_kind")
    return {
        "accepted_as": f"maestro.{kind}.v0.5",
        "record": data,
        "authority": AUTHORITY.copy(),
        "auto_promotion": False,
    }


def _validate_result(result: Any, source_sha256: str) -> dict[str, Any]:
    if not isinstance(result, dict):
        raise WorkerProtocolError("adapter_result_must_be_object")
    allowed = {"adapter_id", "status", "schema", "output", "confidence", "provenance", "warnings", "error"}
    unknown = sorted(set(result) - allowed)
    if unknown:
        raise WorkerProtocolError(f"adapter_result_unknown_fields:{','.join(unknown)}")
    required = {"adapter_id", "status", "schema", "provenance"}
    missing = sorted(required - set(result))
    if missing:
        raise WorkerProtocolError(f"adapter_result_missing_fields:{','.join(missing)}")
    data = dict(result)
    adapter_id = data["adapter_id"]
    if not isinstance(adapter_id, str) or adapter_id not in ADAPTERS:
        raise WorkerProtocolError(f"audio_worker_unknown_adapter_result:{adapter_id}")
    if data["status"] not in RESULT_STATUSES:
        raise WorkerProtocolError("audio_worker_invalid_adapter_status")
    if not isinstance(data["schema"], str) or not data["schema"].strip():
        raise WorkerProtocolError("audio_worker_result_schema_required")
    warnings = data.get("warnings", [])
    if not isinstance(warnings, list) or not all(isinstance(x, str) for x in warnings):
        raise WorkerProtocolError("audio_worker_result_warnings_invalid")
    provenance = data["provenance"]
    if not isinstance(provenance, dict):
        raise WorkerProtocolError("audio_worker_result_provenance_required")
    required_provenance = {"source_sha256", "implementation", "implementation_version"}
    if not required_provenance.issubset(provenance):
        raise WorkerProtocolError("audio_worker_result_provenance_incomplete")
    if provenance.get("source_sha256") != source_sha256:
        raise WorkerProtocolError("audio_worker_result_source_identity_mismatch")
    if data["status"] == "completed" and not isinstance(data.get("output"), dict):
        raise WorkerProtocolError("audio_worker_completed_result_requires_object_output")
    if data["status"] == "failed" and not isinstance(data.get("error"), str):
        raise WorkerProtocolError("audio_worker_failed_result_requires_error")
    evidence_class = provenance.get("evidence_class")
    if evidence_class is not None and evidence_class != ADAPTERS[adapter_id]["evidence_class"]:
        raise WorkerProtocolError("audio_worker_result_evidence_class_mismatch")
    return data


def _validate_job_response(response: Any, *, require_identity: bool, expected_job_id: str | None = None) -> dict[str, Any]:
    if not isinstance(response, dict):
        raise WorkerProtocolError("audio_worker_response_must_be_object")
    allowed = {"job_id", "status", "source_sha256", "adapters", "results", "error", "created_at", "updated_at", "completed_at"}
    unknown = sorted(set(response) - allowed)
    if unknown:
        raise WorkerProtocolError(f"audio_worker_response_unknown_fields:{','.join(unknown)}")
    job_id = response.get("job_id")
    status = response.get("status")
    if not isinstance(job_id, str) or not JOB_ID_RE.fullmatch(job_id):
        raise WorkerProtocolError("audio_worker_invalid_job_id")
    if expected_job_id is not None and job_id != expected_job_id:
        raise WorkerProtocolError("audio_worker_job_id_mismatch")
    if status not in JOB_STATUSES:
        raise WorkerProtocolError("audio_worker_invalid_job_status")
    if not require_identity:
        return {"job_id": job_id, "status": status}
    source_sha = response.get("source_sha256")
    try:
        _require_sha(source_sha)
    except GatewayValidationError as exc:
        raise WorkerProtocolError("audio_worker_source_sha256_invalid") from exc
    adapters = response.get("adapters")
    if not isinstance(adapters, list) or not adapters or not all(isinstance(x, str) and x in ADAPTERS for x in adapters):
        raise WorkerProtocolError("audio_worker_adapters_invalid")
    if len(set(adapters)) != len(adapters):
        raise WorkerProtocolError("audio_worker_adapters_duplicate")
    results_raw = response.get("results", [])
    if not isinstance(results_raw, list):
        raise WorkerProtocolError("audio_worker_results_must_be_list")
    results = [_validate_result(item, source_sha) for item in results_raw]
    result_ids = [item["adapter_id"] for item in results]
    if len(set(result_ids)) != len(result_ids):
        raise WorkerProtocolError("audio_worker_duplicate_adapter_results")
    if status == "completed" and set(result_ids) != set(adapters):
        raise WorkerProtocolError("audio_worker_completed_results_do_not_cover_adapters")
    if status in {"queued", "running"} and results:
        raise WorkerProtocolError("audio_worker_incomplete_job_must_not_publish_results")
    if status == "failed" and not isinstance(response.get("error"), str):
        raise WorkerProtocolError("audio_worker_failed_job_requires_error")
    normalized = dict(response)
    normalized["results"] = results
    return normalized


def _default_transport(method: str, url: str, payload: dict[str, Any] | None, token: str | None) -> dict[str, Any]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {"Accept": "application/json"}
    if body is not None:
        headers["Content-Type"] = "application/json"
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, data=body, headers=headers, method=method)
    try:
        with urlopen(request, timeout=20) as response:
            raw = response.read(MAX_WORKER_RESPONSE_BYTES + 1)
    except (HTTPError, URLError, TimeoutError) as exc:
        raise WorkerUnavailable(f"audio_worker_request_failed:{exc.__class__.__name__}") from exc
    if len(raw) > MAX_WORKER_RESPONSE_BYTES:
        raise WorkerProtocolError("audio_worker_response_too_large")
    try:
        parsed = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise WorkerProtocolError("audio_worker_invalid_json") from exc
    if not isinstance(parsed, dict):
        raise WorkerProtocolError("audio_worker_response_must_be_object")
    return parsed


def submit_job(payload: Any, *, transport: Callable[[str, str, dict[str, Any] | None, str | None], dict[str, Any]] | None = None) -> dict[str, Any]:
    request_payload = validate_job_request(payload)
    base = _worker_base_url()
    token = os.environ.get("MAESTRO_AUDIO_WORKER_TOKEN")
    response = (transport or _default_transport)("POST", f"{base}/v1/jobs", request_payload, token)
    worker = _validate_job_response(response, require_identity=False)
    return {
        "schema": SCHEMA_VERSION,
        "job_id": worker["job_id"],
        "status": worker["status"],
        "source_sha256": request_payload["source_sha256"],
        "adapters": request_payload["adapters"],
        "authority": AUTHORITY.copy(),
    }


def get_job(job_id: str, *, transport: Callable[[str, str, dict[str, Any] | None, str | None], dict[str, Any]] | None = None) -> dict[str, Any]:
    if not JOB_ID_RE.fullmatch(job_id or ""):
        raise GatewayValidationError("invalid_job_id")
    base = _worker_base_url()
    token = os.environ.get("MAESTRO_AUDIO_WORKER_TOKEN")
    response = (transport or _default_transport)("GET", f"{base}/v1/jobs/{quote(job_id, safe='._:-')}", None, token)
    normalized = _validate_job_response(response, require_identity=True, expected_job_id=job_id)
    normalized["authority"] = AUTHORITY.copy()
    normalized["canon_promotion"] = False
    normalized["auto_promotion"] = False
    return normalized


def _read_json(environ) -> dict[str, Any]:
    try:
        length = int(environ.get("CONTENT_LENGTH") or 0)
    except ValueError:
        length = 0
    if length < 0 or length > MAX_REQUEST_BYTES:
        raise GatewayValidationError("request_body_too_large")
    raw = environ["wsgi.input"].read(length) if length else b"{}"
    value = json.loads(raw.decode("utf-8")) if raw else {}
    if not isinstance(value, dict):
        raise GatewayValidationError("JSON_object_required")
    return value


def _json(start_response, status: str, payload: Any):
    body = json.dumps(payload, indent=2).encode("utf-8")
    start_response(status, [("Content-Type", "application/json; charset=utf-8"), ("Content-Length", str(len(body))), ("Cache-Control", "no-store")])
    return [body]


def handle_wsgi(environ, start_response):
    """Handle `/api/audio-analysis/*` and `/api/renderer-learning/*`; return None otherwise."""
    method = environ.get("REQUEST_METHOD", "GET").upper()
    path = environ.get("PATH_INFO", "/")
    if not (path.startswith("/api/audio-analysis/") or path.startswith("/api/renderer-learning/")):
        return None
    try:
        if method == "GET" and path == "/api/audio-analysis/capabilities":
            return _json(start_response, "200 OK", capabilities())
        if method == "POST" and path == "/api/audio-analysis/jobs":
            result = submit_job(_read_json(environ))
            code = "200 OK" if result["status"] == "completed" else "202 Accepted"
            return _json(start_response, code, result)
        if method == "GET" and path == "/api/audio-analysis/jobs":
            query = parse_qs(environ.get("QUERY_STRING", ""))
            job_id = (query.get("job_id") or [""])[0]
            return _json(start_response, "200 OK", get_job(job_id))
        if method == "POST" and path == "/api/renderer-learning/validate":
            data = _read_json(environ)
            data = _strict_object(data, allowed={"kind", "record"}, required={"kind", "record"}, label="renderer_record_request")
            return _json(start_response, "200 OK", validate_renderer_record(str(data["kind"]), data["record"]))
        return _json(start_response, "404 Not Found", {"error": "not found"})
    except GatewayValidationError as exc:
        return _json(start_response, "400 Bad Request", {"error": str(exc), "type": "validation"})
    except WorkerUnavailable as exc:
        return _json(start_response, "503 Service Unavailable", {"error": str(exc), "type": "worker_unavailable", "authority": AUTHORITY.copy()})
    except WorkerProtocolError as exc:
        return _json(start_response, "502 Bad Gateway", {"error": str(exc), "type": "worker_protocol", "authority": AUTHORITY.copy()})
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        return _json(start_response, "400 Bad Request", {"error": str(exc), "type": "validation"})
