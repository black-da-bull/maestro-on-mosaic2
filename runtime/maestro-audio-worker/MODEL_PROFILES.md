# Model profiles and isolation policy

The worker core is intentionally lightweight. Heavy model environments are isolated from the worker-core Python environment even when they are packaged into the same deployable image. Model source code existing in an image is not proof that model inference is available; checkpoint/model assets, device requirements, provenance, and a real inference must still pass.

All profile Dockerfiles are built with `runtime/maestro-audio-worker` as the Docker build context, for example:

```bash
cd runtime/maestro-audio-worker
docker build -f profiles/basic-pitch/Dockerfile -t maestro-audio-worker:basic-pitch .
```

## Beat This

Reference: `CPJKU/beat_this`. Upstream exposes `File2Beats`; checkpoints may be selected by name or local path. Maestro chooses CUDA only when PyTorch reports CUDA available; otherwise `auto` selects CPU. An explicitly requested unavailable CUDA backend fails rather than silently changing evidence conditions.

For reproducible production deployment, pre-seed and hash-pin a local checkpoint and set `BEAT_THIS_CHECKPOINT`; do not treat successful package import as proof that a checkpoint executed. CI has executed the real upstream `small0` checkpoint on CPU and intentionally validates half/double relational tempo behavior rather than exact integer BPM lock.

```bash
docker build --build-arg EXTRA_REQUIREMENTS=requirements-beat-this.txt -t maestro-audio-worker:beat-this .
```

## SongFormer

Reference: `ASLP-lab/SongFormer` at the pinned repository revision in `model-lock.json`.

The upstream repository inference path is not a generic `AutoModel(audio_path)` call. It explicitly constructs MuQ and MusicFM representations, loads the SongFormer checkpoint/config, and executes the SongFormer inference pipeline on CUDA. The Maestro bridge therefore invokes the pinned upstream `src/SongFormer/infer/infer.py` path rather than inventing a simplified API.

The provided profile uses an isolated Python 3.10 virtual environment and requires a GPU plus pre-provisioned local assets:

```text
/models/songformer/ckpts/SongFormer.safetensors
/models/songformer/ckpts/MusicFM/pretrained_msd.pt
/models/songformer/ckpts/MusicFM/msd_stats.json
/models/songformer/hf/...   # dedicated pre-populated MuQ Hugging Face cache
```

The image symlinks the upstream `ckpts` location to the mounted model tree and forces Hugging Face/Transformers offline mode during inference. The bridge records hashes for the SongFormer checkpoint, MusicFM model/stats, MuQ cache tree, and config. If CUDA or any required local model asset is absent, the run fails instead of downloading an untracked replacement.

```bash
docker build -f profiles/songformer/Dockerfile -t maestro-audio-worker:songformer .
docker run --gpus all --rm -p 8080:8080 \
  -e MAESTRO_AUDIO_WORKER_TOKEN=... \
  -v /host/songformer-models:/models/songformer:ro \
  -v /host/maestro-data:/data \
  maestro-audio-worker:songformer
```

SongFormer output remains inferred section evidence, not canonical MAP/lyrics structure.

## ChordMini

Reference: `ptnghia-j/ChordMini`. Upstream ships ChordNet/BTC checkpoints and a repository-local evaluation CLI capable of single-file inference through `src/evaluation/test.py --audio_dir <file> --save_dir <dir> --checkpoint <checkpoint> --model_type <ChordNet|BTC>`.

The provided profile keeps the ChordMini dependency stack in its own virtual environment, while the authenticated worker service stays on the core environment. Mount the selected checkpoint at `/models/chordmini/model.pth` or supply an explicit context path. The bridge records the checkpoint SHA-256 and parses the emitted `.lab` segments. Chord labels remain model inference and must be calibrated against project evidence/listening.

```bash
docker build -f profiles/chordmini/Dockerfile -t maestro-audio-worker:chordmini .
```

## Basic Pitch

Reference: `spotify/basic-pitch`. The pinned upstream README documents Python support through 3.11 for the referenced revision, so Basic Pitch is isolated in a Python 3.11 virtual environment instead of being forced into the Python 3.12 core.

The bridge uses the upstream programmatic `predict()` API, records the package version, hashes the selected packaged model artifact (file or directory), and returns MIDI identity/summary without replacing source MIDI. Basic Pitch is instrument-agnostic/polyphonic but upstream states that it works best on one instrument at a time; for Bitter Thank You, stem-level AMT is therefore the preferred calibration surface where practical.

```bash
docker build -f profiles/basic-pitch/Dockerfile -t maestro-audio-worker:basic-pitch .
```

## Advanced AMT / tsumugi

Reference: `anime-song/tsumugi`. The pinned upstream revision supports Python 3.10–3.14 and a locked `uv` environment. Device `auto` resolves CUDA → MPS → CPU, while an explicitly requested unavailable backend fails.

The Maestro image retains the upstream locked model environment separately from the core worker environment. Production inference requires a pre-provisioned local checkpoint at `/models/tsumugi/model.pt` (or an explicit context path); the bridge records its SHA-256, device, model variant, generated MIDI identity, and MIDI summary. It does not use an untracked first-run checkpoint download.

For dense mixes, prefer the stem-separated workflow when practical because upstream reports better behavior on acoustically simpler stems.

```bash
docker build -f profiles/tsumugi/Dockerfile -t maestro-audio-worker:tsumugi .
```

## CLAP

Reference: `LAION-AI/CLAP`. The pinned repository environment is Python 3.10-oriented and publishes multiple checkpoints, including music-specific models. The provided profile isolates `laion-clap` in its own virtual environment and requires a pre-provisioned checkpoint at `/models/clap/model.pt` (or an explicit context path).

The bridge records checkpoint SHA-256, model name, fusion setting and embedding dimension. Embedding distances have no Maestro meaning until calibrated on operator-labeled examples. No universal quality score is allowed.

```bash
docker build -f profiles/clap/Dockerfile -t maestro-audio-worker:clap .
```

## Audio-language reasoning

`MAESTRO_AUDIO_LANGUAGE_COMMAND_JSON` accepts evidence-grounded reasoning only. The bridge receives measured/MIR evidence in `{context}` and must return `claims` with non-empty `evidence_refs` plus a `contradictions` list. Maestro marks the result advisory, preserves contradictions, and never promotes it into Technical UST/canon automatically.

## Environment rule

Do not force model stacks into one dependency environment merely to make installation look complete. A profile can be `bridge_configured` while its model assets/device remain unverified. A model is considered execution-proven only after package/code, checkpoint/model identity, device/runtime, source hash, output contract, and a real inference all pass. Otherwise the model remains experimental, unavailable, or failed for that run.
