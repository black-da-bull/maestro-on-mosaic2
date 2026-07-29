---
component: 05_WORKFLOW.md
status: RECONSTRUCTED (original MISSING) — W0–W9 rebuilt from the pipeline positions named in
  fold_laminate_v0_1.py ("skill SS05 W0-W9"), the found 03 draft's W5 reference (lineage records),
  and the practice validated by P1-narrow + REPAIR.P1N.PANEL-VALIDATION.R1 (PASS, 2026-07-19).
provenance: Found original outranks on discovery. Phase names for W5 anchored; others reconstructed.
---

# 05 — Workflow W0–W9

Each phase has a mechanical frontend (python/, no model) and a classification layer (patterns/, model). Mechanical always runs first. Gates between phases are STOP points — operator F or verified output, never momentum.

**W0 — Congruency + inventory.** Restate what is canonical and what is open from the state pack (STATE/LEDGER/OPEN snapshot); get the operator's yes (KERNEL: establish congruency). Inventory sources: paths, sizes, hashes, internal dates (mtimes unreliable after consolidation — M7). Declare primaries (DEC-02 pattern). Gate: operator confirms scope.

**W1 — Calibration (M9).** One small verifiable case end-to-end before any corpus-scale pass. Gate: calibration case reproduces.

**W2 — Mechanical split.** `python/parse_transcript_v0_2.py`: role-tagged contiguous segments, CRLF-normalized (state the normalization), zero-gap verified. Includes the O-14 repairs: assistant-tail sweep for embedded operator inputs, attachment-event chrome detection, transcript-within-transcript "You said:" disambiguation. Gate: `python/verify_coverage_v0_1.py` passes (concat == normalized source; role census; every operator segment present).

**W3 — Operator extraction.** Operator verbatim file + enumeration of [mediated] decisions (M8) and attachment events (MF-3). Spelling and spacing preserved; quote-normalization conventions declared (MF-4). Gate: coverage line reconciles counts against full text (M4).

**W4 — Replay classification (backward-primary).** Pattern-driven, per segment, in stream order after a backward pass has fixed Z: candidate mutations with id · type · scope · status · rung reached · direct/indirect impacts · flags (patterns/classify_mutation.md). Recovered inputs numbered at true stream position, never renumbered. Gate: mutation tally + status table internally consistent.

**W5 — Lineage records** [anchored name]. Supersession chains by pointer (ADR discipline); the recursive decision tree reconstructed from branch points; contradiction register with both sides verbatim (patterns/register_contradiction.md). Gate: no silent harmonization — every closed conflict cites the operator turn that closed it.

**W6 — Phantom audit.** `python/phantom_detect_v0_1.py` over AI turns: commitment language without subsequent ROOT ratification → flagged, never promoted (R-RT-PD-01). Gate: zero unflagged phantoms in the fold input.

**W7 — Fold + laminate.** `python/fold_laminate_v0_1.py` (extant original): one session → one Fold; laminate append-only; nulls and conflicts carried as declared first-class state; F1–F6 fail-closed. Never fold this-session outputs as source. Gate: engine invariants pass.

**W8 — Validation pass.** Independent reproduction before promotion: provenance (hashes), coverage (re-split), mutation traces (verbatim probes at offsets), contradiction reproduction, persistence search with declared scope and near-match records. This is the P1N six-pass shape that returned PASS on 2026-07-19 — reuse it. Gate: PASS / PARTIAL / FAIL verdict written; PARTIAL loops to the defect, FAIL stops the corpus work.

**W9 — Emit + session close.** Clean / AI-optimized / RAG-ready artifacts: stable IDs, frontmatter, rung named per claim, impact map, repair candidates as proposals. Session close = the six E's (M3) + continuation packet (STATE version, LEDGER delta, OPEN items) — state travels as an ATP, phantom-free (U57). Gate: every output names the rung it reached; nothing operative lives only in conversation (M1).

## Standing rules across all phases

- Elicitation: operator decisions via multiple-choice + Other, batches 3–5, ≤15/round, context attached (M6).
- Narrow start: corpus sweeps begin with the single most-corrected session, then STOP for validation (M9) — and the density metric that picks it ships with its marker set (FM-15).
- Fabric discipline: one pattern, one job; compose via pipes; no mega-prompts.
- Verified-then-display: iterate in the background until correct; no process chatter (U31/U45).
