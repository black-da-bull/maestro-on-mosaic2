# Maestro Audio Analysis Worker v0.6

Dedicated model-worker boundary for Maestro. The Vercel `maestro-workforce` runtime remains the orchestration and authority gateway; this service owns heavyweight MIR/model execution.

## Contract

- bearer-token authentication on `/v1/*`;
- content-addressed immutable artifact store keyed by SHA-256;
- source bytes are re-hashed before and after analysis;
- filesystem-persisted jobs recover from `queued`/`running` after restart;
- strict result envelopes match the existing `maestro.audio.gateway.v0.5` validator;
- model absence is `not_configured`, not fabricated success;
- no result can mutate Technical UST, canon, renderer policy, or keeper/release state.

## HTTP

- `GET /health` — unauthenticated liveness only.
- `GET /v1/capabilities` — authenticated runtime/model capability probe.
- `POST /v1/jobs` — authenticated job submission using immutable logical artifact refs + SHA-256.
- `GET /v1/jobs/{job_id}` — authenticated job/result retrieval.

The worker deliberately refuses arbitrary source URLs. A source must first be present in its immutable content-addressed store. This keeps network/source acquisition separate from model execution and prevents provider labels or URLs from becoming artifact identity.

## Run

```bash
python -m pip install -r requirements-core.txt
export MAESTRO_AUDIO_WORKER_TOKEN='replace-me'
export MAESTRO_ARTIFACT_ROOT='./data/artifacts'
export MAESTRO_AUDIO_WORKER_STATE='./data/state'
python ingest.py /path/to/song.wav
uvicorn service:app --host 0.0.0.0 --port 8080
```

Install model-specific environments deliberately. Beat This, Basic Pitch, and CLAP have optional requirement files. SongFormer, ChordMini, advanced AMT/tsumugi, and audio-language reasoning are isolated behind JSON argv bridges so each can run in a separately pinned environment/container.

A command bridge receives `{input}`, `{output}`, and `{context}` as exact standalone argv placeholders and must write one JSON object to `{output}`. Shell interpolation is not used.

The core worker always exposes `statistical_embedding`, a non-semantic streaming descriptor. It exists so end-to-end orchestration, hashing, auth and result-envelope behavior can be validated without pretending a heavyweight model ran.

## Authority

```text
deterministic measurement
-> labeled model inference
-> calibration evidence
-> operator listening judgment
```

Worker evidence cannot automatically promote a Technical UST mutation, canon change, renderer policy, keeper, master, or release decision.
