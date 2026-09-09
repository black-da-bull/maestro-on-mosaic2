"""Vercel WSGI entrypoint for the Maestro browser MVP.

The browser is deliberately thin: Technical UST address authority, dispatch, change
impact, lyric locks, and reviewer rules stay in this runtime package. Renderer
adherence observations are empirical adapter evidence and cannot mutate Technical
UST or promote themselves into canon.
"""
from __future__ import annotations

import json
import mimetypes
from pathlib import Path
from urllib.parse import parse_qs

import technical_ust_runtime as technical_ust
import workforce_runtime as workforce

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[1]
APP_ROOT = REPO_ROOT / "apps" / "maestro-browser-mvp"

ADAPTER_VERSION = "suno-adherence-v1"
ADHERENCE_MATRIX = {
    "adapter_version": ADAPTER_VERSION,
    "authority": "empirical_adapter_evidence_not_canon",
    "promotion_rule": "observations may inform a proposed state delta but never mutate Technical UST or Maestro law automatically",
    "controls": [
        {"id": "low_end_presence", "type": "presence", "label": "Low-end intent", "status": "supported_cross_corpus", "validation": "detect/presence plus listening confirmation"},
        {"id": "tempo_relation", "type": "relational", "label": "Relative / half-double tempo behavior", "status": "supported_more_reliably_than_exact_integer_lock", "validation": "relational timing comparison"},
        {"id": "ensemble_response", "type": "interaction", "label": "Ensemble / vocal-space response", "status": "supported_at_signal_proxy_level", "validation": "relationship and listening evidence"},
        {"id": "style_sensitivity", "type": "comparative", "label": "External Style sensitivity", "status": "supported_material_participation", "validation": "controlled comparative render"},
        {"id": "exact_tempo", "type": "exact_numeric", "label": "Exact integer BPM obedience", "status": "unresolved_not_reliable_enough_for_law", "validation": "measured BPM error/tolerance"},
        {"id": "semantic_timbre", "type": "semantic_timbre", "label": "Exact semantic timbre identity (for example B3/Leslie)", "status": "unresolved_narrow_fidelity_probe", "validation": "listening plus semantic/source evidence"},
        {"id": "deterministic_repeatability", "type": "repeatability", "label": "Deterministic exact repeatability", "status": "not_established", "validation": "controlled repeated renders"}
    ]
}


def _json(start_response, status: str, payload: object):
    body = json.dumps(payload, indent=2).encode("utf-8")
    start_response(status, [("Content-Type", "application/json; charset=utf-8"), ("Content-Length", str(len(body))), ("Cache-Control", "no-store")])
    return [body]


def _text(start_response, status: str, body: bytes, content_type: str):
    start_response(status, [("Content-Type", content_type), ("Content-Length", str(len(body))), ("Cache-Control", "no-store")])
    return [body]


def _read_json(environ):
    try:
        length = int(environ.get("CONTENT_LENGTH") or 0)
    except ValueError:
        length = 0
    raw = environ["wsgi.input"].read(length) if length else b"{}"
    if not raw:
        return {}
    data = json.loads(raw.decode("utf-8"))
    if not isinstance(data, dict):
        raise ValueError("JSON object required")
    return data


def _worker_view(worker_id: str):
    worker = workforce.resolve(worker_id)
    if not worker:
        return {"id": worker_id, "name": worker_id}
    return {"id": worker_id, "name": worker["identity"]["role_name"]}


def _binding_view(address: str):
    binding = technical_ust.binding_for(address)
    return {
        "address": address,
        "axis": binding["axis"],
        "key": binding["key"],
        "subkey": binding["subkey"],
        "primary_owner": _worker_view(binding["primary_owner"]),
        "required_reviewers": [_worker_view(ref) for ref in binding["required_reviewers"]],
        "ownership_source": technical_ust.OVERLAY_NAME
    }


def _runtime_addresses():
    overlay = technical_ust.load_overlay()
    addresses = []
    for axis, axis_binding in (overlay.get("axis_bindings") or {}).items():
        keys = axis_binding.get("key_bindings") or {}
        if not keys and axis_binding.get("primary_owner"):
            addresses.append(axis)
            continue
        for key, key_binding in keys.items():
            if key_binding.get("primary_owner"):
                addresses.append(key)
            for subkey in (key_binding.get("subkey_bindings") or {}):
                addresses.append(subkey)
    seen = set()
    views = []
    for address in addresses:
        if address in seen:
            continue
        seen.add(address)
        views.append(_binding_view(address))
    return sorted(views, key=lambda item: item["address"])


def _static_file(path: str):
    rel = "index.html" if path == "/" else path.lstrip("/")
    if rel not in {"index.html", "app.js", "styles.css"}:
        return None
    target = APP_ROOT / rel
    if not target.exists():
        return None
    content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
    if content_type.startswith("text/") or content_type in {"application/javascript", "application/json"}:
        content_type += "; charset=utf-8"
    return target.read_bytes(), content_type


def app(environ, start_response):
    method = environ.get("REQUEST_METHOD", "GET").upper()
    path = environ.get("PATH_INFO", "/")
    try:
        if method == "GET" and path == "/api/health":
            return _json(start_response, "200 OK", {
                "ok": True,
                "runtime": "maestro-workforce",
                "authority": "technical_ust_ownership_dependency_overlay",
                "renderer_adapter": ADAPTER_VERSION
            })

        if method == "GET" and path == "/api/addresses":
            return _json(start_response, "200 OK", {"addresses": _runtime_addresses()})

        if method == "GET" and path == "/api/resolve":
            query = parse_qs(environ.get("QUERY_STRING", ""))
            address = (query.get("address") or [""])[0].strip()
            if not address:
                return _json(start_response, "400 Bad Request", {"error": "address is required"})
            return _json(start_response, "200 OK", _binding_view(address))

        if method == "POST" and path == "/api/dispatch":
            data = _read_json(environ)
            address = str(data.get("address") or "").strip()
            task = str(data.get("task") or "").strip()
            if not address or not task:
                return _json(start_response, "400 Bad Request", {"error": "address and task are required"})
            packet = technical_ust.dispatch_address(address, task, data.get("context_refs") or ["technical.ust", technical_ust.OVERLAY_NAME])
            return _json(start_response, "200 OK", packet)

        if method == "POST" and path == "/api/change-preview":
            data = _read_json(environ)
            address = str(data.get("address") or "").strip()
            worker_id = str(data.get("worker_id") or "").strip()
            if not address or not worker_id:
                return _json(start_response, "400 Bad Request", {"error": "address and worker_id are required"})
            runtime = technical_ust.TechnicalUSTRuntime(values=data.get("values") or {}, lyrics_locked=bool(data.get("lyrics_locked")))
            event = runtime.apply_change(worker_id, address, data.get("value"), operator_authorized_lyric_change=bool(data.get("operator_authorized_lyric_change")))
            return _json(start_response, "200 OK", {
                "event": event,
                "status": runtime.status,
                "technical_ust_mutation": "preview_only_client_must_commit_explicitly"
            })

        if method == "GET" and path == "/api/adherence-matrix":
            return _json(start_response, "200 OK", ADHERENCE_MATRIX)

        if method == "POST" and path == "/api/evidence/validate":
            data = _read_json(environ)
            required = ["control_id", "source_ref", "observation", "verdict"]
            missing = [key for key in required if not str(data.get(key) or "").strip()]
            control_ids = {item["id"] for item in ADHERENCE_MATRIX["controls"]}
            if missing:
                return _json(start_response, "400 Bad Request", {"error": "missing required evidence fields", "missing": missing})
            if data["control_id"] not in control_ids:
                return _json(start_response, "400 Bad Request", {"error": "unknown adherence control"})
            if data["verdict"] not in {"supported", "contextual", "disputed", "unresolved"}:
                return _json(start_response, "400 Bad Request", {"error": "invalid verdict"})
            return _json(start_response, "200 OK", {
                "accepted_as": "empirical_renderer_evidence",
                "adapter_version": ADAPTER_VERSION,
                "record": data,
                "technical_ust_mutation": False,
                "canon_promotion": False,
                "next_state": "eligible_for_operator_or_runtime_review_only"
            })

        if method == "GET":
            static = _static_file(path)
            if static:
                body, content_type = static
                return _text(start_response, "200 OK", body, content_type)

        return _json(start_response, "404 Not Found", {"error": "not found"})

    except technical_ust.RuntimeAuthorityError as exc:
        return _json(start_response, "403 Forbidden", {"error": str(exc), "type": "authority"})
    except technical_ust.RuntimeBlockError as exc:
        return _json(start_response, "409 Conflict", {"error": str(exc), "type": "runtime_block"})
    except (ValueError, json.JSONDecodeError) as exc:
        return _json(start_response, "400 Bad Request", {"error": str(exc), "type": "validation"})
    except Exception as exc:
        return _json(start_response, "500 Internal Server Error", {"error": str(exc), "type": exc.__class__.__name__})
