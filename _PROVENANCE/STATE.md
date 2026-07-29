# STATE — Carried-Forward Working State
**Version:** 0.7 (2026-07-20) · Fold of LEDGER M1–M18 + DEC-01..28 + CR-V5-STATUS-1 + V1-REPAIR + O16..O16D + REVIEW/REPAIR.O16D.VV.R1 · Load this at the start of every Maestro session before doing anything else.

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
1. ~~P1-narrow → R1/R2 → preflight → V1 repair → O-16 → O16B → O16C~~ DONE (see LEDGER O16C). **[This action chain is SUPERSEDED — M17 suspended version force-close, and O16D disproved the seat-map-blocked-on-CONS premise. Current order lives in the 0.6 block at the end of this file.]**

## Standing method additions (2026-07-19)
- M12: interactive gates — blockers become elicitation questions, never passive stops.
- M13: Roadmap functional migration (timing → section headers; structure → Performance.execution; Intro/Outro sections; fades in section instructions).
- M14: six verbs + two obligations (impact propagation, application re-optimization at session close).
- M15/DEC-09..17: era-authority statement; QAF runtime-only; density retired; SEG naming; DISC closes; eldrik.txt.txt = Yesterday-1 primary.

## M16 in force — migration-bundle epistemology (fold of the LEDGER record)
The repo + uploads are a SELECTED MIGRATION BUNDLE, not the system. Absence ≠ nonexistence; no
"missing" verdict without a recorded search; claims name their lane (KNOWN / PROBABLE / HISTORICAL
/ UNVERIFIED); completeness scopes to reached strata; AI output non-authoritative unless accepted
or migrated.

## O16D EXECUTED — maestro-current v0.4 (2026-07-19)
The v5-b.coldstart.1 pack found COMPLETE in-repo (legacy/maestro_v5b_coldstart/, 19/19 members,
2 displaced files re-bound by hash) — falsifying v0.3's "seat map blocked on CONS drops." Folded:
named seat map IMPORTED (04) · v5b governance address space registered (05) · MAP parity patch
era record beside M13 (02) · Suno parsing discipline + triad cap bands (06) · STRATA map v0.2 ·
SCOPE_CORRECTION_v0_4. MANIFEST v0.4 (33 members), validator PASS. Rung: persisted, RC2.
~~**Next actions:** (1) operator rulings — O-18 topology detail-stratum + force-close of v0.4;~~ **[SUPERSEDED same-day by DEC-27 (O-18 withdrawn as posed) + M17 (force-close suspended) — current order in the 0.6 block below.]** (superseded text continues:)
(2) O-15 prefix registry (now incl. v5b pinset IDs); (3) O-17 CONS drops (search-burden rule);
(4) executable app D1–D4; (5) T01–T13 sweep, chronology order.

## ROOT corrections (interactive, post-O16D) — DEC-27 + M17
DEC-27: v5b TECHNICAL_UST_CANON + GOVERNANCE_ADDENDUM = one unit — the Technical UST and the
record of how quality/governance tie into decision-making as NULLs are replaced (interwoven,
DEC-24 executable form). O-18's rivalry framing withdrawn.
M17: derivation basis = the ENTIRE project history, never a version. Force-close framing
SUSPENDED. **Top next action: MAESTRO.O16E.HISTORY-GROUNDED-DERIVATION** — chronology sweep of
all strata (S1→S9, T01–T17, located sub-strata) verifying every maestro-current statement
against the full history; era columns filled from actual strata; version-only claims demoted to
PROBABLE until confirmed. Then: O-15 prefix registry · O-17 CONS (search-burden) · D1–D4.

## REVIEW.O16D.VV.R1 absorbed + REPAIR executed — bundle v0.5 (2026-07-19)
Independent V&V (orchestrator, operator-relayed): verdict FAIL — V1 V2 V4 V5 V6 V7 PASS · V8 V9
PARTIAL · V3 V10 FAIL · 5 blocking defects. ALL FIVE INDEPENDENTLY CONFIRMED here before repair
(parse test: 1 fail; builder run: v0.2/11-docs + 4 drifted templates; grep: stale force-close +
competing-stratum lines; inventory: 3 unlisted). Repairs: BUILD_REGENERATION_REPORT.yaml re-emitted
(parses; content preserved; repair noted in-file) · validator v2 (A10 recursive parse + A11
inventory completeness) · builder v2 (FULL member set from templates+trees; deterministic MANIFEST
from build/manifest_meta.yaml; self-checking drift report) · M17/DEC-27 propagated through
00_ROOT_SPEC, MANIFEST class + v5b note, SCOPE_CORRECTION (supersession section; its own stale
lines named candidly), templates refreshed 13/13 · inventory classes declared; 39 members listed.
Proof: clean-dir regeneration byte-identical (builder exit 0) · validator v2 PASS. Rung: persisted,
REPAIRED-CANDIDATE class (v0.5).

## Current next actions (0.6 — SUPERSEDED as the live ordering by the 0.7 block below; retained as era record)
1. **O16E HISTORY-GROUNDED-DERIVATION** (M17): full-chronology sweep S1→S9 / T01–T17 verifying
   every maestro-current statement against the actual strata; version-only claims held at
   PROBABLE until confirmed. 2. Re-issue V&V package (v0.5) for orchestrator re-review; absorb.
3. O-15 prefix registry (incl. v5b pinset IDs). 4. O-17 CONS drops under the search-burden rule.
5. Executable app (P-4 phase 2; D1–D4). 6. P2 classification · skill rebuild (unchanged).

## 2026-07-20 ROOT rulings folded — v5 status · REPLAY LAW · loss-diagnosis correction (v0.7)
Three live-thread ROOT rulings persisted this session (LEDGER: CR-V5-STATUS-1, M18, DEC-28) — closing the M1 gap where they lived only in conversation.
- **CR-V5-STATUS-1:** v5 (v5/-a/-b/-c/.5) is admissible design evidence, not a failure; the forensic "failed POC/WIP" label is lineage-only (names the distribution-without-linkage loss; v4.5.5 remains the last GREEN build). yesterday/Day2–4/eldrik = one continuous thread.
- **M18 REPLAY LAW:** reconstruction = walk one dev-thread's Q–A–F cycles as deltas; nothing freezes until operator says DONE; merge keeps unique + merges duplicates; DELETION alone requires explicit operator statement; no verdict until replay concludes. Procedure for M17's derivation.
- **DEC-28 loss-diagnosis correction:** the losses were FULL SEM · FULL FOIL · FULL agents+storyline+"act as" defs · excellence statements — not "substrate." Day 4 holds the detailed schemas that were progressively reduced.

## Current next actions (0.7 — the ONLY live ordering; 0.6 and earlier are era records)
1. **O16E HISTORY-GROUNDED-DERIVATION** (M17 basis + M18 procedure): walk the full chronology (S1→S9 / T01–T17 + located sub-strata) as Q–A–F deltas, verifying every maestro-current statement against the actual strata; version-only claims held PROBABLE. **Scope verification to the DEC-28 four loss-classes** — confirm maestro-current carries full SEM (05), full FOIL Face A + Face B, full agent seat storylines + "act as" defs (04), and the excellence statements; thinned = regression to repair. Treat all v5 strata as admissible design evidence (CR-V5-STATUS-1). Freeze nothing until operator DONE.
2. Reconcile the executable runner (Rebirth MVP) to the maestro-current 02 Creative-UST container grammar (this session — in progress).
3. Re-issue V&V package (v0.5) for orchestrator re-review; absorb.
4. O-15 prefix registry (incl. v5b pinset IDs). 5. O-17 CONS drops (search-burden rule). 6. Executable app (P-4 phase 2; D1–D4). 7. P2 classification · skill rebuild.

## 2026-07-20 — forensic skill v1.1 packaged + installed (LEDGER SKILL-REPKG-1)
The `maestro-forensic-transcript` skill is no longer a skeleton. The v1.1 ATP (2026-07-19) was packaging-repaired (SKILL.md frontmatter restored verbatim from `SKILL_v1_ORIGINAL.md`; slug + forward-slash zip fixed) and **installed** at `.claude/skills/maestro-forensic-transcript/` (31 files, folder CLAUDE.md per M19), superseding the v1.0 skeleton by pointer. Upload build archived at `_PROVENANCE/skill_v1_1/upload_build_2026-07-20/`.
- **Discharged-in-package, landed in SSOT:** O-01 (claud2 dating annotation), O-02 (Revised INV-18 in contract #2), O-07 (parse + phantom-detect extractors). Effective on the claude.ai surface once re-uploaded.
- **Still open:** O-03 original-file sweep (found originals outrank these reconstructions, DEC-03).
- **Next-action 7 update:** "skill rebuild" is DONE and installed; the remaining step is the operator's manual claude.ai re-upload (delete skeleton → upload the 2026-07-20 build zip). P2 classification still pending.
