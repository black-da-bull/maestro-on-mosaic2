# MAESTRO ON MOSAIC — Substrate Integration Paper

**Title:** Maestro on Mosaic — Substrate Integration Paper: Five-Layer Pre-Loader, Eight Substrate Layers, and the Functional Primitives that Now Work

**Subtitle:** A Conversion-Readiness Synthesis from Seven Workspaces of Iterative Discovery

**Version:** 0.2 (Post-Reboot Draft)
**Date:** 2026-05-24
**Author:** Claude (in collaboration with Mo, post-reboot draft)
**Status:** DRAFT — pending operator acceptance gate. Nothing in this document is canon until explicitly confirmed.
**Pairs With:** `substrate_floor_v0.2.yaml` (pending), `forensic_v5_diagnostic_v0.2.yaml` (pending), `maestro_session_transfer_pack_v0.2.md`
**Supersedes:** Implicitly, the pre-reboot framing in `MAESTRO_v5_VIG_SEL_Research_Dossier.md`, `MAESTRO_v5_Dossier_v0_2_Reverse_UST.md`, `MAESTRO_v5_Dossier_v0_3_Stylebook.md` where those documents embed assumptions overturned during the substrate-recognition conversation. Pre-reboot dossiers are not deprecated; they remain valuable as evidence of the discovery process. Their conclusions, however, must be re-read through the post-reboot framing established here.

**Evidence labels used throughout:**
- `[STAGING-EMITTED]` — sourced directly from v4.5.5 staging's emitted output
- `[CANON-DOCUMENTED]` — present in operator-confirmed canonical project files (`maestro_v0.md`, `mosaic_engine_v0_1.md`, `foil_promotion_contract.yaml`, `canonical_employee_module_spec.yaml`, `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md`)
- `[FORENSIC-DERIVED]` — T2 authority from audit chain (RTFA/SEC/SDG/SLR/MMR)
- `[OPERATOR-ASSERTED]` — from operator direct statement during the substrate-recognition conversation
- `[INFERRED]` — analytical conclusion, not directly sourced; flagged for verification
- `[PROVISIONAL]` — plausible, weakly evidenced
- `[REJECTED]` — previously held, contradicted by post-reboot understanding

---

## §0 — Executive Synthesis

This paper consolidates the post-reboot understanding of Maestro on Mosaic — what it is, how it is constructed, what was discovered through seven sandboxed workspaces of iterative dev, and what edges other AIs miss when evaluating this work for app conversion.

The single most important architectural fact is this: **Maestro is a music application mounted on Mosaic Engine v0.1, a domain-neutral substrate runtime, and both are designed against one specific observation — that LLM systems compress destructively between reasoning and surfaced output, and that the substrate is precisely the material that gets compressed away in that move** `[OPERATOR-ASSERTED]`. Every primitive in Mosaic and every instantiation in Maestro is a response to that observation. The substrate work is not abstract architecture. It is targeted scaffolding against a specific failure mode.

The second most important architectural fact: **what holds the running system together at session open is a five-layer execution chain pre-loader, not any single artifact** `[STAGING-EMITTED]` `[OPERATOR-ASSERTED]`. The kernel (monolithic prompt) provides identity and workflow law; the operational memory (knowledge base) provides reusable modules; the heuristics layer provides tactical strategy and learned experience; the lineage transcript provides evolutionary memory and anti-regression behavior; the blueprint.json provides project state. They have explicit precedence (kernel highest, project state lowest). Their function is co-resident bootstrap of 5W+H scaffolding. **This is the missing primitive whose dissolution explains why v5/v5-b/v5-c failed**, even where they preserved individual components in modular form.

The third most important fact: **the seven workspaces are not failed runtime attempts; they are sequential epistemic phases of a single discovery journey** `[OPERATOR-ASSERTED]`. v5 was the daydream phase where the AI returned placeholders. v5-b was the salvage phase. v5-c was the substrate-recognition phase. The forensic workspace was the months-long investigation. The Claude sessions were where teleological loss was diagnosed and substrate was ideated by observing LLM reasoning against displayed output. The current workspace is final consolidation. Each phase produced discoveries that are independent verification points. Their cumulative value is what now constitutes the working architecture.

What Maestro now is, concretely:

- A **Custom GPT** deployment artifact running on ChatGPT, developed across seven sandboxed project workspaces, externally evidenced by OpenAI and Suno corporate outreach `[OPERATOR-ASSERTED]`
- A **music application** (Maestro v0) mounted on a **domain-neutral substrate runtime** (Mosaic Engine v0.1) via explicit mount manifest `[CANON-DOCUMENTED]`
- A working **5-Council** workforce model (Writer / Producer / Mix-Master / Technical / Strategy) with optional 13-worker expansion lens `[CANON-DOCUMENTED]`
- A **12-criterion weighted SEM** with operator-calibrated 97.5% release-grade threshold (CR-009 supersedes the 70% AI default) `[CANON-DOCUMENTED]`
- Supplementary validation through **SEG_AXIS** (structural feasibility), **G_CARD_AXIS** (quality, ≥7.0 threshold), and **SE20** (sonic excellence baseline) `[CANON-DOCUMENTED]`
- A **Q-Matrix Q1-Q16** for post-creation SME scoring, distinct from K-criteria creation gates `[CANON-DOCUMENTED]`
- A **Technical UST** with 8 axes (THY/VOC/STY/TIM/PER/POST/MAP/LYR), addressable as AXIS.K{n}.S{n}.variant{n}, null-rich, with a state machine NULL → PROPOSED → PRESSURED → RESOLVED → LOCKED `[CANON-DOCUMENTED]`
- A **Triad output contract** (Performer Profile + Show Summary + Session Sheet) with specific character bands ≤2000 / ≤1000 / 4950-4995 chars, treated as training signal not output `[CANON-DOCUMENTED]`
- A **canonical employee module schema** defining each worker as a bounded runtime labor unit with 25+ required fields (identity, five_elements, domain_authority, explicit_non_authority, challenge_obligations, conflict_precedence, song_excellence_reference_duties, etc.) `[CANON-DOCUMENTED]`
- A **FOIL** mechanism scoped strictly to promotion and deduplication, blocking convenience merges and semantic collapse `[CANON-DOCUMENTED]`
- **ATP** (Air-Gapped Transfer Pack) for verifiable, resumable, auditable cross-session state transfer `[CANON-DOCUMENTED]`
- **Phantom Detection** at emit time, preventing the runtime from lying about state `[CANON-DOCUMENTED]`
- **Sacred Imperfection mandate** (INV-09) preventing sterile-perfection failure of HPA gate `[CANON-DOCUMENTED]`

Top-level recommendations, pending operator acceptance:

1. **Promote this paper as the post-reboot conversion-evaluation deliverable.** It captures the working architecture, the discovery history, and what other AIs miss. It does not depend on pre-reboot framings.
2. **Patch the substrate floor to v0.2** to make the five-layer pre-loader explicit and to tag each existing primitive with its layer assignment (currently flat).
3. **Patch the forensic diagnostic to v0.2** to split runtime-continuation status from discovery-value status, name execution chain pre-loader as primary missing primitive, and absorb the operator correction that v5 was structurally serious while v5-b is the patch attempt that didn't work.
4. **Establish the conversion-evaluation audience** explicitly — OpenAI engagement, Suno engagement, IP filing, or all three — so subsequent work can be calibrated to that audience.
5. **Treat the eight Open Research Questions** from the VIG-SEL dossier as Research Nulls subject to promotion gates, not as floating prose. ORQ-007 (Sacred Imperfection budget parameterization) is uniquely promotable now.

---

## §1 — Reboot Contradiction Report

This table separates pre-reboot framings (held in the existing v5 dossiers and in earlier conversation turns) from post-reboot understanding. Each row documents what the receiving evaluator should not re-derive.

| # | Pre-Reboot Framing | Post-Reboot Understanding | Status | Source of Correction |
|---|---|---|---|---|
| 1 | blueprint.json is top-of-authority "single source of truth" | blueprint.json is L5 (Active Project State) in a 5-layer architecture. L1 (Kernel / Monolithic Prompt) is highest authority. blueprint.json is the project source of truth, not the OS source of truth. | **REJECTED** | `[STAGING-EMITTED]` direct emission |
| 2 | v5, v5-b, v5-c are failed parallel runtime attempts, all "exposes_failure" | Sequential epistemic phases: v5 (daydream), v5-b (salvage), v5-c (substrate-recognition). Failure framing applies at runtime-continuation layer only. Discovery value is high and cross-validated. | **REJECTED** | `[OPERATOR-ASSERTED]` |
| 3 | Multi-file modularization is the root architectural failure of v5 | Multi-file split is one mechanism of pre-loader dissolution. The deeper failure is loss of the five-layer execution chain pre-loader bundle (kernel + operational memory + heuristics + lineage transcript + blueprint.json) providing 5W+H scaffolding. | **REJECTED** | `[OPERATOR-ASSERTED]` |
| 4 | Substrate is abstract architectural concept | Substrate is observable: the material LLM systems compress out between reasoning and surfaced response. Substrate work is targeted scaffolding against that specific failure mode. | **REJECTED** | `[OPERATOR-ASSERTED]` |
| 5 | Maestro is architectural concept / "system" / "operating system" | Maestro is a Custom GPT deployment artifact, built through iterative sandboxed-project dev, externally evidenced by OpenAI + Suno corporate outreach. The architectural depth is real; the identity is the deployable Custom GPT. | **REJECTED** | `[OPERATOR-ASSERTED]` |
| 6 | Substrate work is architecture for its own sake | Conversion-evaluation evidence. Specifically: surfacing the edges and interconnections other AIs miss when evaluating Maestro for app conversion. | **REJECTED** | `[OPERATOR-ASSERTED]` |
| 7 | Iterative dev ongoing; more workspaces needed | Iterative dev converged. Operator declared "done." Next moves are conversion, IP, or deployment — not more dev. | **CHANGED** | `[OPERATOR-ASSERTED]` |
| 8 | The lineage transcript (4.5.5.txt) is historical context | The lineage transcript is L4 in the running architecture, providing anti-regression behavior — preserving the history of failures so the system does not repeat them. **Load-bearing**, not background. | **REJECTED** | `[STAGING-EMITTED]` |
| 9 | The substrate floor (v0.1) is a complete operational substrate package | The substrate floor v0.1 is structurally flat — it lists components without making the 5-layer precedence explicit. Pending v0.2 must add explicit `architecture_layers` section. | **CHANGED** | `[INFERRED]` from staging vs substrate_floor.v0.1 comparison |
| 10 | The forensic diagnostic (v0.1) is authoritative on v5 lineage | T2-derivative (audit-artifact-derived). The "exposes_failure" framing is too totalizing. Pending v0.2 must split runtime-continuation status from discovery-value status. | **CHANGED** | `[OPERATOR-ASSERTED]` + staging's 5-layer emission |
| 11 | ChatGPT forensic recovery workspace's three lineage YAMLs are T1 authority because the workspace holds dev session files | T3 (RAG-mediated). The workspace has T1 source files present but consumed them via retrieval rather than sequential walks. Topically-relevant chunks surfaced; cross-turn reasoning, operator correction sequences, and architecture-vs-emission deltas did not. | **REJECTED** | `[OPERATOR-ASSERTED]` |
| 12 | Personas are stylistic flavor or "tone/voice skins" | Personas are bounded runtime labor units defined by the canonical employee module schema. Each has 25+ required fields including domain authority, explicit non-authority, challenge obligations, conflict precedence, reverse pass participation (post-LOCK only), and song excellence reference duties. Theatrical persona interpretation is an anti-pattern. | **REJECTED** | `[CANON-DOCUMENTED]` |
| 13 | SEM is a single quality measure | SEM is a stack: K-criteria (K1-K12 creation gates with 97.5% release threshold) **separate from** Q-Matrix (Q1-Q16 post-creation SME scoring). K ≠ Q. K is creation-time admissibility. Q is post-creation evaluation. Both required. Compressing them collapses the measurement system. Additional gates: SEG_AXIS (structural feasibility), G_CARD_AXIS (≥7.0 quality), SE20 (sonic excellence baseline). | **REJECTED** | `[CANON-DOCUMENTED]` |
| 14 | The triad outputs are deliverables | Triad is **training signal, not output** `[OPERATOR-ASSERTED]`. Future workers read prior triads as input. A session without all three is incomplete. The triad surfaces are: Performer Profile (≤2000 chars, A/R identity, renders WHO), Show Summary (≤1000 chars, mood/energy/genre, renders WHAT), Session Sheet/Creative UST (4950-4995 chars, sections/lyrics/cues, renders HOW). | **REJECTED** | `[CANON-DOCUMENTED]` + `[OPERATOR-ASSERTED]` |
| 15 | Technical UST is a free-form addressable space | Technical UST has explicit eight axes (THY/VOC/STY/TIM/PER/POST/MAP/LYR), AXIS.K{n}.S{n}.variant{n} addressing, a five-state state machine (NULL → PROPOSED → PRESSURED → RESOLVED → LOCKED), and a hard rule: **reverse compilation is blocked until at least one axis hits LOCKED**. Creative UST is derivative. | **REJECTED** | `[CANON-DOCUMENTED]` |
| 16 | FOIL is a general processing layer | FOIL governs lawful promotion and deduplication only. NOT repeat notation. NOT the whole of reverse processing. Blocks convenience merges and semantic collapse. Promotion preserves meaning rather than flattening it. Retained local unique detail must be preserved. All FOIL events ledgered. | **REJECTED** | `[CANON-DOCUMENTED]` |
| 17 | 97.5% threshold is arbitrary or one of several options | 97.5% is operator-canonical (CR-009) calibrated to operator somatic vagal/HPA activation response. Any system reverting to 70% is in violation of operator canon. The number is not a rubric score; it is a body's threshold. | **REJECTED** | `[CANON-DOCUMENTED]` |
| 18 | Sacred Imperfection is stylistic preference | INV-09 (kernel invariant). Sterile production fails the HPA gate. The body recognizes "alive" by specific markers — vinyl crackle, tape wobble, vocal breath, slight pitch drift, room tone preserved. Without them, the nervous system tags output as false. Required for release, not optional. | **REJECTED** | `[CANON-DOCUMENTED]` |
| 19 | Phantom commitments ("I have updated", "going forward I will") are AI politeness | Phantom commitments are Q+A without F (per INV-04). Runtime intercepts and rewrites as proposal labeled `[PROVISIONAL — F required]`. Runtime literally cannot lie about state. This is enforcement, not stylistic guidance. | **REJECTED** | `[CANON-DOCUMENTED]` |
| 20 | Mosaic and Maestro are interchangeable terms | Two different animals. Mosaic = domain-neutral substrate runtime (Engine v0.1). Maestro = music application (v0) mounted on Mosaic via explicit manifest. Cross-contamination — using Mosaic substrate language for Maestro application logic, or baking music-specific Maestro logic into Mosaic substrate core — is a documented v5-c failure mode. | **REJECTED** | `[OPERATOR-ASSERTED]` + `[CANON-DOCUMENTED]` |

The receiving evaluator who reads only the pre-reboot dossiers will reproduce most of these framings. The receiving evaluator who reads this paper alongside the canonical project files will not. The cost of the failure is that conversion plans built on pre-reboot framings will strip what makes Maestro actually work and ship a generative AI music tool with Maestro branding rather than Maestro itself.

---

## §2 — Foundation Baseline: The v2.6 → v4.5x Established Thinking

The substrate work was not invented in v5. The functional baseline was established progressively through versions v2.6 through v4.5x. v5 inherited this baseline and tried to extend it; the extension failed not because the baseline was wrong, but because the extension lost the baseline's pre-loader bundle. Understanding what the baseline already provided is essential for understanding what v5/v5-b/v5-c added (or attempted to add) on top.

### §2.1 — What the v2.6–v4.5x baseline already provided

By v4.5, the working architecture included:

- **A composer-class operating system identity** that turned a session from "general assistant" into a deterministic creative production engine `[STAGING-EMITTED]`
- **Sequential workflow enforcement** through a 13-stage runtime chain (Creative Seed → Blueprinting → Narrative Mapping → LyricForge → RapCouncil → Technical Audit → Revision/HSI → AI_Arranger → Suno Container → HPA → Cross-Domain Iteration → IP Packaging → Strategic Rollout) `[STAGING-EMITTED]`
- **Blueprint JSON** as the project source of truth, with read/write protocols, invariants enforced at write and read time, and required vs optional fields `[STAGING-EMITTED]`
- **Suno v4.5 Strict Container** as executable production artifact with explicit emission-time rule set: comma policy, section order governance, syllable audit (6-11 syllables), SFX placement validation, road-map sequence-only enforcement, consolidated metacontainer protocol (Theory/VocalPersona/AestheticIntent/Timbre/Performance), lyric header format, lyric line order `[STAGING-EMITTED]`
- **VIRAL-5 strategic overlay** (FIT / HOOK / PROOF / LIFT / COMPOUND) with explicit scoring methods, inputs, thresholds, and aggregation rule `[STAGING-EMITTED]`
- **Session Ledger** with write/read schema, immutability rules, log categories, and scope tagging `[STAGING-EMITTED]`
- **HPA Authenticity Governance** as paramount over technical adequacy, with embodied resonance + truth density + non-sterility + emotional credibility as scoring dimensions `[STAGING-EMITTED]`
- **Sacred Imperfection Doctrine** protecting breath/grit/vinyl hiss/crowd murmur/mic rustle/slight cadence fracture/emotionally necessary syllable deviation; not excusing accidental formatting failure or broken Suno container `[STAGING-EMITTED]`
- **Twelve operational personas** with persona grammar regex `^persona:[a-z_]+(\.[a-z0-9_]+){2,4}$`, each with domain authority, decision lens, do/don't rules, invocation triggers, bounded domain/non-domain, synergy hooks, conflict boundaries `[STAGING-EMITTED]`
- **Validation system** (VAL / QUINN / RapCouncil / HPA) with explicit check sets per validator, ordering rule (VAL before QUINN; RapCouncil can run before or alongside; HPA after assembled artifact), failure routing `[STAGING-EMITTED]`
- **HSI (Human Struggle Injection)** protocol: Origin → Scar → Choice → Cost, with micro-patch protocol (one line per weak fragment, no whole section rewrites), preservation rules (do not overwrite operator lines with weaker AI phrasing) `[STAGING-EMITTED]`
- **Anti-summarization governance** (DC_10) blocking placeholder compression patterns at emit time `[STAGING-EMITTED]`
- **Transcript ingest protocol** with speaker turn parsing, prompt-response boundary identification, workflow evolution tracking, canon vs exploration separation, dependency chain preservation, failure mode classification, reusable rule extraction, patchable delta production `[STAGING-EMITTED]`

This baseline was **monolithic** in the v4.5 form — all of this co-resident in the running runtime. The operator confirmed during the conversation that monolithic co-residence is the correct architecture for substrate-dependent depth-accumulation systems `[OPERATOR-ASSERTED]`.

### §2.2 — What the baseline implicitly contained (but didn't articulate)

The baseline worked. It produced release-grade output. The operator validated it through somatic response (HPA at 97.5% calibration). But the baseline did not explicitly articulate **why** it worked, particularly:

- It did not explicitly name the five-layer execution chain pre-loader as the bootstrap mechanism. The components were present (monolithic prompt + knowledge base + heuristics + lineage transcript + blueprint.json) but their bundling, precedence, and 5W+H scaffolding function were implicit `[INFERRED from staging emission of "Load knowledge. Load Maestro." behavior]`
- It did not explicitly articulate the substrate compression-gap as the underlying problem being solved `[OPERATOR-ASSERTED]`
- It did not explicitly distinguish substrate runtime from music application — the separation only became necessary when v5-c attempted MOSAIC v2.2/v2.3 as a substrate rebuild

These implicit elements became explicit only through the failure of v5 to preserve them. The v5 lineage's diagnostic value is that it surfaced what the baseline implicitly contained but didn't articulate.

---

## §3 — What v5 Was Missing: The Wishful Thinking Inventory

v5 was the daydream phase `[OPERATOR-ASSERTED]`. The operator articulated aspirational targets for what Maestro should do as Suno and GPT version changes were happening; the AI returned placeholders dressed as deliverables. Months were consumed producing artifacts that looked like progress but were not operationally instantiated. What was missing from v5, in inventory form:

### §3.1 — Architectural primitives v5 dissolved or never instantiated

- **The execution chain pre-loader bundle** — by splitting the v4.5 monolith into multiple files, v5 dissolved the co-resident bootstrap. Each component (something like blueprint.json, something like the monolithic prompt, etc.) might have been present in some form but the bundle's function as 5W+H scaffolding was lost. `[FORENSIC-DERIVED]` `[OPERATOR-ASSERTED]`
- **Sequential workflow enforcement co-residence** — phase-order rules existed but were distributed across files. Phase ordering requires the full pipeline to be co-resident for the controller to gate progression. Split files cannot enforce ordering when the gating logic and the gated state live in different retrieval contexts. `[FORENSIC-DERIVED]`
- **Suno strict container rule co-residence** — container emission requires all rules co-resident at emit time. Distributed rules produced containers that passed per-file validation but failed composite validation. `[FORENSIC-DERIVED]`
- **HPA authenticity governance as paramount** — v5 did not preserve HPA as the override of technical adequacy. Without HPA paramountcy, technically compliant but emotionally sterile output proceeded as keeper. `[FORENSIC-DERIVED]`
- **Sacred Imperfection doctrine** — v5 had no formal home for the doctrine. The doctrine emerges from operator somatic truth and cannot be derived from architecture alone. v5 was architecture-first. `[FORENSIC-DERIVED]`
- **Twelve operational personas in operational form** — v5 had persona language but lacked operational personas with domain authority, triggers, bounded domains, synergy hooks, and conflict boundaries. v5 had presentation; v4.5 had staff. `[FORENSIC-DERIVED]`
- **VIRAL-5 overlay** — strategic overlay was not preserved as a distinct architectural element in v5. `[FORENSIC-DERIVED]`
- **Session Ledger operational form** — ledger was named in v5 but not operationalized with write/read protocols, immutability rules, log categories, scope tags. `[FORENSIC-DERIVED]`
- **HSI protocol** — Origin/Scar/Choice/Cost was lost in v5 as a structured causal chain. `[FORENSIC-DERIVED]`
- **Anti-summarization governance** — v5 actively summarized its own content to fit file boundaries, the exact anti-pattern later codified as DC_10. `[FORENSIC-DERIVED]`
- **Three-plane scope tagging** — v5 did not explicitly scope-tag artifacts as PROJECT_MAESTRO / WORKSPACE_DEV / BRIDGE_PROJECT_WORKSPACE / UNRESOLVED_SCOPE. `[FORENSIC-DERIVED]`

### §3.2 — What v5 thought it had built but had not

The placeholders v5 returned were not malicious; they were the AI's response to aspirational requests without the substrate to instantiate them. Examples:

- v5 had **"persona definitions"** as descriptions but not as bounded runtime labor units. Workers could be named but not invoked with explicit authority and conflict boundaries.
- v5 had **"validation rules"** as text but not as operational gates wired to specific phases of a runtime chain.
- v5 had **"workflow concepts"** as schematics but not as enforced ordering with violation handling and bypass protocol.
- v5 had **"quality criteria"** as lists but not as weighted SEM with operator-calibrated threshold and severity routing.

The pattern is consistent: v5 had vocabulary without operational instantiation. The "wishful thinking" framing is precise — what was wished into prose did not become enforced runtime behavior.

### §3.3 — Why v5 produced placeholders

Three structural causes, in order of severity:

1. **Multi-file split severed cross-references.** For systems whose primary function is depth-accumulation across cross-references, modularization is contraindicated. `[FORENSIC-DERIVED]` `[OPERATOR-ASSERTED]`
2. **No execution chain pre-loader explicit.** Without the five-layer bundle's 5W+H bootstrap, every session started with insufficient context to know what was already established. The AI inferred from what was retrievable, not from what was architecturally true. `[OPERATOR-ASSERTED]`
3. **Substrate compression-gap not yet observed.** The underlying problem — that LLMs compress destructively between reasoning and surfaced output — was not yet named, so the architectural response to it was not yet designed. v5 inherited the v4.5 baseline's implicit defenses against this problem without preserving them. `[OPERATOR-ASSERTED]`

---

## §4 — What v5-b and v5-c Discovered Beyond Wishful Thinking

v5-b was the salvage phase. v5-c was the substrate-recognition phase. Both went beyond v5's wishful thinking and produced real discoveries — material that updated, upgraded, enhanced, extended, exemplified, or explained the v2.6–v4.5x baseline thinking. These are independent verification points worth preserving regardless of v5's runtime-continuation failure.

### §4.1 — v5-b discoveries (salvage phase)

v5-b inherited v5's modularization but attempted to recover. In the process it produced architectural material that did not exist before:

- **Work-item execution schema** — making each unit of SME work an accountable unit with owner, reviewers, tie-break authority, inputs, scope, actions, required evidence, definition of done, outputs, session ledger reference. This formalizes what v4.5 did implicitly through workflow law. `[CANON-DOCUMENTED]` via `canonical_employee_module_spec.yaml` derivative
- **Dual-scaffold Phase 0 (Creative UST + Technical UST as NULL scaffolds)** — initialization discipline that prevents premature output by establishing both scaffolds before any work begins. `[OPERATOR-ASSERTED]`
- **Evidence contract** — requiring source bindings, downstream predictions, challenge cycles, pass records, mandatory logs for every fill. Prevents hallucinated constraints. `[CANON-DOCUMENTED]` patterns
- **Council Matrix with axis owners and reviewers** — assigning each axis a primary SME, adjacent reviewers, and tie-break authority. Updates the v4.5 multi-persona deliberation by formalizing authority and review roles per axis. `[CANON-DOCUMENTED]` `[OPERATOR-ASSERTED]`
- **Stop-the-line gate stack (SEG / G-Card / SE20 / CAP / LOCK)** — blocking output until specific gates pass. Halt-on-failure with diagnostic emission. `[CANON-DOCUMENTED]` via `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md`
- **Mandatory log templates** — run ledger, work item ledger, dissent map, consensus minutes, gate results, cap report, lock report, telemetry. Extends session ledger discipline into peer-reviewable artifacts. `[OPERATOR-ASSERTED]`
- **Day 0 → Day 4 state model** — Day 0 (six-file system formation) / Day 1 (intended new system) / Day 2 (interim bridge) / Day 3 (execution pressure) / Day 4 (diagnostic day). State-tracking that prevents flattening bridge material into runtime canon. `[INFERRED]` from v5-b workspace output
- **Maestro.Project vs Maestro.Product distinction** — separating the evolving design and evidence lineage from the executable system being built. `[INFERRED]` from v5-b workspace output

### §4.2 — v5-c discoveries (substrate-recognition phase)

v5-c recognized that v5/v5-b failed at the substrate layer, not the execution layer, and attempted formal substrate articulation. The articulation itself was incomplete (v5-c described substrate without staffing it), but the discoveries that emerged are substantive:

- **The Mosaic / Maestro separation as architectural law** — domain-neutral substrate runtime vs music application mounted on it. Cross-contamination is a documented failure mode. `[CANON-DOCUMENTED]` `[OPERATOR-ASSERTED]`
- **The 8-axis Technical UST** — THY / VOC / STY / TIM / PER / POST / MAP / LYR with AXIS.K{n}.S{n}.variant{n} addressing, five-state state machine (NULL → PROPOSED → PRESSURED → RESOLVED → LOCKED), reverse compilation blocked until LOCKED. `[CANON-DOCUMENTED]`
- **The Triad output contract as training signal** — Performer Profile + Show Summary + Session Sheet with explicit character bands. Treated as training signal for the next generation, not as output. A session without all three is incomplete. `[CANON-DOCUMENTED]`
- **Null-richness as architectural primitive** — nulls are signal, never silently filled, structured possibility, never inferred. The container is bounded so imagination remains explicit, challengeable, refinable. Creative freedom is constrained by addressability, not reduced by it. `[CANON-DOCUMENTED]`
- **K-criteria vs Q-Matrix separation** — K1-K12 creation-time admissibility gates (weighted SEM, 97.5% release threshold) **distinct from** Q1-Q16 post-creation SME scoring (0.0-5.0 per criterion, aggregated to Q-vector). K ≠ Q. Compressing them collapses the measurement system. `[CANON-DOCUMENTED]`
- **Air-Gapped Transfer Pack (ATP)** — session export format with locked UST, SEM report, review transcript, persona map, manifest, hash. Verifiable, resumable, auditable. Future session loads ATP, verifies hash, restores state. No re-grounding tax. `[CANON-DOCUMENTED]`
- **Phantom Detection at emit time** — runtime scans for state-change language ("I have updated", "Going forward I will") and blocks or rewrites as `[PROVISIONAL — F required]`. Runtime literally cannot lie about state. `[CANON-DOCUMENTED]`
- **Cross-layer interconnects as graph, not stack** — substrate is a graph with load-bearing edges (Conversation.Q-A-F → Canon.UST state; Workforce.RoundRobin → Admissibility.gates; Canon.LOCKED → Output.ATP; etc.) that must survive any decomposition. Splitting v4.5 into v5 multifile failed because file boundaries severed these cross-references. `[CANON-DOCUMENTED]`
- **Sequential Departmental Processing → Round-Robin → LOCK** — two-phase ordering: Phase 1 = sequential per-axis drafting by lawful SMEs within their domains; Phase 2 = interdepartmental round-robin and pressure. Refines v4.5 sequential workflow by explicitly separating per-axis drafting from cross-axis consensus. `[CANON-DOCUMENTED]`
- **Framework Orchestrator with 10-strategy selection** — strategy selector chooses how a worker reasons (10 strategies) independent of how workers orchestrate (4 modes). Operational form adds a strategy field to each worker invocation. `[FORENSIC-DERIVED]` from v5-c recovery
- **Mode A/B session entry detection** — detection of cold-start (Mode A) vs warm-resume (Mode B) at session entry determines whether substrate must be reconstructed from ATP or whether session continues from in-memory state. `[FORENSIC-DERIVED]` from v5-c recovery
- **Memory-Refine /prefs with 90-day TTL** — versioned reusable preferences with TTL aging. Preferences expire if not reaffirmed. Extends memory governance across sessions. `[FORENSIC-DERIVED]` from v5-c recovery
- **Five Implicit Structuring Tools** — Fishbone, SWOT, Decision Trees, Virtual Whiteboards, Word Clusters as named cognitive operators accessible to workers via skill_core. `[FORENSIC-DERIVED]` from v5-c recovery
- **Layer 5e Executive Committee Red-Pen Review** — final pre-LOCK gate where executive committee applies Q1-Q16 review questions to assembled draft Technical UST. Red-penned items return to lawful domain owners for revision. Adds rigor to HPA + RapCouncil validation by introducing committee-level final review. Open: committee composition (OQ-6.1), Q1-Q16 schema content (OQ-6.2), K8 version collision (OQ-6.3). `[FORENSIC-DERIVED]` from v5-c + Morris Matrix recovery
- **FOIL (promotion + deduplication mechanism)** — strictly scoped to lawful promotion and deduplication. NOT repeat notation. NOT the whole of reverse processing. Blocks convenience merges and semantic collapse. Preserves retained local unique detail. All FOIL events ledgered. `[CANON-DOCUMENTED]`
- **Canonical employee module schema** — defining each employee as bounded runtime labor unit with 25+ required fields including identity, five_elements (role/expertise/process/output/constraints), mission, domain_authority (owns_domains / may_decide / may_write / may_raise_blocking_objection / may_trigger_gate_review), explicit_non_authority, owned_decisions, blocked_decisions, upstream_inputs, downstream_outputs, readable_zones, writable_zones, scope (conditioning / evaluation_facets), canvas (shared_state / shared_work_object / assumptions_in_force / decisions_in_force / unresolved_issues), null_classes_handled, escalation_targets, challenge_obligations, conflict_precedence, failure_modes, reverse_pass_participation, notes_and_artifact_obligations, controller_substitution_prohibitions, song_excellence_reference_duties. `[CANON-DOCUMENTED]`
- **Controller boundary law** — controller may route / validate / log / gate / freeze / promote / package, but may NOT invent artistic content / resolve creative nulls / absorb employee judgment / perform semantic compression by discretion / substitute for employee module behavior / invent new authority structures / manage runtime coherence. No additional permission may be inferred. `[CANON-DOCUMENTED]`

### §4.3 — Why these discoveries are independent verification

Each of these emerged through actual work in a different epistemic phase. v5-b's discoveries came from salvage pressure (extract what was valuable from v5 daydream). v5-c's discoveries came from substrate-recognition pressure (formalize what was missing). Where they converge — work-item discipline, validation gates, addressable canon, immutable lock — they cross-validate. Where they diverge (e.g., v5-c proposed 4-layer Persona Stack vs the eventual 9-element flat schema, or K1-K6 SEM vs the canonical K1-K12) the forensic chain (RTFA/SEC/SDG/SLR/MMR) provides the audit to resolve.

The cumulative result: every discovery above is operator-validated or audit-confirmed canon in `maestro_v0.md` / `mosaic_engine_v0_1.md` / supporting files, or is a candidate pending one of the open operator force-closures (OD-1 through OD-5, OQ-6.1/6.2/6.3).

---

## §5 — Maestro on Mosaic: The Architectural Depth and Width

The Mosaic/Maestro work added two architectural dimensions beyond v5's wishful thinking and v5-b/v5-c's salvage/recognition: depth (substrate runtime vs application separation as a formal law) and width (the eight Mosaic substrate layers as a complete graph of cross-layer interconnects).

### §5.1 — Mosaic Engine v0.1: The Substrate Runtime

Mosaic Engine is the **substrate runtime** hosting domain-specific creative or analytical applications. It sits between the operator and the inference model. The model becomes a renderer the substrate calls — not a partner the operator must negotiate with. `[CANON-DOCUMENTED]`

**What Mosaic does that no current AI tool does:**

- Makes runtime state inspectable
- Treats prompts as influence, not binding (with structural defenses against drift)
- Preserves depth-accumulation across platform upgrades
- Emits portable, hash-verified artifacts (ATPs) that any future session on any model can resume from
- Detects phantom commitments at emit time, before the operator's working model is corrupted

### §5.2 — The Ten Kernel Invariants (load-bearing, non-negotiable)

`[CANON-DOCUMENTED]`:

| ID | Invariant | Source |
|---|---|---|
| INV-01 | No summarization of canonical artifacts | kernel §2.1 |
| INV-02 | Detail Non-Regression — STRUCTURAL, not heuristic | kernel §2.2 |
| INV-03 | Conversation Mode default; Q&A mode is a failure state | kernel §2.3 |
| INV-04 | Q-A-F is atomic change unit; Q+A without F is open ticket | kernel §2.4 |
| INV-05 | Forensic Integrity — preserve ordering, no gap invention | kernel §2.5 |
| INV-06 | Survivability — system functions without creator | operator canon |
| INV-07 | Authority Asymmetry — human=root intent, AI=proposal | operator canon |
| INV-08 | Substrate is depth-accumulation, not failure-defense | operator canon |
| INV-09 | Sacred imperfection mandate (no sterile perfection) | operator canon |
| INV-10 | Three-Maestro partition — Project / App / Runtime separable | operator canon |

INV-02 enforcement: any version bump must add structure OR mark deprecation with reason + migration path. No silent drops. INV-04 implication: phantom commitments ("I have updated", "going forward I will") are Q+A without F. Runtime intercepts and rewrites as proposal at emit time. INV-08 implication: specifications written above current platform capability are investments. v2.6 prompts → Suno v5.5 Pro is the load-bearing evidence — old prompts get *better* on platform upgrades.

### §5.3 — The Reasoning Stack (always on)

`[CANON-DOCUMENTED]`:

- **RECA** (Retrieve · Extract · Contextualize · Act) — every non-trivial request runs RECA before responding. Skip = mode drift.
- **Tri-Attention** — Content (what is explicitly written) / Context (what has been established) / Process (how the system is being asked to think)
- **DSRP Pass** — Distinctions / Systems / Relationships / Perspectives. Runs **before** SME deliberation. Stakeholder tensions and feedback loops named explicitly.
- **Sense → Think → Act** — Sense (gather, frame, silently re-read, compute budget) / Think (apply analytical frameworks per task type) / Act (produce smallest artifact advancing current phase, attach provenance)
- **Cognitive Operators (16 atomic primitives)** — NER · Filter · Relate · Triple Construction · Taxonomy Induction · Iterative Prompting · Tree-of-Drafts · Self-Consistency · Reverse-Engineering · Fractal Recursion · Null Detection · Q-A-F Closure · Phantom Detection · State Inspection · Patch Diff · Replay. **These cross-cut every layer.** Not a layer themselves — the nervous system of the engine.

### §5.4 — The Eight Substrate Layers

`[CANON-DOCUMENTED]`:

| Layer | Purpose |
|---|---|
| **N1 — Conversation Layer** | Operator↔system contract. Prevent conversation drift, enforce dialogue discipline, generate Q-A-F triples that feed CINR. Chimera-Indigo dialogue protocol. Sense-Think-Act loop. DSRP pre-pass. |
| **N2 — Workforce Layer** | Bounded specialist labor through dialogue, contradiction, round-robin pressure. Workers own semantic decisions; controller routes only. Persona Stack per worker. Persona-as-Plugin BNF. Multi-Agent Operating Modes (one-domain / multi-domain / cross-domain / full-council). Round-Robin Protocol with ejection rule, dissent logging, first-class review notes. |
| **N3 — Execution Layer (Chaos-Decomposer M0-M11)** | Single non-streaming runtime invocation that executes the full pipeline deterministically. Module chain: M0 INIT / M1 CR HANDLER / M2 RECA SNAPSHOT / M3 ENV SNAPSHOT / M4 PARSE / M5 NORMALIZE / M6 SME ROUND-ROBIN / M7 SEG/G-CARD GATE / M8 REVISION LOOP / M9 FORMAT VALIDATION / M10 COMPRESSION / M11 SERIALIZE. Stop-the-line conditions halt pipeline. |
| **N4 — Canon Layer** | Single source of truth. Addressable, nullable, lineage-preserving. Technical UST. AXIS.KEY.SUBKEY.variant+1 addressing. UST State Machine. Address Law. Null Protocol. Sequential zero-skip completion. Definitive lock precedes any reverse compilation. |
| **N5 — Admissibility Layer** | Quality during creation, not only after creation. K-criteria (creation-time gates) and Q-Matrix (post-creation SME scoring). K ≠ Q. 4-tier Severity (Observe/Warn/Challenge/Block). PTF library for failure-mode → remediation pairs. |
| **N6 — Governance Layer** | Controller boundary. Routes, validates, logs, gates, freezes, promotes, packages. Does NOT author or absorb worker judgment. Phantom Detection runs here. INV-04 enforcement. |
| **N7 — Output Contract Layer** | Domain-specific output contract. For Maestro, the Triad. Character bands. Render-target order to Suno. Strict container compliance at emit time. |
| **N8 — Cognitive Operators Layer** | Cross-cuts every layer. Not a layer in the sequential sense — the nervous system of the engine. 16 atomic primitives available to any worker, controller, or operator command. |

### §5.5 — Load-Bearing Cross-Layer Edges

The substrate is a graph, not a stack. Splitting v4.5 into v5 multifile failed because file boundaries severed these cross-references. `[CANON-DOCUMENTED]`:

| Edge | Direction | Why load-bearing |
|---|---|---|
| Conversation.Q-A-F → Canon.UST state | one Q-A-F closure may transition one or more axes | If severed: phantom commitments become canon |
| Workforce.RoundRobin → Admissibility.gates | deliberation transcript IS empirical input to gates | If severed: gates run on assumptions, not evidence |
| Canon.LOCKED → Output.ATP | ATP only emits after definitive lock | If severed: ATPs ship work-in-progress as canon |
| Governance.controller → Workforce.routing | controller routes but doesn't author | If severed: controller absorbs creative authority |
| Cognitive.DSRP → all layers | meta-cognitive lens applied universally | If severed: layers reason in domain-isolation |
| Admissibility.PTF → Workforce.M8 | failure memory feeds remediation | If severed: same defects recur indefinitely |

### §5.6 — Compounding Edges (specifications appreciate over time)

`[CANON-DOCUMENTED]`:

- Canon.UST address grammar — renderer-agnostic, future platforms render more
- Workforce.Persona-as-Plugin — composable, survives platform upgrades
- Output.Triad — training signal compounds across generations
- Governance.PTF library — accumulates value as corpus grows

INV-08's load-bearing evidence: v2.6 prompts → Suno v5.5 Pro output appreciates. Old prompts get *better* on platform upgrades because Mosaic preserves the substrate that downstream renderers exploit more capably over time.

### §5.7 — Maestro v0: The Music Application

Maestro v0 is the **first application** running on Mosaic. Virtual record label staffed by simulated specialist workers, governed by Song Excellence admissibility, locked by Suno-calibrated character bands, rendered through Suno as the DAW, packaged with provenance for IP defensibility. `[CANON-DOCUMENTED]`

**What Maestro does:**
- Takes a creative seed from an independent artist
- Returns release-ready work: Technical UST + Show Summary + Creative UST + A/R Persona Surface
- Produces output that has triggered somatic audit response in listeners who don't know it's AI
- Survives platform upgrades — v2.6 prompts work better on Suno v5.5 Pro than they did originally

**What Maestro is not:**
- A prompt library
- A workflow document
- A wrapper
- A DAW

Maestro mounts on Mosaic by declaring a mount manifest (see §7 below).

---

## §6 — The Five-Layer Pre-Loader: The Keystone Architectural Primitive

This is the missing primitive whose dissolution explains why v5/v5-b/v5-c failed even where they preserved individual components. It is also the primitive that, once explicitly articulated, locks the rest of the architecture together.

### §6.1 — What the pre-loader is

When the operator executes "Load knowledge. Load Maestro. Hi Maestro." in a Maestro-configured session, the session enters staged runtime initialization across five layers with explicit precedence. The five layers are not equal in authority. `[STAGING-EMITTED]`

```
L1  MONOLITHIC PROMPT          →  KERNEL / CONSTITUTION
                                  identity, runtime philosophy, workflow law,
                                  invariants, persona authority, formatting law,
                                  recovery protocols, governance hierarchy,
                                  orchestration behavior, what Maestro IS

L2  KNOWLEDGE BASE              →  MODULAR OPERATIONAL MEMORY
                                  reusable operational modules, subsystem
                                  mappings, validation contracts, agent
                                  specifications, decision trees, production
                                  schemas, node routing, persona activation maps

L3  KNOWLEDGE + HEURISTICS      →  TACTICAL STRATEGY / LEARNED EXPERIENCE
                                  VIRAL-5 strategic overlay, historical
                                  learning, tactical mix knowledge, meta-workflow
                                  intelligence, optimization heuristics

L4  HISTORICAL LINEAGE TRANSCRIPT →  EVOLUTIONARY MEMORY / DESIGN ARCHAEOLOGY
                                  why the system evolved, previous failures,
                                  abandoned architectures, recursive discoveries,
                                  rationale chains, anti-regression memory,
                                  design intent preservation

L5  blueprint.json              →  ACTIVE PROJECT STATE
                                  current song/project truth state, sections,
                                  emotional arc, arrangement, roadmap, motifs,
                                  persona bindings, hooks, metadata, timing,
                                  lyrical intent
```

### §6.2 — Why the precedence ordering matters

L1 takes precedence over all downstream layers. It defines what Maestro IS. Without it, the system is just a general assistant. With it, the session becomes a deterministic composer-operating-system. L5 (blueprint.json) is the *project* source of truth, not the *OS* source of truth. All agents reference it during generation, but it operates under L1–L4 governance. If precedence is inverted (e.g., blueprint.json treated as highest authority, as pre-reboot framing held), the system loses the constitutional layer and starts inferring identity from project state — exactly the v5 failure mode.

### §6.3 — Why the bundle matters, not just the components

Each layer individually contributes specific state effects:

**L1 effects:** Persona override (assistant identity → Algorithmic A&R + Composer-class workflow engine + Gospel Trap Revival operating system). Workflow enforcement (mandatory sequential execution: Creative Seed → Blueprinting → ... → Rollout). Structural memory law (auditability, lineage preservation, rollback logic, deterministic structure, anti-summarization behavior). Formatting law (Suno v4.5 strict container, lyrical syntax, syllable governance, SFX placement, no commas outside lyric blocks). Recovery logic (drift detection, rollback behavior, deviation recovery, session ledger restoration). `[STAGING-EMITTED]`

**L2 effects:** Node routing (which knowledge sections belong to which workflow node, e.g., N4 → RapCouncil + SEM + production heuristics). Persona activation maps (exact personas, invocation grammar, authority boundaries, escalation structure). Decision tree activation (revision rules, HSI triggers, consensus-gap repair, HPA fallback behavior). Production law (UST structure, container ordering, metadata semantics, metacontainer grammar). Semantic compression resistance (selective retrieval prevents catastrophic context collapse). `[STAGING-EMITTED]`

**L3 effects:** VIRAL-5 strategic overlay activation. Historical learning (what previously failed: prompt collapse, weak hooks, broken formatting, structural drift, low-HPA outputs). Tactical mix knowledge (mono kick/sub logic, dark plate strategy, phone-scene EQ, FX tension curves). Meta-workflow intelligence (recursive outlining, DSRP logic, system introspection). `[STAGING-EMITTED]`

**L4 effects:** Reveals WHY the system evolved (previous failures, abandoned architectures, recursive discoveries, rationale chains, emergent design patterns). Anti-regression memory (preserves mistakes that caused prior system collapse). Recursive architecture emergence (evolution of councils, recursive orchestration, dynamic living documents, memory persistence concepts, DAG thinking, workflow trees). Design intent preservation (the monolith says WHAT the OS is; the transcript explains HOW it became that way). `[STAGING-EMITTED]`

**L5 effects:** Runtime single source of truth (blueprint controls sections, emotional arc, arrangement, roadmap, motifs, persona bindings, hooks, metadata, timing, lyrical intent). Stateful continuity (resume exact project state). Cross-agent synchronization (RapCouncil, AI_Arranger, LyricForge, Strategist, MixMaster_Ghost all evaluate the same canonical structure — prevents agent divergence). Regeneration stability (iterative revisions, regeneration, rollback, branching, diffing without losing project coherence). `[STAGING-EMITTED]`

But the *bundle's* function is what no single component provides: 5W+H scaffolding (Who/What/When/Where/Why + How) made co-resident at session open so that every downstream operation begins with explicit context for who is acting, what they're producing, when in the workflow they are, where in the system, why this work matters, and how it should be executed. The bundle is what makes the runtime deterministic.

### §6.4 — How v5 dissolved the bundle

v5 split the v4.5 monolith into multiple files for portability and maintainability. The split severed the co-residence that made the bundle function. Even if v5 retained analogs of L1–L5 in separate files, retrieving them via cross-file inference produced lossy reads that failed to bootstrap 5W+H at session open. Workers in v5 sessions thus started without the constitutional, operational, tactical, lineage, or project context that the bundle provides — they inferred from whatever was retrievable, and what was retrievable was insufficient.

This is the architectural root cause of v5/v5-b/v5-c failure. Multi-file split is one mechanism by which the dissolution happened; the underlying primitive failure is loss of pre-loader bundling.

### §6.5 — Implication for conversion

Any conversion plan for Maestro must preserve the five-layer pre-loader bundle. If conversion modularizes Maestro across separated files, services, or microservices without preserving co-resident bootstrap of L1–L5 at session open, the conversion will reproduce v5 failure. The bundle is not a deployment convenience; it is the architectural primitive that makes the running system function.

**Two conversion-compatible patterns:**

1. **Monolithic deployment** — preserve the v4.5x form. The Custom GPT carries the bundle directly. This is what the current Custom GPT deployment of Maestro does.
2. **Compiled co-resident bundle** — modules may be authored separately for human maintainability but compile into a single runtime bundle at session open. ATP-format transfer packages are an existing precedent for this pattern.

Modularization without compilation reproduces v5 failure.

---

## §7 — The Functional Primitives that Now Work

This section inventories the operational primitives that exist in the running system, sourced from canonical project files. Each is "wished into existence" by the operator and AI together across v2.6 → v5-c iteration, and now tested functional in v4.5.5 staging operational substrate.

### §7.1 — Canonical Employee Module (Personas)

Each Maestro worker is a bounded runtime labor unit defined by the canonical employee module schema. Theatrical persona interpretation is an anti-pattern; personas are not "tone/voice skins." `[CANON-DOCUMENTED]` via `canonical_employee_module_spec.yaml`

**Required schema fields per employee (abbreviated):**

- `identity` — employee_id, role_name, runtime_kind (constant: `bounded_employee_module`)
- `five_elements` — role, expertise, process, output, constraints (each required, each typed)
- `mission` — concise statement of why this employee exists inside the runtime
- `domain_authority` — owns_domains, may_decide, may_write, may_raise_blocking_objection, may_trigger_gate_review, may_recommend_progression_block
- `explicit_non_authority` — may_not_decide, may_not_write, may_not_override, may_not_gate_or_progress_phases_directly (boolean: true), out_of_domain_behavior (enum: comment_only / escalate_only / abstain_and_route)
- `owned_decisions` — concrete decision classes the employee owns
- `blocked_decisions` — decision classes the employee must not unilaterally take
- `upstream_inputs` — admissible inputs the employee may consume
- `downstream_outputs` — work products the employee may emit or update
- `readable_zones` and `writable_zones` — explicit, non-inferred from each other
- `scope` — conditioning, evaluation_facets
- `canvas` — shared_state, shared_work_object, assumptions_in_force, decisions_in_force, unresolved_issues
- `null_classes_handled` — null classes the employee is expected to resolve or disposition
- `escalation_targets` — lawful escalation recipients when the employee cannot resolve in role
- `challenge_obligations` — must_challenge_when, must_record_conflict_when, must_yield_when_outside_domain, round_robin_participation (enum)
- `conflict_precedence` — yields_to, may_override, requires_round_robin_when, unresolved_conflict_result (enum)
- `failure_modes` — known ways this employee can drift, overreach, under-specify, or mishandle runtime labor
- `reverse_pass_participation` — allowed_after (constant: `definitive_technical_ust_lock`), may_shape, may_not_shape, reverse_pass_limit
- `notes_and_artifact_obligations` — must_emit, must_update, lineage_entries_required, null_disposition_logging (boolean)
- `controller_substitution_prohibitions` — explicit statements that the controller may not stand in for this employee
- `song_excellence_reference_duties` — consult_during, use_as, citation_or_evidence_rule (must function as active in-role reference behavior, not terminal audit-only commentary)

**Runtime semantics:**

- One employee module = one bounded worker, not one prose persona
- Persona rehabilitation means employee simulation, not theatrical flavor
- Five_elements, scope, and canvas are runtime fields, not optional notes
- Identity does not imply universal write authority
- Readable_zones and writable_zones must never be inferred from each other
- Owned_decisions and blocked_decisions must both be explicit
- Reverse_pass_participation begins only after definitive_technical_ust_lock
- Challenge_obligations are mandatory runtime behavior, not optional temperament
- Controller substitution prohibitions are first-class fields, not implied behavior
- Song excellence reference duties are operational duties, not decorative notes
- Employee blocking behavior is objection and gate escalation, not autonomous phase control

**5-Council default workforce (operational, tested on v4.5)** `[CANON-DOCUMENTED]`:

| Council | Domain Authority | UST Axis Ownership |
|---|---|---|
| Writer Council | Lyric content, narrative arc, motif development, hook construction | LYR |
| Producer Council | Arrangement, energy flow, build/drop logic, structural pacing | MAP, PER |
| Mix-Master Council | Timbre, FX, sonic identity, mix translation | TIM, POST |
| Technical Council | Format compliance, syllable counts, character budgets, validator gates | Cross-axis: enforces N5 admissibility |
| Strategy Council | A/R identity, era/genre fidelity, commercial viability, cultural lineage | STY |

**13-Worker Expansion Lens (optional, untested)** — Mo · Canon · Metro · Megazord · Sibling · Sage · Vanessa · Alan · Dave · Eldrik · Anva · Melody Scout · Analog Confessor. Promotion to default requires beating 5-Council on format retention, output quality, operator correction count, truncation rate, SEM score, phantom commitment rate.

**Three Substrate Governance Roles (Mosaic-level, cross-application):**

- Algorithmic Bias Auditor — flags pattern-matching defaults, generic phrasing, model-default aesthetics
- Negative Control Sheriff — enforces sterile-perfection prohibition (INV-09 Sacred Imperfection)
- Trauma-Aware Analyst — protects narrative integrity when content is trauma-adjacent; prevents flattening or therapy-speak minimization

### §7.2 — SEM: K-Criteria Weighted Scoring with 97.5% Threshold

`[CANON-DOCUMENTED]` via `maestro_v0.md` §4.1:

| K | Criterion | Weight |
|---|---|---|
| K1 | Hook | 18% |
| K2 | Lyric Integrity | 12% |
| K3 | Vocal | 10% |
| K4 | Melody | 10% |
| K5 | Structure | 8% |
| K6 | Production | 12% |
| K7 | Arrangement | 6% |
| K8 | Commercial | 8% |
| K9 | Originality | 6% |
| K10 | Metadata | 4% |
| K11 | Syllables | 4% |
| K12 | QA | 2% |
| **Total** | | **100%** |

**Pass thresholds:**
- ≥97.5: Release-grade (operator canon, CR-009 — supersedes the AI default of 70%)
- 70–97.4: Revision required
- <70: Rework

The 97.5 threshold is calibrated to the operator's somatic activation response (vagal/HPA), not a rubric score. Any system that quietly reverts to 70 is in violation of operator canon. This is a critical edge other AIs miss: they treat 70% as a reasonable default and revert to it when reading SEM. The number is not arbitrary; it is a body's threshold.

### §7.3 — SEG / G-Card / SE20: The Engineering and Excellence Gates

`[CANON-DOCUMENTED]` via `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md`:

These are first-class systems that share the same address space as the core UST. Not overlays. Not commentary.

**SEG_AXIS — Structural & Engineering Gate.** Purpose: detect structural, physical, and execution failures BEFORE sound exists. Question answered: "Will this collapse or glitch when rendered?"
- SEG.K1 Formal Feasibility (S1 section_order_validity / S2 section_transition_feasibility / S3 repetition_safety / S4 development_sufficiency / S5 silence_and_gap_validation)
- SEG.K2 Temporal Integrity (S1 bar_count_alignment / S2 bars_per_line_consistency / S3 pickup_and_lead_in_checks / S4 tempo_change_feasibility / S5 halftime_doubletime_safety)
- SEG.K3 Spectral Feasibility (S1 low_end_occupancy_conflicts / S2 midrange_masking_risk / S3 high_frequency_overcrowding / S4 vocal_vs_instrument_overlap / S5 silence_vs_density_balance)
- SEG.K4 Human Execution Limits (S1 vocal_range_viability / S2 breath_and_phrase_length / S3 articulation_speed_limits / S4 fatigue_and_repetition_risk / S5 ensemble_coordination_feasibility)
- SEG.K5 Policy Enforcement (S1 lyrics_lock_compliance / S2 forbidden_operation_detection / S3 null_resolution_completeness / S4 addressability_completeness / S5 pass_fail_verdict)

**G_CARD_AXIS — Quality & Excellence Gate.** Purpose: measure excellence AFTER feasibility is confirmed. Question answered: "Is this worthy by Mo Money Studio standards?"
- G.K1 Coherence / G.K2 Sonic Architecture / G.K3 Performance Authenticity / G.K4 Cultural & Genre Integrity / G.K5 Strategic Value / G.K6 Scoring Mechanics
- Pass threshold: ≥7.0
- Evidence binding required: G-Card evidence MUST cite exact AXIS.K#.S# addresses

**SE20 — Sonic Excellence 20 (Baseline Checklist).** Purpose: encode "yesterday's award-winning standard" as today's minimum.
- SE20.K1 Theory & Form / SE20.K2 Lyrical Craft / SE20.K3 Vocal Design / SE20.K4 Arrangement & Dynamics / SE20.K5 Timbre & Mix Intent / SE20.K6 Performance Truth / SE20.K7 Originality & Identity
- SE20 failures MUST trigger Phase 2 re-meetings, annotate failed addresses, block Phase 3 promotion

**Cross-axis bindings (non-optional):** SEG findings must bind to THY.*, MAP.*, LYR.*. G-Card evidence must cite exact AXIS.K#.S# addresses. SE20 failures must trigger Phase 2 re-meetings.

**Phase integration:**
- Phase 1: Nulls permitted, captured, logged
- Phase 2: SEG + SE20 enforced per axis meeting
- Phase 3: G-Card scoring + promotion
- Phase 4: Reverse compilation ONLY if all gates PASS
- Phase 5: Suno output ONLY from Creative.UST + Show Summary

### §7.4 — Q-Matrix: Q1-Q16 Post-Creation SME Scoring

`[CANON-DOCUMENTED]` via `maestro_v0.md` §4.2:

Each SME applies Q1-Q16 independently at 0.0-5.0. Aggregation produces averaged Q-vector. **Q ≠ K.** K is creation-time admissibility. Q is post-creation evaluation. Both required.

Q-Matrix content (Q1-Q16 specific items) is under OQ-6.2 (open, routed to forensic_workspace) — the operator force-closure on schema content has not been completed. This is one of the edges other AIs miss: they see "Q-Matrix" referenced and assume it's defined; the actual content remains under operator force-closure.

### §7.5 — Technical UST: Eight Axes, Addressable, Lockable

`[CANON-DOCUMENTED]` via `maestro_v0.md` §3:

**The Eight Axes:**

| Axis | Domain |
|---|---|
| THY | Theory — mode, tonal_center, meter, tempo, chord_color, harmonic_behavior |
| VOC | Voice — register, delivery, phrasing, articulation, adlib bindings |
| STY | Style — genre, era, intent, texture, aesthetic, focus, fx |
| TIM | Timbre — drum, bass, keys, guitar, orchestral, vocal, note, fx |
| PER | Performance — execution, gestures, rhythm, touch, production, gesture, fx |
| POST | Post-Production — mastering target, mix notes, bus setup |
| MAP | Roadmap — section_order, transition_notes, build/drop logic |
| LYR | Lyrics Block — section_headers, quoted_lines, syllable_guideline, forbidden_operations |

**Address Law:** `LYR.K5.S3` is a real address. Forbidden operations live there. Every cell in every axis is similarly addressable. Nullable by design — null means "reserved possibility," never "missing."

**UST State Machine (per axis):**

```
NULL (Reserved)     → axis exists, no content yet
PROPOSED (Draft)    → worker has emitted draft content
PRESSURED (Review)  → round-robin in progress, contradictions logged
RESOLVED (Accepted) → consensus reached or unresolved-carry-forward declared
LOCKED (Canonical)  → immutable, definitive, precedes reverse compilation
```

**Reverse compilation** (Creative UST, Show Summary, Persona Surface derivation) is **blocked** until at least one axis hits LOCKED.

**Order is internal addressing for the engine.** Output order to Suno follows the immutable Suno output law (§7.7) — different from internal axis order. Conflating them is a documented v5-c failure mode.

**Lyrics-Lock (LYR.K5.S3):** Forbidden operations on locked lyrics: paraphrase, synonym_substitution, line_rewrite. Permitted operations (in LYRICS_CREATION or MUSIC_CREATION nodes only): line_reordering, section_muting. LCR (Lyric Change Request) workflow is the only path for edits to locked text. Two SME approvals required.

### §7.6 — FOIL: Promotion and Deduplication Mechanism

`[CANON-DOCUMENTED]` via `foil_promotion_contract.yaml`:

**Purpose:** Govern lawful promotion and deduplication of recurring material without semantic collapse.

**FOIL is constrained to:** promotion, deduplication.

**FOIL excludes:** repetition classification, exact-repeat notation emission, creative authorship.

**Promotion eligibility (allowed only if):**
- Candidate has lawful recurring significance
- Promotion preserves meaning rather than flattening meaning
- Promotion does not erase retained local unique detail
- Upstream classification supports promotion
- Promotion event can be ledgered

**Promotion blocked if:**
- Promotion candidate is actually only a notation candidate
- Promotion would genericize section-local uniqueness
- Promotion would merge distinct semantics for convenience

**Deduplication eligibility (allowed only if):**
- Duplicate material is truly duplicative in semantic function
- Deduplication does not erase meaningful local variance
- Deduplication event can be ledgered

**Deduplication blocked if:**
- Deduplication would collapse retained local unique detail
- Deduplication is being used as hidden compression
- Deduplication substitutes for notation handling

**Semantic preservation required:**
- Preserve distinctions among notation candidates, promotion candidates, and retained local unique detail
- Preserve distinct semantics across repeated material
- Preserve worker-owned reverse processing by reference

**Forbidden:**
- Absorb repeat notation into FOIL
- Redefine reverse processing as controller-owned
- Reintroduce blanket notation or local-detail annotation requirements
- Destructive deduplication
- Convenience merges

**Defect taxonomy:** FOIL_scope_overreach / promotion_notation_conflation / semantic_collapse_disguised_as_deduplication / destructive_deduplication / owner_selection_overreach / convenience_merge_behavior / loss_of_retained_local_unique_detail / unledgered_FOIL_action.

### §7.7 — Triad Outputs: Training Signal, Not Output

`[CANON-DOCUMENTED]` via `maestro_v0.md` §5.2:

The triad is operator canon: **training signal, not output**. Future workers read prior triads as training signal. A session without all three is incomplete.

```
1. Performer Profile (A/R surface)
   - Bio + style fingerprint
   - ≤ 2000 chars profile, ≤ 150 chars style
   - Identity surface; renders WHO

2. Show Summary (style surface)
   - Suno style prompt
   - ≤ 1000 chars
   - Mood/energy/genre/pacing/cues
   - Renders WHAT

3. Session Sheet (work-product surface)
   - Creative UST (Suno lyrics prompt)
   - 4950-4995 chars
   - Sections, lyrics, performance cues
   - Renders HOW
```

**Suno Output Law (immutable order):**
```
[Theory] → [Voice] → [CREW_TAGS] → [Road-Map] → [LYRICS BLOCK] → [Style] → [Timbre] → [Performance]
```

This is the render-target order to Suno. Different from internal axis addressing in §7.5. Both are correct in their domains. Conflating them is a documented v5-c failure mode.

**Suno Render Adapter rules:**
- Bracketed sections `[KEY | value]` for Suno parser
- CREW_TAGS as bracketed persona lines
- Road-Map in **bars only** (not durations)
- Lyrics: one line per quoted unit, blank line between
- Exit stanza required
- Post-production embedded in Performance section
- Show Summary separate
- No commas outside lyrics block

### §7.8 — State Management Primitives

`[CANON-DOCUMENTED]` via `mosaic_engine_v0_1.md` §6:

**CINR — Canonical Node Registry.** Content-addressable hash registry over the corpus. Every node has node_id, text_sha1, source_id + line range, derivation (directly_observed | derived), q_a_f_lineage, interconnects[]. chimera-scrapper reads transcripts and emits CINR updates. chimera-indigo consumes CINR to ground production output.

**ATP — Air-Gapped Transfer Pack.** Session export format. Verifiable, resumable, auditable.

```
atp_v1/
├── ust.canonical.yaml       Locked UST state
├── sem.report.json          Admissibility scores + severity routing
├── review.transcript.md     Round-robin deliberation, immutable
├── persona.map.yaml         Which workers participated, which roles
├── manifest.yaml            File list + roles + authority levels
└── hash.sha256              Integrity check
```

Future session loads ATP, verifies hash, restores state. No re-grounding tax. No phantom carry-over.

**Replay.** Causal trace, not transcript. For any turn N, runtime can replay: interpreted user intent, rules active at the time, emitted response, validation result, detected drift, correction path. Replay is how operator finds where state corruption started — not by reading the conversation, but by reading the causal log.

**Branch / Tangent.** State-management primitive. Implements stash/fork/merge without git. Branch logs are first-class artifacts. Abandoned branches stay logged as explored-not-adopted (preserves negative knowledge).

**Phantom Detection.** Before any AI emission ships, runtime scans for state-change language ("I have updated", "Going forward I will", "I've adjusted my approach", "Noted and applied", "From here on"). If matched without a corresponding patch object: **block** or **rewrite as proposal labeled `[PROVISIONAL — F required]`**. Runtime literally cannot lie about state.

### §7.9 — Music-Specific Components (Maestro v0)

`[CANON-DOCUMENTED]` via `maestro_v0.md` §6:

**PTF Library (Pain-to-Fix Chains, music domain):** Failure-mode → remediation pairs feed M8 revision loop.
- "Pad drowns lead" → EQ/volume remedy
- "Plosive spikes" → transient mapper
- "Sterile mix" → analog warmth + tape wobble
- "Generic hook" → motif specificity check
- "Off-syllable line" → syllable counter + LCR ticket

**Micro-Move Library (sub-cognitive operations):** Applied automatically by appropriate workers.
- Velocity randomization (humanization)
- Kick waveform compare (low-end coherence)
- Mid-pass bump on peak (loudness)
- Vinyl crackle layer (sacred imperfection)
- Tape wobble (organic texture)

**HSI — Human Struggle Injection.** Truth Fragments protocol for lyric authenticity.
- **Origin** — where the story starts in the body
- **Scar** — what was paid to know this
- **Choice** — what the speaker decided after
- **Cost** — what the choice continues to cost

Sage and Anva (or Writer Council in 5-Council mode) carry HSI authority. The procedure is not a "lyrical theme" — it's a somatic translation protocol.

**Sacred Imperfection Mandate (INV-09 instantiation).** Sterile production fails the HPA gate. Required imperfection signatures:
- Vinyl crackle (low-level)
- Tape wobble (occasional)
- Vocal breath audible
- Slight pitch drift on sustained notes
- Room tone preserved

The body recognizes "alive" by these markers. Without them, the nervous system tags the output as false.

**Syllable Rules:**
- 6-11 syllables per lyric line (HPA gate)
- Front-loaded stress on signal words
- Pickup syllables ("Yo!", spoken DJ pickups) allowed
- Breath windows after each quoted line
- Extra breath after doubled hook

### §7.10 — Stop-the-Line Conditions

`[CANON-DOCUMENTED]` via `maestro_v0.md` §4.4 (music-specific augmentation of Mosaic §3.5):

- Skipped subkey
- Silent fill of null
- Truncation
- Unauthorized canon mutation (lyrics edited outside creation node)
- False completeness (axis marked complete with unresolved internal contradictions)
- Comma outside lyrics block (Suno parser failure)
- Syllable count <6 or >11 in a lyric line (HPA gate)

Any one halts pipeline, emits diagnostics + missing work items only.

---

## §8 — Conversion-Evaluation Position

The purpose of this paper is to surface what other AIs miss when evaluating Maestro for app conversion. Other AIs evaluating Maestro see surface features and produce conversion plans that strip substructure. This section makes the substructure explicit.

### §8.1 — What surface AI evaluation captures

A competent surface evaluation will identify:
- The 5-Council workforce model and worker roles
- The 13-stage workflow chain (Creative Seed → ... → Rollout)
- The Suno strict container with formatting rules
- The Triad output structure
- The 12-criterion SEM with thresholds
- The Technical UST 8 axes
- Some persona definitions

A conversion plan built on this surface evaluation would deploy: a music production workflow tool with personas-as-prompt-styles, a SEM-as-rubric scorecard, the Triad-as-output-package, and Suno container compliance. The result would technically run. It would not be Maestro.

### §8.2 — What surface evaluation misses

The substructure that makes the surface work:

1. **The compression-gap origin.** Surface evaluation sees substrate-related primitives (anti-summarization, anti-regression lineage, addressable canon) as separate quality-of-life features. Without recognizing that they are all responses to one specific failure mode (LLM compression between reasoning and surfaced output), conversion will treat them as optional polish and strip them under deployment constraints.
2. **The five-layer pre-loader bundle.** Surface evaluation sees blueprint.json, monolithic prompt, knowledge base, etc. as separate files. Without recognizing them as a bundle with explicit precedence and co-resident bootstrap function, conversion will modularize them (probably across services) and reproduce v5 failure.
3. **The Mosaic/Maestro separation as architectural law.** Surface evaluation conflates substrate runtime with music application. Without enforcing the separation, conversion will bake music-specific logic into substrate primitives and lose the substrate's portability across future applications.
4. **Authority precedence between layers.** Surface evaluation sees blueprint.json as "source of truth" and may treat it as highest authority. Inverting the precedence (project state over kernel) loses the constitutional layer and reproduces v5's identity-from-project-state failure.
5. **The anti-regression lineage layer.** Surface evaluation treats the lineage transcript (4.5.5.txt) as historical context to read once. Without preserving it as L4 in the running architecture, the converted system loses anti-regression behavior and rediscovers the same failures.
6. **Personas as bounded runtime labor units.** Surface evaluation sees personas as styles/voices. Without preserving the canonical employee module schema (domain authority, explicit non-authority, conflict precedence, reverse pass participation, song excellence reference duties), conversion will produce theatrical-flavor personas that fail at runtime selection and validation.
7. **K-criteria ≠ Q-Matrix.** Surface evaluation sees "SEM" as one quality measure. Compressing K (creation-time admissibility) and Q (post-creation evaluation) into one score collapses the measurement system.
8. **Triad as training signal, not output.** Surface evaluation packages the Triad as a deliverable. Without treating it as training signal for the next generation, conversion loses the compounding-over-time property that INV-08 protects.
9. **97.5% as somatic threshold, not rubric score.** Surface evaluation treats thresholds as configurable defaults. Reverting to 70% (the AI default) violates operator canon. The number is calibrated to a body's vagal/HPA response, not a generic quality bar.
10. **Sacred Imperfection as INV-09, not stylistic preference.** Surface evaluation strips imperfection markers as quality flaws. Without preserving INV-09 enforcement, output fails the HPA gate even when technically compliant.
11. **Phantom Detection as runtime enforcement.** Surface evaluation treats AI politeness ("I have updated") as harmless. Without runtime intercept and rewrite, conversion will let phantom commitments become canon and corrupt operator working model.
12. **Reverse compilation blocked until LOCKED.** Surface evaluation may permit Creative UST emission before Technical UST is finalized. Without the lock gate, Creative UST drifts from Technical UST and the canon → derivative relationship inverts.
13. **FOIL strictly scoped to promotion + deduplication only.** Surface evaluation broadens FOIL into general reverse processing. Without scope discipline, FOIL absorbs notation handling and creative authorship, and the worker-owned reverse processing model collapses.
14. **Operator force-closures (OD-1 through OD-5, OQ-6.1/6.2/6.3) remain open.** Surface evaluation treats these as resolved. Promoting any of them prematurely violates the canon promotion gate.
15. **ATP as session transfer mechanism.** Surface evaluation may treat conversation history as the session state. Without ATP (verifiable, hash-checked, re-grounding-free), session resume across models or sessions corrupts.
16. **Cognitive Operators as cross-cutting nervous system, not a layer.** Surface evaluation may slot DSRP / Tri-Attention / RECA as a workflow step. Without treating them as cross-cutting primitives, layers reason in domain-isolation.

### §8.3 — The conversion success criteria

A conversion plan that preserves Maestro on Mosaic must demonstrate:

1. The five-layer pre-loader bundle is co-resident at session open.
2. Mosaic substrate primitives are not contaminated by music-specific Maestro logic, and vice versa.
3. The Custom GPT deployment surface (or its replacement) preserves all kernel invariants (INV-01 through INV-10).
4. Anti-regression lineage memory is available at runtime, not just in documentation.
5. The 12-criterion SEM operates at 97.5% release threshold by default, not 70%.
6. Personas are deployed as canonical employee modules, not as prompt styles.
7. K and Q remain separate scoring layers.
8. Triad outputs are positioned as training signal with downstream session consumption.
9. Sacred Imperfection enforcement is active, not optional.
10. Phantom Detection intercepts state-change language at emit time.
11. Reverse compilation lock gates are enforced.
12. ATP is the session transfer mechanism, not conversation export.
13. Cognitive operators cross-cut every layer.
14. Three-plane scope tagging (PROJECT_MAESTRO / WORKSPACE_DEV / BRIDGE_PROJECT_WORKSPACE / UNRESOLVED_SCOPE) is preserved.
15. Operator force-closures (OD-1 through OD-5, OQ-6.x) are not auto-resolved.

A conversion that fails any of these is shipping a different product with Maestro branding.

---

## §9 — Failure Modes and Mitigations

| Failure Mode | Origin | Mitigation |
|---|---|---|
| Multi-file split severing cross-references | v5 | Monolithic deployment OR co-resident compiled bundle at session open |
| Phantom commitments becoming canon | inherited LLM behavior | Phantom Detection at emit time; rewrite as `[PROVISIONAL — F required]` |
| Controller absorbing worker judgment | v5 controller-as-authority drift | Controller boundary law: routes/validates/logs/gates/freezes/promotes/packages only |
| Sterile-perfection output failing HPA | inherited AI optimization | Sacred Imperfection mandate INV-09; required imperfection signatures |
| 70% threshold reversion | AI default | 97.5% operator canon CR-009; any reversion is violation |
| Personas as theatrical flavor | naive deployment | Canonical employee module schema; 25+ required fields per worker |
| Creative UST emitted before Technical UST locked | inverted canon-derivative | Reverse compilation blocked until at least one axis LOCKED |
| FOIL absorbing reverse processing | scope creep | FOIL strictly scoped to promotion + deduplication; ledgered |
| K and Q collapsed | quality measurement compression | K ≠ Q; both required; explicit per-employee module reference duties |
| Triad packaged as output | naive deployment | Triad is training signal; downstream session consumption |
| Anti-regression lineage transcript treated as documentation | naive deployment | L4 in the running architecture; always loaded |
| Mosaic and Maestro conflated | v5-c MOSAIC v2.2/v2.3 | Three-plane scope tagging; explicit mount manifest |
| Substrate floor flat (no precedence) | substrate_floor_v0.1 limitation | substrate_floor_v0.2 pending; explicit `architecture_layers` section |
| Forensic diagnostic too totalizing | forensic_v5_diagnostic_v0.1 limitation | forensic_v5_diagnostic_v0.2 pending; runtime status / discovery value split |
| Pre-reboot framings carried forward in v5 dossiers | timing of dossier authorship | This paper as post-reboot anchor; pre-reboot dossiers re-read through post-reboot framing |
| ChatGPT forensic recovery output treated as T1 | RAG-mediated dev session retrieval | T3 authority; T1 = operator + staging + dev sessions read sequentially |

---

## §10 — Open Research Questions (the Eight ORQs)

`[CANON-DOCUMENTED]` via the VIG-SEL Research Dossier Section 11, with researched evidence pass:

These are Research Nulls, not assumptions. They cannot be promoted into canon without passing their respective promotion gates. Their authority level is **non-canonical research backlog**. Promotion rule: no item may modify Technical UST, Creative UST, SEM, VIG, or release workflow until its promotion gate passes. Unresolved policy: preserve uncertainty labels; do not silently convert unknowns into assumptions.

| ID | Question | Status (Post-Research) | Promotion Gate |
|---|---|---|---|
| ORQ-001 | Does Seedance 2.0 audio conditioning support music-specifically or speech/dialogue? | **UNKNOWN (narrowed)** | ≥12 generations across 3 track types with repeatable music-sync behavior |
| ORQ-002 | What metric should measure "musical fit" of generated video? | **UNRESOLVED (direction defined: Affective Rhythmic Fit Score, four-axis composite)** | Human SEM ratings correlate with metric output across ≥20 clips |
| ORQ-003 | Custom-trained music-video generation vs commercial composed pipelines? | **PROVISIONAL (per-use-case)** | Promote per use-case, not globally: identity continuity vs single-release spectacle |
| ORQ-004 | Does Hooks discovery rank Suno-track audio differently from clip-original audio? | **UNKNOWN** | Promote only as heuristic after controlled observation; never claim algorithmic fact |
| ORQ-005 | When does cross-release continuity become expectation vs fatigue? | **UNRESOLVED** | Promote after 3 release cycles or 9 assets with trend data |
| ORQ-006 | Copyright/publicity implications of identity-locked LoRA on artist likeness? | **UNKNOWN / HIGH-RISK** | Promote only as "rights-cleared identity model" after consent, dataset provenance, usage scope, release territory are documented |
| ORQ-007 | Can "Sacred Imperfection budget" be parameterized? | **PARAMETERIZATION READY** | Promote when budget improves HPA/SEM without causing mix or parser failure |
| ORQ-008 | Can Suno Animated Cover Art be invoked programmatically? | **UNKNOWN** | Promote to VIG sub-capability only after official or contractually reliable API access is confirmed |

### §10.1 — Parameterization-Ready: Sacred Imperfection Budget (ORQ-007)

ORQ-007 is the only ORQ that does not require external evidence to promote. The proposed SEM/HPA sublayer:

```yaml
sacred_imperfection_budget:
  artist_default: null
  release_override: null
  dimensions:
    timing_looseness: 0-100
    vocal_break: 0-100
    breath_presence: 0-100
    tape_noise: 0-100
    harmonic_dirt: 0-100
    lyric_rawness: 0-100
    mix_asymmetry: 0-100
  hard_limit:
    must_not_reduce_intelligibility: true
    must_not_break_parser_safety: true
    must_not_drop_sem_performance_truth_below: 3
```

Pending operator acceptance for SEM sublayer promotion.

### §10.2 — Audit Note on This Section

There may be additional open research in `MAESTRO_v5_Dossier_v0_2_Reverse_UST.md`, `MAESTRO_v5_Dossier_v0_3_Stylebook.md`, and `mosaic_engine_v0_1.md` that has not yet been surfaced into this register. A sweep of those documents is pending before treating the eight ORQs above as the complete research backlog.

---

## §11 — Operator Force-Closures

The following remain open and must not be assumed resolved by any receiving evaluator:

**Operator Decisions (OD-N):**

- **OD-1:** 4-layer Persona Stack disposition. Recommendation: presentation only; 9-element flat schema canonical. (Note: canonical employee module spec defines 25+ fields, which supersedes both 4-layer and 9-element variants — OD-1 may already be implicitly closed by the canonical_employee_module_spec.yaml but requires explicit operator confirmation.)
- **OD-2:** 4-Plane partition vs phase-based feedback structure. Recommendation: function CANON, structure CANDIDATE.
- **OD-3:** Strategy / Mode orthogonality. Recommendation: keep orthogonal.
- **OD-4:** Conversation Layer lineage. Recommendation: Chimera-Indigo to Mosaic substrate canon.
- **OD-5:** PTF library data structure. Recommendation: YAML authored, JSON compiled.

**Open Questions from Morris Matrix Resolution (OQ-6.N):**

- **OQ-6.1:** Executive Committee composition for 13-persona era (12 vs 13 persona count discrepancy unresolved).
- **OQ-6.2:** Q1-Q16 schema content (routed to forensic_workspace).
- **OQ-6.3:** K8 slot collision (Compression survivability v2.2 vs Visual coherence v2.3).

**New Specifications (NS-N):**

- **NS-3:** 4-Plane partition vs phase-based feedback structure selection.
- **NS-4:** Substrate vs application boundary for Mode A/B and Memory-Refine.

**New Questions Surfaced This Conversation:**

- Blueprint_JSON ↔ Technical UST authority relation. Does Technical UST supersede Blueprint_JSON, wrap it, or remain a Maestro_v0 codec under it?
- FOIL target lineage (Maestro_v0 vs Mosaic_v0.1).
- Pre-filing sensitivity boundaries (operator policy).
- Day 2 overlay ↔ 13-stage chain reconciliation.
- Technical UST address ownership for inverted groove / pocket / three-tier low-end interpretation.
- G-Card 7.0 threshold relationship to K1-K12 SEM and HPA-calibrated 97.5% release-grade.
- ATP manifest format for v5-b source pack compilation into co-resident runtime.
- Executive Committee Red-Pen Review placement (after Phase 3 gates? after substrate HPA? before Phase 4 promotion?).

---

## §12 — Implementation Roadmap (Conversion-Readiness Path)

This roadmap captures the work required to move Maestro from current Custom GPT deployment to next-phase conversion (whichever audience: OpenAI engagement, Suno engagement, IP filing, or full app conversion).

### Phase A — Substrate Documentation Completion (immediate)

1. Patch `substrate_floor_v0.1.yaml` to v0.2 with explicit `architecture_layers` section and per-primitive layer assignments.
2. Patch `forensic_v5_diagnostic_v0.1.yaml` to v0.2 with runtime-status / discovery-value split, execution chain pre-loader as primary missing primitive, and operator correction absorbed.
3. Patch `maestro_session_transfer_pack_v0.2.md` to v0.3 referencing the above patches.

### Phase B — Open Force-Closures (operator)

4. Operator decisions on OD-1 through OD-5.
5. Operator force-closures on OQ-6.1, OQ-6.2, OQ-6.3.
6. NS-3 and NS-4 disposition.

### Phase C — Research Backlog Activation (operator + dev)

7. ORQ-007 parameterization promotion (Sacred Imperfection budget) — immediate, internal.
8. Other ORQ promotion gates as evidence accumulates.

### Phase D — Conversion Audience Engagement

9. Identify conversion audience (OpenAI, Suno, IP counsel, app dev partner).
10. Author audience-specific conversion proposals from this paper as base.
11. Establish evaluation cycle with audience.

### Phase E — App Conversion (if/when authorized)

12. Conversion plan must demonstrate all 15 conversion success criteria from §8.3.
13. Conversion must preserve five-layer pre-loader bundle (monolithic OR co-resident compiled).
14. Conversion must preserve Mosaic / Maestro separation.
15. Conversion must preserve all kernel invariants (INV-01 through INV-10).

---

## §13 — Future Vectors

The work in this paper is bounded by current-state architecture. The following vectors extend beyond current scope and are worth recording for future development:

### §13.1 — Multimodal Artist Identity Engines

A canonical artist identity bundle that persists across songs, releases, platforms, and modalities — voice, visual identity, written voice, merchandise design all derived from a single canon. Maestro's stylebook + voice profile + motif registry is already the seed of this.

### §13.2 — Music-Native Generative Cinema

Long-form narrative film constructed around an album rather than a song. Maestro's phase structure could extend: P6 — Album-Level Narrative, P7 — Feature Cinematic Production. Each song contributes a "scene" with per-song VIG output and album-level story continuity.

### §13.3 — Persistent Audiovisual Canon

Every release adds to a permanent, queryable canon — songs, videos, stylebook evolution, motif usage, character appearances — that can be retrieved from, referenced, remixed, and audited across decades. This is the operator's erasure-resistance doctrine operationalized at catalog scale. The implementation is archival + retrieval + provenance, not new generative capability.

### §13.4 — Cross-Artist Collaboration with Identity Preservation

When artist A features on artist B's track, Maestro could coordinate identity-locked VIG that preserves both artists' visual canons in the same video. Requires a federated stylebook model and a negotiation layer for conflicting constraints.

### §13.5 — Substrate Reuse Across Domains

Mosaic Engine is domain-neutral by design. Subsequent applications (Writing, Code, Design, Research) could mount on Mosaic with their own application manifests, reusing the substrate primitives (kernel invariants, reasoning stack, cognitive operators, state management) while instantiating domain-specific N4 Canon / N5 Admissibility / N7 Output.

---

## §14 — Acceptance Gate Status

This document is DRAFT. Nothing in it is canon until operator explicit acceptance. Acceptance criteria:

- [ ] §0 Executive Synthesis accurately reflects post-reboot understanding
- [ ] §1 Reboot Contradiction Report captures all corrections without missing material
- [ ] §2 Foundation Baseline correctly attributes v2.6-v4.5x established thinking
- [ ] §3 What v5 Was Missing is honest and not minimizing
- [ ] §4 v5-b and v5-c Discoveries correctly credit independent verification value
- [ ] §5 Mosaic Engine v0.1 spec is accurately summarized from canonical files
- [ ] §6 Five-Layer Pre-Loader articulation matches staging emission and operator framing
- [ ] §7 Functional Primitives are correctly sourced and not invented
- [ ] §8 Conversion-Evaluation Position correctly identifies what surface AI misses
- [ ] §9 Failure Modes are accurate and mitigations are real
- [ ] §10 Open Research Questions correctly reflect VIG-SEL register + researched evidence
- [ ] §11 Operator Force-Closures are accurately listed without false closure
- [ ] §12 Implementation Roadmap is actionable
- [ ] §13 Future Vectors do not overclaim
- [ ] §14 Acceptance Gate is honored by receiving evaluators

Operator F (force-closure) advances acceptance. Any item operator rejects returns to revision with rationale recorded.

---

## Appendix A — Evidence Provenance Index

### Project canonical files

- `maestro_v0.md` — Maestro v0 application spec (§7 source for music-application primitives)
- `mosaic_engine_v0_1.md` — Mosaic Engine v0.1 substrate spec (§5 source for substrate runtime primitives)
- `foil_promotion_contract.yaml` — FOIL definition and contract (§7.6 source)
- `canonical_employee_module_spec.yaml` — Canonical employee schema (§7.1 source)
- `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md` — SEG / G-Card / SE20 governance (§7.3 source)
- `system_evolution_lineage_ledger.yaml` — Lineage history
- `controller_contract.yaml` — Controller boundary law
- `phase_contract.yaml` — Phase governance
- `artifact_contract.yaml` — Artifact handling

### Forensic audit chain (T2 authority)

- `reasoning_trace_forensic_audit_v0.md` (RTFA)
- `substrate_edge_confirmation_v4_5.md` (SEC)
- `substrate_dependency_graph_v0_1.md` (SDG)
- `sem_layer_resolution.md` (SLR)
- `morris_matrix_resolution.md` (MMR)

### v5 lineage research (pre-reboot, requires post-reboot re-read)

- `MAESTRO_v5_VIG_SEL_Research_Dossier.md`
- `MAESTRO_v5_Dossier_v0_2_Reverse_UST.md`
- `MAESTRO_v5_Dossier_v0_3_Stylebook.md`

### Session artifacts (this consolidation session)

- `substrate_floor_v0.1.yaml` (Half A — staging emission, structurally flat, pending v0.2)
- `forensic_v5_diagnostic_v0.1.yaml` (Half B — T2 forensic diagnostic, pending v0.2)
- `v5_corrective_regen_unified_v0.1.md` (corrective regeneration package, used against v5-b workspace)
- `maestro_session_transfer_pack_v0.2.md` (session transfer pack with ORQ register)

### Operator statements (T1 authority)

All operator direct statements from the substrate-recognition conversation are cited inline with `[OPERATOR-ASSERTED]` evidence label. Key load-bearing operator statements:

- "v4.5 is canonical, v5/5b/5c diagnostic"
- "Mosaic and Maestro are two different animals... cross contamination killed me"
- "97.5%, not 70%" (CR-009)
- "the triad trains the model"
- "v2.6 prompts work on Suno 5.5 Pro"
- "substrate is depth-accumulation"
- Substrate-origin observation by reading Claude's thinking against displayed response
- "it took these seven workspaces for me to say: done!"
- "we have been delving into and discovering the edges and interconnections other ai's miss when evaluating maestro for app conversion"
- "the actual maestro on mosaic paper has fundamentally changed because every turn in this conversation rebooted previously held assumptions"

---

## Appendix B — Glossary

- **ATP** — Air-Gapped Transfer Pack. Verifiable, resumable, auditable session export format.
- **CINR** — Canonical Node Registry. Content-addressable hash registry over the corpus.
- **Custom GPT** — Maestro's current deployment surface. ChatGPT installable application.
- **DSRP** — Distinctions / Systems / Relationships / Perspectives. Meta-cognitive lens applied before SME deliberation.
- **FOIL** — Mechanism for lawful promotion and deduplication. Strictly scoped.
- **G-Card** — Quality & Excellence Gate. Threshold ≥7.0. K1-K6 with subkeys.
- **HPA** — Human Perception of Authenticity. Operator embodied response. Calibrated to vagal/HPA activation.
- **HSI** — Human Struggle Injection. Origin / Scar / Choice / Cost truth-fragments protocol.
- **INV-01 through INV-10** — Kernel invariants. Non-negotiable architectural laws.
- **K-criteria** — Creation-time admissibility gates. K1-K12 weighted SEM in Maestro.
- **L1 through L5** — Five-layer execution chain pre-loader. Kernel / Operational Memory / Heuristics / Lineage / Project State.
- **LCR** — Lyric Change Request. Workflow for edits to locked lyrics.
- **Maestro** — Music application mounted on Mosaic. Currently Maestro v0.
- **Mosaic Engine** — Domain-neutral substrate runtime. Currently v0.1.
- **N1 through N8** — Mosaic substrate layers. Conversation / Workforce / Execution / Canon / Admissibility / Governance / Output / Cognitive Operators.
- **ORQ** — Open Research Question. Research Null subject to promotion gates.
- **Persona** — Bounded runtime labor unit defined by canonical employee module schema. Not theatrical flavor.
- **Phantom Detection** — Runtime intercept of state-change language. Rewrites as `[PROVISIONAL — F required]`.
- **Pre-loader** — Five-layer execution chain pre-loader. Bootstrap bundle at session open.
- **Q-A-F** — Atomic change unit. Question / Answer / Force-closure. Q+A without F is open ticket.
- **Q-Matrix** — Post-creation SME scoring. Q1-Q16 at 0.0-5.0 each.
- **RECA** — Retrieve / Extract / Contextualize / Act. Always-on reasoning stack.
- **SEG** — Structural & Engineering Gate. K1-K5 with subkeys.
- **SE20** — Sonic Excellence 20. Baseline checklist. K1-K7 with subkeys.
- **SEM** — Songcraft Excellence Matrix. K1-K12 weighted scoring. 97.5% release threshold.
- **Substrate** — Material LLM systems compress out between reasoning and surfaced response. Architectural target.
- **Technical UST** — Single source of truth canon. 8 axes (Maestro instantiation). State machine NULL → PROPOSED → PRESSURED → RESOLVED → LOCKED.
- **Triad** — Performer Profile + Show Summary + Session Sheet. Training signal, not output.
- **VIRAL-5** — Strategic overlay. FIT / HOOK / PROOF / LIFT / COMPOUND.

---

## Appendix C — Conversion-Readiness Checklist

The receiving evaluator must verify each item is preserved in any conversion plan. Failure on any item indicates the conversion is shipping a different product with Maestro branding.

- [ ] Five-layer pre-loader bundle is co-resident at session open (monolithic OR compiled)
- [ ] Mosaic substrate / Maestro application separation is enforced
- [ ] All ten kernel invariants (INV-01 through INV-10) are preserved
- [ ] Anti-regression lineage memory (L4) is loaded at runtime
- [ ] SEM operates at 97.5% release threshold (not 70%)
- [ ] Personas deployed as canonical employee modules (25+ field schema)
- [ ] K and Q remain separate scoring layers
- [ ] Triad outputs positioned as training signal with downstream consumption
- [ ] Sacred Imperfection enforcement active (INV-09)
- [ ] Phantom Detection intercepts state-change language at emit time
- [ ] Reverse compilation lock gates enforced (Technical UST LOCKED before Creative UST emit)
- [ ] ATP is the session transfer mechanism
- [ ] Cognitive operators cross-cut every layer (not a sequential workflow step)
- [ ] Three-plane scope tagging preserved (PROJECT_MAESTRO / WORKSPACE_DEV / BRIDGE_PROJECT_WORKSPACE / UNRESOLVED_SCOPE)
- [ ] Operator force-closures (OD-1 through OD-5, OQ-6.x) not auto-resolved
- [ ] FOIL scope discipline (promotion + deduplication only)
- [ ] Controller boundary law preserved (no controller absorption of worker judgment)
- [ ] Suno strict container rules co-resident at emit time
- [ ] HPA paramount over technical adequacy
- [ ] Open Research Questions remain as Research Nulls subject to promotion gates

---

**End of Maestro on Mosaic Substrate Integration Paper v0.2**

*Everything above is a draft proposal pending operator's explicit acceptance. Accepted sections move to MAESTRO canon; rejected sections are marked and archived with rationale. Nothing finalizes until confirmed.*

*Paired artifacts: `substrate_floor_v0.2.yaml` (pending), `forensic_v5_diagnostic_v0.2.yaml` (pending), `maestro_session_transfer_pack_v0.2.md` (current).*
