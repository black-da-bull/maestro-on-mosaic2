# Model profiles and isolation policy

The worker core is intentionally lightweight. Heavy model environments are optional and should be deployed as dedicated images or sidecars when their runtime constraints differ. Model availability is evidence, not authority.

## Beat This

Reference: `CPJKU/beat_this`. Upstream exposes `File2Beats`; checkpoints may be selected by name or local path. Maestro chooses CUDA only when PyTorch reports CUDA available; otherwise `auto` selects CPU. An explicitly requested unavailable CUDA backend fails rather than silently changing evidence conditions.

For reproducible deployment, pre-seed and hash-pin a local checkpoint and set `BEAT_THIS_CHECKPOINT`; do not treat successful package import as proof that a checkpoint executed. The current CI has executed the real `small0` checkpoint on CPU and intentionally validates half/double relational tempo behavior rather than exact integer lock.

```bash
docker build --build-arg EXTRA_REQUIREMENTS=requirements-beat-this.txt -t maestro-audio-worker:beat-this .
```

## SongFormer

Reference: `ASLP-lab/SongFormer`. Upstream documents a Python 3.10 conda environment, recursive submodules, its own requirements, pretrained checkpoint retrieval, and MD5 verification. Keep this environment outside the Python 3.12 worker core and configure `MAESTRO_SONGFORMER_COMMAND_JSON` to invoke a pinned SongFormer sidecar/runner. SongFormer output remains inferred section evidence, not canonical MAP/lyrics structure.

Required production provenance: repository revision, SongFormer checkpoint hash, MuQ/MusicFM dependency/checkpoint identities, device, and inference configuration.

## ChordMini

Reference: `ptnghia-j/ChordMini`. Upstream ships ChordNet/BTC checkpoints and a repository-local evaluation CLI capable of single-file inference through `src/evaluation/test.py --audio_dir <file> --save_dir <dir> --checkpoint <checkpoint> --model_type <ChordNet|BTC>`. Keep its dependency stack isolated and configure `MAESTRO_CHORDMINI_COMMAND_JSON` through the Maestro bridge wrapper. Chord labels remain inference and must be calibrated against project evidence/listening.

## Basic Pitch

Reference: `spotify/basic-pitch`. The current upstream README documents Python 3.7–3.11 compatibility. Therefore **Basic Pitch is not installed into the Python 3.12 worker-core image**. Run it in the provided Python 3.11 profile/sidecar and connect it through `MAESTRO_BASIC_PITCH_COMMAND_JSON`.

Basic Pitch is instrument-agnostic/polyphonic but upstream says it works best on one instrument at a time. For Bitter Thank You, stem-level AMT is therefore the preferred calibration surface where practical. Generated MIDI remains an inferred transcription and never replaces Suno-exported/source MIDI.

## Advanced AMT / tsumugi

Reference: `anime-song/tsumugi`. Upstream supports Python 3.10–3.14, uses a locked `uv` environment, and currently documents `python -m instrument_agnostic_amt.amt.cli.infer --audio <file>`. Device `auto` resolves CUDA → MPS → CPU, while an explicitly requested unavailable backend fails. A 12 GB+ NVIDIA GPU is recommended but CPU/MPS are supported.

Keep the pinned `uv.lock` environment and configure `MAESTRO_ADVANCED_AMT_COMMAND_JSON`. For dense mixes, prefer the stem-separated workflow because upstream explicitly reports better behavior on acoustically simpler stems. Preserve model variant, checkpoint hash, device, window/batch settings, and generated MIDI identity in provenance.

## CLAP

Reference: `LAION-AI/CLAP`. Upstream's repository environment documents Python 3.10 and provides multiple checkpoints, including music-specific models. Keep the CLAP environment isolated from the Python 3.12 core unless a tested PyPI combination proves compatible. Configure `MAESTRO_CLAP_COMMAND_JSON` or run a dedicated CLAP sidecar.

For Maestro music similarity, prefer an explicitly selected music-capable checkpoint and record its hash. Embedding distances have no project meaning until calibrated on operator-labeled examples; no universal quality score is allowed.

## Audio-language reasoning

`MAESTRO_AUDIO_LANGUAGE_COMMAND_JSON` accepts evidence-grounded reasoning only. The bridge receives measured/MIR evidence in `{context}` and must return `claims` with non-empty `evidence_refs` plus a `contradictions` list. Maestro marks the result advisory, preserves contradictions, and never promotes it into Technical UST/canon automatically.

## Environment rule

Do not force model stacks into one dependency environment merely to make installation look complete. A model profile is considered configured only when its package/code, checkpoint, device/runtime, provenance, and output contract all pass a real smoke test. Otherwise it remains `not_configured` or `unavailable`.