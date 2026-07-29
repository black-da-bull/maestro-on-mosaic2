# 04_OPEN_DECISIONS_AND_BLOCKERS

Items requiring operator action or external dependency before forward motion. Each entry: what it is · why it blocks · what unblocks it · authority source.

---

## D-list — Operator Decisions Required

### D1. Executive committee composition
- **What:** Which 4 of the 13 personas (or 4 distinct workers) hold the department head roles. Which head owns which output surface.
- **Why it blocks:** Without composition, the executive red-pen review layer (5e) cannot be instantiated. Triad + VIG output ownership is ambiguous.
- **What unblocks:** Operator selection from MMR.v0 §5.2 Options A–E (or new option). Mapping each head to one of 4 surfaces.
- **Authority:** MMR.v0 (PROVISIONAL); WRVV §10 (composition selection FORBIDDEN without operator).
- **Constraint:** Mo is likely one of the 4 heads (likely A/R Persona Surface, given excellence-ratchet role in MOSAIC v2.3 diagram). Not confirmed.

### D2. Headcount disambiguation
- **What:** "21 workers" framing — are these 21 distinct individuals or 17 distinct + 4 dual-role (executive heads drawn from the 13)?
- **Why it blocks:** Workforce instantiation in Maestro v0 cannot resolve. Affects persona registry. Conflict C1.
- **What unblocks:** Operator turn confirming role-count vs headcount semantics.
- **Authority:** WRVV §10 mandates phrasing "13 core + 4 Plane-4 surface governors" — does not resolve distinct headcount.

### D3. SOURCE_GAP_LIST_v0.1 visibility
- **What:** SGL is declared the controlling reference for frozen gaps per WRVV §1 and §9, but is NOT present in `/mnt/project`.
- **Why it blocks:** Any closure attempt against frozen gaps requires SGL cross-check. Without SGL, the WRVV §9 orientation list is approximate, not authoritative.
- **What unblocks:** Either (a) operator surfaces SGL to dev workspace, or (b) operator confirms SGL is intentionally external and authorizes proceeding under the WRVV §9 orientation list as working basis.
- **Authority:** WRVV §1 ("controlling references: SOURCE_GAP_LIST_v0.1 ... ACCEPTED"), §9 ("actual SGL controls").

### D4. Phase 5 teleological collapse — architectural answer
- **What:** General inference-model architecture problem. v4.5 worked around it via monolithic context; v5 split exposed it. Mosaic Engine cannot complete Runtime Design (Phase 5) without an answer.
- **Why it blocks:** Phase 5 Runtime Design cannot proceed. Mosaic Engine remains CANDIDATE.
- **What unblocks:** Architectural answer from operator. Candidate directions per tangent_resumption §10.1: explicit cross-reference primitives as first-class substrate objects (+2 unread).
- **Authority:** tangent_resumption_2026-04-27.md §10.1 (UNSOLVED, PHASE-5 BLOCKER).

### D5. v2.6 corpus assessment strategy
- **What:** Lineage anchor moves from v4.5 to v2.6+. Evidence is in `chat.html` (595 MB), `longDevWorkLog.txt` (present, 342 KB), `longDevWorkLog2.txt` (NOT present). Sectional ingestion strategy needed.
- **Why it blocks:** Depth-accumulation timeline cannot be reconstructed. v2.6 monolith may not be recoverable as standalone artifact.
- **What unblocks:** Operator decision on (a) whether to upload chat.html sectionally, (b) accept v4.5+ as practical anchor and treat v2.6+ as evidence-only, or (c) defer until other priorities clear.
- **Authority:** tangent_resumption §3.3, §10.3, §12.3.

### D6. Workforce default at Maestro v0 mount
- **What:** maestro_v0.md §2 states "5-Council default + 13-worker expansion" — promotion criteria stated, choice not made.
- **Why it blocks:** Application mount cannot finalize. Affects whether the 4 department heads are drawn from 5 or 13.
- **What unblocks:** Operator selection of default. Interacts with D1.
- **Authority:** maestro_v0.md §2.

### D7. Substrate / application boundary
- **What:** SDG.v0.1 NS-4 / OD-4 — Conversation Layer, Mode A/B, `/prefs` boundary between substrate and application is unresolved.
- **Why it blocks:** E17 and E18 edges in SDG remain UNRESOLVED.
- **What unblocks:** Operator decision on which side of the substrate boundary these primitives sit.
- **Authority:** SDG.v0.1 NS-4 / OD-4.

### D8. 4-Plane vs phase-based feedback partition
- **What:** SDG.v0.1 NS-3 / OD-2 — feedback architecture organization is deferred.
- **Why it blocks:** Affects when and how validation feedback flows between layers.
- **What unblocks:** Operator decision on organizing principle.
- **Authority:** SDG.v0.1 NS-3 / OD-2.

### D9. Capture of fresh 4-heads → 4-surfaces framing
- **What:** Today's operator framing (4 department heads map to 4 output surfaces = triad + VIG) is NOT in any artifact yet.
- **Why it blocks:** Will drift / be lost if not captured. Affects D1, D2, D6.
- **What unblocks:** Either operator authorizes a cumulative-deltas entry capturing the framing as T1, or operator drafts it themselves. (Per WRVV discipline, I will not author this delta without explicit instruction.)
- **Authority:** OP-DIRECT this session, not yet ratified into canon.

---

## M-list — Missing Material

### M1. SOURCE_GAP_LIST_v0.1.md
- **Status:** NOT FOUND in `/mnt/project`
- **Need:** Controlling gap ledger per WRVV §1
- **Workaround:** WRVV §9 orientation list (approximate)

### M2. chat.html (595 MB)
- **Status:** NOT FOUND
- **Need:** v2.6+ depth-accumulation timeline evidence
- **Workaround:** longDevWorkLog.txt present (342 KB)

### M3. longDevWorkLog2.txt (262 KB)
- **Status:** NOT FOUND (sibling file longDevWorkLog.txt present)
- **Need:** Continued evidence timeline

### M4. chatgpt_export.txt (55.6 KB)
- **Status:** NOT FOUND
- **Need:** Cross-platform evidence

### M5. ai_personas.txt
- **Status:** NOT FOUND directly. May be contained inside `Maestro_Personas_aka_the_subagents.md` (128 KB, May 3) or `clarity_architect_ii__birth_certificate.txt` (559 KB). Unverified.
- **Need:** Persona definitions referenced in MMR.v0 evidence ledger; required for canonical_employee_module_spec.yaml.

### M6. Yesterday.txt
- **Status:** `Yesterday.md` present (Apr 26); unverified as equivalent.
- **Need:** Blocking dependency for canonical_13_employee_instances.yaml.

### M7. canonical_employee_module_spec.yaml
- **Status:** NOT YET AUTHORED
- **Need:** Next lawful artifact before persona registry per Zero-Day Restore Pack §10.
- **Blocked on:** M5 + M6.

### M8. canonical_13_employee_instances.yaml
- **Status:** NOT YET AUTHORED
- **Blocked on:** M5 + M6 + M7.

### M9. DEFINITIONS_v0.md
- **Status:** NOT YET AUTHORED
- **Need:** Phase 1 deliverable per tangent_resumption §12.2.
- **Note:** Also blocked indirectly per WRVV §10 (BLUEPRINT_v0.1 is FORBIDDEN; DEFINITIONS_v0 may be upstream and lawful, but operator has not authorized).

### M10. CORPUS_MANIFEST_TEMPLATE.md
- **Status:** NOT YET AUTHORED
- **Need:** Source-role taxonomy applied as fillable template.

### M11. Q1–Q16 question content
- **Status:** NEEDS SOURCE per MMR.v0 §3
- **Need:** Executive committee review rubric
- **Workaround:** None. Per WRVV §10, reconstruction FORBIDDEN.

### M12. A&R-20 axes 11–20
- **Status:** NEEDS SOURCE per CMA.v0 §9 OQ-8
- **Workaround:** None. Per WRVV §10, reconstruction FORBIDDEN.

### M13. SongCouncil per-member metric enumeration
- **Status:** NEEDS SOURCE per CMA.v0 §9 OQ-7
- **Workaround:** None. Per WRVV §10, reconstruction FORBIDDEN.

### M14. RapCouncil execution trace for a named track
- **Status:** NEEDS SOURCE per CMA.v0 §9 OQ-9 (corpus evidence gap)
- **Workaround:** None. Do not fabricate.

### M15. Uninspected directories
- `eldrik/` (3.4 MB) — staff-engineer-perspective sessions per operator typology
- `day_3/` (1.4 MB single file) — meta-reflection session on Day 2 failure
- `foil/` (864 KB) — FOIL cascade / tiered-system content
- `AI_OPTIMIZED_PROBLEM_SOLVING_MATRIX/` (20 KB) — sub-agent personas matrix
- **Status:** Not opened during this session.
- **Need:** Each directory's content/role to be classified.

---

## P-list — Procedural Blockers

### P1. Persona Schema authoring is paused
- **Per:** operator instruction (captured in WRVV §10)
- **Cleared by:** operator instruction lifting the pause

### P2. SUBSTRATE_SPEC_v0.1 is blocked
- **Per:** operator instruction (WRVV §10)
- **Cleared by:** operator instruction

### P3. BLUEPRINT_v0.1 is blocked
- **Per:** operator instruction (WRVV §10)
- **Cleared by:** operator instruction

### P4. Treating diagrams as canon is FORBIDDEN
- **Per:** WRVV §10
- **Permanent constraint** — diagrams are diagnostic only

### P5. Promoting CANDIDATE artifacts to canon is FORBIDDEN
- **Per:** WRVV §10 + operator memory
- **Cleared by:** operator ratification per artifact

### P6. Silent reclassification of NEEDS SOURCE to RESOLVED is FORBIDDEN
- **Per:** WRVV §10
- **Permanent constraint**

### P7. Filename-based authority elevation is FORBIDDEN
- **Per:** WRVV §10
- **Detail:** "CANONICAL" in standalone filenames does not override declared control state
- **Permanent constraint**

---

## Priority order for next session

The five items most likely to unblock forward motion, in order:

1. **D9** — capture today's 4-heads framing (cheapest, prevents loss)
2. **D3** — surface or boundary-confirm SGL (unblocks closure attempts)
3. **D1** — committee composition (unblocks 5e instantiation, interacts with D2/D6)
4. **M5/M6** — surface ai_personas.txt and Yesterday.txt (unblocks M7 → M8)
5. **D4** — Phase 5 architectural answer (unblocks Runtime Design)
