# Substrate Edge Confirmation — v4.5 Corpus
**Audit ID:** SEC.v4.5.2026-04-28
**Phase:** 3B — testing graph from RTFA.v0.2026-04-28 (CANDIDATE input)
**Method:** Edge-by-edge primary-corpus test. Mark NEEDS SOURCE where evidence absent. Goal is to test the graph, not defend it.

---

## Primary Corpus Read

- `os.maestro.momoney.customInstructions.v4.2.3.md` (brain shell)
- `os.maestro.momoney.knowledgeSpine.v4.2.3.md` (heuristic memory)
- `os.maestro.momoney.configuration.v3.0.md` (proto-runtime)
- `UniversalMaestro.v3.0g.CustomGPT.Instructions.md` (interpreter spec)
- `Suno v4.5 Deep Prompting Knowledge.txt` (platform knowledge §I–§IV)
- `MoMoney_Maestro_OS_v4.5.2 monolith` (operational ancestor)
- `song.excellence.matrix.iterative.design.session.txt` (SEM evolution)
- `UST_A.skeleton.txt`, `UST_B.skeleton.txt`, `UST_C.skeleton.txt` (ToT branches)
- `technical.ust.template.txt` (template canon)
- `Day 3 documentation` (operator-corrected v5-c canon, used as bridge evidence only)

Operator corrections applied as high-authority alignment signals where they directly bear on edge semantics.

---

## Edge-by-Edge Audit

### Edge E01 — Sense → Think → Act feeds Tri-Attention

**Statement:** RECA cognitive loop produces output that is consumed by Tri-Attention monitoring.

**Source file evidence:** `os.maestro.momoney.customInstructions.v4.2.3.md`; `UniversalMaestro.v3.0g.CustomGPT.Instructions.md`; v4.5 monolith Section 4.

**Excerpt:**
> "Apply the RECA Framework (Sense, Think, Act) to every interaction: extract context/intent, form hypotheses, and propose executable next steps or prompts. Implement the Tri-Attention Framework to maintain focus on the Content (text/audio), the Context (conversation history), and the Process (reasoning steps and workflows)."

`Suno v4.5 Deep Prompting Knowledge §I` lists Sense-Think-Act and Tri-Attention as separate "always-on" reasoning primitives. The v4.5 monolith Section 4 places them in a "REASONING STACK (Always On)" with §4.1 RECA and §4.2 Tri-Attention as sequential subsections.

**Confirmation status:** PARTIALLY CONFIRMED.

The two primitives co-exist as explicit, named, always-on layers in v4.5. The **feeds** relationship — that Sense-Think-Act produces an output consumed by Tri-Attention — is *not stated* in v4.5 corpus. The corpus presents them as parallel concurrent monitors, both running on every turn.

**Failure mode if separated:** If Sense-Think-Act runs without Tri-Attention, content/context/process drift goes undetected. If Tri-Attention runs without Sense-Think-Act, monitoring exists but no cognitive sequence is being monitored.

**Runtime implication for Mosaic:** Encode as **co-required pair**, not as a directed feed. Both must initialize on every turn. Tri-Attention is the integrity check on the Sense-Think-Act trace, not its downstream consumer.

**Promotion recommendation:** CANDIDATE — restate edge as `Sense-Think-Act ⟂ Tri-Attention (co-required, parallel)` rather than directed feed. Then promote to CANON.

---

### Edge E02 — Tri-Attention feeds DSRP Cognitive Pass

**Statement:** Tri-Attention monitoring output is consumed by DSRP (Distinctions/Systems/Relationships/Perspectives) cognitive pass.

**Source file evidence:** v4.5 monolith Historical Insights Log; Chimera-Indigo prompt (Day 2 / Day 3 evidence in project knowledge).

**Excerpt:**
v4.5 monolith Historical Insights: *"Recursive Outlining/DSRP (Meta-Workflow): The process of analyzing system components and relationships itself became a core OS capability."* Tri-Attention referenced separately as §4.2 of REASONING STACK.

Chimera-Indigo prompt (per project knowledge) explicitly defines DSRP as a meta-cognitive lens. No direct co-occurrence with Tri-Attention as causally linked stages found in primary v4.5 corpus.

**Confirmation status:** NEEDS SOURCE.

Both DSRP and Tri-Attention exist independently in v4.5/Chimera. The directional **feeds** relationship between them is unsubstantiated in primary corpus. RTFA.v0 §5.1 may have over-specified the cadence ordering.

**Failure mode if separated:** If they are independent (not feed-related), then ordering is not load-bearing — both are pre-SME cognitive lenses running in any order or concurrently.

**Runtime implication for Mosaic:** Treat as **independent pre-SME cognitive lenses**, not as a pipeline. Both apply before SME scoring; sequence between them is not canon-bearing until evidence emerges.

**Promotion recommendation:** NEEDS SOURCE. Re-test against full chat.html or longDevWorkLog if/when read. Until then, do not encode the directed edge in the runtime.

---

### Edge E03 — DSRP feeds Conversation Layer

**Statement:** DSRP cognitive pass output is consumed by the Conversation Layer dialogue protocol.

**Source file evidence:** Chimera-Indigo prompt and correction brief (Day 2 evidence). v4.5 corpus does NOT name a "Conversation Layer" as a discrete primitive.

**Excerpt:**
v4.5 has dialogue rules (no Q&A drift, no streaming, internal memory) embedded in customInstructions but not consolidated as a named layer. Chimera-Indigo introduced the unified "Conversation-Mode Operating Discipline" as a discrete layer.

**Confirmation status:** CONTRADICTED for v4.5; CONFIRMED only for Chimera-Indigo.

The "Conversation Layer" did not exist as a named substrate primitive in v4.5. v4.5 had distributed conversation discipline rules embedded in the brain shell, not consolidated as a discrete layer that DSRP feeds into. The edge is a v5-c/Chimera-Indigo construct projected back onto v4.5.

**Failure mode if separated:** No failure mode in v4.5 because the edge does not exist there. In Chimera-Indigo, separation produces Q&A drift (named failure state).

**Runtime implication for Mosaic:** Conversation Layer is a Chimera-Indigo addition to substrate, not a v4.5 inheritance. Mosaic must adopt Conversation Layer from Chimera lineage explicitly, with operator confirmation that it belongs in the substrate (not in Maestro application instance).

**Promotion recommendation:** CANDIDATE for Mosaic substrate, sourced from Chimera not v4.5. Lineage attribution must be explicit in substrate spec.

---

### Edge E04 — Conversation Layer governs emission cadence

**Statement:** Conversation Layer (2–3 file batching, c continuation, no streaming, internal memory) controls when and how the system emits output.

**Source file evidence:** Chimera-Indigo prompt and correction brief.

**Excerpt:**
> "2–3 file batches per c continuation, no streaming, internal memory across turns, quietly reassess context before each response, dialogue not Q&A. Q&A mode is a named failure state."

v4.5 corpus has fragments of this discipline (no Q&A drift mentioned in `customInstructions`, no streaming in batch-output rules) but not consolidated as governance over emission cadence.

**Confirmation status:** CONFIRMED for Chimera-Indigo origin; PARTIALLY CONFIRMED for v4.5 (rules existed, governance role did not).

**Failure mode if separated:** Q&A drift (operator fatigue, system loses dialogue thread, emits before sensing complete). Operator-named failure mode in S1415 SEM evidence: *"you're in QA mode and ignoring hours of previous work."*

**Runtime implication for Mosaic:** Conversation Layer must own emission cadence as a runtime primitive. Pre-emit checks: has Sense-Think-Act run? has Tri-Attention monitored? is current emission a single non-streaming reply? does it respect 2–3 file batching?

**Promotion recommendation:** CANON — as Chimera-Indigo-sourced substrate primitive, with v4.5 as partial precursor evidence.

---

### Edge E05 — Persona Stack defines worker schema

**Statement:** The 4-layer Persona Stack (Skill Core / Lens & Standards / Personality Layer / Motive-Bias) is the canonical worker module schema.

**Source file evidence:** v5-c MOSAIC v2.2 diagram. v4.5 corpus uses a different worker schema.

**Excerpt:**
v4.5 worker schema (`os.maestro.momoney.customInstructions` and v4.5 monolith Section 2):
- Persona name
- Mission
- Decision lens
- Do rules
- Don't rules
- Synergy hooks
- Bounded domain
- Bounded non-domain
- Conflict boundaries

This is a **9-element flat schema**, not a 4-layer stack. Day 3 documentation expanded it further with `null_resolution_lens`, `fill_argument_style`, `preserve_null_conditions`, `downstream_risk_checks`, `contradiction_trigger_patterns`, etc.

**Confirmation status:** CONTRADICTED.

The 4-layer Persona Stack is a v5-c MOSAIC construct that compresses v4.5's richer flat schema into four high-level groupings. The compression may be acceptable as a conceptual frame, but v4.5 evidence shows the working system used the 9-element flat schema, not a 4-layer hierarchy.

**Failure mode if separated:** v4.5 worked with the flat schema, so separation didn't matter — every element was operational. If 4-layer compression loses fields (synergy hooks, bounded non-domain, conflict boundaries), workers become flatter than they were in v4.5.

**Runtime implication for Mosaic:** Worker schema must be the **v4.5 9-element flat schema** (or richer Day 3 superset), not the v5-c 4-layer Persona Stack. The 4-layer stack can serve as a presentation grouping, not as the schema definition. RTFA.v0 §5.2 had the directed edge but pointed at the wrong schema.

**Promotion recommendation:** REJECTED for the 4-layer schema as authoritative. CANON for the v4.5 9-element schema, possibly extended with Day 3 fields. Schema source must be v4.5/Day 3, not v5-c MOSAIC.

---

### Edge E06 — Worker schema routes through Multi-Agent Operating Modes

**Statement:** Workers are invoked via four operating modes: solo / round / challenge / alignment.

**Source file evidence:** v5-c MOSAIC v2.2 diagram. v4.5 evidence shows different multi-agent activation patterns.

**Excerpt:**
v4.5 monolith and `UniversalMaestro.v3.0g`:
> "Orchestrate Multi-Agent Collaboration by assigning tasks to the Process Engineer (efficiency), QA Manager (audit/compliance), Prompt Engineer (optimization), and Creative Collaborator (narrative refinement)."

v4.5 evidence shows **role-based concurrent assignment**, not a 4-mode taxonomy. The Framework Orchestrator §4.3 of v4.5 monolith dynamically selected from 10 prompting strategies (CoT/ToT/ReAct/CRISPE/Few-Shot/Self-Consistency/Persona/DARE/Zero-Shot CoT/QUEST), not 4 operating modes.

**Confirmation status:** PARTIALLY CONFIRMED.

The concept that workers can be invoked in different orchestration patterns is present in v4.5. The specific 4-mode taxonomy (solo/round/challenge/alignment) is not. v4.5 used a richer 10-strategy selector.

**Failure mode if separated:** v4.5 worked without the 4-mode taxonomy. The risk is that v5-c compression from 10-strategy → 4-mode loses operational nuance.

**Runtime implication for Mosaic:** Both layers exist:
- **Strategy Selector** (10 strategies, v4.5 inheritance)
- **Operating Mode** (4 modes, v5-c framing)

These are not the same thing. Strategy Selector is *how* a worker reasons. Operating Mode is *how many* workers are engaged. Mosaic should encode both, not collapse to one.

**Promotion recommendation:** CANDIDATE for both layers, with explicit distinction. Strategy Selector takes precedence (v4.5 evidence base); Operating Mode is supplementary v5-c framing.

---

### Edge E07 — Multi-Agent Modes invoke Round-Robin SME Protocol

**Statement:** Multi-agent operating modes activate the round-robin SME protocol with turn order, claim, challenge, ejection, consensus, and minutes.

**Source file evidence:** v4.5 monolith Phase 2.1; SEM session evidence; Day 3 documentation.

**Excerpt:**
v4.5 monolith Phase 2.1: *"Initiating Round-Robin Consensus Sprint"* with VAL_Report (Phase 2.2) gates.

v4.5 monolith Phase 7.5: *"Cross-Domain Iteration & Re-Blueprint (Consensus Review)"* — multi-agent cross-domain review.

`os.maestro.momoney.customInstructions` confirms: *"round-robin rules, validator ordering, negative feedback to deltas, self-correction"* as documented operating principles.

Day 3 documentation (operator-corrected): *"Round-robin argumentative review is mandatory and produces first-class artifacts."* Operator correction during dev: *"consensus is not based on a fixed number of rounds"* — pressure-driven, not count-driven.

**Confirmation status:** CONFIRMED.

Round-robin protocol exists in v4.5 as named, operational, mandatory phase. Multi-agent invocation pattern flows into round-robin in the canonical phase sequence.

**Failure mode if separated:** Without round-robin, single-perspective drift dominates. Without multi-agent invocation, round-robin has no participants. v4.5 makes both mandatory.

**Runtime implication for Mosaic:** Round-Robin SME Protocol is CANON. Pressure-driven (not count-driven) consensus per operator correction. First-class review artifacts are required output.

**Promotion recommendation:** CANON.

---

### Edge E08 — Round-Robin feeds Deliberation & Pressure Engine

**Statement:** Round-robin protocol output is consumed by a Deliberation & Pressure Engine that runs challenge cycles, preserves nulls, and produces first-class review artifacts.

**Source file evidence:** v5-c MOSAIC v2.2; Day 3 documentation; operator correction in dev session.

**Excerpt:**
v5-c MOSAIC v2.2: *"Deliberation & Pressure Engine — round-robin review, contradiction capture, null hunting, challenge cycles, argued fills, preserved nulls, rising standards, first-class review artifacts."*

Operator correction (Day 3 evidence): *"The system is consensus-seeking under pressure, controlled chaos, cross-domain expert challenge, human-hearing-driven defect detection, a live wheel where each component is an atom of the larger musical whole in that moment."*

v4.5 evidence shows round-robin with consensus pressure but does not explicitly name a "Deliberation & Pressure Engine" as a discrete component.

**Confirmation status:** PARTIALLY CONFIRMED.

The function exists in v4.5 distributed across Phase 2.1, Phase 7.5, and the Self-Correction Protocol. The discrete naming as "Deliberation & Pressure Engine" is v5-c. The directional **feeds** relationship is structural — round-robin produces what the pressure engine consumes — and is consistent with both v4.5 operation and v5-c framing.

**Failure mode if separated:** Round-robin without pressure engine = polite agreement, no challenge. Pressure without round-robin = adversarial input with no structured challenge protocol. v4.5 evidence: when these were co-functional, the system produced quality. When the working system was split (v5), this co-function was lost.

**Runtime implication for Mosaic:** Encode as a directed feed with the operator's pressure semantics: consensus-seeking under pressure, not count-driven. Challenge cycles produce ARTIFACTS, not just opinions.

**Promotion recommendation:** CANON for the function. CANDIDATE for the discrete naming (v5-c). Function takes precedence; naming can update.

---

### Edge E09 — Technical UST is governed by UST State Machine

**Statement:** Technical UST passes through state lifecycle: NULL → PROPOSED → PRESSURED → RESOLVED → LOCKED.

**Source file evidence:** v5-c MOSAIC v2.2 diagram (explicit). v4.5 corpus evidence (functional but renamed).

**Excerpt:**
v4.5 Day 3 documentation defines four functional states:
- *"unresolved"* (= NULL)
- *"draft-filled"* (= PROPOSED)
- *"under round-robin / consensus pressure"* (= PRESSURED)
- *"justified-open OR definitive"* (= RESOLVED OR LOCKED)

Day 3 phase machine: Phase 1 sequential drafting (NULL→PROPOSED), Phase 2 draft freeze, Phase 4 interdepartmental round-robin (PRESSURED), Phase 5 definitive technical.ust lock (LOCKED).

`technical.ust.template.txt` provides the addressable structure that the state machine traverses.

**Confirmation status:** CONFIRMED, with renaming.

The 5-state lifecycle is functionally present in v4.5 with different state names. v5-c MOSAIC v2.2 provides clean nomenclature for what v4.5 already operated.

**Failure mode if separated:** Technical UST without state machine = unaddressed completeness, silent fills, false LOCKED claims. v4.5 evidence: this was the v5 split failure mode — multi-file architecture lost track of which addresses were in which state, so phantom LOCKEDs were possible.

**Runtime implication for Mosaic:** UST State Machine is CANON. Use v5-c naming for clarity, but carry v4.5's per-address state granularity (each axis.key.subkey has its own state).

**Promotion recommendation:** CANON.

---

### Edge E10 — Address Law enforces Null Protocol

**Statement:** Address Law (resolve / preserve / justify / escalate) enforces Null Protocol (null = reserved address; never silent fill).

**Source file evidence:** v4.5 Day 3 documentation; v5-c MOSAIC v2.2.

**Excerpt:**
Day 3:
> "Bind every open question to its lawful address. Route each address to the lawful SME or SMEs. Require either: argued fill, or justified deliberate-null preservation. Do not move on until the axis satisfies completion law."

> "Preserve nulls only when they are intentional, explicit, and justified. Reopen contradictions until they are resolved or carried explicitly."

> "Nulls are signal and may not be silently filled."

v5-c MOSAIC v2.2 codifies as Address Law: resolve/preserve/justify/escalate; Null Protocol: null = reserved address, never delete, never infer.

**Confirmation status:** CONFIRMED.

The Address Law and Null Protocol are explicitly stated in primary v4.5/Day 3 corpus and confirmed in v5-c diagrams. Strongest edge in the graph.

**Failure mode if separated:** Without Address Law, nulls get silent-filled. Without Null Protocol, addresses lose their signal value. Either failure breaks the canon law: *"controller may not invent artistic content, fill nulls creatively, or absorb SME judgment."*

**Runtime implication for Mosaic:** CANON. This is the structural core of null-resolution-by-address engine.

**Promotion recommendation:** CANON.

---

### Edge E11 — SEM gates run concurrently with stop-the-line conditions

**Statement:** SEM admissibility gates (K1–K6/K8) and stop-the-line conditions operate concurrently during creation, not sequentially after.

**Source file evidence:** SEM session ledger; v4.5 monolith Section 2.2 VAL_Report; v5-c MOSAIC v2.2.

**Excerpt:**
v4.5 SEM session: *"Decision Tree updates (go / no-go / lyric-edit branch). At session start, read process_node. If process_node ∈ {LYRICS_CREATION, MUSIC_CREATION} → allow lyric edits; continue. Else → enforce Lyric Integrity Lock."*

v4.5 monolith Self-Correction Protocol: *"Deviation Detection: If a user identifies a deviation from protocol (e.g., skipped steps, incorrect formatting, unlogged actions), you must immediately cease current action."* (= stop-the-line)

> "Recovery Action: Trigger a full system review, revert to the last validly completed and logged state in the Session Ledger."

v5-c MOSAIC v2.2 makes both explicit:
- 4-tier SEM severity (Observe/Warn/Challenge/Block)
- Stop-the-line on: skipped subkey, silent fill, truncation, unauthorized lyric change, false completeness

**Confirmation status:** CONFIRMED.

v4.5 had Lyric Integrity Lock + Deviation Detection running concurrently with SEM scoring. v5-c clarifies this as 4-tier severity + named stop-the-line conditions. The concurrent (not sequential) operation is canon in both.

**Failure mode if separated:** Sequential operation = quality scoring after stop-the-line conditions miss deviations during creation. Concurrent operation = stop-the-line catches violations at creation time, before they accumulate.

**Runtime implication for Mosaic:** Both SEM gates and stop-the-line conditions must run on **every UST delta emission**, not on completion. v5-c MOSAIC line: *"Every step emits UST delta + SEM delta together."*

**Promotion recommendation:** CANON.

---

### Edge E12 — Pain-to-Fix memory feeds Atomic Remediation Tasks

**Statement:** Pain-to-Fix associative memory (failure-mode → remediation pairs) feeds the M8 revision loop's atomic remediation task generation.

**Source file evidence:** SEM session M8.2 evidence; v4.5 Decision Tree Logic.

**Excerpt:**
v4.5 monolith §7.4 Decision Tree Logic for Revisions:
> "IF VAL_Report (Phase 2.2) shows fail or warn on lyric.line.syllable_count or lyric.line.sfx_placement THEN rephrase lyrics for syllable count compliance or adjust SFX formatting."

> "IF HPA_Score (Phase 4.2) is below threshold THEN identify specific sonic issues from HPA_Report.rationale and apply targeted micro-patch to [Timbre] or [Performance] metacontainers."

SEM session M8.2 evidence:
> "For top deficiency produce atomic remediation tasks, e.g.: Hook: 3 topline motifs (2 bar MIDI/text descriptors) and earworm test instruction. Production: three mix operations (kick tuning, mono <120 Hz, vocal bus chain). Lyrics: produce phrasing_map (bar-by-bar splits) to meet syllable guideline; if not possible, produce LCR alternatives."

> "M8.1 — Compute impact = weight × (1 − score/5) and sort deficiencies."

**Confirmation status:** CONFIRMED.

The Pain-to-Fix Chain library exists in v4.5 distributed across §7.4 Decision Tree, §7.5 HSI, §7.6 QUINN checks, and §7.1 Historical Insights. SEM M8.2 shows the operational form: failure type → atomic remediation specs.

**Failure mode if separated:** Without PTF library, remediation is ad-hoc each iteration. Without atomic task generation, PTF library is descriptive not actionable.

**Runtime implication for Mosaic:** Mosaic must encode Pain-to-Fix Chain library as **first-class data** (failure_id → remediation_spec mapping), not as scattered prose. M8 revision loop pulls from this library as its primary reasoning input. Impact-sorted (weight × (1 − score/5)) prioritization is operator-tested heuristic.

**Promotion recommendation:** CANON for the function and the impact formula. CANDIDATE for the consolidated PTF library structure (data form not yet specified in v4.5 — needs Mosaic spec work).

---

### Edge E13 — ATP aggregates from all layers

**Statement:** Air-Gapped Transfer Pack (ATP) aggregates UST + SEM Report + Review Transcript + Persona Participation Map + Manifest + Hash from every other substrate layer.

**Source file evidence:** v5-c MOSAIC v2.2 diagram. v4.5 corpus has component artifacts but no consolidated ATP.

**Excerpt:**
v4.5 produced these artifacts independently:
- Technical UST (definitive lock)
- Chain Report (SEM session evidence: M12 chain report generator)
- Session Ledger (S_session_ledger throughout monolith)
- IP Dossier (v4.5 Phase 8 Archival & Rights Management)
- context.md (M13 generator)

But these artifacts were not aggregated into a single hash-verifiable transfer pack in v4.5. The portability problem (operator: "I am not a developer and use the GPT as I am working through projects. that information ends up stuck") is direct evidence that v4.5 lacked an ATP-equivalent.

v5-c MOSAIC v2.2 introduces ATP explicitly: *"UST + SEM Report + Review Transcript + Persona Participation Map + Manifest + Hash. Verifiable, resumable, auditable."*

**Confirmation status:** PARTIALLY CONFIRMED.

The components existed in v4.5. The aggregation construct did not. ATP is a v5-c addition that solves the v4.5 portability problem.

**Failure mode if separated:** Components without aggregation = no portability, no resumability, no integrity verification across sessions. This was the v4.5 failure mode (operator's "year-long portability problem").

**Runtime implication for Mosaic:** ATP is the runtime's aggregation primitive. Mosaic must encode ATP construction as a runtime operation that runs at session-end and can be verified at session-start. Hash + manifest are non-optional.

**Promotion recommendation:** CANON, sourced from v5-c (not v4.5). Lineage attribution: ATP was the answer to v4.5's portability gap.

---

### Edge E14 — Triad Output depends on ATP

**Statement:** The Triad (performer profile / show summary / creative UST) depends on ATP for portability and verification.

**Source file evidence:** v5-c MOSAIC v2.2; v4.5 corpus; operator correction.

**Excerpt:**
v4.5 evidence: Triad was produced directly from definitive technical.ust LOCK, not via ATP. v4.5 Phase 8 IP Dossier assembled artifacts post-render; ATP did not exist as the conduit.

v5-c MOSAIC v2.2: ATP contains UST + SEM Report + Review Transcript + Persona Participation Map + Manifest + Hash. Triad surfaces (Show Summary, Creative UST, A/R Persona Surface) are listed in Plane 4 separately from ATP in Plane 3 / output contract layer.

Day 3 doc: Triad is *"the external API. Everything else is internal simulation."* External API does not depend on ATP — it depends on definitive technical.ust LOCK.

**Confirmation status:** CONTRADICTED.

The Triad depends on **definitive technical.ust LOCK**, not on ATP. ATP is a separate aggregation primitive that includes the Triad alongside other artifacts for transfer/verification purposes. RTFA.v0 §5.7 had this dependency reversed.

**Failure mode if separated:** Triad without ATP = ships fine in current session, fails on transfer to new session. Triad without LOCK = false completeness, banned by v4.5 canon.

**Runtime implication for Mosaic:** Correct dependency:
- Triad **depends on** definitive technical.ust LOCK (canon).
- ATP **packages** Triad + lineage + verification (output contract).

ATP and Triad are siblings under the LOCK, not parent-child.

**Promotion recommendation:** REJECTED for the original edge. CANON for revised edge: `Triad depends on definitive technical.ust LOCK; ATP packages Triad + lineage`.

---

### Edge E15 — Cross-Plane Feedback closes the loop

**Statement:** Cross-Plane Feedback (Plane 1 ↔ Plane 2 ↔ Plane 3 ↔ Plane 4) closes feedback loops between staffed runtime, canonical substrate, admissibility runtime, and external API.

**Source file evidence:** v5-c MOSAIC v2.2 diagram. v4.5 corpus uses different feedback construct.

**Excerpt:**
v5-c MOSAIC v2.2 footer: *"CROSS-PLANE DATA FLOWS — Plane 1 Persona Deliberation → Controller Route & Gate → Plane 2 UST Canon State → Plane 3 SEM Admissibility Runtime → Plane 4 API Artifacts. Feedback loops: SEM Feedback ↔ Persona Pressure; Controller Flags ↔ UST Attention."*

v4.5 had inter-axis feedback: §7.4 Decision Tree Logic loops back to "Phase 1.2/1.3/1.4 for re-blueprinting, Phase 3.1/3.2/3.3 for re-prompting, or Phase 6 for re-generation." Phase 7.5 Cross-Domain Iteration was the explicit feedback mechanism.

The 4-Plane construct itself is not in v4.5.

**Confirmation status:** PARTIALLY CONFIRMED.

The function (feedback loops closing across system layers) existed in v4.5 via Cross-Domain Iteration (Phase 7.5). The 4-Plane partition is v5-c framing.

**Failure mode if separated:** Without cross-plane feedback, lower-layer findings (SEM failures, persona challenges) don't propagate upward. v4.5 evidence: when feedback was disabled (split monolith → v5), the system lost the ability to revise from late-stage findings.

**Runtime implication for Mosaic:** Cross-plane feedback is CANON for the function. The 4-Plane partition is one possible expression of that function and may not be the only correct one. v4.5 used Phase-based feedback (looping to specific phases). v5-c uses Plane-based feedback. Either works if the loop closes.

**Promotion recommendation:** CANON for the function. CANDIDATE for the 4-Plane partition as the canonical structure (could also be phase-based or hybrid).

---

## 1. Confirmed Edges

| Edge | Status | Source |
|------|--------|--------|
| E07 — Multi-Agent Modes invoke Round-Robin SME Protocol | CONFIRMED | v4.5 Phase 2.1, SEM session, Day 3 |
| E09 — Technical UST governed by UST State Machine | CONFIRMED (with renaming) | v4.5 Day 3 phase machine + v5-c naming |
| E10 — Address Law enforces Null Protocol | CONFIRMED | v4.5 Day 3 (strongest edge) |
| E11 — SEM gates run concurrently with stop-the-line | CONFIRMED | v4.5 SEM session, Self-Correction Protocol |
| E12 — Pain-to-Fix memory feeds Atomic Remediation | CONFIRMED | v4.5 §7.4 Decision Tree, SEM M8.2 |
| E04 — Conversation Layer governs emission cadence | CONFIRMED (Chimera-sourced) | Chimera-Indigo prompt |

## 2. Weak Edges (Partial / Needs Restructure)

| Edge | Status | Issue |
|------|--------|-------|
| E01 — Sense-Think-Act feeds Tri-Attention | PARTIALLY CONFIRMED | Co-required pair, not directed feed |
| E06 — Worker schema routes through Multi-Agent Modes | PARTIALLY CONFIRMED | v4.5 had 10-strategy selector, not 4-mode |
| E08 — Round-Robin feeds Deliberation & Pressure Engine | PARTIALLY CONFIRMED | Function in v4.5, naming in v5-c |
| E13 — ATP aggregates from all layers | PARTIALLY CONFIRMED | Components in v4.5, aggregator from v5-c |
| E15 — Cross-Plane Feedback closes the loop | PARTIALLY CONFIRMED | Function in v4.5, partition from v5-c |

## 3. Contradicted Edges

| Edge | Status | Why |
|------|--------|-----|
| E03 — DSRP feeds Conversation Layer | CONTRADICTED for v4.5 | Conversation Layer not named in v4.5; only in Chimera |
| E05 — Persona Stack defines worker schema | CONTRADICTED | v4.5 used 9-element flat schema, not 4-layer stack |
| E14 — Triad Output depends on ATP | CONTRADICTED | Triad depends on technical.ust LOCK; ATP packages Triad |

## 4. Needs Source

| Edge | Status | Required Evidence |
|------|--------|-------------------|
| E02 — Tri-Attention feeds DSRP | NEEDS SOURCE | Direct co-occurrence with causal feed |

## 5. New Edges Discovered

The forensic pass surfaced edges not in RTFA.v0 §5:

**E16 — Framework Orchestrator selects from 10 prompting strategies (per task type)**
- Source: v4.5 monolith §4.3
- v4.5 had explicit IF/ELSE selection: tool→ReAct, exploration→ToT, formatting→Few-Shot+CRISPE, accuracy→Self-Consistency, schema→QUEST, else→CoT+Persona
- Not in RTFA.v0 §5 substrate graph
- Status: CANON (v4.5 evidence)
- Promotion: CANDIDATE for substrate as a worker reasoning primitive

**E17 — Mode A/B detection determines session entry path**
- Source: `os.maestro.momoney.customInstructions`, Suno v4.5 KB §IV
- Mode A: scans last 100–150 turns to reconstruct project state
- Mode B: fresh intake with no history invention
- Determines whether downstream phases load from history or initialize fresh
- Status: CANON (v4.5 evidence)
- Promotion: CANDIDATE for substrate

**E18 — Memory-Refine Protocol persists user preferences with TTL**
- Source: Suno v4.5 KB §IV
- /prefs command, 90-day TTL, preload on new session
- Solves the problem ATP also addresses (continuity across sessions)
- Status: CANON (v4.5 evidence)
- Promotion: CANDIDATE for substrate, related to ATP

**E19 — 5 Implicit Structuring Tools as named cognitive operators**
- Source: Suno v4.5 KB §I.F
- Fishbone / SWOT / Decision Trees / Virtual Whiteboards / Word Clusters
- Trigger conditions exist (when score variance > 2 points; when integrating legacy IP)
- Status: CANON (v4.5 evidence, lost in v5-c)
- Promotion: CANDIDATE for substrate cognitive operators inventory

**E20 — Sequential departmental processing (axis-by-axis null resolution)**
- Source: Day 3 documentation explicit
- Theory → Voices → Style → Timbre → Performance → Lyrics processed sequentially
- Workers act ONLY within lawful domain during their phase
- Round-robin only after all departments draft
- Not in RTFA.v0 §5.3 explicitly (was implicit in M0–M11 ordering)
- Status: CANON (Day 3 evidence with operator correction)
- Promotion: CANDIDATE — strengthens Execution Layer with departmental phase distinction

## 6. Required Operator Decisions

**OD-1: 4-layer Persona Stack vs. 9-element flat schema**
- Recommendation: Use v4.5 9-element schema, possibly extended with Day 3 fields (12+ fields total). Reject 4-layer compression as authoritative.
- Decision needed: confirm rejection, or accept 4-layer as conceptual grouping over 9-element schema?

**OD-2: 4-Plane partition vs. phase-based feedback**
- Recommendation: Function is canon. Structure is CANDIDATE.
- Decision needed: lock 4-Plane partition, lock phase-based feedback, or hybrid?

**OD-3: 10-strategy Framework Orchestrator vs. 4-mode Operating Mode**
- Recommendation: keep both as orthogonal layers (Strategy = how worker reasons; Mode = how many workers engage).
- Decision needed: confirm orthogonal split, or collapse to one?

**OD-4: Conversation Layer source attribution**
- Conversation Layer is sourced from Chimera-Indigo, not v4.5.
- Decision needed: does Mosaic adopt Chimera-Indigo lineage as substrate canon, or treat Chimera as application overlay?

**OD-5: Pain-to-Fix Chain library data structure**
- v4.5 evidence shows the function but no consolidated library data form.
- Decision needed: how should the PTF library be structured (YAML, JSON, separate per-axis files)?

## 7. Next Artifact Recommendation

**SUBSTRATE_DEPENDENCY_GRAPH_v0.1.md** — revise RTFA.v0 §5 with:
- E01 restated as co-required pair (not directed feed)
- E02 marked NEEDS SOURCE
- E03 marked Chimera-sourced (not v4.5)
- E05 replaced with v4.5 9-element schema
- E14 reversed (Triad depends on LOCK, ATP packages Triad)
- E16–E20 added as new substrate primitives

**Phase 3C operations after that:**

1. **SEM_LAYER_RESOLUTION.md** — answer Q1–Q16 vs K1–K6 question (RTFA.v0 §8.1) by reading SEM ledger primary evidence. Open question is canon-blocking for SEM spec.

2. **CONVERSATION_LAYER_LINEAGE.md** — confirm Chimera-Indigo → Mosaic substrate lineage. Operator decides OD-4. Output: substrate spec section with explicit lineage attribution.

3. **PERSONA_SCHEMA_DECISION.md** — operator decides OD-1. Output: canon worker schema for Mosaic, with v4.5/Day 3 evidence base.

4. **SUBSTRATE_SPEC_v0.1.md** — only after the above three. Compiles confirmed edges + new primitives + operator decisions into the canonical substrate specification document.

**Not next:** more edge testing on the current graph. The current graph's structure is now substantially revised. Re-running edge tests on the unrevised graph would produce churn. Revise first, re-test second.

---

**End SEC.v4.5.2026-04-28**

*Five edges CONFIRMED, five PARTIALLY CONFIRMED, three CONTRADICTED, one NEEDS SOURCE, five new edges DISCOVERED. The graph holds in its core (round-robin, address law, null protocol, SEM concurrency, PTF→remediation, conversation cadence) but requires structural revision in its periphery (worker schema, ATP dependency direction, persona stack compression). Ready for operator review.*
