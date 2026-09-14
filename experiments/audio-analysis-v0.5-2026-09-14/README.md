# Maestro Audio Analysis v0.5 — Calibration + Renderer Learning Checkpoint

**Date:** 2026-09-14  
**Doctrine:** Your Vision. Our Mission.  
**Status:** approved for controlled calibration/renderer-learning execution; **not** Technical UST canon/runtime promotion  
**Parent experimental checkpoint:** v0.4

## Objective

v0.5 preserves the v0.4 deterministic and adapter trust boundaries and adds the missing layer between “an adapter ran” and “Maestro learned something”:

`source -> deterministic measurement -> strict experimental inference -> calibration against project evidence -> operator listening assessment -> observation/heuristic evidence`

No step automatically mutates Technical UST, rewrites prompts, approves a keeper/master/release, or promotes renderer policy.

## Delivered in the reconciled session package

- strict `AdapterCalibrationRecord` contract (`maestro.audio.adapter_calibration.v0.5`);
- Beat This calibration: independent median-IBI tempo, beat/downbeat counts, interval CV, optional expected-BPM delta, timeline coverage;
- SongFormer calibration: declared-vs-detected section sequence, edit-distance similarity, optional boundary-time error, duration coverage;
- AMT/MIDI calibration: independently inspect reference/generated MIDI and compare note count, pitch range, tempo median, and duration summaries;
- `RendererExperimentRecord` preserving objective, starting state, Lyrics Prompt, Style Prompt, Studio instruction, Suno response, model/version, generation settings, references, generated artifacts, analyses, controlled variables, and held constants;
- immutable `OperatorAssessmentRecord` for keep/reject/redirect/neutral listening decisions;
- operator-gated heuristic lifecycle: `observation -> candidate_heuristic -> validated_heuristic -> renderer_policy`;
- renderer policies require explicit operator confirmation and reversibility;
- descriptive repeated-condition effect statistics that report within-condition variance while forcing `causal_claim=false` and `auto_promotion=false`;
- API and CLI surfaces for calibration and renderer-learning records;
- generated JSON schemas for v0.5 records.

## Trust-boundary invariants retained from v0.4

1. Adapter output is structurally validated and malformed/undeclared fields fail closed.
2. External bridges receive read-only snapshots rather than preserved source paths.
3. Preserved source and bridge snapshot hashes are checked before/after execution; mutation invalidates the run.
4. Fast analysis reports true peak as `not_assessed` when it was not measured.
5. Heavy adapters may report `not_configured` without blocking deterministic analysis or unrelated adapters.
6. No universal `quality_score` exists.

## Validation

Current reconciled session package:

- **74 tests passed**, 2 unrelated third-party Python 3.13 deprecation warnings;
- `python -m compileall -q maestro bridges` PASS;
- package hash manifest verification PASS;
- ZIP integrity PASS.

### Real Bitter Thank You HTTP/API E2E

The v0.5 runtime was exercised with the actual `0 Bitter Thank You.wav` through:

1. resumable source upload + immutable registration;
2. source inspection;
3. deterministic `audio_analysis`;
4. `audio_experimental` with the built-in statistical descriptor;
5. `audio_calibration` using the exact prerequisite analysis records;
6. append-only ledger verification.

This proves orchestration/calibration state transitions on a real project artifact. It does **not** claim heavyweight MIR execution on the current host.

## Current model execution boundary

Beat This, SongFormer, ChordMini, Basic Pitch, advanced AMT, CLAP, and direct audio-language bridges remain explicit model-dependent adapters. On the session host they were `not_configured`; no heavyweight inference result is fabricated.

The existing librosa fallback produced a useful-but-cautious tempo estimate around 103.36 BPM for the original fixture. It remains labeled `librosa_fallback`, not Beat This and not canonical project tempo.

## Deployment boundary — reconciled after PR #16 promotion

PR #16 is no longer a blocker or parallel draft stream. It was merged into `main` as `0ac963d784eb68c7e2e70b090e0aeb98d91d51e0`, and the linked Vercel production deployment is **READY**. The deployed `/api/health` endpoint returned HTTP 200 and reports the accepted Technical UST ownership/dependency overlay as authority.

The remaining separation is intentional: the v0.5 audio-analysis implementation exists as a validated session package and evidence checkpoint but has **not** yet been mapped into `runtime/maestro-workforce/`. Heavy MIR/GPU adapters should remain isolated/background workers rather than inline Vercel request handlers.

Recommended deployment topology:

- Vercel: browser/API/job orchestration;
- isolated/dedicated workers: heavy MIR/GPU adapters;
- OpenAI: structured evidence reasoning over measured facts, server-side;
- operator: listening/creative authority.

## Worktree reconciliation

- PR #2 (original browser-local MVP) — closed as superseded by the integrated runtime path.
- PR #14 (browser reconciliation) — closed as superseded by PR #16.
- PR #18 (dependency bumps in historical `code/D-Maestro/.../frontend` trees) — closed as out-of-scope for the active runtime/browser surfaces; update those dependencies if those historical frontends are ever reactivated.
- PR #16 — promoted and production-deployed.
- PR #20 — carries only the experimental audio-analysis evidence/checkpoint; it does not claim the session ZIP is already runtime-integrated.

Formal numbered `_PROVENANCE/OPEN.md` items retain their explicit operator-close rule. Technical work may make an item non-blocking, but this checkpoint does not silently close an `O-*` item without an operator statement citing the ID.

## Next execution

1. Map the v0.5 implementation into a repository integration branch based on current `main`, keeping heavyweight adapters isolated.
2. Run the repository promotion validator plus the audio-analysis 74-test suite against that integrated tree.
3. Provision Beat This in an isolated worker and calibrate it on Bitter Thank You against known project/Studio tempo evidence.
4. Provision SongFormer and compare detected structure with declared lyric/Technical Road-Map evidence.
5. Run Basic Pitch + advanced AMT against Suno MIDI while retaining both as inferred hypotheses.
6. Run CLAP/embedding calibration only after collecting operator-labeled pairs/groups.
7. Run audio-language reasoning only after deterministic/MIR evidence exists.
8. Execute the first controlled Suno v6 repeated-take experiment with renderer settings captured.
9. Promote no renderer heuristic automatically.

## Session package

`Maestro_Develop_v0_5.zip`  
SHA-256: `83e65ebf20aef1b95a4eae9d8449bb1c64bbcdf3a79501d7c388e66adbb3bbe9`

The ZIP remains a conversation/session artifact and is not represented here as already integrated into `runtime/maestro-workforce`.