---
component: 04_KERNEL.md
status: RECONSTRUCTED (original MISSING) — invariants + negative costs + mini index
provenance: >
  Invariant texts are verbatim from their locking sources: claud2.txt (INV-17/INV-18/Revised
  INV-18, April 2026 session exported May 12-14 per DEC-01), session-13 transcripts (R-INV-07,
  R-RT-QAF-01, R-RT-PD-01 FIRM locks, U53/U56), fold_laminate_v0_1.py (F1-F6, extant original),
  LEDGER/STATE 2026-07-16. The operator-voice kernel ("How to work with me") lives in
  00_OPERATOR_ABOUT_ME.md §A — recovered byte-verified, not duplicated here.
  Found original outranks on discovery. Never mutate this file's invariants; supersede by pointer.
---

# 04 — Kernel: Invariants · Negative Costs · Mini Index

## Invariants (never mutate; supersession only by operator ROOT statement citing the ID)

**INV-17 — Mid-stream provisional; narrative is the methodology.** No final assessment until the last human turn is processed. Operator narrative is system specification, not padding.

**INV-18 — Authority asymmetry** (verbatim, claud2.txt ~byte 252,444): *"Human turns have root authority. AI turns have proposal authority only… the system drifts toward confident AI language instead of human intent…"*

**Revised INV-18 — with influence acknowledgment** (verbatim, claud2.txt ~byte 255,842; never propagated to skill v1 — carried now per O-02): *"Human turns hold root authority over intent and canon. AI turns hold influence over the operator's working model… Neither can be discarded during re-read… Flag phantom commitments as model corruptions."* Includes the re-read protocol — the functional anti-erasure mechanism.

**INV-04 — Q-A-F atomic** (mosaic_engine_v0.1.md, extant): Q-A-F is the atomic change unit; Q+A without F is an open ticket. Phantom commitments are Q+A without F — intercept at emit time.

**R-INV-07 [FIRM]** (session 13, T10): authority asymmetry as locked runtime rule.

**R-RT-QAF-01 [FIRM]** — Q-A-F provenance chain / authority hierarchy: substrate canon > application canon > operator F in active session > AI A without F. Proposed as R-RT-05 in R-list v0.2 (U52); FIRM by operator F at U53 (Config B); locked in live authority use by operator turn U56: *"Authority placed per R-RT-QAF-01."*

**R-RT-PD-01 [FIRM]** — Phantom Commitment Detection, pre-emit. Behavioral lineage from operator turns U31/U43/U45/U47; locked by U56: *"Phantom-resolution audit method SUPERSEDED by R-RT-PD-01."* Reaffirmed U57: phantom commitments must not leak into a transfer pack.

**M4 — Precedence + coverage, never an action limiter** (operator, authoritative, 2026-07-16): operator conversational input outranks structured AI output on conflict — regenerate the structured output, never the reverse. Chunking/parsing must not drop operator deltas. *"it was never intended to prevent or limit the ai from action."*

**State ladder (DEC-08):** conversational guidance < proposed < accepted < operative < persisted < runtime-enforced. A change is not done until you can name the rung it reached and the dependents it touched.

**Fold invariants F1–F6** (fold_laminate_v0_1.py, fail-closed): F1 no-flatten · F2 provenance-complete (anti-skeleton) · F3 no-silent-fill · F4 no-silent-merge · F5 root-authority · F6 append-only.

## Negative costs (what the documented failures actually cost — read these as prices, not anecdotes)

- **FOIL collapse:** a full tier language (macro.micro.tactical.variable+1; stanza.section.line.word; duplicate upshift) reduced by a later synthesis pass to "a frequency count + one edge case." The fold engine's self-test carries this exact case as a fixture.
- **Hundreds of lines lost to chunked parsing:** SEM, FOIL, phases, and agent interactions dropped in structured summaries that then outranked the source (M4 origin).
- **Six months of skeleton files:** the ten-step mechanism in 03_WHY_AI_DEFAULTS_HERE.md, run repeatedly.
- **The highest-authority ruling in the corpus never persisted:** operator-ratified FIRM canon (R-list v0.2, 96 entries / 92 FIRM, Config B, version trinity) exists only inside session-13 transcripts; the v5c canon register never mentions v4.5.5, and a persisted draft still carries conflicting K7/K8 semantics (V1, grep-confirmed and independently validated 2026-07-19).
- **A working skill shipped as a skeleton:** 9 of 10 components missing from the installed package (P0-a) — every session that "loaded the skill" got the contract without the catalog.

## Mini index (where authority lives)

- Operator voice: `00_OPERATOR_ABOUT_ME.md` (recovered kernel §A, verbatim fragments §B) · `OPERATOR_CONTEXT.md` (thin; SOURCE_PENDING marked)
- Method: `01_METHODOLOGY.md` · workflow: `05_WORKFLOW.md` · root cause: `03_WHY_AI_DEFAULTS_HERE.md` (found draft, verbatim)
- Catalog: `02_FAILURE_MODES.md` (18 modes + 2026-07 field notes)
- Mechanical: `python/` (parse · coverage · phantom-detect · fold/laminate) · prompts: `patterns/`
- Evidence: `examples/` (verbatim corpus passages) · state: `state_snapshot_2026-07-19/` (snapshot, NOT SSOT)
- SSOT: `D:\maestro-on-mosaic\_PROVENANCE\` (STATE.md · LEDGER.md · OPEN.md) — this package is a transfer pack; on conflict the SSOT wins.
