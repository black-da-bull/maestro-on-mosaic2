# CONTINUATION — 2026-09-14 — AUDIO ANALYSIS v0.5 PROMOTION

Doctrine: **Your Vision. Our Mission.**

## Current promoted state

The Maestro browser/runtime and audio-analysis orchestration lanes are now promoted to current `main`.

Promoted merge sequence:

1. PR #16 — browser MVP connected to accepted Technical UST runtime.
   - merge commit: `0ac963d784eb68c7e2e70b090e0aeb98d91d51e0`
   - workforce/golden/browser/intake/parity CI: PASS
   - Vercel production deployment: READY
2. PR #20 — reconciled v0.4/v0.5 audio-analysis evidence and renderer-learning checkpoint.
   - merge commit: `e726dd862ab93da226d919f2b4d3b60f79de4d71`
   - evidence/continuation promotion only; no model output or Technical UST canon promotion
3. PR #21 — v0.5 audio-analysis gateway integrated into `runtime/maestro-workforce`.
   - merge commit: `5f2bb4fce8e6b4b81ecb5547cd85aed12ca59cc6`
   - CI: PASS across workforce, golden structural fixture, creator-facing MVP contract, audio-analysis gateway contract, compiler/bundle/runtime parity, standalone browser parity, and intake proposal contract
   - Vercel production: READY
   - live `GET /api/health`: HTTP 200
   - live `GET /api/audio-analysis/capabilities`: HTTP 200, schema `maestro.audio.gateway.v0.5`

At this checkpoint the GitHub PR worktree is clean: superseded PRs #2 and #14 are closed, historical-frontend dependency PR #18 is closed as out-of-scope for active runtime surfaces, and promoted PRs #16/#20/#21 are merged.

## Approved authority boundary

The current audio-analysis authority order is:

`deterministic measurement -> labeled model inference -> calibration evidence -> operator listening judgment`

Hard boundaries now enforced at the runtime gateway:

- `technical_ust_mutation = false`
- `canon_promotion = false`
- `renderer_policy_promotion = false`
- `keeper_or_release_approval = false`
- `operator_decision_required = true`
- `auto_promotion = false`

No universal quality score is authorized.

Renderer-learning status progression remains:

`observation -> candidate_heuristic -> validated_heuristic -> renderer_policy`

Anything above `observation` requires explicit operator confirmation. A renderer policy must be model/version scoped and reversible.

## v0.5 runtime integration now in force

The active deployed runtime contains a lightweight fail-closed audio-analysis gateway. It does not install heavyweight MIR/GPU models into the Vercel web process.

Supported adapter IDs:

- `beat_this`
- `songformer`
- `chordmini`
- `basic_pitch`
- `advanced_amt`
- `clap`
- `audio_language`
- `statistical_embedding`

The gateway now enforces:

- logical artifact references rather than arbitrary URL/file fetch instructions;
- immutable lowercase SHA-256 source identity;
- deterministic-analysis prerequisite identifiers;
- strict adapter allowlist;
- bounded request/context/worker-response sizes;
- HTTPS for remote worker transport;
- strict worker job envelopes;
- strict per-adapter result envelopes;
- provenance requirements and source-identity agreement;
- rejection of unknown fields, duplicate/missing results, malformed statuses, and unprovenanced outputs.

The gateway routes are:

- `GET /api/audio-analysis/capabilities`
- `POST /api/audio-analysis/jobs`
- `GET /api/audio-analysis/jobs?job_id=...`
- `POST /api/renderer-learning/validate`

## Resolved blockers / contradictions

### RESOLVED — browser authority duplication

The older browser-local PRs #2 and #14 are closed. PR #16 is the promoted browser/runtime path. Browser surfaces do not widen Technical UST ownership.

### RESOLVED — Vercel Python entrypoint

Main previously failed deployment because no Python entrypoint was discovered. PR #16 established the deployable runtime. During PR #21 integration a second routing issue was discovered: the Vercel project root is `runtime/maestro-workforce`, so a repository-root wrapper did not receive audio-analysis requests. The active runtime-root `gateway_entry.py` plus nested `pyproject.toml` now pins `[tool.vercel] entrypoint = "gateway_entry:app"`. Production capability and health endpoints both return HTTP 200.

### RESOLVED — adapter-output trust gap

Worker results are no longer accepted as arbitrary JSON. Result/job structure, provenance, adapter identity, evidence class, source SHA, and completed-result coverage are validated fail-closed.

### RESOLVED — source mutation / arbitrary fetch risk

The v0.4 package already proved source/snapshot immutability. The deployed gateway further refuses arbitrary remote/file source references; durable workers receive logical artifact identity plus immutable SHA evidence.

### RESOLVED — false true-peak PASS

The accepted v0.4/v0.5 package rule stands: when true peak was not measured, `AUDIO.TRUE_PEAK.001` is `not_assessed`, never PASS.

### RESOLVED — evidence versus canon ambiguity

Experimental model evidence, renderer observations, and operator judgments remain separate from Technical UST mutation and canon promotion. The gateway encodes that boundary rather than relying on documentation alone.

### RESOLVED — historical dependency churn treated as active work

PR #18 targeted historical `code/D-Maestro/.../frontend` trees with no active caller/deployment path. It is closed. Dependency/security updates should be reapplied if a historical frontend is deliberately reactivated.

## Remaining execution dependency — external analysis worker

`MAESTRO_AUDIO_WORKER_URL` is currently unconfigured in production, and `/api/audio-analysis/capabilities` therefore reports `worker.configured = false`.

This is **not a blocker to the promoted runtime contract**. It is the next experimental-infrastructure dependency for actual heavyweight inference.

The deployment split is intentional:

- **Vercel:** browser, API, authority validation, job orchestration
- **dedicated durable worker:** Beat This / SongFormer / harmony / AMT / CLAP and other heavyweight analysis
- **OpenAI reasoning layer:** structured evidence interpretation after measured/MIR facts exist
- **operator:** creative and listening authority

Until a worker is configured, job submission must fail closed rather than claiming inference occurred.

## Experimental model status

Implemented/accepted as adapter contracts and calibration surfaces, but no new heavyweight production inference is claimed by this promotion:

- Beat This — worker execution prerequisite remains
- SongFormer — worker execution prerequisite remains
- ChordMini — worker execution prerequisite remains
- Basic Pitch — worker execution prerequisite remains
- advanced AMT — worker execution prerequisite remains
- CLAP — worker execution prerequisite remains
- audio-language reasoning — worker/provider execution prerequisite remains

The built-in statistical descriptor/calibration baseline remains non-semantic and must not be interpreted as a general quality score.

## Bitter Thank You calibration fixture

`Bitter Thank You` remains the first calibration fixture because it includes known project evidence across original render, A/B states, a known silent/invalid artifact, full-mix candidate, stems, MIDI, Studio claims, and operator listening decisions.

Known evidence retained from the validated v0.5 session package includes:

- silent Contrast artifact rejected before higher-order analysis;
- A versus Preferred B waveform correlation approximately `0.999438`;
- Preferred B versus Full Mix approximately `0.899101`;
- Original versus Full Mix approximately `0.694648`;
- Full Mix approximately 5.1 LU below Preferred B, requiring temporary level matching for a fair audition;
- fallback tempo estimate around 103.36 BPM remains explicitly labeled `librosa_fallback`, not Beat This or canonical project tempo.

These observations are fixture/calibration evidence, not renderer policy.

## Formal OPEN-item governance

`_PROVENANCE/OPEN.md` retains its explicit rule: numbered `O-*` items close only by an explicit operator statement citing the item ID.

This promotion does not silently close numbered OPEN items. A technically discharged or non-blocking item may remain formally OPEN until that operator gate is satisfied. That governance rule is not itself a product blocker.

## Next execution order

1. Provision an isolated durable analysis worker and bind `MAESTRO_AUDIO_WORKER_URL`/token server-side.
2. Bring up Beat This first and calibrate its beat/downbeat/tempo evidence against Bitter Thank You project evidence.
3. Add SongFormer and compare detected structure against declared lyrics/Technical MAP evidence.
4. Run Basic Pitch and advanced AMT against Suno MIDI while retaining transcription as inference rather than ground truth.
5. Add ChordMini/harmony disagreement reporting.
6. Add CLAP/embedding calibration only after operator-labeled comparison pairs/groups exist.
7. Run audio-language reasoning only over deterministic/MIR evidence and preserve contradictions between model interpretation and measured facts.
8. Execute the first controlled Suno v6 repeated-take experiment with renderer settings, including Variety/Max Mode where applicable, recorded as first-class inputs.
9. Promote no renderer heuristic automatically.

## Continuation checkpoint

Current repository authority after this promotion:

- `runtime/maestro-workforce/` — accepted active runtime
- `apps/maestro-browser-mvp/` — current browser surface
- `maestro-current/` — generated current bundle
- `_PROVENANCE/` — acceptance/state/continuation evidence

Historical corpus files remain evidence, not active instructions unless deliberately re-promoted.
