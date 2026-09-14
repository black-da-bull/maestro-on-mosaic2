from __future__ import annotations

import io
import json
import os
from contextlib import contextmanager

import audio_analysis_gateway as a

SHA = "a" * 64


@contextmanager
def env(**values):
    old = {k: os.environ.get(k) for k in values}
    try:
        for k, v in values.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        yield
    finally:
        for k, v in old.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def expect_error(fn, contains):
    try:
        fn()
    except Exception as exc:
        assert contains in str(exc), (contains, str(exc))
    else:
        raise AssertionError(f"expected error containing {contains}")


def call_wsgi(method, path, payload=None, query=""):
    raw = b"" if payload is None else json.dumps(payload).encode()
    envp = {
        "REQUEST_METHOD": method,
        "PATH_INFO": path,
        "QUERY_STRING": query,
        "CONTENT_LENGTH": str(len(raw)),
        "wsgi.input": io.BytesIO(raw),
    }
    captured = {}

    def start(status, headers):
        captured["status"] = status
        captured["headers"] = headers

    body_parts = a.handle_wsgi(envp, start)
    return captured["status"], json.loads(b"".join(body_parts).decode())


def main():
    checks = 0
    caps = a.capabilities()
    assert caps["auto_promotion"] is False
    assert caps["authority"]["technical_ust_mutation"] is False
    assert {x["id"] for x in caps["adapters"]} >= {
        "beat_this", "songformer", "chordmini", "basic_pitch", "advanced_amt", "clap", "audio_language"
    }
    checks += 3

    valid = {
        "project_id": "p1",
        "source_ref": "artifact:original",
        "source_sha256": SHA,
        "deterministic_analysis_id": "analysis:signal:1",
        "adapters": ["beat_this", "songformer"],
        "context": {"expected_bpm": 103.0},
    }
    normalized = a.validate_job_request(valid)
    assert normalized["source_sha256"] == SHA
    expect_error(lambda: a.validate_job_request({**valid, "source_sha256": "bad"}), "lowercase_sha256")
    expect_error(lambda: a.validate_job_request({**valid, "adapters": ["imaginary"]}), "unknown_adapter")
    expect_error(lambda: a.validate_job_request({**valid, "surprise": 1}), "unknown_fields")
    expect_error(lambda: a.validate_job_request({**valid, "source_ref": "https://attacker.invalid/x"}), "logical_artifact_reference")
    checks += 5

    with env(MAESTRO_AUDIO_WORKER_URL=None):
        expect_error(lambda: a.submit_job(valid), "not_configured")
        status, payload = call_wsgi("POST", "/api/audio-analysis/jobs", valid)
        assert status.startswith("503") and payload["type"] == "worker_unavailable"
    checks += 2

    with env(MAESTRO_AUDIO_WORKER_URL="http://worker.invalid"):
        expect_error(lambda: a.submit_job(valid, transport=lambda *args: {}), "must_use_https")
    checks += 1

    def ok_transport(method, url, payload, token):
        assert method == "POST" and url.endswith("/v1/jobs")
        assert payload["authority"]["canon_promotion"] is False
        return {"job_id": "job-123", "status": "queued"}

    with env(MAESTRO_AUDIO_WORKER_URL="https://worker.invalid", MAESTRO_AUDIO_WORKER_TOKEN="secret"):
        submitted = a.submit_job(valid, transport=ok_transport)
        assert submitted["status"] == "queued"
        assert submitted["authority"]["renderer_policy_promotion"] is False
    checks += 2

    completed_response = {
        "job_id": "job-123",
        "status": "completed",
        "source_sha256": SHA,
        "adapters": ["beat_this"],
        "results": [{
            "adapter_id": "beat_this",
            "status": "completed",
            "schema": "maestro.audio.beat_this.v0.5",
            "output": {"bpm": 103.0, "beats": [0.0, 0.58]},
            "provenance": {
                "source_sha256": SHA,
                "implementation": "beat_this_bridge",
                "implementation_version": "1",
                "evidence_class": "model_inference",
            },
            "warnings": [],
        }],
    }

    def completed_transport(method, url, payload, token):
        assert method == "GET"
        return completed_response

    with env(MAESTRO_AUDIO_WORKER_URL="https://worker.invalid"):
        got = a.get_job("job-123", transport=completed_transport)
        assert got["results"][0]["adapter_id"] == "beat_this"
        bad = json.loads(json.dumps(completed_response))
        bad["results"][0]["provenance"]["source_sha256"] = "b" * 64
        expect_error(lambda: a.get_job("job-123", transport=lambda *args: bad), "source_identity_mismatch")
        bad_unknown = {**completed_response, "surprise": True}
        expect_error(lambda: a.get_job("job-123", transport=lambda *args: bad_unknown), "unknown_fields")
        bad_missing = json.loads(json.dumps(completed_response))
        bad_missing["results"] = []
        expect_error(lambda: a.get_job("job-123", transport=lambda *args: bad_missing), "do_not_cover_adapters")
    checks += 4

    experiment = {
        "objective": "Compare controlled renders",
        "style_prompt": "Warm Southern soul pocket",
        "generation_settings": {"renderer": "Suno", "model_version": "v6", "variety": 0},
        "causal_claim_authorized": False,
    }
    accepted = a.validate_renderer_record("renderer_experiment", experiment)
    assert accepted["auto_promotion"] is False
    expect_error(
        lambda: a.validate_renderer_record("renderer_experiment", {**experiment, "causal_claim_authorized": True}),
        "must_be_false",
    )
    checks += 2

    observation = {
        "statement": "Low Variety was associated with smaller style drift in this run",
        "status": "observation",
        "model_version_scope": "Suno v6",
        "experiment_artifact_ids": ["exp:1"],
        "rationale": "single controlled observation",
        "operator_confirmed": False,
    }
    a.validate_renderer_record("renderer_heuristic", observation)
    candidate = {**observation, "status": "candidate_heuristic"}
    expect_error(lambda: a.validate_renderer_record("renderer_heuristic", candidate), "operator_confirmation")
    a.validate_renderer_record("renderer_heuristic", {**candidate, "operator_confirmed": True})
    expect_error(
        lambda: a.validate_renderer_record(
            "renderer_heuristic",
            {**candidate, "status": "renderer_policy", "operator_confirmed": True, "reversible": False},
        ),
        "must_be_reversible",
    )
    checks += 4

    status, payload = call_wsgi("GET", "/api/audio-analysis/capabilities")
    assert status.startswith("200") and payload["schema"] == a.SCHEMA_VERSION
    status, payload = call_wsgi(
        "POST",
        "/api/renderer-learning/validate",
        {"kind": "renderer_experiment", "record": experiment},
    )
    assert status.startswith("200") and payload["authority"]["technical_ust_mutation"] is False
    checks += 2

    print(json.dumps({"passed": True, "checks": checks, "schema": a.SCHEMA_VERSION}, indent=2))


if __name__ == "__main__":
    main()
