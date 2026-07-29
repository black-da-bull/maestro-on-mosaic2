# SUBSTRATE_DEPENDENCY_GRAPH_v0.1.md

**Artifact ID:** SDG.v0.1.2026-04-28
**Inputs:** RTFA.v0.2026-04-28 (candidate graph) · SEC.v4.5.2026-04-28 (corrective evidence) · Operator decisions OD-1 through OD-5
**Status:** CANDIDATE — proposal authority only. Operator confirmation required for promotion to substrate canon.
**Replaces:** RTFA.v0.2026-04-28 §5 (Substrate Dependency Graph)

---

## 1. Revision Summary

This artifact revises RTFA.v0 §5 against the SEC.v4.5 forensic audit. Eight categories of change:

**1. Cognitive Operators Layer restructured.** Sense-Think-Act and Tri-Attention restated as co-required parallel primitives instead of directed feed. Per SEC E01: v4.5 corpus presents both as parallel always-on monitors, not as sequential pipeline. The directed edge in RTFA.v0 was unsubstantiated.

**2. DSRP coupling weakened.** Tri-Attention → DSRP feed marked NEEDS SOURCE. DSRP → Conversation Layer feed REJECTED. DSRP exists as independent cognitive operator; coupling to either Tri-Attention or Conversation Layer lacks primary evidence.

**3. Conversation Layer lineage corrected.** Conversation Layer marked Chimera-Indigo-sourced per OD-4. v4.5 had distributed conversation discipline rules but did not consolidate them as a discrete substrate primitive. Lineage attribution is now explicit on every edge.

**4. Workforce schema corrected.** Per OD-1, the canonical worker schema is the v4.5 9-element flat schema (mission, decision_lens, do_rules, dont_rules, synergy_hooks, bounded_domain, bounded_non_domain, conflict_boundaries, persona_name), not the v5-c 4-layer Persona Stack. The Persona Stack is preserved as presentation grouping only.

**5. Strategy/Mode separation.** Per OD-3, Strategy Selector (10 strategies, v4.5) and Operating Mode (4 modes, v5-c) are now separate orthogonal layers — Strategy = how a worker reasons, Mode = how workers orchestrate. RTFA.v0 had these collapsed.

**6. Triad/ATP dependency reversed.** Per SEC E14: Triad depends on definitive `technical.ust` LOCK (not on ATP). ATP packages Triad plus lineage. RTFA.v0 had this dependency direction inverted.

**7. New substrate primitives added.** E16 (Framework Orchestrator 10-strategy), E17 (Mode A/B detection), E18 (Memory-Refine /prefs with TTL), E19 (5 Implicit Structuring Tools), E20 (Sequential Departmental Processing) — all evidenced in v4.5 primary corpus and absent from RTFA.v0 §5.

**8. Feedback layer split.** Per OD-2, Cross-Plane Feedback function is CANON. Both 4-plane partition (v5-c) and phase-based feedback (v4.5) coexist as CANDIDATE structures pending runtime design selection.

**SEC count reconciliation:** SEC.v4.5 §1 confirmed-edge table listed six edges (E04, E07, E09, E10, E11, E12). The closing line in SEC stated "Five edges CONFIRMED" — a transcription error. Authoritative count is **six confirmed edges** in SEC.v4.5. SDG.v0.1 promotes all six to CANON.

---

## 2. Corrected Graph Overview

The substrate is a layered directed dependency system. Each layer's outputs are inputs to the next layer. Cognitive Operators run on every turn. Operating Cadence governs emission. Workforce supplies bounded SME labor. Execution traverses Technical UST under SME labor. Canon Layer is the single source of truth. Admissibility runs concurrently during creation. Output Contract is the only externally visible surface. Feedback closes loops across all layers.

```
┌─ LAYER 0 — COGNITIVE OPERATORS (per-turn, parallel) ─────────────────┐
│                                                                       │
│   Sense-Think-Act  ⟂  Tri-Attention      DSRP        Structuring     │
│   (co-required parallel primitives)    (independent)   Tools (5)      │
│                                                                       │
└──────────────────────────────┬────────────────────────────────────────┘
                               │
                               ▼
┌─ LAYER 1 — OPERATING CADENCE (Chimera-Indigo sourced) ────────────────┐
│                                                                       │
│   Conversation Layer ◀── Mode A/B Detection ──▶ Memory-Refine /prefs  │
│   (governs emission)     (session entry path)    (preference TTL 90d) │
│                                                                       │
└──────────────────────────────┬────────────────────────────────────────┘
                               │
                               ▼
┌─ LAYER 2 — WORKFORCE (v4.5 / Day 3 sourced) ──────────────────────────┐
│                                                                       │
│   Worker Schema (v4.5 9-element flat) ◀══ canonical                   │
│        │                                                              │
│        ├── Strategy Selector (10 strategies)  → how worker reasons    │
│        ├── Operating Mode (4 modes)           → how workers orchestrate│
│        └── 4-layer Persona Stack              → presentation only     │
│                                                                       │
└──────────────────────────────┬────────────────────────────────────────┘
                               │
                               ▼
┌─ LAYER 3 — EXECUTION ─────────────────────────────────────────────────┐
│                                                                       │
│   Framework Orchestrator  →  selects Strategy per task type           │
│        │                                                              │
│        ▼                                                              │
│   Sequential Departmental Processing                                  │
│        (Theory → Voices → Style → Timbre → Performance → Lyrics)      │
│        │                                                              │
│        ▼                                                              │
│   Draft Freeze  →  Round-Robin SME Protocol  →  Deliberation &        │
│                    (multi-agent invocation)     Pressure Engine       │
│                                                                       │
└──────────────────────────────┬────────────────────────────────────────┘
                               │
                               ▼
┌─ LAYER 4 — CANON (Plane 2 in MOSAIC) ─────────────────────────────────┐
│                                                                       │
│   Technical UST  ◀── governed by ──  UST State Machine                │
│        ▲                              (NULL → PROPOSED → PRESSURED →  │
│        │                               RESOLVED → LOCKED)             │
│        │                                                              │
│        └── Address Law ── enforces ──▶ Null Protocol                  │
│            (resolve/preserve/         (null = signal, never silent    │
│             justify/escalate)          fill)                          │
│                                                                       │
└──────────────────────────────┬────────────────────────────────────────┘
                               │
                               ▼ (concurrent during creation, not after)
┌─ LAYER 5 — ADMISSIBILITY (Plane 3 in MOSAIC) ─────────────────────────┐
│                                                                       │
│   SEM Gates ◀── concurrent with ──▶ Stop-the-Line Conditions          │
│   (K1–K6/K8 admissibility)          (skipped subkey, silent fill,     │
│                                      truncation, false completeness)  │
│                                                                       │
│   Pain-to-Fix Library (YAML)  →  compiled JSON  →  Atomic Remediation │
│   (axis/failure_id/trigger/     (runtime-validated)  (impact-sorted   │
│    spec/severity/source)                              by w × (1−s/5)) │
│                                                                       │
└──────────────────────────────┬────────────────────────────────────────┘
                               │
                               ▼
┌─ LAYER 6 — DEFINITIVE LOCK ───────────────────────────────────────────┐
│                                                                       │
│              technical.ust  →  definitive LOCK                        │
│              (single canonical truth object)                          │
│                                                                       │
└──────────────────────────────┬────────────────────────────────────────┘
                               │
                               ▼
┌─ LAYER 7 — OUTPUT CONTRACT (Plane 4 in MOSAIC) ───────────────────────┐
│                                                                       │
│   Triad  ◀── depends on ── definitive technical.ust LOCK              │
│   ├── Show Summary       (≤ 1000 chars, Suno style prompt)            │
│   ├── Creative UST       (≤ 5000 chars, Suno lyrics prompt)           │
│   └── A/R Persona Surface (style ≤ 150, profile ≤ 2000)               │
│                                                                       │
│   ATP  ── packages ──▶  Triad + UST + SEM Report + Review Transcript  │
│   (v5-c)                + Persona Participation Map + Manifest + Hash │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘

┌─ LAYER 8 — FEEDBACK (closes loops across all layers) ─────────────────┐
│                                                                       │
│   Cross-Plane Feedback (function CANON)                               │
│        ├── 4-Plane partition (v5-c structure, CANDIDATE)              │
│        └── Phase-based partition (v4.5 structure, CANDIDATE)          │
│                                                                       │
│   Both partitions coexist until runtime design selects implementation │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

**Read order from top:** every operator turn enters Layer 0 (cognitive operators run), passes through Layer 1 (cadence governs emission), engages Layer 2 (workers selected), executes Layer 3 (sequential then deliberative), modifies Layer 4 (canonical UST state) under Layer 5 (admissibility runs concurrently), reaches Layer 6 (LOCK only when lawful), produces Layer 7 (Triad and ATP). Layer 8 closes loops back to any prior layer when feedback fires.

---

## 3. Edge Ledger

### Layer 0 — Cognitive Operators

#### E01 — Sense-Think-Act ⟂ Tri-Attention

- **Edge statement:** Sense-Think-Act and Tri-Attention are co-required parallel primitives that both run on every operator turn. Neither feeds the other directionally; both produce concurrent inputs to the operator's response cycle.
- **Source lineage:** v4.5 monolith Section 4.1 and 4.2 ("REASONING STACK (Always On)"); `os.maestro.momoney.customInstructions.v4.2.3`; `UniversalMaestro.v3.0g.CustomGPT.Instructions`; Suno v4.5 Deep Prompting Knowledge §I.
- **Status:** CANON
- **Evidence basis:** v4.5 corpus presents both as "always-on" parallel layers with no causal feed language. SEC E01 confirmed parallel co-presence; rejected the directed feed RTFA.v0 had asserted.
- **Failure mode if separated:** Sense-Think-Act without Tri-Attention loses Content/Context/Process integrity monitoring → drift goes undetected. Tri-Attention without Sense-Think-Act has nothing to monitor → empty validation. Both are required; neither is sufficient.
- **Mosaic runtime implication:** Initialize both on every turn. Tri-Attention is the per-turn integrity check on the Sense-Think-Act trace, not a downstream consumer. No ordering enforced.

#### E02 — DSRP exists as independent cognitive operator

- **Edge statement:** DSRP (Distinctions / Systems / Relationships / Perspectives) operates as an independent meta-cognitive lens. Its causal coupling to Tri-Attention or to other Layer 0 primitives is not established by primary v4.5 corpus.
- **Source lineage:** v4.5 monolith Historical Insights Log ("Recursive Outlining/DSRP (Meta-Workflow)"); Chimera-Indigo prompt (separate occurrence).
- **Status:** NEEDS SOURCE for any directional coupling; CANDIDATE for independent existence.
- **Evidence basis:** SEC E02 found no primary corpus evidence of "Tri-Attention feeds DSRP" or "DSRP feeds Conversation Layer". DSRP exists; its position in a causal graph does not.
- **Failure mode if separated:** Without DSRP, recursive analysis of system components and their relationships is unavailable. With DSRP isolated from other operators, no architectural failure follows because the causal couplings were never established.
- **Mosaic runtime implication:** Encode DSRP as an optional cognitive operator that may be invoked when the operator's task involves system decomposition. Do not encode directional feeds to or from DSRP without primary evidence.

#### E19 — Five Implicit Structuring Tools

- **Edge statement:** Five named cognitive operators (Fishbone, SWOT, Decision Trees, Virtual Whiteboards, Word Clusters) are available to workers and the controller for task-specific structuring. Trigger conditions are evidenced.
- **Source lineage:** Suno v4.5 Deep Prompting Knowledge §I.F; v4.5 monolith Heuristics.
- **Status:** CANON (v4.5) — function lost in v5-c; recoverable for Mosaic.
- **Evidence basis:** v4.5 corpus names all five with explicit trigger conditions: "Apply Tri-Attention when score variance between creative & technical judges > 2 points or when integrating legacy IP" (Tri-Attention trigger). Fishbone for root cause analysis. Decision Trees for branched evaluation. Virtual Whiteboards for parallel-state tracking. Word Clusters for thematic compression.
- **Failure mode if separated:** Without these structuring tools, workers default to unstructured prose reasoning when domain-specific structures would produce sharper output. v4.5 evidence: these tools were operationally referenced; their absence in v5-c contributed to unstructured persona output and SEM degradation.
- **Mosaic runtime implication:** Encode as a cognitive operator inventory accessible to workers via skill_core. Each tool has trigger conditions. Workers may invoke; controller may not (controller is procedural only).

### Layer 1 — Operating Cadence (Chimera-Indigo sourced)

#### E04 — Conversation Layer governs emission cadence

- **Edge statement:** Conversation Layer (2–3 file batching, "c" continuation, no streaming, internal memory across turns, dialogue-not-Q&A discipline) controls when and how the system emits output.
- **Source lineage:** Chimera-Indigo prompt and correction brief (Day 2 evidence). v4.5 had distributed precursor rules in `os.maestro.momoney.customInstructions` (no Q&A drift, no streaming, internal memory) but did not consolidate them as a layer.
- **Status:** CANON, Chimera-Indigo-sourced. v4.5 = precursor evidence only (per OD-4).
- **Evidence basis:** Chimera-Indigo prompt explicitly defines Conversation-Mode Operating Discipline as a discrete layer. Operator-named failure mode: "you're in QA mode and ignoring hours of previous work" (SEM session S1415).
- **Failure mode if separated:** Q&A drift — system emits before sense complete, fragments dialogue thread across turns, treats each turn as isolated transaction. Operator fatigue. Loss of cumulative context.
- **Mosaic runtime implication:** Conversation Layer owns emission cadence as a runtime primitive. Pre-emit checks: has Sense-Think-Act run? has Tri-Attention monitored? is current emission a single non-streaming reply? does it respect 2–3 file batching where applicable? Internal memory persists across turns within a session.

#### E17 — Mode A/B Detection determines session entry path

- **Edge statement:** Two distinct session-entry paths exist. Mode A: scan last 100–150 turns to reconstruct project state. Mode B: fresh intake with no history invention. Mode determines whether downstream phases load from history or initialize fresh.
- **Source lineage:** `os.maestro.momoney.customInstructions.v4.2.3`; Suno v4.5 Deep Prompting Knowledge §IV.
- **Status:** CANON (v4.5).
- **Evidence basis:** v4.5 customInstructions documents the two-mode entry pattern explicitly. Cold-start reset behavior is named. Mode A reconstruction limits (100–150 turns) are stated.
- **Failure mode if separated:** Without Mode A, resumed sessions hallucinate prior state. Without Mode B, fresh intake gets contaminated with phantom history. Without detection, both modes get conflated and history fabrication results.
- **Mosaic runtime implication:** Session start always classifies entry as Mode A or Mode B. Mode A engages reconstruction protocol with explicit window limits. Mode B engages fresh intake with no backfill. Misclassification is a stop-the-line condition.

#### E18 — Memory-Refine /prefs with TTL

- **Edge statement:** A `/prefs` command persists user preferences across sessions with a 90-day TTL. Preloads on new session start. Supplements but does not replace Conversation Layer's internal memory.
- **Source lineage:** Suno v4.5 Deep Prompting Knowledge §IV.
- **Status:** CANON (v4.5).
- **Evidence basis:** v4.5 KB §IV documents the protocol explicitly with command, TTL, and preload behavior. Solves a partial slice of the cross-session continuity problem ATP also addresses (E13).
- **Failure mode if separated:** Without /prefs, every new session re-elicits the same preferences, breaking efficiency and operator trust. Without TTL, stale preferences persist beyond their relevance.
- **Mosaic runtime implication:** Encode /prefs as a runtime command that writes to a TTL'd preference store. On Mode A session start, preload current preferences. On Mode B, prompt for any missing required preferences. Coordinate with ATP (E13) so that preferences are part of the lineage manifest when applicable.

### Layer 2 — Workforce

#### E05a — Worker Schema is the v4.5 9-element flat schema

- **Edge statement:** The canonical worker module schema is the v4.5 9-element flat schema: persona_name, mission, decision_lens, do_rules, dont_rules, synergy_hooks, bounded_domain, bounded_non_domain, conflict_boundaries. Day 3 documentation may extend this with additional null-resolution fields (null_resolution_lens, fill_argument_style, preserve_null_conditions, downstream_risk_checks, contradiction_trigger_patterns).
- **Source lineage:** v4.5 monolith Section 2; `os.maestro.momoney.customInstructions.v4.2.3`; Day 3 documentation worker contract.
- **Status:** CANON (per OD-1). Replaces RTFA.v0 §5.2's 4-layer Persona Stack as authoritative schema.
- **Evidence basis:** SEC E05 documented the 9-element schema in v4.5 primary corpus. Day 3 added null-resolution fields. v5-c MOSAIC compressed to 4 layers — compression is rejected as authoritative.
- **Failure mode if separated:** A worker missing any of the 9 elements becomes flatter than v4.5 operational baseline. Lost fields produce specific failures: missing `synergy_hooks` → no cross-domain collaboration patterns; missing `bounded_non_domain` → unlawful cross-domain authoring; missing `conflict_boundaries` → unresolvable persona collisions.
- **Mosaic runtime implication:** All worker definitions must instantiate the 9-element schema. Day 3 extension fields are recommended additions, not optional cuts. Schema validation on worker registration: reject any worker module missing a required field.

#### E05b — 4-layer Persona Stack as presentation grouping

- **Edge statement:** The v5-c 4-layer Persona Stack (Skill Core / Lens & Standards / Personality Layer / Motive-Bias) may be used as a presentation grouping for documentation, diagrams, and operator-facing summaries. It is not the operational schema.
- **Source lineage:** v5-c MOSAIC v2.2 diagram.
- **Status:** CANDIDATE for presentation use only (per OD-1). Explicitly REJECTED as operational schema.
- **Evidence basis:** OD-1 permits the 4-layer grouping for non-operational contexts.
- **Failure mode if separated:** Documentation loses a useful conceptual grouping. No runtime failure.
- **Mosaic runtime implication:** Presentation layer (diagrams, operator-facing summaries) may render workers grouped under the 4 layers. Runtime worker registry, validation, and execution operate on the 9-element schema only. The two views must be kept consistent at presentation time but never confused at runtime.

#### E06a — Strategy Selector defines how a worker reasons

- **Edge statement:** A 10-strategy selector (CoT, ToT, ReAct, CRISPE, Few-Shot, Self-Consistency, Persona, DARE, Zero-Shot CoT, QUEST) is invoked per task type to determine the worker's reasoning strategy.
- **Source lineage:** v4.5 monolith Section 4.3 (Framework Orchestrator).
- **Status:** CANON (v4.5).
- **Evidence basis:** v4.5 monolith provides explicit IF/ELSE selection rules: tool use → ReAct, exploration → ToT, formatting → Few-Shot+CRISPE, accuracy → Self-Consistency, schema → QUEST, default → CoT+Persona. SEC E06 confirmed this as v4.5 canon.
- **Failure mode if separated:** Without Strategy Selector, all reasoning collapses to a single default (typically CoT). Worker outputs lose task-appropriate structure. v4.5 evidence: the strategy-per-task pattern produced higher quality than monostrategic approaches.
- **Mosaic runtime implication:** Framework Orchestrator (E16) reads task type and selects from the 10-strategy library. Workers execute under the selected strategy. Strategy is logged in the session ledger for audit.

#### E06b — Operating Mode defines how workers are orchestrated

- **Edge statement:** A 4-mode taxonomy (solo / round / challenge / alignment) governs how many workers engage with a task and how they interact.
- **Source lineage:** v5-c MOSAIC v2.2 diagram.
- **Status:** CANDIDATE (per OD-3). Coexists with E06a as orthogonal layer.
- **Evidence basis:** OD-3 separates Strategy from Mode and keeps both. v5-c MOSAIC v2.2 explicitly enumerates the 4 modes.
- **Failure mode if separated:** Without Operating Mode, orchestration patterns are ad-hoc per task. With Operating Mode but without Strategy, workers engage in patterns but reason monolithically.
- **Mosaic runtime implication:** Operating Mode is selected per task or per phase: solo for single-domain work, round for sequential review, challenge for adversarial pressure, alignment for consensus formation. Mode is orthogonal to Strategy — a worker in any Mode reasons under whatever Strategy was selected.

### Layer 3 — Execution

#### E16 — Framework Orchestrator selects Strategy per task type

- **Edge statement:** A Framework Orchestrator examines incoming task type and selects the appropriate Strategy from the 10-strategy library (E06a). Selection rules are deterministic per task type.
- **Source lineage:** v4.5 monolith Section 4.3.
- **Status:** CANON (v4.5).
- **Evidence basis:** v4.5 §4.3 documents the selection rules with explicit IF/ELSE logic. SEC E16 confirmed.
- **Failure mode if separated:** Without Framework Orchestrator, Strategy selection becomes manual per turn or defaults to a single strategy. Workers lose task-appropriate reasoning.
- **Mosaic runtime implication:** Encode Framework Orchestrator as a runtime function that takes a task type, applies selection rules, and returns a Strategy. Workers consume Strategy via their reasoning context. Selection is logged.

#### E20 — Sequential Departmental Processing

- **Edge statement:** Technical UST is processed sequentially by axis-departmental phase: Theory → Voices → Style → Timbre → Performance → Lyrics. Workers act only within their lawful domain during their phase. Round-robin only after all departments draft.
- **Source lineage:** Day 3 documentation; operator correction during dev session.
- **Status:** CANON (Day 3 + operator correction).
- **Evidence basis:** Day 3 explicit: "Technical UST shall be treated as a sequentially processed canonical null-bearing substrate whose axes, keys, and subkeys are worked phase-by-phase by the lawful SMEs, null-by-null, before cross-departmental consensus pressure loops refine the whole draft." Operator correction confirmed sequential-then-deliberative ordering.
- **Failure mode if separated:** Two failure modes. (a) "Everyone discusses everything at once" — round-robin without prior sequential drafting produces unfocused debate over undefined surfaces. (b) "Each department finishes in total isolation" — sequential without round-robin produces departmentally-coherent but cross-domain-broken UST.
- **Mosaic runtime implication:** Phase machine enforces order. Phase 1 = sequential per-axis drafting. Phase 2 = draft freeze. Phase 3 = intradepartmental refinement. Phase 4 = interdepartmental round-robin and pressure. Phase 5 = definitive lock. Skipping Phase 1 or running Phases 1 and 4 concurrently is a stop-the-line violation.

#### E07 — Multi-agent invocation activates Round-Robin SME Protocol

- **Edge statement:** When Operating Mode (E06b) selects round / challenge / alignment, the Round-Robin SME Protocol activates with mandatory turn order, claim, challenge, ejection, consensus, and minutes.
- **Source lineage:** v4.5 monolith Phase 2.1 (Initiating Round-Robin Consensus Sprint); Phase 7.5 (Cross-Domain Iteration); Day 3 documentation.
- **Status:** CANON.
- **Evidence basis:** v4.5 monolith Phase 2.1 names the protocol. Day 3 codifies as mandatory: "Round-robin argumentative review is mandatory and produces first-class artifacts." SEC E07 confirmed.
- **Failure mode if separated:** Without round-robin, single-perspective drift dominates. Without multi-agent invocation, round-robin has no participants. v4.5 made both mandatory.
- **Mosaic runtime implication:** Round-Robin SME Protocol is invoked when Operating Mode is round / challenge / alignment. Pressure-driven (not count-driven) consensus per operator correction. First-class review artifacts (transcript, contradiction log, defense notes, dissent register) are required outputs of every round-robin invocation.

#### E08 — Round-Robin → Deliberation & Pressure Engine

- **Edge statement:** Round-Robin protocol output is consumed by a Deliberation & Pressure Engine that runs challenge cycles, preserves nulls, captures contradictions, and produces first-class review artifacts.
- **Source lineage:** Function: v4.5 distributed across Phase 2.1, Phase 7.5, Self-Correction Protocol. Naming: v5-c MOSAIC v2.2.
- **Status:** CANON for the function. CANDIDATE for the discrete naming.
- **Evidence basis:** SEC E08 confirmed the function operationally in v4.5 with the discrete naming as v5-c framing. Operator correction: "consensus-seeking under pressure, controlled chaos, cross-domain expert challenge."
- **Failure mode if separated:** Round-robin without pressure engine = polite agreement, no challenge, false consensus. Pressure without round-robin = adversarial input with no structured challenge protocol. SEC documented this as an empirical failure of the v5 split.
- **Mosaic runtime implication:** The Deliberation & Pressure Engine is the consumer of every round-robin invocation's output. Challenge cycles iterate until either consensus pressure resolves or contradictions are explicitly carried forward. Review artifacts are first-class — they participate in admissibility and lineage, not just process logging.

### Layer 4 — Canon

#### E09 — Technical UST governed by UST State Machine

- **Edge statement:** Technical UST passes through a five-state lifecycle per address: NULL → PROPOSED → PRESSURED → RESOLVED → LOCKED. State transitions are governed by SME labor under canon law.
- **Source lineage:** Function: v4.5 Day 3 phase machine (unresolved → draft-filled → under-pressure → justified-open OR definitive). Naming: v5-c MOSAIC v2.2.
- **Status:** CANON.
- **Evidence basis:** SEC E09 confirmed function in v4.5 Day 3 with renaming in v5-c. The 5-state lifecycle is functionally present in v4.5 with different state names. v5-c provides clean nomenclature.
- **Failure mode if separated:** Technical UST without state machine = unaddressed completeness, silent fills, false LOCKED claims. SEC documented the v5 split failure mode where multi-file architecture lost track of which addresses were in which state, enabling phantom LOCKEDs.
- **Mosaic runtime implication:** Use v5-c naming for clarity. Carry v4.5 per-address state granularity (each axis.key.subkey has its own state). State machine is enforced by the controller as a procedural check; controller may not transition states based on its own creative judgment, only based on lawful SME labor outputs.

#### E10 — Address Law enforces Null Protocol

- **Edge statement:** Address Law (resolve / preserve / justify / escalate) enforces Null Protocol (null = reserved address, never silent fill, never delete, never infer).
- **Source lineage:** v4.5 Day 3 documentation; v5-c MOSAIC v2.2.
- **Status:** CANON. Strongest edge in the substrate.
- **Evidence basis:** Day 3 explicit: "Bind every open question to its lawful address. Route each address to the lawful SME or SMEs. Require either: argued fill, or justified deliberate-null preservation. Nulls are signal and may not be silently filled. Preserve nulls only when intentional, explicit, and justified." v5-c MOSAIC v2.2 codifies the law explicitly.
- **Failure mode if separated:** Without Address Law, nulls get silent-filled. Without Null Protocol, addresses lose their signal value. Either failure breaks the canon: "controller may not invent artistic content, fill nulls creatively, or absorb SME judgment."
- **Mosaic runtime implication:** This is the structural core of the null-resolution engine. Every address has a lawful owner. Every fill must be argued, defensible, downstream-aware, domain-consistent, challengeable. Every null preservation must be justified, explicit, intentional. Silent fill is a stop-the-line violation. Skipped subkey is a stop-the-line violation.

### Layer 5 — Admissibility (concurrent with Layer 4 during creation)

#### E11 — SEM Gates run concurrently with Stop-the-Line Conditions

- **Edge statement:** SEM admissibility gates (K1 Structural viability, K2 Cross-axis coherence, K3 Creative strength, K4 Performance truth, K5 Sonic identity, K6 Compression survivability) and stop-the-line conditions (skipped subkey, silent fill, truncation, unauthorized lyric change, false completeness) operate concurrently during creation, not sequentially after.
- **Source lineage:** v4.5 SEM session; v4.5 monolith Section 2.2 (VAL_Report) and Self-Correction Protocol; v5-c MOSAIC v2.2.
- **Status:** CANON.
- **Evidence basis:** v4.5 had Lyric Integrity Lock + Deviation Detection running concurrently with SEM scoring. SEC E11 confirmed. v5-c MOSAIC v2.2: "Every step emits UST delta + SEM delta together."
- **Failure mode if separated:** Sequential operation = quality scoring after stop-the-line conditions miss deviations during creation, allowing deviations to accumulate before any block fires. Concurrent operation = stop-the-line catches violations at creation time. SEC documented this as the v4.5 operational pattern that v5-c preserves.
- **Mosaic runtime implication:** SEM gates and stop-the-line conditions both run on every UST delta emission, not on completion. Severity tiers (Observe / Warn / Challenge / Block) determine response. Block is non-negotiable — no Suno output without PASS, reverse compilation blocked until definitive lock.

#### E12 — Pain-to-Fix Library → Atomic Remediation Tasks

- **Edge statement:** A Pain-to-Fix associative library, organized as YAML (axis, failure_id, trigger, remediation_spec, severity, source) and compiled to JSON for runtime validation, feeds the M8 revision loop's atomic remediation task generation. Impact-sorted by formula `weight × (1 − score/5)`.
- **Source lineage:** Function: v4.5 monolith §7.4 Decision Tree, §7.5 HSI, §7.6 QUINN; SEM session M8.2. Data design: per OD-5.
- **Status:** CANON for the function. CANDIDATE for the YAML→JSON data structure (operator-specified per OD-5).
- **Evidence basis:** v4.5 §7.4 provides explicit IF/THEN remediation rules. SEM M8.2 documents atomic remediation task patterns: hook (3 topline motifs), production (kick tuning, mono <120 Hz, vocal bus chain), lyrics (phrasing_map or LCR alternatives). Impact formula explicit in M8.1.
- **Failure mode if separated:** Without PTF library, remediation is ad-hoc each iteration — same failures get re-diagnosed instead of looked up. Without atomic task generation, PTF library is descriptive (lists what's wrong) but not actionable (no concrete fix). Without impact sorting, remediation order is arbitrary, wasting iterations on low-impact items.
- **Mosaic runtime implication:** PTF library is first-class data. Schema:
  ```yaml
  - axis: VOC
    failure_id: VOC.K3.S2.syllable_overflow
    trigger: lyric.line.syllable_count > 11
    remediation_spec:
      type: phrasing_map
      action: bar_split
      preserve: original_lyric_text
    severity: block
    source: SEM session M8.3 (v4.5)
  ```
  Compiled to JSON at runtime startup for fast lookup. M8 revision loop pulls from this library as primary reasoning input. Impact sort applies the v4.5 formula. Library is versioned and operator-extensible.

### Layer 6 — Definitive Lock

#### E21 — Definitive `technical.ust` LOCK is the canonical truth gate

- **Edge statement:** The definitive `technical.ust` LOCK is the single canonical truth object. No reverse compilation, derivative surface drafting, or external output may proceed without LOCK. LOCK is achieved only when all required addresses are filled or justified-open, all axes are complete, all round-robin contradictions are resolved or carried, and all gate checks pass.
- **Source lineage:** v4.5 Day 3 documentation; v5-c MOSAIC v2.2.
- **Status:** CANON.
- **Evidence basis:** Day 3 explicit: "Lock definitive Technical UST only after lawful completion." v5-c MOSAIC v2.2: "Definitive technical.ust LOCK precedes any reverse compilation."
- **Failure mode if separated:** Reverse compilation before LOCK = derivative surfaces built on shifting foundation, contradictions baked into outputs. External outputs before LOCK = false completeness presented as canonical work. Either failure breaks canon law and corrupts the IP record.
- **Mosaic runtime implication:** Controller enforces LOCK as a procedural gate. LOCK transition is logged with state of every address. Once LOCKED, technical.ust is immutable for the duration of the production cycle. Any required revision after LOCK requires explicit unlock procedure with full audit trail.

### Layer 7 — Output Contract

#### E14a — Triad depends on definitive `technical.ust` LOCK

- **Edge statement:** The Triad (Show Summary ≤ 1000 chars, Creative UST ≤ 5000 chars, A/R Persona Surface with style ≤ 150 / profile ≤ 2000) depends directly on the definitive `technical.ust` LOCK. Triad surfaces are derived via worker-owned reverse compilation from LOCKED Technical UST.
- **Source lineage:** v4.5 Day 3 documentation; v4.5 Phase 8; v5-c MOSAIC v2.2.
- **Status:** CANON. Replaces RTFA.v0's incorrect Triad-depends-on-ATP edge.
- **Evidence basis:** Day 3 explicit: "Reverse compilation begins only after definitive Technical UST lock." Triad is the external API; everything else is internal simulation. SEC E14 corrected the dependency direction.
- **Failure mode if separated:** Triad without LOCK dependency = Triad becomes derivative-of-derivative, losing canonical grounding. Triad with phantom LOCK = false completeness shipped to external surface.
- **Mosaic runtime implication:** Triad generation is gated by LOCK state. Reverse compilation is worker-owned, not controller-owned (controller may not absorb SME judgment). Each Triad surface respects character budget. Compression is governed by FOIL discipline (promotion and deduplication only, not summarization).

#### E14b — ATP packages Triad plus lineage

- **Edge statement:** Air-Gapped Transfer Pack (ATP) is a packaging primitive that aggregates Triad + Technical UST + SEM Report + Review Transcript + Persona Participation Map + Manifest + Hash. ATP enables verifiable, resumable, auditable transfer across sessions and environments.
- **Source lineage:** v5-c MOSAIC v2.2. Sourced as solution to v4.5 portability gap (operator: "the information ends up stuck in that GPT").
- **Status:** CANON, v5-c-sourced.
- **Evidence basis:** SEC E13 documented that v4.5 produced the components independently but did not aggregate them into a single hash-verifiable transfer pack. SEC E14 reversed the dependency direction. v5-c MOSAIC v2.2 introduces ATP explicitly with full component list.
- **Failure mode if separated:** Components without ATP aggregation = no portability, no resumability, no integrity verification. This was the v4.5 failure mode that motivated the substrate work.
- **Mosaic runtime implication:** ATP construction runs at session-end as a procedural controller operation. ATP verification runs at session-start (Mode A path) before reconstruction begins. Hash verifies integrity. Manifest enumerates contents and lineage. ATP is the packaging output, not the canonical truth — Triad is the external API; ATP is the transport.

#### E13 — ATP aggregates from all layers

- **Edge statement:** ATP collects content from every other substrate layer: Triad from Layer 7, technical.ust from Layer 6, SEM Report and Pain-to-Fix invocations from Layer 5, round-robin transcripts and persona participation from Layer 3, worker schema instances from Layer 2, conversation cadence metadata from Layer 1, cognitive operator traces from Layer 0.
- **Source lineage:** v5-c MOSAIC v2.2.
- **Status:** CANON, v5-c-sourced.
- **Evidence basis:** v5-c MOSAIC v2.2 explicit on ATP contents. SEC E13 confirmed components in v4.5 with aggregation as v5-c addition.
- **Failure mode if separated:** Partial aggregation = some layers' state lost on transfer, breaking resumability. Full aggregation = complete state portable across environments.
- **Mosaic runtime implication:** ATP construction is layer-aware. Each layer registers its serializable state with the ATP builder. Builder produces manifest with hash. ATP is verifiable end-to-end before transfer.

### Layer 8 — Feedback

#### E15a — Cross-Plane Feedback closes the loop

- **Edge statement:** Cross-plane / cross-layer feedback closes loops between every layer of the substrate. Lower-layer findings (SEM failures, persona challenges, address contradictions) propagate upward to revise prior decisions. Upper-layer changes (operator corrections, conversation context shifts) propagate downward to revise in-flight execution.
- **Source lineage:** Function: v4.5 §7.4 Decision Tree feedback loops; v4.5 Phase 7.5 Cross-Domain Iteration. Structure: v5-c MOSAIC v2.2 4-plane partition.
- **Status:** CANON for the function (per OD-2). Structure is split into E15b and E15c.
- **Evidence basis:** v4.5 evidence: feedback function existed via Phase-based loops (Phase 7.5). v5-c evidence: 4-plane partition introduced as alternative structure. Per OD-2, function is canonized; structure remains candidate.
- **Failure mode if separated:** Without cross-plane feedback, lower-layer findings don't propagate upward — SEM failures get logged but don't trigger revision; persona challenges fire but don't close. SEC documented this as the v5 split failure: feedback was disabled when the system lost the ability to revise from late-stage findings.
- **Mosaic runtime implication:** Encode feedback as a runtime mechanism that fires on Layer 5 stop-the-line conditions, on operator corrections, on round-robin contradictions, on Tri-Attention drift detection. Feedback target depends on partition structure (E15b vs E15c).

#### E15b — 4-Plane partition (CANDIDATE structure)

- **Edge statement:** The v5-c 4-plane partition (Plane 1 staffed runtime, Plane 2 canon, Plane 3 admissibility, Plane 4 external API) is a candidate structure for cross-plane feedback routing.
- **Source lineage:** v5-c MOSAIC v2.2.
- **Status:** CANDIDATE (per OD-2).
- **Evidence basis:** v5-c MOSAIC v2.2 explicit. SEC E15 partially confirmed function while flagging partition as v5-c framing.
- **Failure mode if separated:** Without a partition, feedback routing has no target structure. With this partition, feedback routes between 4 planes.
- **Mosaic runtime implication:** If selected at runtime design, encode as 4 planes with explicit edges: SEM Feedback ↔ Persona Pressure; Controller Flags ↔ UST Attention. Feedback events route to the appropriate plane.

#### E15c — Phase-based partition (CANDIDATE structure)

- **Edge statement:** The v4.5 phase-based partition (Phase 1.x intake, Phase 2.x analysis, Phase 3.x revision, Phase 4.x generation, Phase 7.5 cross-domain) is a candidate structure for feedback routing. Feedback loops to specific named phases.
- **Source lineage:** v4.5 monolith Phase machine; §7.4 Decision Tree.
- **Status:** CANDIDATE (per OD-2).
- **Evidence basis:** v4.5 evidence explicit: "loop back to Phase 1.2/1.3/1.4 for re-blueprinting, Phase 3.1/3.2/3.3 for re-prompting, or Phase 6 for re-generation."
- **Failure mode if separated:** Without phase-based feedback, v4.5's empirical feedback pattern is lost. With phase-based feedback, feedback routes to named phases.
- **Mosaic runtime implication:** If selected at runtime design, encode as phase machine with explicit feedback targets per failure type. Feedback routes to the specific phase that owns the broken decision.

---

## 4. Rejected or Reversed Edges

| Old Edge (RTFA.v0) | Why Rejected | Replacement |
|---|---|---|
| **E01 (RTFA): Sense-Think-Act feeds Tri-Attention** | SEC found no causal feed in v4.5 corpus; both are parallel always-on monitors | E01 (SDG): Co-required parallel primitives |
| **E03 (RTFA): DSRP feeds Conversation Layer** | Conversation Layer not present in v4.5 as named layer; DSRP–Conversation Layer coupling unsubstantiated; lineage attribution wrong | No directional successor edge. DSRP and Conversation Layer are independent. E04 source-marked as Chimera-sourced per OD-4. |
| **E05 (RTFA): 4-layer Persona Stack defines worker schema** | v4.5 used 9-element flat schema, not 4-layer stack; 4-layer compression loses operational fields | E05a (CANON): 9-element flat schema as canonical operational schema. E05b (CANDIDATE): 4-layer Persona Stack as presentation grouping only. |
| **E06 (RTFA): Worker schema routes through Multi-Agent Operating Modes** | v4.5 had 10-strategy selector, not 4-mode; conflated two orthogonal layers | E06a (CANON): Strategy Selector (10 strategies) — how worker reasons. E06b (CANDIDATE): Operating Mode (4 modes) — how workers orchestrate. Both per OD-3. |
| **E14 (RTFA): Triad Output depends on ATP** | Dependency direction reversed; Triad depends on technical.ust LOCK; ATP packages Triad | E14a (CANON): Triad depends on definitive technical.ust LOCK. E14b (CANON): ATP packages Triad plus lineage. |

Three edges fully rejected. Two edges split into orthogonal pairs. One edge fully reversed in direction.

---

## 5. New Edges Added

| Edge ID | Edge | Status | Source |
|---|---|---|---|
| E16 | Framework Orchestrator selects Strategy per task type | CANON | v4.5 monolith §4.3 |
| E17 | Mode A/B Detection determines session entry path | CANON | v4.5 customInstructions; Suno v4.5 KB §IV |
| E18 | Memory-Refine /prefs with 90-day TTL | CANON | Suno v4.5 KB §IV |
| E19 | Five Implicit Structuring Tools (Fishbone/SWOT/DT/Whiteboards/Word Clusters) | CANON (recoverable, lost in v5-c) | Suno v4.5 KB §I.F |
| E20 | Sequential Departmental Processing | CANON | Day 3 documentation + operator correction |

E21 (Definitive `technical.ust` LOCK as canonical truth gate) was implicit in RTFA.v0 but not explicitly named as an edge. Added as Layer 6 anchor in this revision.

---

## 6. Remaining Needs-Source Items

Only items that block canonization are listed.

**NS-1: DSRP causal couplings (E02).**
Primary corpus does not establish DSRP → Tri-Attention or DSRP → Conversation Layer as directed feeds. DSRP exists as independent operator. If full chat.html or longDevWorkLog evidence surfaces a causal coupling, NS-1 may resolve. Until then, DSRP is encoded as independent.
Blocks: nothing critical — Mosaic can ship without DSRP coupling. Promote DSRP to optional cognitive operator.

**NS-2: Pain-to-Fix Chain library data canonical schema fields.**
OD-5 specifies: axis, failure_id, trigger, remediation_spec, severity, source. Schema needs operator review against actual v4.5 SEM session content to ensure no required field is missing (e.g., dependency on prior remediation, success criteria, rollback condition).
Blocks: PTF library construction at runtime startup.

**NS-3: 4-Plane vs phase-based feedback partition selection.**
OD-2 defers selection until runtime design. Both coexist as CANDIDATE. Selection blocks final feedback routing implementation.
Blocks: feedback layer concrete implementation. Does not block other layers.

**NS-4: Conversation Layer → Mosaic substrate ↔ Maestro application boundary.**
OD-4 puts Conversation Layer in Mosaic substrate canon. Open question: does Mode A/B Detection (E17) and Memory-Refine /prefs (E18) belong in substrate or in application overlay? They were v4.5 operational, not Chimera. Substrate vs application boundary needs operator decision before SUBSTRATE_SPEC_v0.1.
Blocks: SUBSTRATE_SPEC_v0.1 layer classification.

---

## 7. Runtime Consequences

What Mosaic must implement because the graph changed.

**RC-1: Worker Registry uses 9-element schema.**
Worker registration accepts only modules with all 9 required fields plus optional Day 3 extension fields. Modules using the 4-layer Persona Stack as schema are rejected at registration with a translation error. Presentation layer renders 4-layer grouping for diagrams; runtime ignores it.

**RC-2: Strategy Selector and Operating Mode are orthogonal runtime layers.**
Per-task selection of Strategy is independent of per-phase selection of Mode. Both are logged. Workers consume Strategy via reasoning context. Mode determines orchestration pattern (which workers, in what order, with what challenge protocol).

**RC-3: Triad generation gated by LOCK, not by ATP.**
Reverse compilation runs only after LOCK transition is logged. Triad surfaces are produced by worker-owned reverse compilation from LOCKED Technical UST. ATP is constructed from Triad + lineage post-Triad-completion, as a packaging step. Controller does not absorb SME judgment during reverse compilation.

**RC-4: Pain-to-Fix Library is human-authored YAML compiled to JSON.**
Library file format: YAML, organized by axis, with per-failure-id entries. Build step compiles to JSON for runtime validation. Library is version-controlled. M8 revision loop pulls from compiled JSON at runtime. Library is operator-extensible — new failure_ids may be added without architecture changes.

**RC-5: Conversation Layer is initialized before any other Layer 1+ operation.**
On every operator turn: Layer 0 cognitive operators run, Layer 1 Conversation Layer governs emission, then Layers 2–8 engage as needed. Conversation Layer pre-emit checks are enforced. Q&A drift is detected and corrected.

**RC-6: SEM Gates and Stop-the-Line Conditions emit on every UST delta.**
Not every UST commit. Every UST delta emission. SEM delta and UST delta are paired output streams from creation through LOCK. Block-severity events halt the pipeline; lower severities log without blocking.

**RC-7: Address Law applies per-address, per-state-transition.**
State machine transitions (NULL → PROPOSED → PRESSURED → RESOLVED → LOCKED) require lawful SME labor at every step. Controller may transition only when SME labor authorizes. Silent fill, skipped subkey, and infer-from-defaults are stop-the-line violations.

**RC-8: Cross-Plane Feedback function is implemented; partition is selected later.**
Feedback events fire on stop-the-line conditions, operator corrections, round-robin contradictions, Tri-Attention drift. Routing structure is deferred until partition is selected (E15b vs E15c). Until selection, log feedback events with both potential routing targets.

**RC-9: ATP construction runs at session-end as procedural controller operation.**
Controller orchestrates ATP build. Each layer registers serializable state. Builder produces manifest with hash. ATP is verifiable end-to-end before transfer. ATP verification runs at session-start on Mode A path.

**RC-10: Five Implicit Structuring Tools are recoverable cognitive operators.**
Mosaic must restore Fishbone, SWOT, Decision Trees, Virtual Whiteboards, Word Clusters as named cognitive operators accessible to workers via skill_core. Trigger conditions per v4.5 §I.F. These were lost in v5-c; their absence contributed to unstructured persona output.

---

## 8. Next Artifact Recommendation

**SEM_LAYER_RESOLUTION.md**

Rationale: the substrate dependency graph is now structurally corrected. Layer 5 (Admissibility) is anchored on SEM gates with concurrent stop-the-line, but the SEM internal structure has an unresolved tension flagged in RTFA.v0 §8.1: the question of whether SEM uses 16 criteria (Q1–Q16, weighted) from the v4.5 SEM session ledger or 6 criteria (K1–K6) per the v5-c MOSAIC v2.2 diagram, and how K8 (Compression survivability) relates to either schema.

This question is canon-blocking for Layer 5 specification. Cannot produce SUBSTRATE_SPEC_v0.1 without it. Cannot produce BLUEPRINT_v0.1 without SUBSTRATE_SPEC. Resolving SEM layer is the next forensic task.

Method: walk the SEM session ledger (8000+ lines) primary evidence, document the criterion lineage from the early 12-weighted-criterion form through the operator's CR-009 correction (97.5% threshold), through the v5-c K1–K6/K8 framing. Identify which is canon and how the criteria map (compression vs preservation vs renaming).

Inputs: `song.excellence.matrix.iterative.design.session.txt`, `song.excellence.yaml`, v4.5 monolith §2.2, v5-c MOSAIC v2.2 Plane 3, operator's CR-009 statement.

Output: SEM_LAYER_RESOLUTION.md with: criterion lineage, mapping table (v4.5 12-criterion → v5-c K1–K6/K8), operator-confirmed canon, blocked/needs-source items, runtime implications for Layer 5.

**Not next:** SUBSTRATE_SPEC_v0.1, PERSONA_SCHEMA_DECISION, CONVERSATION_LAYER_LINEAGE, BLUEPRINT_v0.1. All blocked on either SEM_LAYER_RESOLUTION or pending operator decisions for OD-4 substrate boundary (NS-4).

---

**End SDG.v0.1.2026-04-28**

*Substrate dependency graph corrected against SEC.v4.5 evidence and operator decisions OD-1 through OD-5. Three edges rejected, two edges split into orthogonal pairs, one edge reversed, five new edges added, one anchor edge made explicit (E21 LOCK gate). All edges carry explicit source lineage. CANON / CANDIDATE / NEEDS SOURCE / REJECTED status assigned per edge. Runtime consequences enumerated. Next forensic task is SEM_LAYER_RESOLUTION.md to unblock Layer 5 specification.*

*All edges remain CANDIDATE pending operator confirmation. FOIL discipline honored.*
