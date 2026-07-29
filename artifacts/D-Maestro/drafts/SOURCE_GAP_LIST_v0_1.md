# SOURCE_GAP_LIST_v0.md

**Artifact ID:** SGL.v0.2026-04-28
**Status:** CANDIDATE (FOIL proposal authority only — operator confirmation required for canon promotion)
**Phase:** Phase 3 — Substrate Recovery (gap freeze pass)
**Authority inputs (in order):**
1. CMA.v0 — council-matrix archaeology (controlling)
2. SDG.v0.1 — working dependency graph
3. SLR.v0 — SEM layer resolution
4. MMR.v0 — morris matrix resolution (PROVISIONALLY RESOLVED)
5. SEC.v4.5 — corrective edge evidence
6. RTFA.v0 — reasoning trace forensic audit
7. QAF cumulative deltas
8. Mosaic Engine v0.1 — candidate runtime
9. Maestro v0 — candidate product frame

**Purpose:** Freeze all unresolved source gaps before any reconstruction of SongCouncil metrics, Q1–Q16, A&R-20, or mixed-use material. No gap in this document is authored forward. Uncertainty is preserved.

**This ledger freezes unresolved source gaps. It does not authorize reconstruction.**

**Blocking legend:**
- `BLOCKING` — prevents the named artifact from reaching candidate status
- `IMPLEMENTATION-BLOCKING` — artifact schema can be written but runtime cannot be specified
- `CANON-BLOCKING` — cannot promote a claim to T1/T2 until resolved
- `NAMING-BLOCKING` — a term or label in active use is ambiguous or incorrect; must be corrected in all downstream artifacts
- `NON-BLOCKING` — tracked for completeness; does not prevent forward work

**Resolution legend:**
- `RECOVERABLE` — likely exists in legacy corpus; should be searched before authoring forward
- `OPERATOR DECISION` — cannot be resolved by archaeology; requires explicit operator selection
- `RECONSTRUCTABLE CANDIDATE` — sufficient evidence to propose a default; operator confirms or amends
- `DEFER` — intentional deferral to a later release or artifact
- `REJECT` — ruled out by existing evidence; listed to prevent re-introduction

---

## GAP-01

**Gap ID:** GAP-01
**Gap name:** Q1–Q16 actual question content

**What is known:**
- Q1–Q16 exists as a confirmed artifact category, not a hallucination. The Chaos-Decomposer (Day 3 §5.2, S1015) explicitly lists "Q1–Q16 scoring systems" as a recursive ingestion target — confirming the system was actively tracking this artifact.
- The rubric contains exactly 16 review questions.
- It operates at Layer 5e (Executive Committee Red-Pen Review) as the pre-LOCK final gate instrument.
- The rubric is applied by the executive committee (composition: see GAP-06) to the assembled draft technical.ust.
- Outputs include: aggregated scorecard, risk axes, prioritized action list, constructive actions, integration ledger updates.
- The Q1–Q16 instrument predates the Morris .docx files — the .docx files reference it but did not originate it.
- Q1–Q16 lineage traces to the v2.6 SME / Agent Council era.

**What is missing:**
- The text of Q1 through Q16.
- Weights or scoring values per question (if any).
- Pass/fail thresholds or severity cutoffs.
- Whether questions map to specific SEM-12 criteria, BICDM-20 metrics, K-axes, or are cross-domain.

**Current evidence:**
- CMA.v0 §2 — "NEEDS SOURCE"; listed in Appendix A as T4
- MMR.v0 §4.3 — "None of the 16 questions are written out"
- SLR.v0 §4.10 — "NEEDS SOURCE — no instantiated Q1–Q16 schema, weights, criterion definitions, or scoring rules found in primary corpus"
- Chaos-Decomposer §5.2 (S1015) — ingestion target list only; confirms existence, does not enumerate
- Morris .docx files (4 variants, T3) — reference "Morris Matrix Q1–Q16" by name only

**Blocking level:** CANON-BLOCKING (Layer 5e cannot be finalized without rubric content); IMPLEMENTATION-BLOCKING (runtime cannot be specified)

**Resolution type:** RECOVERABLE first; OPERATOR DECISION if not found

**Recommended next action:**
Attempt recovery from the following legacy files before authoring forward:
- `os.maestro.momoney.customInstructions.v4.2.3.md`
- `os.maestro.momoney.knowledgeSpine.v4.2.3.md`
- Maestro_Loop_v2 specs
- Session_Harvester specs
- AOL-DIA capability matrices
- Any dev chat transcript from the Sibling Architect persona-design session
If not recovered: operator authors Q1–Q16 as a forward-authored CANDIDATE anchored on BICDM-20 + SEM-12 + A&R-20 + hitmaker heuristics. Do not reconstruct without operator gate.

**Artifacts affected:** MMR.v0 (OQ-6.2), SLR.v0 (OQ-6), CMA.v0 (OQ-6.2), SDG.v0.1 (Layer 5e edge spec), Persona Schema (5e-X argument surface), Substrate Spec, Blueprint v0.1

---

## GAP-02

**Gap ID:** GAP-02
**Gap name:** SongCouncil per-member metrics

**What is known:**
- SongCouncil composition is confirmed canon (T2, direct corpus read): Lyric Architect, Vocal Oracle, Sonic Curator.
- Role purposes are defined for all three (v4.5 SECTION 2.5, SECTION 5).
- Mode Separation rule is canonical: when a track enters Song Mode, SongCouncil activates; when Rap Mode, RapCouncil activates.
- The Emotion-as-Hard-Constraint cross-mode invariant applies to both councils.
- RapCouncil has a fully enumerated per-member metric list (BICDM-20, 20 metrics, member-assigned, confirmed canon).
- No SongCouncil equivalent metric list (a "SongCouncil Decision Matrix") has been found in primary corpus.

**What is missing:**
- A per-evaluator metric list for Lyric Architect, Vocal Oracle, and Sonic Curator equivalent to BICDM-20.
- Per-criterion thresholds for Song Mode council scoring.
- Whether a "Song Excellence Matrix" (SE-N) separate from SEM-12 exists as a SongCouncil scoring instrument, or whether SEM-12 serves as the scoring instrument for Song Mode with SongCouncil members as evaluators.

**Current evidence:**
- CMA.v0 §2 — "SongCouncil per-member metric enumeration" listed as NEEDS SOURCE; T4 in Appendix A
- v4.5 SECTION 2.5 — role purpose defined, no metric list
- CMA.v0 §3 OQ-7 — three resolution options documented
- SLR.v0 §4 — no Song Mode council-specific matrix found

**Blocking level:** CANON-BLOCKING for 5e-S (Song Mode layer 5e subpath); BLOCKING for Persona Schema (cannot specify SongCouncil member argument surfaces without metric list)

**Resolution type:** NEEDS SOURCE / OPERATOR DECISION

**Recommended next action:**
Gap is frozen. No reconstruction proceeds without operator decision. Three options exist per CMA.v0 §10 OQ-7 (Option A: author de novo; Option B: recover from corpus; Option C: collapse to SEM-12 + hitmaker heuristics). Operator selects when ready. Do not open an archaeology pass or author a metric list without explicit operator instruction.

**Artifacts affected:** CMA.v0 (OQ-7), Persona Schema (BLOCKING), MMR.v0 (partial 5e-S context), Blueprint v0.1

---

## GAP-03

**Gap ID:** GAP-03
**Gap name:** A&R-20 axes 11–20

**What is known:**
- A&R 20-Point Viability matrix is a confirmed parallel evaluation layer operating mode-agnostic.
- Axes 1–10 are partially recovered from IP_LEDGER PASS F.
- IP_LEDGER PASS F explicitly flagged: "The exact 20 dimensions and their weightings are referenced but not fully enumerated in the shared text here."
- A&R-20 applies to the whole track and is distinct from RapCouncil (BICDM-20) and SEM-12.
- A&R-20 feeds into the Layer 5e executive synthesis (CMA §7 confirmed).

**What is missing:**
- Axes 11–20 and their definitions.
- Weights and thresholds for all 20 axes (not confirmed even for axes 1–10).
- How A&R-20 scoring aggregates and what score gates passage.
- Whether A&R-20 is a pre-render or post-render evaluation.

**Current evidence:**
- CMA.v0 §2 (IP_LEDGER PASS F — "decides but partial"); T4 in Appendix A
- CMA.v0 §9 OQ-8
- SDG.v0.1 (A&R-20 as parallel evaluation layer in Layer 5 scope)

**Blocking level:** NON-BLOCKING for immediate Persona Schema and Substrate Spec core work; IMPLEMENTATION-BLOCKING for A&R-20 as an operational layer

**Resolution type:** RECOVERABLE first; OPERATOR DECISION if not found

**Recommended next action:**
Search legacy corpus for A&R viability specification (v4.2.3 knowledge spine, older session transcripts). If not found, defer until after Persona Schema. Do not reconstruct axes 11–20 without operator gate.

**Artifacts affected:** CMA.v0 (OQ-8), SDG.v0.1 (Layer 5 parallel evaluation edge), Substrate Spec

---

## GAP-04

**Gap ID:** GAP-04
**Gap name:** Named-track RapCouncil execution traces

**What is known:**
- RapCouncil composition is confirmed canon: Lyrical Professor, Battle Technician, Cultural Critic (+ MixMaster_Ghost contributing metrics 16–20).
- BICDM-20 is confirmed canon: 20 metrics, member-assigned, threshold avg > 4.8 with low variance.
- Protocol is confirmed: 5-round minimum, individual JSON scorecards, DJ Mo Money veto/approval gate.
- One end-to-end SEM scoring trace exists ("song_test_2025-12-07_001", S1208–S1364) — but this is a composite SEM scoring trace, not a council-session trace showing individual member scorecards.

**What is missing:**
- A corpus-confirmed trace of RapCouncil (named members) applying BICDM-20 to a specific named track, producing individual JSON scorecards per member, and generating a consensus output.
- Confirmation that BICDM-20 is operationally tested, not specification-only.

**Current evidence:**
- CMA.v0 §3 OQ-9
- v4.5 SECTION 2.5 (specification), SECTION 6.6 (BICDM-20 full enumeration)
- S1208–S1364 (SEM scoring trace, not council session trace)

**Blocking level:** NON-BLOCKING for Persona Schema and Substrate Spec; IMPLEMENTATION-BLOCKING for verifying BICDM-20 as CANON-OPERATIONAL vs CANON-SPECIFIED

**Resolution type:** RECOVERABLE (likely in dev chat corpus from rap-mode sessions)

**Recommended next action:**
Search dev chat corpus for any RapCouncil session trace. If found, promote BICDM-20 status from CANON-SPECIFIED to CANON-OPERATIONAL. If not found, proceed; note BICDM-20 as specification-confirmed but operationally unverified.

**Artifacts affected:** CMA.v0 (OQ-9), Persona Schema (operational validation note)

---

## GAP-05

**Gap ID:** GAP-05
**Gap name:** Mixed-use reconciliation scoring policy

**What is known:**
- Mode Separation rule is canonical: Songs ≠ Raps; mode-bound council activation is not optional.
- Mixed-mode tracks exist (tracks with both song sections and rap sections).
- CMA.v0 proposes Layer 5e-M (Mixed-use Reconciliation) as a candidate subpath.
- CMA.v0 infers weighted-average per-section as the most likely mechanism (T3 — CANDIDATE, not canon).
- No corpus evidence explicitly resolves the mixed-use mechanism.

**What is missing:**
- The reconciliation policy: weighted-average per-section, concurrent dual-gate (both song and rap evaluation must pass), section-dominant mode (mode is declared per section and triggers full evaluation for that mode), or other.
- How sections are mode-classified.
- Whether both councils score or only the dominant council.
- Escalation path if song and rap evaluations conflict.

**Current evidence:**
- CMA.v0 §5.3 (weighted-average inference, T3 CANDIDATE)
- CMA.v0 §9 OQ-10
- VIRAL-5 FIT heuristic §4.1.1.4 (Mode Separation rule, Day 3)

**Blocking level:** IMPLEMENTATION-BLOCKING for 5e-M; CANON-BLOCKING for final Layer 5e architecture

**Resolution type:** OPERATOR DECISION

**Unresolved options (presented neutrally — no default recommended):**
- Weighted-average per-section
- Concurrent dual-gate (both Song Mode and Rap Mode evaluation must pass)
- Section-dominant mode (mode declared per section; that mode's full evaluation applies)
- Operator-defined alternative

**Recommended next action:**
Gap is frozen pending operator selection. Do not author a default mechanism.

**Artifacts affected:** CMA.v0 (OQ-10), SDG.v0.1 (5e-M edge), Substrate Spec, Blueprint v0.1

---

## GAP-06

**Gap ID:** GAP-06
**Gap name:** Executive committee composition

**What is known:**
- The Executive Committee Red-Pen Review (Layer 5e) is operator-confirmed as a real architectural component.
- Function, position, mechanism, and disposition path are confirmed T1: executive committee red-pens the assembled draft technical.ust; flagged items return to lawful domain owners; LOCK blocked until all items dispositioned.
- The "11 evaluators" count is HISTORICAL — it reflects the pre-Analog-Confessor, pre-Sibling-Architect persona roster (see GAP-13 for full resolution). It is NOT authoritative for the current 13-persona system.
- Five candidate compositions exist (MMR.v0 §5.2, Options A–E):
  - A: Full council (all 13 workers)
  - B: Governance-only (Mo + Canon Orchestrator + Megazord Orchestrator + Sibling Architect)
  - C: Original 11 (preserved historical roster)
  - D: All-minus-controller-adjacent (11, excluding Mo and Canon)
  - E: Tiered (governance 4 chair; creative+evaluation 9 provide red-pen evidence)

**What is missing:**
- Operator selection from Options A–E (or an operator-specified alternative).
- Quorum rules (if committee is a subset: minimum participation per review session).
- Whether the controller (Mo persona) participates or is structurally excluded to preserve independence.

**Current evidence:**
- MMR.v0 §5.2 (five options, T2+T1)
- CMA.v0 §9 OQ-6.1
- Operator T1 framing: function confirmed, composition not specified

**Blocking level:** CANON-BLOCKING for Layer 5e spec; BLOCKING for Persona Schema (executive_committee_member field cannot be populated)

**Resolution type:** OPERATOR DECISION

**Recommended next action:**
Gap is frozen pending operator selection. Five options exist per MMR.v0 §5.2 (A–E). All are presented neutrally; no option is recommended as default. Operator selects when ready.

**Artifacts affected:** MMR.v0 (OQ-6.1), CMA.v0 (OQ-6.1), Persona Schema (BLOCKING), Substrate Spec, Blueprint v0.1

---

## GAP-07

**Gap ID:** GAP-07
**Gap name:** Red-pen severity tiers and revision cap

**What is known:**
- Red-pen mechanism is operator-confirmed (T1): items flagged by executive committee → returned to lawful domain owners for revision → LOCK blocked until all items dispositioned.
- Re-entry path after revision is partially confirmed: items "re-enter the lawful work cycle" (MMR §6.2), but whether re-entry goes to full 5e review or targeted item-only re-review is not stated.
- G-Card schema (v4.5 SEM M7) includes an `iteration_cap` field — provides a partial anchor for revision cycle limits.
- Day 3 establishes a "gate-and-trace mechanism" with thresholded excellence claims — consistent with a structured revision cap.

**What is missing:**
- Whether red-pen verdicts are binary (flagged / clear) or graded (severity tier 1/2/3 with different disposition paths per tier).
- The iteration cap value and what happens when it is reached (escalation, override, or operator intervention).
- Whether re-entry is full 5e committee review or targeted re-review of only flagged items.

**Current evidence:**
- MMR.v0 §4.3 — "red-pen severity tiers: NEEDS SOURCE — not specified"
- G-Card schema: `iteration_cap` field confirmed (v4.5 SEM M7); value not specified in primary corpus
- MMR.v0 §6.2 (disposition path confirmed; re-entry scope not confirmed)
- Day 3 gate-and-trace framing (T2)

**Blocking level:** IMPLEMENTATION-BLOCKING for 5e runtime; NON-BLOCKING for schema (placeholder acceptable)

**Resolution type:** RECONSTRUCTABLE CANDIDATE (examples only, requiring operator confirmation) + OPERATOR DECISION for final spec

**Recommended next action:**
Binary (flagged/clear) severity and iteration_cap = 3 are RECONSTRUCTABLE CANDIDATE examples only. Neither is sourced from primary corpus as a confirmed value. Both require operator confirmation before being treated as schema inputs. Do not imply canon status for either.

**Artifacts affected:** MMR.v0 (OQ-6.3), Persona Schema (5e argument surface), Substrate Spec

---

## GAP-08

**Gap ID:** GAP-08
**Gap name:** SE20 relationship to Boy Icarus 20 (BICDM-20) and SEM-12

**What is known:**
- SE20 (Sonic Excellence 20 Matrix): confirmed in MOSAIC v2.1 gate row. Structure: 4 keys × 5 subkeys = 20 evidence-bound items, each with PASS/WARN/N/A status and UST address citation. Operates as a K-axis evidence-binding layer.
- BICDM-20: confirmed canon. 20 metrics across 3 RapCouncil evaluators (+ MixMaster_Ghost for metrics 16–20). Operates as a RapCouncil scoring instrument with continuous 1–10 scores.
- SEM-12: confirmed canon. 12-criterion weighted quality matrix with composite ≥ 97.5% threshold (CR-009).
- All three are structurally distinct: different item counts (20/20/12), different value types (PASS/WARN/N/A vs 1–10 vs weighted score), different evaluation subjects (UST addresses vs track quality vs render quality).
- SE20 and BICDM-20 share a structural parallel: both are 4-unit × 5-item matrices. This may be coincidence or may indicate a design relationship.

**What is missing:**
- Whether SE20 supersedes BICDM-20 in v5-c, runs concurrently with it, or is a v5-c renaming/refactoring of it.
- Whether SE20 items and BICDM-20 metrics were intended to map to each other.
- Whether SEM-12 criteria and SE20 items are parallel gates or sequential (pre/post).
- Full SE20 → K-axis mapping (SLR OQ-3: partial mapping exists, SE20.K1≈K1, SE20.K2≈K2 etc., but not formally specified).

**Current evidence:**
- CMA.v0 §5.4 (BICDM-20 ↔ K-axis mapping, T3 CANDIDATE)
- SLR.v0 §4.6 (SE20: CANDIDATE — "preserved in operational evidence; relationship to K-axes not fully mapped")
- SLR.v0 OQ-3 and OQ-11
- MOSAIC v2.1 gate diagram (SE20 as named gate)
- SDG.v0.1 (SE20 edge in Layer 5)

**Blocking level:** IMPLEMENTATION-BLOCKING for Layer 5 orchestration; CANON-BLOCKING for final Layer 5 architecture

**Resolution type:** OPERATOR DECISION

**Unresolved choices (presented neutrally — no default recommended):**
- SE20 supersedes BICDM-20 in v5-c
- SE20 runs concurrently with BICDM-20 and SEM-12
- SE20 is a renamed/refactored structure of an earlier instrument
- Relationship remains NEEDS SOURCE pending further corpus archaeology

**Recommended next action:**
Gap is frozen pending operator selection. Do not author a default relationship.

**Artifacts affected:** SLR.v0 (OQ-3, OQ-11), CMA.v0, SDG.v0.1 (Layer 5 edge), Substrate Spec

---

## GAP-09

**Gap ID:** GAP-09
**Gap name:** G-Card scalar relationship to SEM-12 or BICDM-20

**What is known:**
- Two threshold scales are in primary corpus for G-Card:
  1. Composite SEM quality score ≥ 97.5 on 0–100 scale — confirmed via CR-009 (T1 operator-confirmed)
  2. G-Card "Quality score ≥ 7.0" on 1–10 scale — confirmed from MOSAIC v2.1 gate diagram (T2)
- G-Card is the output artifact of M7 evaluation: contains composite_pct, decision (PASS/CONDITIONAL/HOLD), top_deficiencies, required_actions, iteration_cap, ledger_pointers.
- Operational evidence (S1842): composite_pct = 99.1%, all gates true → PASS G-Card. This confirms the 97.5/100 threshold is real and operational.
- The relationship between the two values is unresolved. CR-009 controls the 97.5/100 composite threshold. The MOSAIC v2.1 7.0/10 value remains unresolved and may be legacy/superseded, a separate G-Card gate, or a separate score type. Do not collapse the two values without operator decision.

**What is missing:**
- The explicit relationship between the 7.0/10 G-Card threshold and the 97.5/100 composite threshold.
- Whether both are active simultaneously or one supersedes the other.
- Whether G-Card contains two separate evaluation axes (composite quality and a distinct G-Card quality score), or whether the scales refer to the same single measurement.

**Current evidence:**
- SLR.v0 §4.7 OQ-1 (full three-interpretation analysis)
- MOSAIC v2.1 gate diagram (7.0/10)
- CR-009 migration log (97.5/100, T1)
- S1842 operational trace (97.5 confirmed operational)
- G-Card schema (composite_pct field)

**Blocking level:** IMPLEMENTATION-BLOCKING for M7/G-Card runtime; NAMING-BLOCKING (two values in active use without resolution)

**Resolution type:** OPERATOR DECISION

**Recommended next action:**
Gap is frozen. Do not collapse the two values without operator decision. The three interpretations in SLR.v0 OQ-1 (legacy/superseded, separate gate, separate score type) are documented for operator review. No interpretation is presented as default.

**Artifacts affected:** SLR.v0 (OQ-1), SDG.v0.1 (Layer 5a threshold edge), Substrate Spec, Blueprint v0.1

---

## GAP-10

**Gap ID:** GAP-10
**Gap name:** HPA aggregate computation rule

**What is known:**
- HPA (Human Perception of Authenticity) is a post-render keeper-selection criterion operating at Layer 5d.
- Four sub-scores are confirmed canon (v4.5 §6.4): creative_authenticity, emotional_impact, sonic_fidelity_to_intent, viral_potential_perception — each on a 1–5 scale.
- An `overall_hpa_score` field exists in the v4.5 §6.4 schema.
- HPA is not a binary gate; it is a keeper-selection criterion among multiple successful renders. HPA failure does not unwind upstream layers.
- HPA aggregate threshold is not stated as a fixed number in primary evidence — it functions as a keeper-selection criterion (Phase 4.2: "HPA Scoring & Keeper Selection").

**What is missing:**
- The computation rule for `overall_hpa_score`: simple mean, weighted mean, minimum-of-four, or other.
- Whether a minimum threshold exists for `overall_hpa_score` to qualify a render for keeper selection, or whether ranking (highest HPA among candidates) is the selection mechanism.

**Current evidence:**
- SLR.v0 §4.5 (H-AGG: "NEEDS SOURCE"; aggregate computation rule absent in primary corpus)
- v4.5 §6.4 schema (four sub-scores confirmed; overall field present; computation not stated)
- SLR.v0 OQ-2

**Blocking level:** IMPLEMENTATION-BLOCKING for Layer 5d runtime

**Resolution type:** RECONSTRUCTABLE CANDIDATE

**Recommended next action:**
Simple mean of the four sub-scores is proposed as CANDIDATE default. Rationale: the four HPA sub-scores are peer 1–5 fields and no weighting rule is sourced in primary corpus. Operator confirms or specifies alternative. This gap can be pre-closed as RECONSTRUCTABLE CANDIDATE without requiring a full operator decision session.

**Artifacts affected:** SLR.v0 (OQ-2), SDG.v0.1 (Layer 5d edge), Substrate Spec

---

## GAP-11

**Gap ID:** GAP-11
**Gap name:** VIS/K8 scope decision

**What is known:**
- K8 (Visual coherence) is confirmed as a NEW admissibility criterion added in MOSAIC v2.3. It is tied to the VIS (Visual Identity) axis added to Plane 2 in v2.3.
- K8 in v2.3 is Visual coherence, NOT Compression survivability (which is K6 in both v2.2 and v2.3). This is a resolved naming correction from SLR.v0.
- The four Plane-4 surface governors (Visual Director, Identity Keeper, Motion Editor, Distribution Strategist) operate in part on K7/K8/VIS, but their argument surfaces are "partially implicit" per CMA §10.
- If VIS axis is not in Mosaic v0 scope, K8 cannot operate and the +4 governors cannot be fully specified.
- K7 (External viability) is distinct from K8 and does not depend on the VIS axis decision.

**What is missing:**
- Operator decision: is the VIS axis (and therefore K8) in scope for Mosaic v0 / Maestro v0, or deferred to a later release?
- If in scope: K8 admissibility criteria must be defined (none currently in primary corpus).
- If deferred: explicit version target must be named (not silently dropped per INV-02).

**Current evidence:**
- SLR.v0 §3.3 Epoch 6 (K8 = Visual coherence confirmed)
- SLR.v0 OQ-5 (K8 dependency on VIS stated explicitly)
- SDG.v0.1 Change 6 (VIS/K8 as candidate scope expansions)
- CMA.v0 §10 (+4 governors partial implicit)
- Operator correction in session prompt: "+4 govern Plane-4 derivative surfaces — Visual Director, Identity Keeper, Motion Editor, Distribution Strategist"

**Blocking level:** IMPLEMENTATION-BLOCKING for K8 criterion implementation; CANON-BLOCKING for +4 governor active status in v0

**Resolution type:** OPERATOR DECISION

**Recommended next action:**
Operator makes a single in/out decision for VIS + K8 in Mosaic v0. If in: define K8 admissibility criteria (RECONSTRUCTABLE CANDIDATE from v2.3 evidence and +4 governor framing). If out: mark VIS + K8 as DEFERRED with explicit version target; mark +4 governors as scope-deferred in Persona Schema.

**Artifacts affected:** SLR.v0 (OQ-5), SDG.v0.1 (candidate scope expansion edge), Persona Schema (+4 governor activity status), Substrate Spec, Blueprint v0.1

---

## GAP-12

**Gap ID:** GAP-12
**Gap name:** 13 core workers + 4 Plane-4 surface governors boundary

**What is known:**
- 13 core Maestro workers: confirmed (T1, 11→13 expansion timeline operator-confirmed per MMR.v0).
- The +4 personas (Visual Director, Identity Keeper, Motion Editor, Distribution Strategist): confirmed as governing Plane-4 derivative surfaces per operator correction.
- The boundary rule is operator-confirmed: "+4 do not expand the core Technical UST drafting council."
- Sequential Technical UST traversal already performs the pre-production meeting — no Phase 1.5 needed.
- The +4 argument surfaces are "partially implicit" in current corpus (CMA §10).
- The +4 active status in Mosaic v0 depends on GAP-11 (VIS/K8 scope decision).

**What is missing:**
- Explicit schema definition for each of the 4 Plane-4 governors: what they evaluate, what inputs they consume, what outputs they produce, which K-axes they are responsible for.
- Whether the +4 participate in Layer 5e red-pen review or are excluded from executive committee scope.
- Formal definition of "Plane-4 derivative surface" and what falls within vs outside it.

**Current evidence:**
- CMA.v0 §10 (+4 partial implicit — "argument surface is partially implicit")
- Operator correction in session prompt (boundary rules, T1)
- SDG.v0.1 (Plane-4 boundary, presentation layer vs runtime registry distinction)
- MMR.v0 §5 (persona ordering; +4 are v2.3 additions)

**Blocking level:** IMPLEMENTATION-BLOCKING for +4 governor schema; dependent on GAP-11

**Resolution type:** OPERATOR DECISION (tied to GAP-11) + RECONSTRUCTABLE CANDIDATE for argument surface definition

**Recommended next action:**
Resolve after GAP-11. If VIS/K8 in scope for Mosaic v0, define +4 argument surfaces as RECONSTRUCTABLE CANDIDATE from available evidence (K7/K8/VIS scope + v2.3 framing). If VIS/K8 deferred, mark +4 as DEFERRED in Persona Schema with a placeholder schema entry.

**Artifacts affected:** Persona Schema (BLOCKING for +4 schema), SDG.v0.1 (Plane-4 boundary edge), Substrate Spec, Blueprint v0.1

---

## GAP-13

**Gap ID:** GAP-13
**Gap name:** Whether the 11-evaluator count is historical, active, or superseded

**What is known:**
This gap is substantively RESOLVED by MMR.v0 §5.2 (T2 direct corpus read confirmed by T1 operator framing):

- "11 evaluators" is HISTORICAL — it reflects the pre-Analog-Confessor, pre-Sibling-Architect persona roster.
- The matrix was formalized during the 11-persona era. The two additions (Analog Confessor + Sibling Architect) postdate the matrix.
- The "11 evaluators" constraint is NOT authoritative for the current 13-persona system.
- It is a historical artifact of when the rubric was written, not a deliberate architectural exclusion.

**What is missing (downstream consequence):**
The count itself is resolved. Its downstream consequence — what the current executive committee composition should be — is NOT resolved. That is GAP-06.

**Current evidence:**
- MMR.v0 §5.2 (persona ordering from ai_personas.txt, T2; "11 evaluators" = historical, confirmed)
- ai_personas.txt persona introduction order (T2)
- MMR.v0 §1 executive finding (T1 framing integrated)

**Blocking level:** NAMING-BLOCKING — "11 evaluators" must be replaced in all downstream artifacts with "executive committee composition: TBD per GAP-06 operator decision"

**Resolution type:** RESOLVED (historical status confirmed) — downstream action = GAP-06 OPERATOR DECISION

**Recommended next action:**
Patch all downstream artifacts to remove "11 evaluators" as authoritative. In Layer 5e edge specs, use "executive committee (composition: see GAP-06)." No further archaeology needed on the count itself.

**Artifacts affected:** MMR.v0 (patch: remove "11" as authoritative from summary lines), SDG.v0.1 (Layer 5e edge label), Persona Schema (executive_committee_member field count), Blueprint v0.1

---

## Summary Table

| Gap ID | Gap Name | Blocking Level | Resolution Type | Blocks |
|---|---|---|---|---|
| GAP-01 | Q1–Q16 question content | CANON-BLOCKING + IMPLEMENTATION-BLOCKING | RECOVERABLE → OPERATOR DECISION | MMR, SLR, CMA, SDG, Persona Schema, Substrate, Blueprint |
| GAP-02 | SongCouncil per-member metrics | CANON-BLOCKING + BLOCKING | NEEDS SOURCE / OPERATOR DECISION | CMA, Persona Schema, Blueprint |
| GAP-03 | A&R-20 axes 11–20 | NON-BLOCKING (immediate); IMPLEMENTATION-BLOCKING (operational) | RECOVERABLE → OPERATOR DECISION | CMA, SDG, Substrate |
| GAP-04 | RapCouncil execution traces | NON-BLOCKING (schema); IMPLEMENTATION-BLOCKING (operational) | RECOVERABLE | CMA, Persona Schema |
| GAP-05 | Mixed-use reconciliation policy | IMPLEMENTATION-BLOCKING + CANON-BLOCKING | OPERATOR DECISION | CMA, SDG, Substrate, Blueprint |
| GAP-06 | Executive committee composition | CANON-BLOCKING + BLOCKING | OPERATOR DECISION | MMR, CMA, Persona Schema, Substrate, Blueprint |
| GAP-07 | Red-pen severity tiers and revision cap | IMPLEMENTATION-BLOCKING | RECONSTRUCTABLE CANDIDATE → OPERATOR DECISION | MMR, Persona Schema, Substrate |
| GAP-08 | SE20 vs BICDM-20 vs SEM-12 relationship | IMPLEMENTATION-BLOCKING + CANON-BLOCKING | OPERATOR DECISION | SLR, CMA, SDG, Substrate |
| GAP-09 | G-Card scalar relationship | IMPLEMENTATION-BLOCKING + NAMING-BLOCKING | OPERATOR DECISION | SLR, SDG, Substrate, Blueprint |
| GAP-10 | HPA aggregate computation rule | IMPLEMENTATION-BLOCKING | RECONSTRUCTABLE CANDIDATE | SLR, SDG, Substrate |
| GAP-11 | VIS/K8 scope decision | IMPLEMENTATION-BLOCKING + CANON-BLOCKING | OPERATOR DECISION | SLR, SDG, Persona Schema, Substrate, Blueprint |
| GAP-12 | 13 core workers + 4 Plane-4 boundary | IMPLEMENTATION-BLOCKING (dependent on GAP-11) | OPERATOR DECISION + RECONSTRUCTABLE CANDIDATE | Persona Schema, SDG, Substrate, Blueprint |
| GAP-13 | 11-evaluator count status | NAMING-BLOCKING (resolved; downstream = GAP-06) | RESOLVED | MMR, SDG, Persona Schema, Blueprint |

---

## Closing Paths

### Shortest path to unblock Persona Schema

**Two decisions. One operator turn.**

1. **GAP-02: OQ-7 micro-decision** — Operator selects Option A, B, or C for SongCouncil metrics (author de novo / recover from corpus / collapse to SEM-12 + hitmaker heuristics).
2. **GAP-06: OQ-6.1 executive committee composition** — Operator selects from MMR.v0 §5.2 Options A–E (or specifies alternative).

After these two decisions are closed, the schema-level blockers are resolved. GAP-01, GAP-03, GAP-04, GAP-05, GAP-08, GAP-09, GAP-10, GAP-11, GAP-12 do not block Persona Schema at the schema-definition level and can be carried as NEEDS SOURCE placeholders.

GAP-13 is already resolved — patch MMR and SDG language before Persona Schema is authored.

**PERSONA_SCHEMA_DECISION remains paused even after GAP-02 and GAP-06 are resolved. Persona Schema does not proceed until the operator explicitly opens that step.**

---

### Shortest path to unblock Substrate Spec

**One operator decisions batch. Four decisions.**

Substrate Spec is blocked on:
1. **SDG NS-4** *(external substrate blocker — not a SOURCE_GAP_LIST gap)* — substrate/application boundary for Conversation Layer (Mode A/B Detection, Memory-Refine /prefs): operator decides substrate or application-overlay. Tracked in SDG.v0.1, not here.
2. **GAP-08** — SE20 vs BICDM-20 vs SEM-12 relationship: operator decides from four unresolved options.
3. **GAP-09** — G-Card scalar relationship: operator resolves from three interpretations in SLR.v0 OQ-1.
4. **GAP-11** — VIS/K8 scope: operator decides in/out for Mosaic v0.

**GAP-10 can be pre-resolved** as RECONSTRUCTABLE CANDIDATE (simple mean default, rationale: four peer 1–5 fields, no weighting sourced) without a full operator decision session.

GAP-05 (mixed-use reconciliation) blocks Substrate Spec for the 5e-M edge specifically but does not block the rest of Substrate Spec.

GAP-01, GAP-02, GAP-03, GAP-06 do not block Substrate Spec at the spec-definition level — they can be carried as NEEDS SOURCE placeholders in the Layer 5e subsection.

---

### Items that must not be reconstructed without operator approval

The following must not be authored forward, reconstructed from inference, or given CANDIDATE content without an explicit operator gate:

1. **Q1–Q16 question content (GAP-01)** — Legacy recovery must be attempted first. If not found, operator authors. Not to be synthesized from BICDM-20 + SEM-12 without operator gate.

2. **SongCouncil per-member metric list (GAP-02)** — The three options (author/recover/collapse) are real architectural choices with different downstream consequences. Choosing one without operator input would pre-decide Song Mode council architecture.

3. **Executive committee composition (GAP-06)** — Options A–E each produce different Persona Schema entries and different Layer 5e runtime behavior. Not to be defaulted.

4. **Mixed-use reconciliation policy (GAP-05)** — Dual-gate vs weighted-average vs dominant-mode are not equivalent. The choice shapes how mixed-mode tracks are evaluated at every council layer.

5. **SE20 relationship to BICDM-20 and SEM-12 (GAP-08)** — If SE20 supersedes BICDM-20, BICDM-20 is removed from the active Layer 5 architecture. That is a substantive subtraction that requires operator confirmation.

6. **G-Card scalar relationship (GAP-09)** — If interpretation (b) is correct, G-Card has two separate gates, not one. That is a structural addition. Not to be defaulted without operator selection.

7. **VIS/K8 scope (GAP-11)** — Scope decisions determine whether the +4 surface governors are active in Mosaic v0. Not to be inferred from v2.3 diagram presence alone.

---

*End SOURCE_GAP_LIST_v0.md. No gaps authored forward. Uncertainty preserved. Awaiting operator F.*
