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
    caps = a.capabilities()
    assert caps["auto_promotion"] is False
    assert caps["authority"]["technical_ust_mutation"] is False
    assert {x["id"] for x in caps["adapters"]} >= {
        "beat_this", "songformer", "chordmini", "basic_pitch", "advanced_amt", "clap", "audio_language"
    }

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

    with env(MAESTRO_AUDIO_WORKER_URL=None):
        expect_error(lambda: a.submit_job(valid), "not_configured")
        status, payload = call_wsgi("POST", "/api/audio-analysis/jobs", valid)
        assert status.startswith("503") and payload["type"] == "worker_unavailable"

    def ok_transport(method, url, payload, token):
        assert method == "POST" and url.endswith("/v1/jobs")
        assert payload["authority"]["canon_promotion"] is False
        return {"job_id": "job-123", "status": "queued"}

    with env(MAESTRO_AUDIO_WORKER_URL="https://worker.invalid", MAESTRO_AUDIO_WORKER_TOKEN="secret"):
        submitted = a.submit_job(valid, transport=ok_transport)
        assert submitted["status"] == "queued"
        assert submitted["authority"]["renderer_policy_promotion"] is False

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

    status, payload = call_wsgi("GET", "/api/audio-analysis/capabilities")
    assert status.startswith("200") and payload["schema"] == a.SCHEMA_VERSION
    status, payload = call_wsgi(
        "POST",
        "/api/renderer-learning/validate",
        {"kind": "renderer_experiment", "record": experiment},
    )
    assert status.startswith("200") and payload["authority"]["technical_ust_mutation"] is False

    result = {"passed": True, "checks": 16, "schema": a.SCHEMA_VERSION}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
