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
from urllib.parse import parse_qs, quote
from urllib.request import Request, urlopen

SCHEMA_VERSION = "maestro.audio.gateway.v0.5"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
JOB_ID_RE = re.compile(r"^[A-Za-z0-9._:-]{1,200}$")

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


def capabilities() -> dict[str, Any]:
    worker_url = os.environ.get("MAESTRO_AUDIO_WORKER_URL", "").strip()
    return {
        "schema": SCHEMA_VERSION,
        "authority": AUTHORITY.copy(),
        "worker": {
            "configured": bool(worker_url),
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
    project_id = _require_text(data["project_id"], "project_id", max_len=300)
    source_ref = _require_text(data["source_ref"], "source_ref", max_len=1000)
    source_sha = _require_sha(data["source_sha256"])
    deterministic_id = _require_text(data["deterministic_analysis_id"], "deterministic_analysis_id", max_len=500)
    adapters = data["adapters"]
    if not isinstance(adapters, list) or not adapters:
        raise GatewayValidationError("adapters_must_be_nonempty_list")
    clean: list[str] = []
    for item in adapters:
        if not isinstance(item, str) or item not in ADAPTERS:
            raise GatewayValidationError(f"unknown_adapter:{item}")
        if item not in clean:
            clean.append(item)
    context = data.get("context") or {}
    if not isinstance(context, dict):
        raise GatewayValidationError("context_must_be_object")
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
        if not isinstance(data["generation_settings"], dict):
            raise GatewayValidationError("generation_settings_must_be_object")
        if data.get("causal_claim_authorized", False) is not False:
            raise GatewayValidationError("causal_claim_authorized_must_be_false")
        surfaces = [data.get("lyric_prompt", ""), data.get("style_prompt", ""), data.get("studio_instruction", "")]
        if not any(isinstance(x, str) and x.strip() for x in surfaces):
            raise GatewayValidationError("experiment_requires_renderer_input_surface")
    elif kind == "operator_assessment":
        allowed = {"experiment_artifact_id", "decision", "notes", "blind_listening", "loudness_matched", "preferred_artifact_id", "criteria"}
        data = _strict_object(record, allowed=allowed, required={"experiment_artifact_id", "decision", "notes"}, label=kind)
        _require_text(data["experiment_artifact_id"], "experiment_artifact_id", max_len=500)
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
        if not isinstance(ids, list) or not ids or not all(isinstance(x, str) and x.strip() for x in ids):
            raise GatewayValidationError("experiment_artifact_ids_must_be_nonempty_string_list")
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
            raw = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        raise WorkerUnavailable(f"audio_worker_request_failed:{exc.__class__.__name__}") from exc
    try:
        parsed = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise WorkerProtocolError("audio_worker_invalid_json") from exc
    if not isinstance(parsed, dict):
        raise WorkerProtocolError("audio_worker_response_must_be_object")
    return parsed


def submit_job(payload: Any, *, transport: Callable[[str, str, dict[str, Any] | None, str | None], dict[str, Any]] | None = None) -> dict[str, Any]:
    request_payload = validate_job_request(payload)
    base = os.environ.get("MAESTRO_AUDIO_WORKER_URL", "").strip().rstrip("/")
    if not base:
        raise WorkerUnavailable("audio_worker_not_configured")
    token = os.environ.get("MAESTRO_AUDIO_WORKER_TOKEN")
    response = (transport or _default_transport)("POST", f"{base}/v1/jobs", request_payload, token)
    job_id = response.get("job_id")
    status = response.get("status")
    if not isinstance(job_id, str) or not JOB_ID_RE.fullmatch(job_id):
        raise WorkerProtocolError("audio_worker_invalid_job_id")
    if status not in {"queued", "running", "completed", "failed"}:
        raise WorkerProtocolError("audio_worker_invalid_job_status")
    return {
        "schema": SCHEMA_VERSION,
        "job_id": job_id,
        "status": status,
        "source_sha256": request_payload["source_sha256"],
        "adapters": request_payload["adapters"],
        "authority": AUTHORITY.copy(),
    }


def get_job(job_id: str, *, transport: Callable[[str, str, dict[str, Any] | None, str | None], dict[str, Any]] | None = None) -> dict[str, Any]:
    if not JOB_ID_RE.fullmatch(job_id or ""):
        raise GatewayValidationError("invalid_job_id")
    base = os.environ.get("MAESTRO_AUDIO_WORKER_URL", "").strip().rstrip("/")
    if not base:
        raise WorkerUnavailable("audio_worker_not_configured")
    token = os.environ.get("MAESTRO_AUDIO_WORKER_TOKEN")
    response = (transport or _default_transport)("GET", f"{base}/v1/jobs/{quote(job_id, safe='._:-')}", None, token)
    if not isinstance(response.get("status"), str):
        raise WorkerProtocolError("audio_worker_missing_status")
    response = dict(response)
    response["authority"] = AUTHORITY.copy()
    response["canon_promotion"] = False
    return response


def _read_json(environ) -> dict[str, Any]:
    try:
        length = int(environ.get("CONTENT_LENGTH") or 0)
    except ValueError:
        length = 0
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
