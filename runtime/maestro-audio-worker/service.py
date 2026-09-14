from __future__ import annotations

import hmac
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException, Request

from artifact_sync import ArtifactFetchUnavailable, DEFAULT_MAX_BYTES, sync_artifact
from worker_core import (
    AUTHORITY,
    ArtifactStore,
    ArtifactUnavailable,
    JobStore,
    WorkerValidationError,
    create_job,
    execute_job,
    probe_capabilities,
    public_job,
    validate_job_request,
)

ARTIFACT_ROOT = Path(os.getenv("MAESTRO_ARTIFACT_ROOT", "/data/artifacts"))
STATE_ROOT = Path(os.getenv("MAESTRO_AUDIO_WORKER_STATE", "/data/state"))
TOKEN = os.getenv("MAESTRO_AUDIO_WORKER_TOKEN", "")
MAX_WORKERS = max(1, int(os.getenv("MAESTRO_AUDIO_WORKER_CONCURRENCY", "1")))

artifacts = ArtifactStore(ARTIFACT_ROOT)
jobs = JobStore(STATE_ROOT)
executor = ThreadPoolExecutor(max_workers=MAX_WORKERS, thread_name_prefix="maestro-audio")
app = FastAPI(title="Maestro Audio Analysis Worker", version="0.6")


def require_auth(authorization: str | None) -> None:
    if not TOKEN:
        raise HTTPException(status_code=503, detail="worker_auth_token_not_configured")
    expected = f"Bearer {TOKEN}"
    if authorization is None or not hmac.compare_digest(authorization, expected):
        raise HTTPException(status_code=401, detail="unauthorized")


def schedule(job_id: str) -> None:
    executor.submit(execute_job, job_id, artifacts, jobs)


def ensure_artifact(request_payload: dict) -> None:
    sha256 = request_payload['source_sha256']
    try:
        artifacts.retrieve(sha256)
        return
    except ArtifactUnavailable:
        pass

    base_url = os.getenv('MAESTRO_ARTIFACT_FETCH_BASE_URL', '').strip()
    if not base_url:
        raise ArtifactUnavailable(f'artifact_not_present:{sha256}')
    token = os.getenv('MAESTRO_ARTIFACT_FETCH_TOKEN')
    max_bytes = int(os.getenv('MAESTRO_ARTIFACT_FETCH_MAX_BYTES', str(DEFAULT_MAX_BYTES)))
    sync_artifact(
        sha256,
        artifacts,
        base_url=base_url,
        token=token,
        max_bytes=max_bytes,
        timeout_s=int(os.getenv('MAESTRO_ARTIFACT_FETCH_TIMEOUT_S', '120')),
    )


@app.on_event("startup")
def recover_jobs() -> None:
    for record in jobs.recoverable():
        schedule(record["job_id"])


@app.get("/health")
def health() -> dict:
    return {"ok": True, "service": "maestro-audio-worker", "version": "0.6", "authority": AUTHORITY}


@app.get("/v1/capabilities")
def capabilities(authorization: str | None = Header(default=None)) -> dict:
    require_auth(authorization)
    caps = probe_capabilities()
    caps['artifact_fetch'] = {
        'configured': bool(os.getenv('MAESTRO_ARTIFACT_FETCH_BASE_URL', '').strip()),
        'source_identity': 'sha256_derived_object_path_only',
        'arbitrary_source_urls_allowed': False,
    }
    return caps


@app.post("/v1/jobs", status_code=202)
async def submit(request: Request, authorization: str | None = Header(default=None)):
    require_auth(authorization)
    try:
        payload = await request.json()
        normalized = validate_job_request(payload)
        ensure_artifact(normalized)
        record = create_job(normalized, artifacts, jobs)
    except ArtifactUnavailable as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    except ArtifactFetchUnavailable as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    except WorkerValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    schedule(record["job_id"])
    return public_job(record)


@app.get("/v1/jobs/{job_id}")
def get_job(job_id: str, authorization: str | None = Header(default=None)):
    require_auth(authorization)
    try:
        return public_job(jobs.get(job_id))
    except (KeyError, WorkerValidationError) as exc:
        raise HTTPException(status_code=404, detail="job_not_found") from exc
