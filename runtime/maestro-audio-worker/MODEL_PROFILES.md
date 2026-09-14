# Model profiles and isolation policy

The worker core is intentionally lightweight. Heavy model environments are optional and may be deployed as dedicated images or sidecars. Model availability is evidence, not authority.

## Beat This

Reference: `CPJKU/beat_this`. Upstream exposes `File2Beats`; checkpoints may be selected by name or local path. Maestro chooses CUDA only when PyTorch reports CUDA available; otherwise `auto` selects CPU. An explicitly requested unavailable CUDA backend fails rather than silently changing evidence conditions.

For reproducible deployment, pre-seed and hash-pin a local checkpoint and set `BEAT_THIS_CHECKPOINT`; do not treat successful package import as proof that a checkpoint executed.

```bash
docker build --build-arg EXTRA_REQUIREMENTS=requirements-beat-this.txt -t maestro-audio-worker:beat-this .
```

## SongFormer

Reference: `ASLP-lab/SongFormer`. Keep its model/checkpoint environment outside the worker core and configure `MAESTRO_SONGFORMER_COMMAND_JSON`. SongFormer output remains inferred section evidence, not canonical MAP/lyrics structure.

## ChordMini

Reference: `ptnghia-j/ChordMini`. Use `MAESTRO_CHORDMINI_COMMAND_JSON`. Chord labels remain model inference and must be calibrated against project evidence/listening.

## Basic Pitch

Reference: `spotify/basic-pitch`. When the `basic-pitch` executable exists, Maestro invokes it directly. Generated MIDI is an inferred transcription and never replaces source MIDI.

```bash
docker build --build-arg EXTRA_REQUIREMENTS=requirements-basic-pitch.txt -t maestro-audio-worker:basic-pitch .
```

## Advanced AMT / tsumugi

Reference: `anime-song/tsumugi`. Configure `MAESTRO_ADVANCED_AMT_COMMAND_JSON`. Keep checkpoints/cache in the dedicated model environment and record the actual backend/model provenance returned by the bridge.

## CLAP

Reference: `LAION-AI/CLAP`. The worker can use `laion-clap` directly. Embedding distances have no Maestro meaning until calibrated on operator-labeled examples; no universal quality score is allowed.

```bash
docker build --build-arg EXTRA_REQUIREMENTS=requirements-clap.txt -t maestro-audio-worker:clap .
```

## Audio-language reasoning

`MAESTRO_AUDIO_LANGUAGE_COMMAND_JSON` accepts evidence-grounded reasoning only. The bridge receives measured/MIR evidence in `{context}` and must return `claims` with non-empty `evidence_refs` plus a `contradictions` list. Maestro marks the result advisory, preserves contradictions, and never promotes it into Technical UST/canon automatically.
