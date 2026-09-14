# Maestro Worktree Resolution and Promotion Record — 2026-09-14

**Doctrine:** Your Vision. Our Mission.  
**Scope:** repository worktree cleanup, browser/runtime promotion, and audio-analysis evidence reconciliation.

## Decision

The browser/runtime deployment lane is promoted. The experimental audio-analysis lane remains evidence/calibration-scoped until its implementation is integrated into the current repository runtime and passes repository promotion gates.

## Repository evidence

### Browser/runtime lane

PR #16 head `15d44c6ef1d135f6183d19664ff66736d5715ad7` passed the repository CI workflow including:

- integrated workforce validation;
- golden structural-interpretation fixture;
- creator-facing MVP contract fixture;
- compiler/bundle/runtime parity validation;
- standalone browser parity;
- intake proposal contract.

Its Vercel preview was READY and `GET /api/health` returned HTTP 200. PR #16 was then merged to `main` as `0ac963d784eb68c7e2e70b090e0aeb98d91d51e0`. The resulting production Vercel deployment also reached READY and its `/api/health` endpoint returned HTTP 200.

This resolves the prior `main` Python-entrypoint/deployment blocker. Renderer observations remain explicitly non-canonical and do not mutate Technical UST authority.

### Superseded lanes

- PR #2: closed, superseded by the later browser reconciliation/integration path.
- PR #14: closed, superseded by PR #16.
- PR #18: closed, because it updates historical `code/D-Maestro/.../frontend` trees rather than the active `runtime/maestro-workforce/` and `apps/maestro-browser-mvp/` surfaces. Security updates should be applied if one of those historical frontends becomes an active caller; merging dependency churn into inactive historical code is not a current runtime fix.

## Audio-analysis lane

The v0.5 session package remains approved for controlled calibration/renderer-learning execution and reports 74 passing tests. It includes deterministic measurement, strict adapter contracts, source immutability, calibration records, renderer experiment records, operator assessments, and an operator-gated heuristic lifecycle.

Heavy Beat This, SongFormer, ChordMini, Basic Pitch, advanced AMT, CLAP, and direct audio-language model environments were not configured on the session host. Their absence is an adapter execution prerequisite, not a blocker to the deterministic runtime or evidence model. No heavyweight inference is claimed.

The v0.5 implementation is **not yet integrated into `runtime/maestro-workforce/`**. Therefore merging this checkpoint promotes evidence/continuation state only, not runtime code or Technical UST canon.

## Open/contradiction disposition

1. **Deployment contradiction — RESOLVED.** `main` previously failed Vercel entrypoint discovery while PR #16 previews succeeded. Promoting #16 produced a READY production deployment.
2. **Duplicate browser authority paths — RESOLVED.** #2 and #14 are closed; #16 is the promoted browser/runtime path.
3. **Historical dependency PR treated as live work — RESOLVED.** #18 is closed and preserved as history.
4. **“Delivered adapter” versus “model executed” ambiguity — RESOLVED BY CLASSIFICATION.** Adapter contract/bridge/runtime integration and actual heavyweight inference are separate states. Unconfigured models remain `not_configured`.
5. **Sites editability — EXTERNAL/NON-BLOCKING.** No available tool exposes the private OpenAI Sites source/editor in this run; no site edit is claimed.
6. **Numbered `_PROVENANCE/OPEN.md` items — AUTHORITY-GATED.** The register requires explicit operator closure citing the item ID. This run does not silently close those items. Items already technically discharged/non-blocking remain so; formal close awaits the required operator citation.

## Next promoted execution order

1. Persist this evidence checkpoint on current `main`.
2. Create a fresh integration branch from current `main` for v0.5 runtime mapping; do not patch historical runtime copies.
3. Map only the minimal v0.5 components needed for AudioAnalysisService, adapter registry/calibration, experiment records, and background job boundaries.
4. Keep heavyweight model environments outside the Vercel request runtime.
5. Run repository integration/promotion validators plus the v0.5 audio-analysis test suite.
6. Deploy a preview and exercise health/API/job boundaries.
7. Then calibrate Beat This -> SongFormer -> AMT -> embeddings -> audio-language reasoning on Bitter Thank You.
8. Begin controlled Suno v6 repeated-take experiments only after analyzer calibration records exist.
9. Promote renderer heuristics only through explicit operator-gated lifecycle; never from sample count alone.

## Promotion boundary

**Promoted:** browser/runtime vertical slice, deployability, worktree cleanup, audio-analysis evidence/checkpoint.  
**Not promoted:** experimental model outputs, session-package code into current runtime, renderer policies, keeper/master decisions, Technical UST mutations, or any numbered OPEN item requiring explicit operator close.