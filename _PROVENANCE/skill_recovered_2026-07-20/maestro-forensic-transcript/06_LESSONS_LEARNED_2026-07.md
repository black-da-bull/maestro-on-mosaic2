---
component: 06_LESSONS_LEARNED_2026-07.md
status: NEW (update layer — this is the v1.0 → v1.1 delta, fold of LEDGER M1–M11 + V1 + P1N validation)
provenance: >
  LEDGER.md / STATE.md / OPEN.md (operator-ratified, 2026-07-16) and
  REPAIR.P1N.PANEL-VALIDATION.R1 (PASS, 2026-07-19). Snapshot copies ship in
  state_snapshot_2026-07-19/; the SSOT is D:\maestro-on-mosaic\_PROVENANCE\.
---

# 06 — Lessons Learned (2026-07 update layer)

## Operator-ratified method mutations (LEDGER, authoritative/operative)

- **M1** Dialogue is not a persistent mutation engine. State exists only when externalized to files consumed next session. Prior sessions are an evidence-grade mutation record, not applied state.
- **M2** Canon = the reconciled working state (fold of events), not a doctrine document. Polished artifacts never overwrite originating dialogue.
- **M3** Session close = the six E's (Extension, Enhancement, Exemplification, Explanation, Impact propagation, Application re-optimization) + continuation packet.
- **M4** The INV-18 lineage is a precedence + coverage rule, NEVER an action limiter. Chunked parses must verify operator-delta survival. Lineage: E1 eldrik raw instruction → E2 INV-18 → E3 Revised INV-18 → E4 R-INV-07/R-RT-PD-01 [FIRM].
- **M5** The v1 skill package was a skeleton: 9 of 10 components missing. This package is the repair (see MANIFEST for per-file status).
- **M6** Elicitation: operator decisions via interactive multiple-choice + Other, batches 3–5, ≤15/round, context attached.
- **M7** Multi-machine consolidation: duplicates and flattened mtimes are expected artifacts; internal dates authoritative.
- **M8** Coverage must enumerate tool-mediated operator decisions ([mediated]) — widget answers do not render as user turns.
- **M9** Calibration step · rung-naming rule · narrow P1 start (most-corrected session first, then STOP for validation).
- **M10** Ayo "Run It To Me" covers = canonical calibration example (operative AND persisted, wrong context — M1 in miniature).
- **M11** Cross-surface SSOT: the repo folder is the single source of truth; external surfaces carry pointer docs only.

## Validation results (P1N, 2026-07-19 — independent reproduction, verdict PASS)

Confirmed from source: the 61-mutation / 9-contradiction session-13 replay; the split (character-lossless after CRLF→LF); REC-A/REC-B recoveries with no third missed input; R-list v0.2 totals 96/92/3/1 verbatim in transcript; V1 (FIRM canon persisted nowhere); canon register carries zero v4.5.5 references; Revised INV-18 present in claud2.txt and absent from skill v1; recovered kernel byte-identical to im_dead_kb.zip. Full scorecard: state_snapshot_2026-07-19/P1_NARROW_VERDICT.yaml.

New facts the validation added:

- **MF-1** Say "character-lossless after CRLF→LF normalization," not "byte-lossless."
- **MF-2** The correction-density marker set behind session selection was never persisted — rank reproduced, numbers not. Persist every metric with its run (now FM-15).
- **MF-3** Operator file-attachment events don't render as user turns — enumerate them (extends M8).
- **MF-4** Declare quote-normalization conventions; two "verbatim" quotes had flattened line breaks.
- **MF-5** Non-text canon members (zip, pdf) escape grep sweeps — name the gap.
- **MF-6** `drafts/maestro_v0.md` K7/K8 semantics conflict with session-13 FIRM Config B — a persisted artifact actively contradicting ratified canon. Routed to O-13; not patched.

## Operator rulings in force for this package

- **2026-07-19 (this session):** "the files need to be created. do this before continuing. use updated understanding and prediction to infer optimized solution." — supersedes the DEC-03 *hold* on reconstruction. The DEC-03 *search* continues, and its priority rule survives: **found originals outrank these reconstructions**; on discovery, replace the reconstructed file and record the diff in the ledger.
- **DEC-01:** claud2 = April 2026 session, exported May 12–14 (annotated in SKILL.md v1.1 provenance).
- Open items carried, not resolved here: O-03 (component search), O-04 (session-ID mapping), O-05 (suppressed-output audit), O-12 (design-project export), O-13 (R-list v0.2 reconstruction — top repair candidate), O-14 (splitter repair — partially addressed by parse_transcript_v0_2.py's R1/R2/R3 audits; full repair pending).
