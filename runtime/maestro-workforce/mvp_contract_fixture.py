#!/usr/bin/env python3
"""Deterministic contract checks for the creator-facing Maestro MVP bridge."""
from __future__ import annotations

import io
import json
from typing import Any, Dict, Tuple

import app as mvp


def call(method: str, path: str, payload: Dict[str, Any] | None = None, query: str = "") -> Tuple[int, Dict[str, Any] | str]:
    body = json.dumps(payload or {}).encode("utf-8") if payload is not None else b""
    captured = {}

    def start_response(status, headers):
        captured["status"] = int(status.split()[0])
        captured["headers"] = dict(headers)

    environ = {
        "REQUEST_METHOD": method,
        "PATH_INFO": path,
        "QUERY_STRING": query,
        "CONTENT_LENGTH": str(len(body)),
        "wsgi.input": io.BytesIO(body),
    }
    raw = b"".join(mvp.app(environ, start_response))
    ctype = captured["headers"].get("Content-Type", "")
    parsed = json.loads(raw.decode("utf-8")) if "application/json" in ctype else raw.decode("utf-8")
    return captured["status"], parsed


def check(name: str, condition: bool, details: Any):
    if not condition:
        raise AssertionError(f"{name} failed: {details}")
    return {"name": name, "passed": True, "details": details}


def main():
    results = []

    status, health = call("GET", "/api/health")
    results.append(check("health", status == 200 and health["ok"] is True and health["authority"] == "technical_ust_ownership_dependency_overlay", health))

    status, root = call("GET", "/")
    results.append(check("browser_static_delivery", status == 200 and "Maestro Browser MVP" in root, {"status": status, "contains_title": "Maestro Browser MVP" in root}))

    status, resolved = call("GET", "/api/resolve", query="address=THY.K3.S2")
    results.append(check("address_runtime_resolution", status == 200 and resolved["primary_owner"]["name"] == "Dave", resolved))

    status, packet = call("POST", "/api/dispatch", {"address": "THY.K3.S2", "task": "Resolve rhythmic theory only."})
    results.append(check("lawful_dispatch", status == 200 and packet["worker_name"] == "Dave" and packet["technical_ust"]["address"] == "THY.K3.S2", packet))

    status, denied = call("POST", "/api/change-preview", {
        "address": "THY.K3.S2",
        "worker_id": "MAESTRO.AUDIO.05.METRO",
        "value": {"tempo": 92}
    })
    results.append(check("wrong_owner_fail_closed", status == 403 and denied.get("type") == "authority", denied))

    status, lyric_denied = call("POST", "/api/change-preview", {
        "address": "LYR.K1",
        "worker_id": "MAESTRO.AUDIO.07.SAGE",
        "value": "rewrite",
        "lyrics_locked": True
    })
    results.append(check("locked_lyrics_fail_closed", status == 409 and lyric_denied.get("type") == "runtime_block", lyric_denied))

    status, impact = call("POST", "/api/change-preview", {
        "address": "THY.K3.S2",
        "worker_id": "MAESTRO.AUDIO.09.DAVE",
        "value": {"tempo_relation": "half_double_allowed"},
        "values": {"MAP.K3.S1": {"Chorus": ["THY.K3.S2"]}}
    })
    targets = {entry.get("target") for entry in impact.get("event", {}).get("impacts", [])}
    results.append(check("dependency_impact_propagates", status == 200 and "LYR.K4" in targets and "MAP.K3.S1@Chorus" in targets, {"status": status, "targets": sorted(t for t in targets if t)}))

    status, evidence = call("POST", "/api/evidence/validate", {
        "control_id": "low_end_presence",
        "source_ref": "fixture://renderer-output",
        "observation": "low-end instruction is detectably present",
        "verdict": "supported"
    })
    results.append(check("renderer_evidence_cannot_promote", status == 200 and evidence["technical_ust_mutation"] is False and evidence["canon_promotion"] is False, evidence))

    report = {"passed": all(item["passed"] for item in results), "checks": results}
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
