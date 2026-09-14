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

## Immutable artifact retrieval

A job never supplies a filesystem path or fetch URL. Artifact identity is the immutable `source_sha256` plus a logical `source_ref`.

When the requested SHA is already present, the worker re-hashes the local content-addressed object before use. When it is absent and `MAESTRO_ARTIFACT_FETCH_BASE_URL` is configured, the worker derives exactly one trusted object URL:

```text
<configured-base>/objects/<first-two-sha-chars>/<full-sha256>
```

The configured base must be HTTPS except for localhost test/development. `MAESTRO_ARTIFACT_FETCH_TOKEN` may authenticate the fetch. Download size is capped, downloaded bytes must hash to the requested SHA, and the final object is atomically imported read-only into the worker store. Arbitrary request/provider URLs remain forbidden.

Relevant settings:

```text
MAESTRO_ARTIFACT_FETCH_BASE_URL
MAESTRO_ARTIFACT_FETCH_TOKEN
MAESTRO_ARTIFACT_FETCH_MAX_BYTES     # default 4 GiB
MAESTRO_ARTIFACT_FETCH_TIMEOUT_S     # default 120
```

## Run core worker

```bash
python -m pip install -r requirements-core.txt
export MAESTRO_AUDIO_WORKER_TOKEN='replace-me'
export MAESTRO_ARTIFACT_ROOT='./data/artifacts'
export MAESTRO_AUDIO_WORKER_STATE='./data/state'
python ingest.py /path/to/song.wav
uvicorn service:app --host 0.0.0.0 --port 8080
```

The core worker always exposes `statistical_embedding`, a non-semantic streaming descriptor. It exists so end-to-end orchestration, hashing, authentication, artifact retrieval and result-envelope behavior can be validated without pretending a heavyweight model ran.

## Model-specific worker images

Do not force incompatible model stacks into the Python 3.12 core. `profiles/` contains deployable worker-image recipes using the runtime version researched for each model family.

Build from this directory so the profile can copy the common worker service:

```bash
docker build -f profiles/basic-pitch/Dockerfile -t maestro-audio-worker:basic-pitch .
docker build -f profiles/songformer/Dockerfile -t maestro-audio-worker:songformer .
docker build -f profiles/chordmini/Dockerfile -t maestro-audio-worker:chordmini .
docker build -f profiles/tsumugi/Dockerfile -t maestro-audio-worker:tsumugi .
docker build -f profiles/clap/Dockerfile -t maestro-audio-worker:clap .
```

- **Beat This** remains a compatible core profile and has a real `small0` CPU checkpoint smoke in CI.
- **Basic Pitch** uses Python 3.11 because upstream documents support through 3.11, not 3.12.
- **SongFormer** uses the upstream Python 3.10 dependency stack and requires a pre-provisioned local model directory/checkpoint evidence.
- **ChordMini** isolates its own Torch/dependency stack and requires an explicit pre-provisioned ChordNet or BTC checkpoint.
- **tsumugi** keeps its upstream locked `uv` environment and is called from the worker through that environment.
- **CLAP** uses a Python 3.10 profile and requires an explicit local checkpoint whose SHA-256 is recorded.

Model package presence is not considered a completed capability. A profile becomes configured only after a real checkpoint/device smoke test and provenance capture.

## Command bridge contract

SongFormer, ChordMini, tsumugi and optional external reasoners are connected through JSON argv bridge definitions. A bridge receives `{input}`, `{output}`, and `{context}` as exact standalone argv elements and must write one JSON object to `{output}`. Shell interpolation is not used.

## Authority

```text
deterministic measurement
-> labeled model inference
-> calibration evidence
-> operator listening judgment
```

Worker evidence cannot automatically promote a Technical UST mutation, canon change, renderer policy, keeper, master, or release decision.
