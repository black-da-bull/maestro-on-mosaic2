# STATE — Carried-Forward Working State
**Version:** 0.1 (2026-07-16) · Fold of LEDGER M1–M7 + DEC-01..06 · Load this at the start of every Maestro session before doing anything else.

## State ladder — rungs (DEC-08; a change is not done until you can name the rung it reached)
conversational guidance < proposed change < accepted decision < operative state (LEDGER) < persisted artifact (files) < runtime-enforced (consumed by Maestro).

## Operating rules in force (method register)
1. **Authority/precedence (M4, E1–E4 lineage):** operator conversational input outranks structured AI output on conflict; structured output is regenerated, never the reverse. This rule governs evidence weight and coverage — it never limits AI action.
2. **Coverage (M4):** any chunked parse, summary, compaction, or handoff must verify operator-delta survival (per-chunk counts reconciled against full text; mutation IDs enumerated in every handoff).
3. **Canon = fold (M2):** reconciled working state from the event record; polished artifacts never overwrite originating dialogue.
4. **Six E's at session end (M3):** extension, enhancement, exemplification, explanation, impact propagation, application re-optimization — then a continuation packet (STATE version + LEDGER delta + OPEN items).
5. **Elicitation (M6):** operator decisions via interactive multiple-choice + Other, batches 3–5, ≤15/round, with context.
6. **Contradictions:** logged in OPEN.md, never silently harmonized. Supersession only by later explicit operator statement citing the mutation ID.
7. **Persistence (M1):** nothing operative lives only in conversation. If it isn't in _PROVENANCE/ files or a runtime-consumed artifact, it doesn't exist next session.
8. **Rung-naming (M9):** every claim of change names the rung it reached and the dependents it touched. No rung, no integration.
9. **Calibration (M9/M10):** before any corpus-scale pass, validate the frame on one small verifiable case. Canonical example: the Ayo "Run It To Me" covers (operative + persisted, wrong context — M1 in miniature).
10. **Cross-surface SSOT (M11/DEC-07):** this folder is the single source of truth. External surfaces (claude.ai projects) carry pointer docs only, never doctrine copies. `CLAUDE.md` at folder root auto-loads this state for folder-connected sessions.
11. **Mediated coverage (M8, operative):** coverage checks enumerate [mediated] operator decisions (interactive widgets) alongside verbatim user turns.

## Evidence registers (reconstruction domain)
- **Timeline:** `P0_EVIDENCE_INVENTORY_v0_1.md` §1 (T01 2025-05-07 → T17 2026-07-16). Internal dates authoritative; mtimes flattened ~2026-06-18 (M7).
- **Primary transcript copies (DEC-02):** `artifacts/D-Maestro/sources/`.
- **Recovered:** `recovered/KERNEL_from_im_dead_kb_2026-05-20.md` (operator-kernel ancestor).
- **T14 extractions:** `T14_extractions/` — COMPLETE 2026-07-16, 5 files, full operator-turn coverage, 59 candidate mutations provisional pending P2.

## Runtime canon register (Maestro/MOSAIC/UST/SEM/SEG/FOIL) — NOT modified by this file
Pointer only: `artifacts/D-Maestro/canon/` (v5c Root/Spine/Lineage/Conflict register, OS v4.5.2 monolithic prompt, SEG files). Status: **presumptively stale where postdated by corrections** — staleness map is a P1+ deliverable. No runtime mutation has been made by the 2026-07-16 session.

## Next actions
1. ~~T14~~ ~~M8~~ ~~P1-narrow (session 13)~~ DONE — 61 mutations, 9 contradictions, finding V1 → 2. **Operator: validate `P1_narrow/P1_NARROW_IMPACT_MAP.md` §1–§4 and rule on the R-list v0.2 reconstruction (O-13)** → 3. Operator: skill-files search (DEC-03) + design-project export/pointers (O-12) → 4. splitter repair (O-14), then full P1 sweep T01–T13 → 5. P2 classification (61 session-13 + 59 T14 mutations) → 6. skill rebuild with M4/DEC-01 annotations.
