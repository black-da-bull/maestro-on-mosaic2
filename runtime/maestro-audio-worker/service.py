from __future__ import annotations

import hmac
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException, Request

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
    return probe_capabilities()


@app.post("/v1/jobs", status_code=202)
async def submit(request: Request, authorization: str | None = Header(default=None)):
    require_auth(authorization)
    try:
        payload = await request.json()
        record = create_job(payload, artifacts, jobs)
    except ArtifactUnavailable as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
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
