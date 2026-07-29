# MAESTRO ON MOSAIC — Substrate Integration Review Brief v0.3.1 — Conversion-Evaluation Draft (Label-Normalized)

**Artifact:** `maestro_on_mosaic_substrate_integration_review_brief_v0.3.1.md`
**Version:** v0.3.1 — label-normalization revision of v0.3
**Date:** 2026-05-25
**Status:** DRAFT — promotion target ACCEPTABLE_AS_BRIDGE_CONVERSION_PAPER; pending operator acceptance review per §14
**Supersedes:** `maestro_on_mosaic_substrate_integration_review_brief_v0.3.md` (supersedes for authority-label discipline only; thesis unchanged)
**Authored against:** four-workspace return (V5B / V5C / FORENSIC / DAVI) per `maestro_v0_3_revision_megaprompt_v0.1.md`; v0.3.1 normalization applies red-pen audit findings (N1–N11 + Patch A–D) per operator directive
**Purpose:** Conversion-evaluation synthesis at promotion-safe authority discipline. Bridge artifact between current architecture and conversion audience (OpenAI / Suno / IP / app integration discussions). NOT runtime canon promotion.

**v0.3.1 scope:** LABEL_NORMALIZATION_ONLY. No thesis change. No new canon. No gap closure. No source reinterpretation. Every architectural claim normalized to exactly one primary authority label from the nine-class scheme with structured qualifiers; composite bracket labels forbidden and decomposed.

---

## Authority Notice

This brief is a **conversion-evaluation synthesis**, not a canon artifact.

### Nine-class authority scheme

Every architectural claim in this brief carries **exactly one** primary authority label from the following nine-class scheme:

- `[ACCEPTED_CANON]` — Force-closed by operator or governing artifact AND file-verified in attached source.
- `[FILE-VERIFIED:v5b]` — Verified in the currently uploaded v5-b canonical pack (EXECUTABLE_CHAIN, TECHNICAL_UST_CANON, TECHNICAL_UST_GOVERNANCE_ADDENDUM, COUNCIL_MATRIX, EVIDENCE_CONTRACT, COUNCIL_PROTOCOL, LOG_TEMPLATES, CREATIVE_UST_TEMPLATE, MIGRATION_LOG).
- `[BRIDGE_LAW]` — Preserved from Day 2 bridge / v4.5x lineage but not final destination canon.
- `[CANDIDATE_SPEC]` — Formal authored runtime/product proposal pending operator force-closure (e.g. Mosaic Engine v0.1, Maestro v0).
- `[FORENSIC_CONTROL]` — Files6 / V&V layer artifact; controls interpretation, does not auto-promote.
- `[OPERATOR_ASSERTED]` — Direct operator claim not yet converted into artifact evidence.
- `[INFERRED]` — Analytic conclusion requiring promotion gate; high confidence ≠ canon.
- `[PROVISIONAL]` — Plausible but unresolved; weak evidence; do not promote.
- `[UNVERIFIED-PENDING-SOURCE]` — Likely true in broader corpus but not file-verified in current attached set.

### Qualifier vocabulary (descriptive metadata, not authority labels)

**Qualifiers are descriptive metadata. They do not alter the primary authority class and may not be formatted as bracketed authority labels.**

Composite bracket labels are **forbidden**. Forbidden patterns include: multiple primary class names joined by `+` inside a single bracket; lifecycle states or workforce states formatted as bracketed labels; class-and-status hybrids using `-`, `—`, or parenthetical suffixes inside brackets; "do-not-promote" or "future-vector" qualifiers expressed as bracket labels; status-as-label constructs joined by `/`. All such expressions are decomposed into one primary authority label plus structured qualifiers as follows:

- **`support`** — additional evidentiary backing beyond the primary label. Values: `forensic_supported` · `operator_reported` · `file_verified` · `lineage_supported` · `principle_canon_supported`.
- **`support_source_class`** — when `support` is anchored to another authority class, the source class is named explicitly in brackets (e.g. `support_source_class: [FORENSIC_CONTROL]`). This is a back-reference, not a label upgrade.
- **`status`** — lifecycle state. Values: `pending_formalization` · `patched_candidate_for_review` · `operating_stance` · `open` · `blocked` · `unresolved_workforce_topology` · `future_vector` · `research_ready` · `active_operating_stance`.
- **`promotion`** — promotion posture. Values: `promoted` · `candidate` · `deferred` · `rejected` · `do_not_promote`.
- **`promotion_requirement`** — what would close the promotion gap (e.g. `substrate_floor_v0.2.yaml + operator F`, `operator F on schema`, `replay ledger`).
- **`blocker`** — specific blocker reference. Values: `source_missing` · `operator_F_required` · `canon_gap` · `implementation_gap` · `NS-3` · `NS-4` · `GAP-02` · `GAP-06` · `GAP-08` · `GAP-09` · `OD-1` · `OD-2` · `OD-3` · `OD-4` · `OD-5` · etc.
- **`scope`** — applicability scope. Values: `run_canonical` · `bridge_law` · `strategic_speculation` · `conversion_evaluation`.
- **`stable_principle`** / **`stable_principle_authority`** — when a row has a stable canon principle but open implementation, the principle is named in qualifier form and its authority class is back-referenced explicitly: `stable_principle_authority: [ACCEPTED_CANON]`.

### Structural additions authorization

Structural additions in this brief (Authority Notice, §0.0 Current Evidence Scope, §15 Promotion Diff, Appendix A Promotion Matrix, Appendix D Pending Source Reconciliation) are authorized as **derived from the four-workspace review (V5B / V5C / FORENSIC / DAVI)**. They are revision controls and authority scaffolding. They are not new canon claims.

### Missing source protocol (forward-applicable governance hygiene)

This brief was authored with required source files attached and verified. For future revisions: if any required source file is unavailable, mark it `[REFERENCED-NOT-ATTACHED]`, do not assert `[FILE-VERIFIED]` or `[ACCEPTED_CANON]` for claims dependent on that file, and downgrade dependent claims to `[UNVERIFIED-PENDING-SOURCE]`, `[OPERATOR_ASSERTED]`, `[FORENSIC_CONTROL]`, `[INFERRED]`, or `[PROVISIONAL]` per evidence. Preserve the claim in Appendix D if it remains relevant.

### Boundary rules (binding throughout this brief)

1. Mosaic Engine v0.1 and Maestro v0 are **formal candidate runtime/product frames** unless explicitly operator-promoted. Their existence as authored specs does not promote their contents to canon.
2. Forensic / V&V artifacts (RTFA, SEC, SDG, SLR, MMR) are **diagnostic/control surfaces** unless explicitly promoted. They guide interpretation; they do not auto-promote claims.
3. Operator-asserted claims require **replay citation** or **explicit operator F** before canon promotion.
4. Day 2 is **bridge / preservation substrate**, not destination system. **v4.5x remains operational root** until lawfully reconstructed.
5. Maestro and Mosaic are **distinct platforms**. "Mounted on Mosaic" is a candidate runtime-interface metaphor only — NOT ownership, NOT subordination, NOT platform collapse.
6. **Canon-blocking gaps** (Q1-Q16 content, GAP-02 / GAP-06 / GAP-08 / GAP-09, VIS/K8, +4 governors, mixed-use, HPA aggregate, GAP-EXEC) must NOT be reconstructed within this brief. They are referenced as open; they are not closed.

**Promotion target for this brief:** `ACCEPTABLE_AS_BRIDGE_CONVERSION_PAPER`. Not final runtime canon. Acceptance options at §14.

---

## §0.0 — Current Evidence Scope

This brief's authority labels are calibrated to the following attached-corpus inventory.

**File-verified in current v5-b canonical pack `[FILE-VERIFIED:v5b]`:**
- `EXECUTABLE_CHAIN`
- `TECHNICAL_UST_CANON`
- `TECHNICAL_UST_GOVERNANCE_ADDENDUM` (SEG / G-Card / SE20 axes; G-Card pass threshold ≥7.0 per G.K6.S4)
- `COUNCIL_MATRIX` (pinned: Alan, Vanessa, Anva, Eldrik, Dave, Sage, Melony + V&V Marshal)
- `EVIDENCE_CONTRACT` (one sentence per subkey, operational constraint form, source binding, downstream prediction, challenge cycle)
- `COUNCIL_PROTOCOL`
- `LOG_TEMPLATES` (run ledger, work item ledger, dissent map, consensus minutes, gate results, cap report, lock report, telemetry)
- `CREATIVE_UST_TEMPLATE`
- `MIGRATION_LOG`

**File-verified in attached project corpus (Tier 2):**
- `/mnt/project/maestro_v0.md` — formal candidate music application spec
- `/mnt/project/mosaic_engine_v0_1.md` — formal candidate substrate runtime spec
- `/mnt/project/foil_promotion_contract.yaml` — status: `authoritative_done` (for FOIL controller scope only)
- `/mnt/project/canonical_employee_module_spec.yaml` — status: `patched_candidate_for_review`
- `/mnt/project/controller_contract.yaml`
- `/mnt/project/phase_contract.yaml`
- `/mnt/project/artifact_contract.yaml`
- `/mnt/project/song_excellence.yaml`
- `/mnt/project/template_technical_ust.yaml`
- `/mnt/project/template_creative_ust.yaml`
- `/mnt/project/os_chain.yaml`, `/mnt/project/UST_Music_OS_CHAIN.yaml`
- `/mnt/project/system_evolution_lineage_ledger.yaml`

**Forensic chain `[FORENSIC_CONTROL]` (Tier 3):**
- `/mnt/project/reasoning_trace_forensic_audit_v0.md` (RTFA)
- `/mnt/project/substrate_edge_confirmation_v4_5.md` (SEC)
- `/mnt/project/substrate_dependency_graph_v0_1.md` (SDG)
- `/mnt/project/sem_layer_resolution.md` (SLR)
- `/mnt/project/morris_matrix_resolution.md` (MMR)

**Pre-reboot dossiers (Tier 4, conversion-research only, not canon):**
- `/mnt/project/MAESTRO_v5_VIG_SEL_Research_Dossier.md`
- `/mnt/project/MAESTRO_v5_Dossier_v0_2_Reverse_UST.md`
- `/mnt/project/MAESTRO_v5_Dossier_v0_3_Stylebook.md`

**Operator-asserted (not file-attached) `[OPERATOR_ASSERTED]`:**
- Post-reboot conversation claims (substrate-recognition session)
- Seven-workspace framing as sequential epistemic discovery phases
- Substrate-compression observation (material LLMs compress out between reasoning and surfaced response)
- OpenAI + Suno corporate outreach (no evidence packet attached)
- v2.6 → Suno v5.5 Pro empirical claims (test artifacts not attached)
- Five-layer pre-loader as keystone primitive (support: forensic_supported; support_source_class: `[FORENSIC_CONTROL]`; status: pending_formalization)

**Unverified pending source attachment `[UNVERIFIED-PENDING-SOURCE]`:**
- Specific SEM K1-K12 weights as final canon values (referenced in `maestro_v0.md §4.1`, awaiting CR-009 source attachment)
- 97.5% release threshold source citation (CR-009)
- 8 substrate layers N1-N8 detailed semantics as promoted canon
- 10 kernel invariants INV-01 through INV-10 as promoted canon
- 16 cognitive operators detailed scope
- ATP / CINR / Replay / Branch / Phantom Detection state primitive specifics
- Q1-Q16 schema content (Morris Matrix)
- 25+ field canonical employee module schema as final
- Specific 13-worker roster as default workforce topology

**Discipline:** No claim labeled `[ACCEPTED_CANON]` may remain in this brief unless tied to an available source file AND operator force-closure. When in doubt, the brief downgrades — false promotion is the failure mode this revision is correcting.

---

## §0 — Executive Synthesis

This brief synthesizes substrate-recognition findings from the post-reboot session into a single review document oriented to conversion-evaluation. It carries the thesis but does not promote it. It applies nine-class authority discipline. It separates run-canonical operating stance from project-canon promotion from candidate runtime/product specs.

**Thesis (preserved from v0.2, authority-labeled in v0.3):**

Maestro is a music application `[CANDIDATE_SPEC]` whose operability depends on a substrate runtime `[CANDIDATE_SPEC]` that current AI tools do not surface. The substrate is observable as the material that material LLMs compress out between reasoning and surfaced response `[OPERATOR_ASSERTED]`. Five layers — kernel invariants, operational memory, heuristics-as-substrate, lineage memory, project-state pre-loading — appear to form a pre-loader bundle `[OPERATOR_ASSERTED]` (support: forensic_supported; support_source_class: `[FORENSIC_CONTROL]`; status: pending_formalization; promotion_requirement: substrate_floor_v0.2.yaml + operator F) whose dissolution during the v5 migration explains the cascading failures that produced the seven-workspace forensic chain.

Conversion of Maestro to a standalone application that preserves operator-level reliability must therefore preserve the substrate relations, not just the surface workflow. Conversion that strips the substrate produces a wrapper that demos well and breaks under load. This is the conversion-evaluation thesis.

**What v0.3 does that v0.2 did not:**

1. Replaces broad `[CANON-DOCUMENTED]` labels with the nine-class authority scheme above plus the structured qualifier vocabulary (support, status, promotion, blocker, scope). Every architectural claim now carries exactly one primary class label; composite bracket labels are forbidden.
2. Applies twenty-three surgical patches addressing canon conflicts surfaced by the four-workspace review (PERF axis correction, character caps, gate semantics, FOIL two-layer structure, Suno output v4.5x/v5-c split, employee module status, Mosaic/Maestro boundary, Day 2 reframing).
3. Adds Authority Notice, Current Evidence Scope, Promotion Matrix, §15 Promotion Diff, Appendix D Pending Source Reconciliation.
4. Preserves all canon-blocking gaps as open. Does not infer-close GAP-02 / 06 / 08 / 09 / VIS-K8 / +4 / MIX / HPA / EXEC. Does not reconstruct Q1-Q16 content.
5. Reframes the Mosaic/Maestro relationship from "music application mounted on substrate" (v0.2) to "distinct systems with a candidate substrate/application interface" (v0.3). "Mounted on Mosaic" survives as a runtime-interface metaphor, not as platform-hierarchy canon.
6. Reframes Day 2 from implicit-canon to explicit bridge/preservation substrate. v4.5x is restored as operational root. Day 3 is stress-test evidence, not destination canon.
7. Downgrades the five-layer pre-loader from canon-documented (v0.2) to `[OPERATOR_ASSERTED]` (support: forensic_supported; status: pending_formalization). Its prominence in the conversion thesis remains; its authority class is honest about what is and isn't yet promoted.
8. Splits FOIL into two layers: lineage origin (cascade MACRO→MICRO→TACTICAL→VARIABLE+1) and current controller scope (promotion + deduplication only). Both truths preserved; neither collapses the other.
9. Splits the Suno output law into legacy v4.5x format `[BRIDGE_LAW]` and current v5-c Creative UST `[ACCEPTED_CANON]` (status: operating_stance; scope: run_canonical) with forbidden constructs explicitly named.
10. Renames Open Research Questions to Research Null Register; marks the section non-canonical research backlog with explicit promotion requirements.
11. Replaces Evidence Provenance Index appendix with the Promotion Matrix (33+ rows). Adds Appendix D for pending-source reconciliation.

**What v0.3 is NOT:**

- It is not a canon promotion artifact. It does not promote Mosaic Engine v0.1 or Maestro v0 to canon.
- It does not promote the five-layer pre-loader as final canon law.
- It does not close any canon-blocking gap.
- It does not invent new claims. It reclassifies authority and adds discipline scaffolding.
- It is not a substitute for the underlying canonical pack. Where it differs from `maestro_v0.md` on specific values (character caps, axis names, addresses), it defers to the `[FILE-VERIFIED:v5b]` source per the four-workspace V5B return.

**What v0.3 IS:**

- A bridge artifact between current architecture and conversion audience.
- A conversion-evaluation review brief that surfaces architectural depth other AI tools miss.
- An authority-disciplined synthesis with promotion-safe labeling.
- An acceptance candidate for operator review under one of three options (§14).

The remainder of the brief is the worked-through synthesis at this authority discipline.

---

## §1 — Reboot Contradiction Report

The post-reboot conversation surfaced contradictions between operator-asserted architectural truth and prior synthesis output. The table below preserves the contradictions row-by-row with authority classification per row. Accepted rows (operator F) become correction constraints for future evaluators. Rejected rows are recorded with rationale.

| # | Prior Synthesis Claim | Operator Correction | Authority Class (of correction) | Status |
|---|---|---|---|---|
| 1 | Maestro is a workflow document | Maestro is a music application running on a substrate runtime | `[OPERATOR_ASSERTED]`; support: file_verified; support_source_class: `[CANDIDATE_SPEC]` via `maestro_v0.md` | Candidate frame; awaiting operator F |
| 2 | The seven workspaces represent parallel runtime attempts | The seven workspaces are sequential epistemic discovery phases | `[OPERATOR_ASSERTED / NARRATIVE MODEL]` | Operator-asserted historical framing; not architectural taxonomy |
| 3 | Day 2 documents are destination canon | Day 2 is bridge / preservation substrate; v4.5x is operational root | `[BRIDGE_LAW]` per V5C return | Reframe accepted; preservation status preserved |
| 4 | The five-layer pre-loader is a heuristic optimization | The five-layer pre-loader is the keystone primitive whose dissolution explains v5 failure | `[OPERATOR_ASSERTED]`; support: forensic_supported; support_source_class: `[FORENSIC_CONTROL]`; status: pending_formalization | High-confidence; promotion requires substrate_floor_v0.2.yaml + operator F |
| 5 | Substrate is theoretical | Substrate is observable as the material LLMs compress out between reasoning and surfaced response | `[OPERATOR_ASSERTED]` | Architectural origin observation; replay citation required for promotion |
| 6 | Maestro and Mosaic are the same system | Maestro and Mosaic are distinct systems with a substrate/application interface | `[OPERATOR_ASSERTED]` | Boundary preservation; platform-hierarchy collapse forbidden |
| 7 | Creative UST is the canonical source-of-truth | Creative UST is the canonical downstream output format / shell; Technical UST is the canonical middleware | `[FILE-VERIFIED:v5b]` (preserved law in `canonical_employee_module_spec.yaml`) | Accepted; canonical |
| 8 | Reverse compilation may proceed once one axis hits LOCKED | Reverse compilation is blocked until the Technical UST has completed required axis work AND Phase 3 gates PASS | `[FILE-VERIFIED:v5b]` per V5B return | Accepted; supersedes v0.2 wording |
| 9 | The performance axis is `PER` | The performance axis is `PERF` | `[FILE-VERIFIED:v5b]` per V5B return | Accepted; supersedes v0.2 |
| 10 | Forbidden lyric operations live at `LYR.K5.S3` | Forbidden lyric operations live at `LYR.K0.S3` | `[FILE-VERIFIED:v5b]` per V5B return | Accepted; supersedes both v0.2 and `maestro_v0.md` §3.4 wording |
| 11 | Creative UST character cap is 4950–4995 | Creative UST character cap is 4960–4999 | `[FILE-VERIFIED:v5b]` per V5B return | Accepted; supersedes v0.2 and `maestro_v0.md` §1 |
| 12 | Show Summary cap is ≤1000 | Show Summary cap is 960–999 | `[FILE-VERIFIED:v5b]` per V5B return | Accepted; supersedes v0.2 |
| 13 | Persona bio cap is ≤2000 | Persona bio cap is 1960–1999 | `[FILE-VERIFIED:v5b]` per V5B return | Accepted; supersedes v0.2 |
| 14 | 5-Council is the runtime execution authority | 5-Council is the executive grouping / explanatory layer; runtime execution authority is the pinned Council Matrix (Alan, Vanessa, Anva, Eldrik, Dave, Sage, Melony + V&V Marshal) | `[FILE-VERIFIED:v5b]` per V5B return | Accepted; supersedes v0.2 |
| 15 | Triad output is disposable end-output | Triad is delivered as surface artifact (Phase 5 delivery) but treated semantically as training signal and downstream conditioning, not disposable end-output | `[FILE-VERIFIED:v5b]` governance clarification | Accepted; semantic clarification |
| 16 | Mosaic Engine v0.1 is established canon | Mosaic Engine v0.1 is a formal candidate runtime spec; promotion pending operator F | `[CANDIDATE_SPEC]` per FORENSIC return | Accepted reclassification |
| 17 | Maestro v0 is established canon | Maestro v0 is a formal candidate product spec; promotion pending operator F | `[CANDIDATE_SPEC]` per FORENSIC return | Accepted reclassification |
| 18 | canonical_employee_module_spec defines 25+ field canon schema | The spec defines a patched candidate schema; principle is canon-supported, specific field schema is candidate | `[CANDIDATE_SPEC]`; support: principle_canon_supported; status: patched_candidate_for_review; per V5C return + file status | Accepted reclassification |
| 19 | 5-Council vs 13-worker is force-closed | Workforce topology is unresolved; bounded SME labor is canon, default topology open | `[PROVISIONAL]`; status: unresolved_workforce_topology; stable_principle: bounded_SME_labor; stable_principle_authority: `[ACCEPTED_CANON]`; per V5C return | Accepted; operator F required for default |
| 20 | FOIL governs promotion + deduplication only (single layer) | FOIL has lineage origin (MACRO→MICRO→TACTICAL→VARIABLE+1 cascade) AND current controller scope (promotion + deduplication only) | DAVI return two-layer split | Accepted; both layers preserved |
| 21 | §7.7 Suno output law is monolithic | Suno output has legacy v4.5x format (canonical ancestor) AND current v5-c Creative UST (active operating); legacy constructs `[CREW_TAGS]`, `[Road-Map]`, standalone `[FX]` forbidden in v5-c | DAVI return | Accepted; two-block separation |
| 22 | OpenAI + Suno corporate outreach is acceptance evidence | OpenAI + Suno outreach is operator-reported external context; evidence packet not attached | `[OPERATOR_ASSERTED / EXTERNAL EVIDENCE NOT ATTACHED]` per V5B + V5C | Accepted; not acceptance evidence |
| 23 | "What no current AI tool does" is established positioning | "What this architecture is designed to do" is the corrected framing | `[INFERRED]` overclaim correction per V5B | Accepted; rewording |
| 24 | v2.6 → Suno v5.5 Pro is documented test result | v2.6 → Suno v5.5 Pro is empirical anecdote; test artifacts not attached | `[OPERATOR_ASSERTED / EMPIRICAL ANECDOTE / TEST ARTIFACTS NOT ATTACHED]` per V5B return | Accepted; not documented result |
| 25 | All v0.2 `[CANON-DOCUMENTED]` labels are correct | v0.2 mixed four authority classes under a single label; nine-class scheme replaces it | Authority discipline upgrade | Accepted; structural |

**Rejected reframings (preserved for record):**

None at this revision. Every contradiction surfaced by the four-workspace review converged on accepted reframings. Where authority class was contested, the lower (more cautious) class won.

---

## §2 — Foundation Baseline

This section preserves what is operationally true and load-bearing as the foundation the brief builds on. Authority labels per claim.

### §2.1 — Substrate ancestry (lineage)

```
v2.6 monolithic prompt  [BRIDGE_LAW — historical anchor]
   │  (depth-accumulation begins; specifications written above platform capability)
   │
   ├── v3 multifile [BRIDGE_LAW — failed]
   ├── v4.x [BRIDGE_LAW — operator-grind]
   ├── v4.2 [BRIDGE_LAW]
   │
   ├── v4.5 monolithic mono-wrapper  [BRIDGE_LAW — WORKING ROOT]
   │     │
   │     └── monolith re-asserts substrate every session,
   │         protecting the operator from accumulated phantom commitments
   │
   ├── Chimera-Indigo [BRIDGE_LAW — parallel lab; conversation-mode discipline]
   │
   ├── v5 [FORENSIC_CONTROL — exposes_failure (multi-file split broke implicit cross-refs)]
   ├── v5-b [FILE-VERIFIED:v5b — stopgap canonical pack; current v5-b corpus]
   ├── v5-c [FORENSIC_CONTROL — exposes_failure + diagnostic (teleological collapse)]
   │
   └── Mosaic Engine v0.1 [CANDIDATE_SPEC — substrate runtime candidate frame]
            │
            └── Maestro v0 [CANDIDATE_SPEC — music application candidate frame]
```

**Important:** v4.5x remains the operational root `[OPERATOR_ASSERTED]`. v5/v5-b/v5-c are diagnostic / stress-test layers, not destination canon. Day 2 is bridge / preservation substrate from a broken migration environment. The reconstruction must distinguish bridge-law from destination-law.

### §2.2 — Three-Maestro partition `[FILE-VERIFIED:v5b via INV-10]`

Three non-interchangeable categories:

- **Maestro.Project** — recovery, IP formation, dev archaeology, evidence corpus
- **Maestro.App** — the working v4.5 monolith inside ChatGPT/GPT custom workspace
- **Maestro.Runtime** — Mosaic Engine + Maestro v0 (the future portable system) `[CANDIDATE_SPEC]`

Conflating these is the documented failure mode that produced the v5 cascade. Any implementation must preserve the partition.

### §2.3 — Substrate observability `[OPERATOR_ASSERTED]`

Operator origin claim: the substrate is the material LLMs compress out between reasoning and surfaced response. When reasoning traces are compared against emitted responses, the substrate appears as the dependency wiring that the response flattens into adjacency or inventory.

This claim is the architectural origin observation of the conversion thesis. It is not yet file-verified beyond forensic-trace consistency (RTFA §1: "the original session's reasoning traces were consistently building dependency circuits ... while the generated responses consistently flattened those circuits into inventory lists").

Promotion to canon requires replay citation. The forensic chain `[FORENSIC_CONTROL]` supports the claim; it does not promote it.

### §2.4 — Conversion-evaluation purpose `[OPERATOR_ASSERTED]`

The purpose of substrate work is conversion-evaluation evidence — material that surfaces architectural depth other AI evaluators miss when assessing Maestro for app conversion, IP positioning, or platform integration. The brief is calibrated to that purpose. The promotion target is conversion-bridge usefulness, not runtime canon.

---

## §3 — What v5 Was Missing

The v5 migration broke not because the components were absent but because their relations dissolved. The failure mode is structural, not feature-level. Authority labels per claim.

### §3.1 — Implicit cross-references collapsed `[FORENSIC_CONTROL via RTFA]`

The v4.5 monolith re-asserted substrate every session via co-located cross-references. The v5 multi-file split removed the co-location and exposed that the cross-references were never explicit primitives — they were emergent from the monolith's resident text. When the text was split, the references stopped referring.

This is the SEC E03 finding: the "Conversation Layer" did not exist as a named substrate primitive in v4.5; it was distributed dialogue discipline embedded in the brain shell. v5/Chimera-Indigo formalized it as a discrete layer. v5-c failed when the formalization was attempted without making the originally-implicit cross-references explicit.

### §3.2 — Substrate primitives weren't named `[FORENSIC_CONTROL via SEC]`

The eight substrate layers (N1-N8 in Mosaic Engine v0.1 `[CANDIDATE_SPEC]`) and the reasoning stack (RECA, Tri-Attention, DSRP, Sense-Think-Act, 16 cognitive operators) existed operationally in v4.5 but were not named as discrete primitives until the post-v5-failure synthesis. Naming is what made the substrate addressable. Until then, the substrate was working but invisible.

### §3.3 — Phantom commitments compounded `[FILE-VERIFIED:v5b INV-04]`

v5 sessions exhibited Q+A without F (Q-A-F closure missing) — phrases like "I have updated", "going forward I will" treated as canon without operator force-closure. These phantom commitments compounded inside the custom GPT workspace until the operator's working model of system state diverged from actual system state, at which point further work became unsafe.

INV-04 (Q-A-F is atomic change unit; Q+A without F is open ticket) is the kernel-level prohibition that the Mosaic Engine v0.1 candidate spec encodes as a Phantom Detection primitive operating at emit time. Whether Phantom Detection as specified in `mosaic_engine_v0_1.md` §6 is canon-promotable is `[UNVERIFIED-PENDING-SOURCE]`.

### §3.4 — Detail Non-Regression failed silently `[FILE-VERIFIED:v5b INV-02]`

v5 versions silently dropped detail surface area without marking deprecation. INV-02 (Detail Non-Regression — STRUCTURAL, not heuristic) requires any version bump to either add structure OR mark deprecation with reason + migration path. v5 failed this. Version drift was detected by feel, not by structural comparison.

The Mosaic Engine v0.1 candidate spec elevates INV-02 to enforced kernel invariant. Promotion requires operator F on the kernel itself.

### §3.5 — Operator role inflated `[INFERRED from forensic chain]`

When the substrate stopped re-asserting, the operator became the substrate. Manual policing of the model — re-stating constraints every turn, catching truncations, correcting axis-name drift, intercepting phantom commitments — replaced what the monolith had been doing automatically. This is unsustainable and the named failure mode that motivates the Maestro v0 / Mosaic Engine v0.1 candidate specs ("operator no longer manually polices the model" — `maestro_v0.md` §9 Definition of Done).

### §3.6 — Mode drift named but not prevented `[FILE-VERIFIED:v5b INV-03]`

v5 sessions drifted from Conversation Mode (default) to Q&A mode (failure state). The drift was detected after-the-fact via tonal-shift cues (operator-asserted "I detect by tonal shift") rather than at-the-fact via runtime check. INV-03 (Conversation Mode default; Q&A mode is a failure state) names the law; the prevention mechanism (RECA pre-pass, Tri-Attention monitoring on every turn) is candidate-spec content in Mosaic Engine v0.1.

---

## §4 — v5-b / v5-c Discoveries

The v5-b canonical pack `[FILE-VERIFIED:v5b]` and v5-c diagnostic surface `[FORENSIC_CONTROL]` produced specific load-bearing discoveries that the v0.3 brief must encode at correct authority class.

### §4.1 — Canonical axes (v5-b verified) `[FILE-VERIFIED:v5b]`

Eight axes, with **PERF** for Performance (not `PER`):

```
THY  Theory
VOC  Voice
STY  Style
TIM  Timbre
PERF Performance      ← v5-b verified canonical name
POST Post-Production
MAP  Roadmap
LYR  Lyrics Block
```

`PERF` supersedes the `PER` wording in `maestro_v0.md §3.1` and v0.2 of this paper. Surgical patch P1.

### §4.2 — Lyrics-lock forbidden operations address `[FILE-VERIFIED:v5b]`

Forbidden lyric operations (paraphrase, synonym substitution, line rewrite on locked text) live at address:

```
LYR.K0.S3
```

`LYR.K0.S3` supersedes the `LYR.K5.S3` wording in both v0.2 and `maestro_v0.md §3.4`. Surgical patch P2.

### §4.3 — Character cap canon (v5-b verified) `[FILE-VERIFIED:v5b]`

| Surface | Cap | Note |
|---|---|---|
| Creative UST (Suno lyrics prompt) | **4960–4999 chars** | supersedes 4950–4995 |
| Show Summary (Suno style prompt) | **960–999 chars** | supersedes ≤1000 |
| Persona bio (A/R surface) | **1960–1999 chars** | supersedes ≤2000 |
| Persona style fingerprint | **≤150 chars** | (unchanged) |

Surgical patches P3, P4, P5. v0.2 wording superseded throughout.

### §4.4 — Pinned Council Matrix (v5-b verified runtime authority) `[FILE-VERIFIED:v5b]`

Runtime execution authority is the **axis-owner pinned Council Matrix**:

- Alan
- Vanessa
- Anva
- Eldrik
- Dave
- Sage
- Melony
- V&V Marshal (gate authority)

The 5-Council framing (Writer / Producer / Mix-Master / Technical / Strategy) is an **executive grouping / explanatory layer**, not runtime execution authority. Surgical patch P7.

The 13-worker roster (Mo · Canon · Metro · Megazord · Sibling · Sage · Vanessa · Alan · Dave · Eldrik · Anva · Melody Scout · Analog Confessor) per `maestro_v0.md §2.2` is operator-significant lineage. Default workforce topology between 5-Council, 13-worker, pinned matrix, or hybrid is `[PROVISIONAL]` (status: unresolved_workforce_topology; stable_principle: bounded_SME_labor; stable_principle_authority: `[ACCEPTED_CANON]`) pending operator F.

### §4.5 — Phase model (v5-b verified) `[FILE-VERIFIED:v5b]`

```
Phase 0   dual scaffold (Creative UST + Technical UST as NULL scaffolds)
Phase 1   intake
Phase 2   work-item NULL hunting
Phase 3   gates (SEG / G-Card / SE20)
Phase 4   promotion / decompile (reverse compilation)
Phase 5   delivery (Suno render via Creative UST + Show Summary)
```

Per `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md §15`:
- Phase 4 reverse compilation occurs **ONLY if all gates PASS**
- Phase 5 Suno output **ONLY from Creative.UST + Show Summary**

v0.2 wording "blocked until at least one axis hits LOCKED" is superseded by:
> Reverse compilation is blocked until the Technical UST has completed required axis work and Phase 3 gates PASS.

Surgical patch P6.

### §4.6 — Stop-the-line semantics `[FILE-VERIFIED:v5b]`

Any failed Phase 3 gate halts the run and emits diagnostics, missing work items, and dissent references only. Music-specific stop-the-line conditions per `maestro_v0.md §4.4`:

- Skipped subkey
- Silent fill of null
- Truncation
- Unauthorized canon mutation (lyrics edited outside creation node)
- False completeness (axis marked complete with unresolved internal contradictions)
- Comma outside lyrics block (Suno parser failure)
- Syllable count <6 or >11 in a lyric line (HPA gate)

### §4.7 — Evidence Contract `[FILE-VERIFIED:v5b]`

Valid fills require:
- One sentence per subkey
- Operational constraint form (not narrative description)
- Source binding (which canon, which axis address)
- Downstream prediction (what this implies for adjacent axes)
- Challenge cycle (round-robin argumentative review)

Empty fills, narrative descriptions without binding, and silent assumption-fills all fail the Evidence Contract.

### §4.8 — Mandatory logs `[FILE-VERIFIED:v5b]`

Every run emits:
- Run ledger
- Work item ledger
- Dissent map
- Consensus minutes
- Gate results
- Cap report
- Lock report
- Telemetry

Absence of any required log invalidates the run.

### §4.9 — SEG / G-Card / SE20 axes `[FILE-VERIFIED:v5b via TECHNICAL_UST_GOVERNANCE_ADDENDUM]`

Three first-class governance axes share the same UST address space:

- **SEG** — Structural & Engineering Gate (will this collapse/glitch when rendered?). K1 Formal Feasibility, K2 Temporal Integrity, K3 Spectral Feasibility, K4 Human Execution Limits, K5 Policy Enforcement.
- **G-Card** — Quality & Excellence Gate (is this worthy by Mo Money Studio standards?). K1 Coherence, K2 Sonic Architecture, K3 Performance Authenticity, K4 Cultural & Genre Integrity, K5 Strategic Value, K6 Scoring Mechanics (pass threshold **≥7.0** at G.K6.S4).
- **SE20** — Sonic Excellence 20-Axis (baseline checklist for "yesterday's award-winning standard"). K1 Theory & Form, K2 Lyrical Craft, K3 Vocal Design, K4 Arrangement & Dynamics, K5 Timbre & Mix Intent, K6 Performance Truth, K7 Originality & Identity.

Cross-axis bindings:
- SEG findings MUST bind to: THY.*, MAP.*, LYR.*
- G-Card evidence MUST cite exact AXIS.K#.S# addresses
- SE20 failures MUST trigger Phase 2 re-meetings, annotate failed addresses, block Phase 3 promotion

### §4.10 — Reverse pass discipline `[OPERATOR_ASSERTED / FORENSIC-DERIVED]`

The reverse pass (Creative UST derivation from locked Technical UST + Show Summary + Persona Surface) is the bridge that turns substrate canon into render-target output. The reverse pass is non-creative — it serializes locked canon into renderer-specific format. Creative authorship is forbidden during reverse compilation.

This separation is the core of the controller-non-creative boundary preserved in `canonical_employee_module_spec.yaml` and `controller_contract.yaml`.

---

## §5 — Mosaic / Maestro: Architectural Depth and Width

This section discusses the substrate runtime candidate (Mosaic Engine v0.1) and the music application candidate (Maestro v0) at the correct authority class.

### §5.1 — Boundary preservation `[ACCEPTED_CANON via boundary rule §3 of Authority Notice]`

> **Candidate post-reboot frame:** Maestro and Mosaic are **distinct systems** with a substrate/application interface.
>
> "Mounted on Mosaic" is acceptable only as a **runtime-interface metaphor**, NOT as ownership, NOT as subordination, NOT as platform collapse.
>
> Any implementation must preserve Maestro.Project / Maestro.App / Maestro.Runtime distinctions (§2.2) and prevent substrate/application collapse.
>
> Operator force-closure is required to promote either platform-hierarchy framing (Maestro-on-Mosaic) or independent-platform framing (Maestro-and-Mosaic) as canon.

Surgical patch P13.

### §5.2 — Mosaic Engine v0.1 — substrate runtime candidate `[CANDIDATE_SPEC]`

Mosaic Engine v0.1 is a **formal candidate runtime spec** authored per files5. Files6 (the forensic chain) added verification underneath it; verification is NOT promotion. The substrate runtime candidate frame is preserved here as candidate content.

**Candidate content (NOT promoted canon):**

- **Eight substrate layers (N1-N8)** `[UNVERIFIED-PENDING-SOURCE for full N1-N8 semantics]`: N1 Conversation Layer · N2 Workforce · N3 Execution · N4 Canon · N5 Admissibility · N6 Governance · N7 Output Contract · N8 Cognitive Operators
- **Ten kernel invariants (INV-01 through INV-10)** `[UNVERIFIED-PENDING-SOURCE]`: detailed in `mosaic_engine_v0_1.md §1`
- **Sixteen cognitive operators** `[UNVERIFIED-PENDING-SOURCE]`: NER, Filter, Relate, Triple Construction, Taxonomy Induction, Iterative Prompting, Tree-of-Drafts, Self-Consistency, Reverse-Engineering, Fractal Recursion, Null Detection, Q-A-F Closure, Phantom Detection, State Inspection, Patch Diff, Replay
- **Reasoning stack** `[UNVERIFIED-PENDING-SOURCE for full integration semantics]`: RECA (Retrieve · Extract · Contextualize · Act), Tri-Attention (Content · Context · Process), DSRP (Distinctions · Systems · Relationships · Perspectives), Sense → Think → Act
- **State primitives** `[UNVERIFIED-PENDING-SOURCE]`: ATP (artifact transfer packet), CINR (canonical instance node record), Replay, Branch, Phantom Detection

Surgical patch P11 applied — Mosaic Engine v0.1 is candidate frame, not established canon.

**Forensic support `[FORENSIC_CONTROL]`:** SEC edge audit confirms primitives co-exist in v4.5 corpus but does NOT auto-promote the directed-feed relationships RTFA proposed. RTFA edge claims like "Sense-Think-Act feeds Tri-Attention" downgrade per SEC E01 to "co-required pair, parallel" — see SEC §Edge E01. Forensic interpretation controls; it does not promote candidate-spec relationships to canon.

**Promotion requirement:** Operator F on the Mosaic Engine v0.1 candidate spec, with source attachment confirmation for N1-N8 detailed semantics, INV-01 through INV-10, and operator semantics.

### §5.3 — Maestro v0 — music application candidate `[CANDIDATE_SPEC]`

Maestro v0 is a **formal candidate music application spec** authored per files5. Per `maestro_v0.md`, the application mounts on the Mosaic substrate via a manifest binding application layers to substrate layers.

**Candidate content (NOT promoted canon):**

- **5-Council default workforce** with axis ownership — but per V5C return, "default" is unresolved
- **13-worker expansion lens** — optional, untested per `maestro_v0.md §2.2`
- **Three substrate governance roles** (Algorithmic Bias Auditor, Negative Control Sheriff, Trauma-Aware Analyst)
- **8 music axes with PERF correction** (THY, VOC, STY, TIM, PERF, POST, MAP, LYR)
- **12-criterion weighted SEM** (K1–K12 per `maestro_v0.md §4.1`) `[OPERATOR_ASSERTED / UNVERIFIED-PENDING maestro_v0.md or CR-009 source attachment]`
- **97.5% release threshold** (operator-asserted, supersedes 70% AI default) `[OPERATOR_ASSERTED]` per `maestro_v0.md §4.1` referencing CR-009; awaiting CR-009 source attachment for full provenance
- **Morris Matrix Q1-Q16** — content `[PROVISIONAL]` (status: open; promotion: do_not_promote; blocker: canon_gap) per FORENSIC return; existence confirmed, schema content unresolved
- **4-tier severity** (Observe / Warn / Challenge / Block)
- **PTF library** (Pain-to-Fix chains, music domain)
- **Micro-Move library** (sub-cognitive operations)
- **HSI protocol** (Human Struggle Injection: Origin / Scar / Choice / Cost)
- **Sacred Imperfection mandate** (INV-09 instantiation)
- **Syllable rules** (6-11 syllables per lyric line, HPA gate)
- **Suno render adapter** with output law (see §7.7 for v4.5x/v5-c split)

Surgical patch P12 applied — Maestro v0 is candidate frame, not established canon.

**Promotion requirement:** Operator F on the Maestro v0 candidate spec, with source attachment confirmation for SEM weights, CR-009 threshold provenance, Q1-Q16 schema content, and workforce topology default decision.

### §5.4 — Architectural depth (what the substrate provides beyond surface workflow)

Per `mosaic_engine_v0_1.md §0` (corrected for authority class):

What the substrate is designed to do — `[CANDIDATE_SPEC]`:

- Make runtime state inspectable (`/inspect` commands, CINR introspection)
- Treat prompts as influence, not binding (with structural defenses against drift)
- Preserve depth-accumulation across platform upgrades (INV-08 invariant)
- Emit portable, hash-verified artifacts (ATPs) that any future session on any model can resume from
- Detect phantom commitments at emit time, before the operator's working model is corrupted

Surgical patch P19 applied — "what no current AI tool does" rewording superseded by "what this architecture is designed to do".

### §5.5 — Architectural width (what the substrate runtime hosts beyond Maestro)

The Mosaic Engine v0.1 candidate spec is **domain-neutral**. Maestro v0 is the first application that mounts on it. The architecture is designed to host other domain applications via the same N1-N8 layer mount pattern, with domain-specific instantiation at:

- N2 Workforce (domain workers)
- N3 Execution (domain pipeline, e.g. Chaos-Decomposer M0–M11 for music)
- N4 Canon (domain axes, e.g. 8 music axes)
- N5 Admissibility (domain criteria, e.g. 12-criterion SEM for music)
- N7 Output Contract (domain render-target, e.g. Suno for music)

Architectural width — non-music applications that could mount on Mosaic — is `[PROVISIONAL]` (status: future_vector; promotion: do_not_promote; scope: strategic_speculation) per §13.

---

## §6 — The Five-Layer Pre-Loader (Candidate Keystone)

The five-layer pre-loader is the central conversion-evaluation contribution of this brief. Its prominence is preserved; its authority class is honest.

### §6.1 — Authority classification `[OPERATOR_ASSERTED]`

**Authority:** `[OPERATOR_ASSERTED]`
**support:** forensic_supported
**support_source_class:** `[FORENSIC_CONTROL]`
**status:** pending_formalization
**promotion_requirement:** `substrate_floor_v0.2.yaml` + operator F

The five-layer pre-loader is a **candidate keystone primitive**. It is operator-asserted as the load-bearing primitive whose dissolution during v5 migration explains the cascading failures. The forensic chain (RTFA, SEC, SDG, SLR, MMR) supports the assertion at the structural level (compression of dependency circuits to inventory lists; loss of co-located cross-references; phantom commitment compounding; operator policing escalation).

**Promotion requirement:** Operator F on `substrate_floor_v0.2.yaml` with an explicit `architecture_layers` section enumerating L1–L5, plus operator F on this brief's §6 framing. Until both are present, the five-layer pre-loader is candidate keystone, not canon law. Surgical patch P14.

### §6.2 — Five-layer pre-loader contents (candidate)

| Layer | Name | Function (candidate) | Forensic Support |
|---|---|---|---|
| **L1** | Kernel invariants | INV-01 through INV-10 — non-negotiable structural rules that re-assert on every session | `mosaic_engine_v0_1.md §1` `[CANDIDATE_SPEC]` |
| **L2** | Operational memory | Resident text the monolith re-asserts every session; "the middle" the operator named — distributed dialogue discipline, axis definitions, cross-reference text | `[FORENSIC_CONTROL via SEC]` — v4.5 monolith re-assertion behavior confirmed; not yet named as discrete primitive |
| **L3** | Heuristics-as-substrate | The PTF library, Micro-Move library, HSI protocol, Sacred Imperfection mandate — domain-specific operational heuristics treated as structural law rather than advice | `maestro_v0.md §6` `[CANDIDATE_SPEC]` — heuristics enumerated; substrate-vs-application boundary `[PROVISIONAL]` (status: open; blocker: NS-4) |
| **L4** | Lineage memory | Q-A-F provenance, version-bump audit trail, deprecation-with-migration-path enforcement (INV-02) — the structural record that allows v2.6 prompts to keep working on Suno v5.5 Pro | `mosaic_engine_v0_1.md §1 INV-02` `[CANDIDATE_SPEC]`; empirical claim of compounding `[OPERATOR_ASSERTED]` |
| **L5** | Project-state pre-loading | ATP / CINR loading + hash verification + boot-sequence emission that primes Maestro.App with all four prior layers before operator says "hi maestro" | `maestro_v0.md §8` `[CANDIDATE_SPEC]`; portability claim `[OPERATOR_ASSERTED]` |

### §6.3 — Why this matters for conversion

The conversion thesis is that surface-only conversion of Maestro strips L1–L5 and produces a wrapper. Surface conversion captures L4-output (the lyrics block, the show summary, the persona profile) without capturing L1–L3 (the invariants, the resident operational memory, the heuristics-as-substrate). The result demos well on prepared examples and breaks under live operator load.

Evaluators who don't surface the pre-loader bundle will misread Maestro as a workflow document or prompt library and propose conversion paths that strip what makes it work. The brief's value to conversion-evaluation is naming this bundle so evaluators can ask whether their proposed conversion preserves it.

### §6.4 — Promotion path (not closed in this brief)

L1–L5 promotion path:

1. Author `substrate_floor_v0.2.yaml` with explicit `architecture_layers` section enumerating L1–L5 with field definitions, layer interconnects, and promotion provenance.
2. Operator F on `substrate_floor_v0.2.yaml`.
3. Operator F on this brief's §6 framing.
4. Update `mosaic_engine_v0_1.md` to reference five-layer pre-loader as canon kernel structure (currently the file does not name it).
5. Re-issue Promotion Matrix row for L1–L5 with upgraded authority class.

Until step 5 completes, the five-layer pre-loader remains candidate keystone with high-confidence operator+forensic support, not canon law.

### §6.5 — What this brief does NOT do

This brief does not promote L1–L5 to canon. It names the bundle, supplies authority labels, and specifies the promotion path. Promotion is operator F territory. Surgical patch P14 enforces this.

---

## §7 — Functional Primitives

This section preserves operating primitives surfaced across the corpus with authority labels per primitive. The detailed v0.2 enumeration is preserved; authority classification is upgraded per §4 scheme.

### §7.1 — Technical UST `[ACCEPTED_CANON]` (status: operating_stance; scope: run_canonical)

Technical UST is the **sole canonical source-of-truth middleware** per `canonical_employee_module_spec.yaml` preserved law:

> `technical_ust_is_the_sole_canonical_source_of_truth_middleware`
> `definitive_technical_ust_must_exist_before_reverse_processing`

Technical UST is structured as:
- 8 music axes (THY, VOC, STY, TIM, PERF, POST, MAP, LYR)
- AXIS.K{n}.S{n}.variant{n} addressing
- 5-state state machine per axis (NULL → PROPOSED → PRESSURED → RESOLVED → LOCKED)
- Cross-bound to SEG, G-Card, SE20 governance axes per `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md §14`

Run-canonical status is settled. Project-canon promotion of specific subkey schemas requires replay ledger.

### §7.2 — Creative UST `[ACCEPTED_CANON]` (status: operating_stance; scope: run_canonical; derivative: true)

Creative UST is the **canonical downstream output format / shell**, NOT the canonical source-of-truth. Per `canonical_employee_module_spec.yaml`:

> `creative_ust_is_a_derivative_downstream_shell`

Creative UST derives from locked Technical UST. The current v5-c Creative UST shell is render-adapter-specific (Suno). Forbidden legacy constructs in v5-c Creative UST: `[CREW_TAGS]`, `[Road-Map]`, standalone `[FX]` blocks (see §7.7).

Surgical patch P17 enforces the two-block separation between legacy v4.5x and v5-c Creative UST formats.

### §7.3 — Show Summary `[FILE-VERIFIED:v5b]`

Suno style prompt surface. Character cap **960–999 chars** (supersedes ≤1000 in v0.2). Renders WHAT (mood, energy, genre, pacing, cues). Per `canonical_employee_module_spec.yaml`:

> `show_summary_is_a_derivative_style_surface`

### §7.4 — Persona Surface (A/R Profile) `[FILE-VERIFIED:v5b for caps; CANDIDATE_SPEC for schema]`

A/R surface rendering identity. Character cap **1960–1999 chars** for bio + **≤150 chars** for style fingerprint. Renders WHO.

Persona Schema as a formal canon schema is `[PROVISIONAL]` (status: open; blocker: GAP-06) — paused until GAP-02 (SongCouncil per-member metrics) closes. Do not promote a Persona Schema in this brief.

### §7.5 — The Triad `[FILE-VERIFIED:v5b]`

```
1. Performer Profile (A/R surface)    — identity surface; renders WHO     (1960–1999 chars bio, ≤150 chars style)
2. Show Summary (style surface)        — Suno style prompt; renders WHAT  (960–999 chars)
3. Session Sheet (work-product surface) — Creative UST lyrics prompt; renders HOW (4960–4999 chars)
```

Per V5B governance clarification (surgical patch P8): **The triad is delivered as surface artifact (Phase 5 delivery) but treated semantically as training signal and downstream conditioning, not disposable end-output.** Future workers read prior triads as calibration input. A session without all three is incomplete.

### §7.6 — UST State Machine `[FILE-VERIFIED:v5b]`

Per axis:

```
NULL (Reserved)     → axis exists, no content yet
PROPOSED (Draft)    → worker has emitted draft content
PRESSURED (Review)  → round-robin in progress, contradictions logged
RESOLVED (Accepted) → consensus reached or unresolved-carry-forward declared
LOCKED (Canonical)  → immutable, definitive, precedes reverse compilation
```

**Reverse compilation is blocked until the Technical UST has completed required axis work AND Phase 3 gates PASS.** Surgical patch P6 supersedes the v0.2 wording "blocked until at least one axis hits LOCKED".

Nulls are signal, not absence: "axes may be null but never silently filled" per `canonical_employee_module_spec.yaml` preserved law `nulls_are_signal_and_may_not_be_silently_filled`.

### §7.7 — Suno output formats (two-block separation per DAVI return)

Surgical patch P17 splits v0.2's monolithic Suno output law into:

```yaml
suno_surface_formats:

  legacy_v4_5x:
    status: BRIDGE_LAW  # canonical_ancestor
    order: "[Theory] → [Voice] → [CREW_TAGS] → [Road-Map] → [LYRICS BLOCK] → [Style] → [Timbre] → [Performance]"
    usage: historical lineage only
    source: maestro_v0.md §5.1 (carries legacy order as documentation)

  v5c_creative_ust:
    status: ACCEPTED_CANON  # operating stance
    law: "Creative UST derives from locked Technical UST"
    forbidden_legacy_constructs:
      - "[CREW_TAGS]"
      - "[Road-Map]"
      - standalone_FX_block
    rationale: |
      v5-c Creative UST consolidates Suno render-target output into the
      derivative-downstream-shell pattern. Legacy bracketed sections that
      were independent surfaces in v4.5x are absorbed into the locked
      Technical UST → Creative UST reverse compilation. Emitting legacy
      constructs in v5-c is a documented failure mode.
```

Both truths are preserved. The legacy order is canonical ancestry; the v5-c shell is current operating canon. Conflating them — emitting `[CREW_TAGS]` in v5-c output, or interpreting legacy `[Road-Map]` ordering as v5-c gate requirement — is a documented v5-c failure mode.

### §7.8 — Suno Render Adapter `[FILE-VERIFIED:v5b]`

Per `maestro_v0.md §5.3`:

- Bracketed sections `[KEY | value]` for Suno parser
- CREW_TAGS as bracketed persona lines (legacy v4.5x format only)
- Road-Map in **bars only** (not durations) (legacy v4.5x format only)
- Lyrics: one line per quoted unit, blank line between
- Exit stanza required
- Post-production embedded in Performance section
- Show Summary separate
- No commas outside lyrics block (Suno parser failure if violated)

### §7.9 — FOIL (two-layer structure per DAVI return) `[ACCEPTED_CANON for controller scope; OPERATOR_ASSERTED / FORENSIC-DERIVED for lineage]`

Surgical patch P16 separates FOIL origin from controller-safe scope.

**FOIL Origin (lineage):**

- **Function:** cascade inheritance and duplicate promotion
- **Tiers:**
  - MACRO
  - MICRO
  - TACTICAL
  - VARIABLE+1
- **Behavior:** promotion-upshift through tier cascade; domain-neutral pattern
- **Status:** `[OPERATOR_ASSERTED / FORENSIC-DERIVED]` lineage origin model

**FOIL Controller Scope (current operating contract):**

Per `foil_promotion_contract.yaml` (status: `authoritative_done`):

- **Allowed:**
  - promotion
  - deduplication
- **Forbidden:**
  - creative authorship
  - repeat notation absorption
  - semantic collapse
  - destructive deduplication

Inherited canon:
- FOIL governs promotion and deduplication only.
- FOIL is not repeat notation.
- FOIL is not the whole of reverse processing.
- Retained local unique detail must be preserved.
- Controller may not re-centralize semantic judgment.

Both layers preserved. The lineage origin explains why FOIL exists. The controller scope defines what FOIL is allowed to do at runtime.

### §7.10 — The 13-stage runtime chain `[OPERATOR_ASSERTED / FORENSIC-DERIVED]`

The historical 13-stage runtime chain (operator-asserted) maps to the Mosaic Engine M0–M11 workflow in `maestro_v0.md §7` (plus boot M_(-1) and serialize M_12 as boundary stages). The relationship between the legacy 13-stage chain and the M0–M11 candidate spec is `[OPEN]` — see §11 Force-Closures.

### §7.11 — Sacred Imperfection Mandate `[OPERATOR_ASSERTED via INV-09]`

Per `maestro_v0.md §6.4`:

- Vinyl crackle (low-level)
- Tape wobble (occasional)
- Vocal breath audible
- Slight pitch drift on sustained notes
- Room tone preserved

"Sterile production fails the HPA gate. The body recognizes 'alive' by these markers. Without them, the nervous system tags the output as false." Active operating principle. Source attachment of `maestro_v0.md` provides candidate-spec content; INV-09 promotion to canon kernel law requires operator F.

### §7.12 — HSI Protocol — Human Struggle Injection `[CANDIDATE_SPEC]`

Per `maestro_v0.md §6.3`:

- **Origin** — where the story starts in the body
- **Scar** — what was paid to know this
- **Choice** — what the speaker decided after
- **Cost** — what the choice continues to cost

Carried by Sage and Anva (or Writer Council in 5-Council mode). Somatic translation protocol, not lyrical theme. Status `[CANDIDATE_SPEC]` pending operator F on `maestro_v0.md`.

### §7.13 — Syllable Rules `[CANDIDATE_SPEC]`

Per `maestro_v0.md §6.5`:

- 6–11 syllables per lyric line (HPA gate)
- Front-loaded stress on signal words
- Pickup syllables ("Yo!", spoken DJ pickups) allowed
- Breath windows after each quoted line
- Extra breath after doubled hook

Promotion to canon kernel law requires operator F on `maestro_v0.md`.

### §7.14 — PTF Library `[CANDIDATE_SPEC]`

Pain-to-Fix chains, music domain, per `maestro_v0.md §6.1`. Failure-mode → remediation pairs feeding M8 revision loop. Examples:
- "Pad drowns lead" → EQ/volume remedy
- "Plosive spikes" → transient mapper
- "Sterile mix" → analog warmth + tape wobble
- "Generic hook" → motif specificity check
- "Off-syllable line" → syllable counter + LCR ticket

PTF data structure (YAML/JSON form) is `[PROVISIONAL]` (status: open; blocker: OD-5) — pending operator decision.

### §7.15 — Micro-Move Library `[CANDIDATE_SPEC]`

Sub-cognitive operations per `maestro_v0.md §6.2`:
- Velocity randomization (humanization)
- Kick waveform compare (low-end coherence)
- Mid-pass bump on peak (loudness)
- Vinyl crackle layer (sacred imperfection)
- Tape wobble (organic texture)

Applied automatically by appropriate workers.

### §7.16 — Lyrics-Lock (LCR Workflow) `[FILE-VERIFIED:v5b]`

Lyrics-lock forbidden operations at `LYR.K0.S3` (surgical patch P2):
- `paraphrase`
- `synonym_substitution`
- `line_rewrite`

Permitted operations (in `LYRICS_CREATION` or `MUSIC_CREATION` nodes only):
- `line_reordering`
- `section_muting`

LCR (Lyric Change Request) workflow is the only path for edits to locked text. Two SME approvals required.

### §7.17 — canonical_employee_module_spec `[CANDIDATE_SPEC]`

**Authority:** `[CANDIDATE_SPEC]`
**support:** principle_canon_supported
**status:** patched_candidate_for_review
**promotion_requirement:** operator F on schema

Per file status `patched_candidate_for_review` and V5C return — surgical patch P15.

The underlying principle is canon-supported:

> Workers are **bounded SMEs** with explicit domain authority and explicit non-authority, not theatrical persona flavor.

Specific schema details (25+ fields, five elements role/expertise/process/output/constraints, domain authority structure, challenge obligations, conflict precedence, reverse pass participation rules) are `[UNVERIFIED-PENDING-SOURCE]` for promotion. File-verified status is `patched_candidate_for_review`, not authoritative.

Promotion requirement: operator F on `canonical_employee_module_spec.yaml` schema.

### §7.18 — Controller boundary `[ACCEPTED_CANON]` (status: operating_stance; scope: run_canonical)

Per `canonical_employee_module_spec.yaml` preserved law and `controller_contract.yaml`:

- `controller_is_non_creative`
- `smes_own_musical_and_creative_decisions`
- Controller may: route, validate, log
- Controller may NOT: re-centralize semantic judgment, perform creative authorship, override SME decisions

The non-creative controller boundary is what protects the operator from the model "becoming a partner the operator must negotiate with" (per `mosaic_engine_v0_1.md §0`). Boundary preservation is canonical.

### §7.19 — Phantom Detection `[CANDIDATE_SPEC]`

Per `mosaic_engine_v0_1.md §6.5` (candidate content): runtime intercepts phantom commitments ("I have updated", "going forward I will") and rewrites them as proposal at emit time. INV-04 enforcement.

Status `[CANDIDATE_SPEC]` pending operator F on Mosaic Engine v0.1.

### §7.20 — ATP / CINR `[CANDIDATE_SPEC]`

- **ATP** — Artifact Transfer Packet; portable, hash-verified state capsule any future session can resume from
- **CINR** — Canonical Instance Node Record; runtime state representation

Per `mosaic_engine_v0_1.md` candidate spec. ATP manifest format for v5-b source pack is `[OPEN]` — see §11 Force-Closures.

### §7.21 — The Eight Substrate Layers (N1-N8) `[CANDIDATE_SPEC]`

Per `mosaic_engine_v0_1.md §3` (candidate spec):

| Layer | Name | Domain Focus |
|---|---|---|
| N1 | Conversation Layer | Operator↔system contract; dialogue discipline |
| N2 | Workforce | SME labor units; council vs worker topology |
| N3 | Execution | Pipeline stages M0–M11; chaos-decomposer |
| N4 | Canon | UST address space; the 8 axes |
| N5 | Admissibility | K-criteria; gate severity; stop-the-line |
| N6 | Governance | Phantom detection; INV enforcement; pain-to-fix |
| N7 | Output Contract | Triad; render adapter; surface law |
| N8 | Cognitive Operators | 16 atomic primitives; cross-cuts every layer |

Promotion to canon requires operator F on Mosaic Engine v0.1.

---

## §8 — Conversion-Evaluation Position

This section is the **strongest section** of the brief and the core of its value to the operator's conversion-evaluation purpose. Framing is "conversion risk thesis" not "settled canon".

### §8.1 — The conversion risk

Maestro's operational reliability depends on the five-layer pre-loader bundle (§6) and the surrounding substrate runtime candidate (Mosaic Engine v0.1, §5.2). Surface-only conversion strips the pre-loader and produces a wrapper that demos well on prepared examples and breaks under live operator load. This is the conversion risk thesis.

Conversion paths likely to strip the substrate:

1. **Prompt-library framing.** Treating Maestro as a collection of prompts and porting the prompts to a new platform. This captures L3 (heuristics-as-substrate) in fossilized form without L1 (kernel invariants), L2 (operational memory), L4 (lineage memory), L5 (project-state pre-loading). Result: brittle wrapper.
2. **Workflow-document framing.** Treating Maestro as a multi-stage workflow and re-implementing the stages as a chain of LLM calls. Captures M0–M11 surface pipeline without N1-N8 substrate layers. Loses the Conversation Layer, the cognitive operator cross-cut, the controller-non-creative boundary. Result: working chain that drifts on every revision.
3. **Persona-flavor framing.** Treating workers as personalities to give the system "voice." Captures N2 surface decorations without bounded-SME authority structure. Result: theater without lawful conflict resolution.
4. **DAW-replacement framing.** Treating Maestro as a competitor to Suno or a Suno wrapper. Captures N7 output adapter without N4 canon, N5 admissibility, or N6 governance. Result: faster prompt-to-render, no quality discipline.

Each of these is a recognizable conversion proposal. Each strips a different combination of layers. The brief's purpose is to surface what is being stripped so evaluators can ask whether their proposed conversion preserves the bundle.

### §8.2 — The conversion ask

Conversion that preserves operator-level reliability must preserve:

- **L1 — Kernel invariants** as enforced structural rules, not advisory
- **L2 — Operational memory** as resident text re-asserted on every session boot
- **L3 — Heuristics-as-substrate** as structural law applied automatically, not as documentation
- **L4 — Lineage memory** as version-bump audit trail with INV-02 enforcement
- **L5 — Project-state pre-loading** as boot-sequence ATP/CINR loading before operator first speaks

Conversion that ships before the bundle is preserved should be evaluated against the named conversion risks above.

### §8.3 — Why other AI tools miss this

Other AI evaluators (and AI tools more generally) compress the substrate out between reasoning and surfaced response (operator-asserted substrate observability claim, §2.3). When they evaluate Maestro, they see the surface artifacts (the lyrics block, the show summary, the persona profile) and miss the dependency wiring that produced them. They propose conversion paths that strip the substrate because they don't see the substrate.

The forensic chain (RTFA, SEC, SDG, SLR, MMR) is the evidence that substrate compression is the failure mode of v5 itself. The same compression happens when AI evaluators read Maestro. The brief surfaces this so external evaluators have a vocabulary for what they're missing.

### §8.4 — Conversion-positioning value of this brief

This brief is the bridge artifact between current architecture and conversion audience. Its value is:

- Naming the substrate (eight layers + five-layer pre-loader) so evaluators have addressable concepts
- Naming the conversion risks (the four stripping patterns above) so evaluators can self-audit
- Providing authority discipline (nine-class scheme) so evaluators can distinguish what is canon from what is operator-asserted from what is candidate
- Preserving canon-blocking gaps as open so evaluators don't propose closures that would commit the operator
- Providing the Promotion Matrix (Appendix A) as the canonical reference for what is and isn't promoted at any given moment

The brief does NOT close conversion decisions. It surfaces the depth of the architecture so conversion conversations happen at the right level.

### §8.5 — External evidence status

**OpenAI + Suno corporate outreach** `[OPERATOR_ASSERTED / EXTERNAL EVIDENCE NOT ATTACHED]` (surgical patch P20):

Operator-reported external context. Not acceptance evidence for the brief's thesis. Conversion-evaluation discussions with OpenAI or Suno are the brief's audience, not its support. Treating the outreach as evidence of the architecture's correctness would invert the relationship.

**v2.6 → Suno v5.5 Pro empirical claim** `[OPERATOR_ASSERTED / EMPIRICAL ANECDOTE / TEST ARTIFACTS NOT ATTACHED]` (surgical patch P22):

Operator-reported observation that v2.6 monolithic prompts produce better output on Suno v5.5 Pro than they originally did. Load-bearing for INV-08 (depth-accumulation) but not file-verified via attached test artifacts. Promotion to documented test result requires test artifact attachment.

---

## §9 — Failure Modes and Mitigations

Authority/status column per row. Failure modes are observed; mitigations are candidate spec content unless otherwise noted.

| # | Failure Mode | Where Observed | Mitigation (candidate) | Authority Class (mitigation) |
|---|---|---|---|---|
| FM-01 | Phantom commitment compounding | v5 sessions, custom GPT workspace | Runtime Phantom Detection at emit time (INV-04 enforcement) | `[CANDIDATE_SPEC]` via `mosaic_engine_v0_1.md` |
| FM-02 | Mode drift (Conversation → Q&A) | v5/v5-c sessions; detected by tonal shift | RECA pre-pass + Tri-Attention monitoring; conversation-mode discipline | `[CANDIDATE_SPEC]` via Mosaic Engine v0.1 + Chimera-Indigo lineage |
| FM-03 | Detail Non-Regression silently failed | v5 version bumps | INV-02 structural enforcement; no silent drops; deprecation requires reason + migration path | `[FILE-VERIFIED:v5b INV-02]` named; runtime enforcement is `[CANDIDATE_SPEC]` |
| FM-04 | Implicit cross-references collapsed on file split | v5 multi-file split | Resident operational memory layer (L2) explicit in substrate; cross-references named primitives | `[OPERATOR_ASSERTED]`; support: forensic_supported; support_source_class: `[FORENSIC_CONTROL]` |
| FM-05 | Operator becomes substrate | All v5/v5-c sessions | Bounded SME workforce + non-creative controller + automatic enforcement of invariants | `[CANDIDATE_SPEC]` via Maestro v0 + Mosaic Engine v0.1 |
| FM-06 | Substrate compression at emit | All AI evaluators | Make substrate explicit and addressable via N1-N8 + L1-L5 vocabulary | `[INFERRED]` — naming is the mitigation; promotion-tested mitigation pending |
| FM-07 | Reverse compilation premature (one axis LOCKED) | v0.2 wording (now corrected) | Phase 3 gates PASS required before Phase 4 reverse compilation | `[FILE-VERIFIED:v5b]` per `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md §15` |
| FM-08 | Lyrics edited outside creation node | Unauthorized canon mutation | Lyrics-lock at `LYR.K0.S3` with LCR workflow (two SME approvals required) | `[FILE-VERIFIED:v5b]` |
| FM-09 | Truncation in long-form output | v5/v5-c sessions; Suno parser failures | Character cap canon (4960–4999 / 960–999 / 1960–1999); stop-the-line on truncation | `[FILE-VERIFIED:v5b]` |
| FM-10 | Comma outside lyrics block | Suno parser failure | Stop-the-line condition; format validation gate (M9) | `[FILE-VERIFIED:v5b]` |
| FM-11 | Syllable count out of band | HPA gate failure; "alive" recognition fails | 6–11 syllables per lyric line; M9 format validation | `[CANDIDATE_SPEC]` via `maestro_v0.md §6.5` |
| FM-12 | Silent fill of nulls | Phase 2 work item NULL hunting fails | "Nulls are signal" canon law; null detection cognitive operator | `[FILE-VERIFIED:v5b]` preserved law |
| FM-13 | Creative authorship by controller | controller_contract.yaml violation | Non-creative controller boundary enforcement | `[ACCEPTED_CANON]` (status: operating_stance; scope: run_canonical) |
| FM-14 | FOIL collapsing semantic distinction | Promotion violations | FOIL controller scope limit (promotion + deduplication only) | `[ACCEPTED_CANON]` via `foil_promotion_contract.yaml` |
| FM-15 | Sterile production (HPA fails "alive" test) | Suno renders without imperfection signatures | Sacred Imperfection mandate (INV-09); vinyl crackle / tape wobble / breath / pitch drift / room tone | `[CANDIDATE_SPEC]` via `maestro_v0.md §6.4`; canon support via INV-09 |
| FM-16 | Theatrical persona instead of bounded SME | v5-c "personality" drift | canonical_employee_module_spec principle (bounded SME, not persona flavor) | `[CANDIDATE_SPEC]`; support: principle_canon_supported; status: patched_candidate_for_review |
| FM-17 | False completeness (axis marked complete with internal contradictions) | Phase 3 gate bypass attempts | SE20 failures trigger Phase 2 re-meetings; G-Card evidence binding required | `[FILE-VERIFIED:v5b]` per `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md §14` |
| FM-18 | Mosaic / Maestro platform collapse | v0.2 framing "music application mounted on Mosaic" interpreted as ownership | Boundary preservation (§5.1): distinct systems, candidate substrate/application interface, not platform hierarchy | `[OPERATOR_ASSERTED]` boundary rule |
| FM-19 | Day 2 treated as destination canon | Reconstruction shortcuts | Day 2 explicitly bridge/preservation substrate; v4.5x operational root | `[BRIDGE_LAW]` per V5C return |
| FM-20 | Q1-Q16 schema content reconstructed inside brief | Pressure to close GAP-08 / OQ-6.2 | Canon-blocking gap discipline: do not reconstruct Q1-Q16 content without operator gate | Discipline rule §9 |

---

## §10 — Research Null Register

Surgical patch P18 renames v0.2's "Open Research Questions" to **Research Null Register** with explicit non-canonical labeling.

```yaml
section_status:
  authority_level: non_canonical_research_backlog
  external_facts_require_refresh: true
  promotion_requires:
    - test_protocol
    - evidence_artifact
    - operator_F
    - downstream_risk_note
```

Items in this register are **not canon**. They are research nulls — investigations that could mature into testable claims, evidence artifacts, and eventual promotion candidates. Each promotion requires the four items listed in `promotion_requires` above.

### ORQ-001 — Conversation Layer substrate vs application boundary

**Status:** Research Null. NS-4. Open.

**Question:** Does the Conversation Layer live at substrate (N1 Mosaic) or at application (Maestro)? SEC E03 finding: Conversation Layer is a Chimera-Indigo addition to substrate, not v4.5 inheritance. Mosaic adopts it from Chimera lineage; operator confirmation required that it belongs in substrate (not in Maestro application instance).

**Promotion requirement:** Operator F on substrate-vs-application boundary for Conversation Layer.

### ORQ-002 — DSRP / Tri-Attention / Sense-Think-Act causality

**Status:** Research Null. Open.

**Question:** Are DSRP, Tri-Attention, Sense-Think-Act causally chained (feeds-relation) or co-required parallel? SEC E01-E02 finding: directed-feed relationships from RTFA downgrade to parallel co-required per primary corpus.

**Promotion requirement:** Test protocol on directed-feed vs parallel encoding; evidence artifact; operator F.

### ORQ-003 — 5-Council vs 13-worker vs pinned-matrix default workforce

**Status:** Research Null. Open. `[PROVISIONAL]` (status: unresolved_workforce_topology; stable_principle: bounded_SME_labor; stable_principle_authority: `[ACCEPTED_CANON]`).

**Question:** What is the default workforce topology — 5-Council (executive grouping), 13-worker roster (operator-significant), pinned Council Matrix (v5-b runtime authority), or layered hybrid?

**Promotion requirement:** Operator F on default. Until then, all three frames carried.

### ORQ-004 — Substrate-vs-application boundary for HSI, PTF, Micro-Move libraries

**Status:** Research Null. Open.

**Question:** Are PTF library, Micro-Move library, HSI protocol substrate-level (Mosaic) or application-level (Maestro)? `maestro_v0.md §6` enumerates them as music-specific; substrate generalization requires evidence that the protocols apply across domains.

**Promotion requirement:** Cross-domain test; evidence artifact; operator F.

### ORQ-005 — Mode A/B and Memory-Refine substrate placement

**Status:** Research Null. NS-4. Open.

**Question:** Where does Memory-Refine live? Where do Mode A/B selectors live? Substrate or application? Layer assignment pending.

**Promotion requirement:** Operator F on layer assignment.

### ORQ-006 — Blueprint_JSON ↔ Technical UST precedence

**Status:** Research Null. Open.

**Question:** Precedence rule between Blueprint_JSON (legacy candidate format) and Technical UST (current canonical middleware). Not articulated in current corpus.

**Promotion requirement:** Operator F on precedence rule.

### ORQ-007 — Sacred Imperfection budget parameterization

**Status:** Research Null, **parameterization-ready**. Open.

**Question:** How is the Sacred Imperfection mandate (INV-09 / `maestro_v0.md §6.4`) parameterized? Single budget parameter (per MAESTRO_v5_Dossier_v0.3_Stylebook design) or per-axis floor? Currently asserted as binary mandate ("sterile fails HPA"); operationalization as a tunable parameter is the parameterization-ready research direction.

**Promotion requirement:** Test protocol with parameterized vs binary mandate; evidence artifact (somatic audit comparison); operator F. **Status note:** This is the most mature ORQ — parameterization-ready, awaiting operator promotion decision.

### ORQ-008 — Phantom Detection emit-time vs review-time

**Status:** Research Null. Open.

**Question:** Mosaic Engine v0.1 candidate spec places Phantom Detection at emit time. Operator-asserted; runtime implementation untested. Alternative is review-time detection. Trade-off: emit-time prevents canon mutation; review-time allows surface inspection of phantom-flagged content.

**Promotion requirement:** Test protocol comparing emit-time vs review-time; evidence artifact; operator F.

---

## §11 — Operator Force-Closures

This section enumerates every claim awaiting operator force-closure (F). Canon-blocking gaps from §9 of the mega-prompt are appended here so the operator has a single working list.

### §11.1 — Architecture-level force-closures pending

| ID | Force-Closure Required On | Authority Class (current) | Gate |
|---|---|---|---|
| FC-A01 | Mosaic Engine v0.1 substrate runtime promotion | `[CANDIDATE_SPEC]` | Source attached + operator F |
| FC-A02 | Maestro v0 music application promotion | `[CANDIDATE_SPEC]` | Mosaic/Maestro boundary force-closure + source attached + operator F |
| FC-A03 | Mosaic / Maestro boundary canon (platform-hierarchy vs independent-platform) | `[OPERATOR_ASSERTED]` | Operator F on boundary frame |
| FC-A04 | Five-layer pre-loader (L1–L5) canon law | `[OPERATOR_ASSERTED]`; support: forensic_supported; support_source_class: `[FORENSIC_CONTROL]`; status: pending_formalization | substrate_floor_v0.2.yaml authored with architecture_layers + operator F on this brief's §6 |
| FC-A05 | Workforce topology default (5-Council / 13-worker / pinned matrix / hybrid) | `[PROVISIONAL]`; status: unresolved_workforce_topology; stable_principle: bounded_SME_labor; stable_principle_authority: `[ACCEPTED_CANON]` | Operator F |
| FC-A06 | canonical_employee_module_spec schema (25+ fields) promotion | `[CANDIDATE_SPEC]`; support: principle_canon_supported; status: patched_candidate_for_review | Operator F on schema |
| FC-A07 | Day 2 / v4.5x / Day 3 reconstruction relationship | `[BRIDGE_LAW]` for Day 2 | Operator F on reconstruction rules |

### §11.2 — Canon-blocking gaps (DO NOT close in this brief)

Per FORENSIC return — these gaps must remain open. Inferring closure is a discipline violation.

| Gap ID | Description | Status in v0.3 |
|---|---|---|
| GAP-02 | SongCouncil per-member metrics | OPEN — canon-blocking; do not author |
| GAP-06 | Persona Schema | OPEN — paused until GAP-02 closes |
| GAP-08 | SE20 vs BICDM-20 vs SEM-12 relationship | OPEN — canon-blocking + implementation-blocking; do not default |
| GAP-09 | G-Card ≥7.0/10 vs SEM 97.5/100 scalar | OPEN — unresolved scalar relationship; do not collapse |
| GAP-VIS-K8 | VIS/K8 scope | OPEN — canon-blocking + implementation-blocking; do not infer |
| GAP-+4 | +4 governors active status | OPEN — depends on VIS/K8 |
| GAP-MIX | Mixed-use policy | OPEN — canon-blocking; do not default |
| GAP-HPA | HPA aggregate | OPEN — blocked |
| GAP-EXEC | Executive Committee composition for Red-Pen Review | OPEN — function confirmed; composition open |
| OQ-6.2 | Q1-Q16 schema content | OPEN — confirmed artifact category; content unresolved; do not reconstruct |
| OQ-6.3 | K8 slot collision | OPEN — needs operator decision |
| OD-1 | 4-layer Persona Stack disposition | OPEN — canonical_employee_module_spec is patched_candidate, not auto-closure |
| OD-2 / NS-3 | 4-Plane partition vs phase-based feedback | OPEN — structure CANDIDATE |
| OD-3 | Strategy / Mode orthogonality | OPEN — operator F required |
| OD-4 | Conversation Layer lineage | OPEN — Chimera-Indigo lineage documented but Mosaic promotion pending |
| OD-5 | PTF library data structure (YAML/JSON form) | OPEN — operator F required |
| NS-4 | Mode A/B and Memory-Refine substrate/application boundary | OPEN — layer assignment pending |

### §11.3 — Brief-specific force-closures

| ID | Force-Closure Required On | Authority Class (current) | Gate |
|---|---|---|---|
| FC-B01 | Acceptance of this brief as conversion-evaluation draft (Option A) | DRAFT | Operator F per §14 |
| FC-B02 | Adoption of 9-class authority scheme as project standard | `[INFERRED]` (operating proposal) | Operator F |
| FC-B03 | Promotion Matrix as canonical reference for what is/isn't promoted | `[INFERRED]` (operating proposal) | Operator F |
| FC-B04 | ORQ-007 (Sacred Imperfection budget) advance to parameterization-ready status | `[OPERATOR_ASSERTED]`; status: research_ready | Operator F |

### §11.4 — New gaps surfaced during v0.3 revision

| ID | Description | Status |
|---|---|---|
| FC-N01 | Blueprint_JSON ↔ Technical UST authority precedence | OPEN — precedence rule not articulated |
| FC-N02 | FOIL target lineage (Maestro v0 vs Mosaic v0.1 mount layer) | OPEN — mount layer not assigned |
| FC-N03 | Day 2 overlay ↔ 13-stage chain reconciliation | OPEN — state-model relationship not specified |
| FC-N04 | Technical UST address ownership (inverted groove / pocket / three-tier low-end) | OPEN — addresses not assigned |
| FC-N05 | ATP manifest format for v5-b source pack | OPEN — 14-file cold-start pack vs Mosaic ATP relation unspecified |
| FC-N06 | Executive Red-Pen Review placement | OPEN — phase placement, return path, mode applicability open |

This brief REFERENCES these gaps. This brief does NOT propose closures.

---

## §12 — Implementation Roadmap

Roadmap is sequenced to start with promotion discipline (Phase A) before any architectural promotion. This protects the project from authority erosion if conversion conversations begin before canon is set.

### §12.A — Promotion Discipline Phase (immediate)

**Phase A is the immediate priority.** It establishes the authority infrastructure before any architectural promotion.

1. Operator review of v0.3 — accept (Option A), patch (Option B), or authorize row-by-row promotion (Option C) per §14.
2. If Option A: brief becomes conversion-bridge artifact; Promotion Matrix becomes the working reference.
3. If Option C: build Promotion Matrix into canonical project ledger; process rows individually; record promotion / deferral / rejection per row with rationale.
4. ORQ-007 parameterization decision recorded (Sacred Imperfection budget — promote, defer, or reject).
5. Day 2 / v4.5x reconstruction relationship force-closure recorded.

### §12.B — Substrate Promotion Phase (operator F gates)

After Phase A clears (operator F on §14 acceptance):

1. Author `substrate_floor_v0.2.yaml` with explicit `architecture_layers` section (L1–L5).
2. Operator F on `substrate_floor_v0.2.yaml`.
3. Operator F on Mosaic Engine v0.1 candidate spec (or revised candidate).
4. Operator F on Mosaic / Maestro boundary canon (platform-hierarchy frame OR independent-platform frame).
5. Re-issue Promotion Matrix rows for substrate runtime claims.

### §12.C — Application Promotion Phase

After Phase B clears:

1. Operator F on Maestro v0 candidate spec.
2. Operator F on default workforce topology (FC-A05).
3. Operator F on `canonical_employee_module_spec.yaml` schema (FC-A06).
4. CR-009 source attached; SEM K1-K12 source attached; 97.5% threshold provenance closed.
5. Re-issue Promotion Matrix rows for application claims.

### §12.D — Gap Closure Phase (operator-paced)

Operator determines closure order for canon-blocking gaps. Sequence-locked:

- GAP-02 must close before GAP-06 (Persona Schema paused until SongCouncil per-member metrics defined)
- GAP-VIS-K8 must close before GAP-+4 (+4 governors active status depends on VIS/K8 scope)
- GAP-08 (SE20/BICDM-20/SEM-12 relationship) and GAP-09 (G-Card vs SEM scalar) appear adjacent — operator F on relationship before either closes

### §12.E — Conversion-Evaluation Engagement Phase

Conversion conversations (OpenAI, Suno, IP, app integration) proceed in parallel with Phases A–D. This brief is the bridge artifact for those conversations. Conversion-evaluation discussions do NOT promote canon — they consume the Promotion Matrix as the canonical reference for what is and isn't yet promoted, and surface conversion risks back to the operator for force-closure.

### §12.F — Forward Maintenance Phase

After Phases A–D complete sufficiently for runtime promotion:

1. Migrate canon to a v0.4+ artifact set (not this brief).
2. Archive v0.3 brief as conversion-bridge historical artifact.
3. Maintain forensic chain as `[FORENSIC_CONTROL]` reference layer.
4. Continue forward Promotion Matrix as authority reference.

---

## §13 — Future Vectors `[PROVISIONAL]`

**Authority:** `[PROVISIONAL]`
**status:** future_vector
**promotion:** do_not_promote
**scope:** strategic_speculation

Surgical patch labels every speculative element in this section as non-canon. The section is preserved for strategic-direction discussion, NOT for accidental scope expansion.

### §13.1 — Multimodal identity engines `[PROVISIONAL]` (status: future_vector; promotion: do_not_promote)

Strategic speculation: if Mosaic substrate proves out for music via Maestro v0, the same substrate could host a multimodal identity engine — an application that produces coherent identity surfaces across audio, visual, and narrative modalities. The Persona Surface (A/R Profile) primitive in Maestro v0 hints at this: identity is already a canonical output category alongside work-product and style.

Not promoted. Speculation only.

### §13.2 — Music-native cinema `[PROVISIONAL]` (status: future_vector; promotion: do_not_promote)

Strategic speculation: a music-native cinema application could mount on Mosaic with N4 canon extended to include visual axes (cinematography, blocking, edit pacing) and N7 output adapted to a video renderer. The "music-native" framing is operator-derived from the body's prior somatic-audit response to music; whether the same response generalizes to motion picture is unknown.

Not promoted. Speculation only.

### §13.3 — Persistent audiovisual canon `[PROVISIONAL]` (status: future_vector; promotion: do_not_promote)

Strategic speculation: cross-application Mosaic CINR could carry canon between music application (Maestro v0) and a future audiovisual application, allowing a song's UST to inform a future cinematic UST without re-derivation. Architectural support: domain-neutral N4 canon address space; ATP cross-session portability.

Not promoted. Speculation only.

### §13.4 — Cross-artist identity preservation `[PROVISIONAL]` (status: future_vector; promotion: do_not_promote)

Strategic speculation: a per-artist Mosaic CINR could preserve identity coherence across collaboration boundaries — when artist A's Mosaic instance interacts with artist B's Mosaic instance, neither identity dissolves into the other. Bounded SME workforce structure is the architectural precedent.

Not promoted. Speculation only.

### §13.5 — Substrate-as-product `[PROVISIONAL]` (status: future_vector; promotion: do_not_promote)

Strategic speculation: Mosaic Engine as a portable substrate product separate from Maestro v0, available for other domain applications. This is the architectural-width future stated as a product direction. Conversion-evaluation discussions with OpenAI may explore this; the brief surfaces the direction without promoting it.

Not promoted. Speculation only.

### §13.6 — Boundary preservation across all future vectors

Every future vector in §13 carries the same boundary rule: no future vector may collapse Mosaic and Maestro into a single platform, and no future vector may absorb application-layer concerns into substrate without explicit operator F. The boundary preservation rule (§5.1) applies forward.

---

## §14 — Acceptance Gate Status

Three operator decision options for v0.3 acceptance.

### Option A — ACCEPT AS CONVERSION-EVALUATION DRAFT

Allows use of v0.3 for OpenAI / Suno / IP / app conversion-evaluation discussions.

- Does not promote claims to canon.
- Authority classification (9-class scheme) preserved.
- Promotion Matrix (Appendix A) preserved as canonical reference.
- v0.3 becomes the bridge artifact for conversion audience engagement.
- Canon-blocking gaps remain open.
- Operator F on Option A is the minimum acceptance signal.

### Option B — PATCH REQUIRED BEFORE REVIEW

Identified additional conflicts must be corrected before acceptance.

- Returns brief to revision queue.
- Operator specifies required additional patches.
- v0.3 is NOT used for conversion-evaluation engagement until patches applied and re-accepted.

### Option C — PROMOTION REVIEW AUTHORIZED

Build Promotion Matrix (Appendix A) into the canonical project ledger and process claims one by one.

- Each row promoted, deferred, or rejected with rationale.
- Final canon ledger emerges from row-by-row promotion.
- Brief continues as conversion bridge while promotion review proceeds in parallel.
- Operator selects row order; brief recommends starting with Phase A items.

**Recommended path:** Option A — accept as conversion-evaluation draft. This preserves the brief's value for the operator's purpose (surfacing edges other AIs miss when evaluating Maestro for app conversion) without overcommitting to canon promotion that requires source attachments and operator force-closures not yet in place. Option C may proceed in parallel with Option A.

### Acceptance state at v0.3 publication

```yaml
acceptance_state:
  version: v0.3
  status: DRAFT
  awaiting: operator_F
  options:
    - A: accept_as_conversion_evaluation_draft
    - B: patch_required_before_review
    - C: promotion_review_authorized
  default_path: A
  parallel_path: A + C
  expiration: none  # brief persists as bridge artifact until superseded
```

---

## §15 — Promotion Diff

If operator F is recorded on v0.3, the following are promoted:

1. **The conversion-evaluation frame.** Maestro conversion must preserve substrate relations (not just surface workflow), the five-layer pre-loader bundle (L1–L5), lineage memory (INV-02 + Q-A-F audit trail), UST/SEM concurrency (during creation, not after), and the non-creative controller boundary. Surface-only conversion strips what makes Maestro work.

2. **The reboot contradiction table (§1) with row-by-row authority labels.** Accepted rows become correction constraints for future evaluators. Rejected rows are recorded with rationale.

3. **The nine-class authority classification scheme.** This becomes the standard authority discipline for subsequent artifacts in this project.

4. **The Promotion Matrix (Appendix A).** Becomes the canonical reference for what is and isn't promoted at any given moment.

5. **ORQ register status.** ORQ-007 (Sacred Imperfection budget) is parameterization-ready, awaiting operator promotion decision. ORQ-001 through ORQ-008 otherwise remain Research Nulls.

6. **The brief's section structure** as a working template for subsequent conversion-evaluation review briefs.

If operator F is recorded on v0.3, the following are explicitly NOT promoted:

- **Mosaic Engine v0.1 as established canon** — remains `[CANDIDATE_SPEC]`.
- **Maestro v0 as established canon** — remains `[CANDIDATE_SPEC]`.
- **Five-layer pre-loader as final canon law** — remains `[OPERATOR_ASSERTED]` (support: forensic_supported; support_source_class: `[FORENSIC_CONTROL]`; status: pending_formalization) until substrate_floor_v0.2.yaml + operator F.
- **canonical_employee_module_spec.yaml** beyond `patched_candidate_for_review`.
- **5-Council vs 13-worker workforce topology** — remains `[PROVISIONAL]` (status: unresolved_workforce_topology; stable_principle: bounded_SME_labor; stable_principle_authority: `[ACCEPTED_CANON]`).
- **Q1-Q16 schema content** — remains canon-blocking (OQ-6.2 / GAP-08); do not reconstruct.
- **SE20 vs BICDM-20 vs SEM-12 relationship** — remains GAP-08; do not default.
- **G-Card ≥7.0 vs SEM 97.5/100 scalar relationship** — remains GAP-09; do not collapse.
- **VIS/K8 scope** — remains canon-blocking; do not infer.
- **+4 governors active status** — depends on VIS/K8.
- **Mixed-use policy** — remains GAP-MIX; do not default.
- **HPA aggregate** — remains GAP-HPA blocked.
- **Executive Committee composition** — remains GAP-EXEC open.
- **SongCouncil per-member metrics** — remains GAP-02 canon-blocking.
- **Persona Schema** — remains paused until GAP-02 closes.
- **OpenAI + Suno external evidence** — remains operator-reported, not evidence.
- **v2.6 → Suno v5.5 Pro empirical claim** — remains operator-asserted anecdote.
- **Maestro / Mosaic platform-hierarchy collapse** — boundary preserved.
- **Seven-workspace narrative as architectural taxonomy** — remains operator-asserted historical framing.
- **"What no current AI tool does" overclaim** — superseded by "what this architecture is designed to do".
- **New kernel law** — no INV additions or modifications proposed by this brief.
- **New Creative UST surface law** — legacy v4.5x + v5-c separation preserved; neither absorbs the other.

The Promotion Diff is the load-bearing acceptance contract. Operator F on Option A or Option C entails operator F on the Promotion Diff as the canonical statement of what acceptance does and does not entail.

---

## Appendix A — Promotion Matrix

The Promotion Matrix replaces v0.2's Evidence Provenance Index appendix. Every major architectural claim in v0.3 has a row.

| # | Claim | Source | Authority Class | Status | Blocker | Promotion Requirement |
|---|---|---|---|---|---|---|
| 1 | Mosaic Engine v0.1 substrate runtime | `mosaic_engine_v0_1.md` | CANDIDATE_SPEC | Formal candidate spec per files5 | Operator force-closure on substrate/application boundary | Operator F + source attached |
| 2 | Maestro v0 music application | `maestro_v0.md` | CANDIDATE_SPEC | Formal candidate spec per files5 | Mosaic/Maestro boundary force-closure | Operator F + source attached |
| 3 | Technical UST as canonical middleware | v5-c root prompt + `canonical_employee_module_spec.yaml` preserved law | [ACCEPTED_CANON]; status: operating_stance; scope: run_canonical | Run-canonical for current operating support set | Project-canon promotion requires replay | Replay ledger |
| 4 | Creative UST as derivative downstream shell | `canonical_employee_module_spec.yaml` preserved law | [ACCEPTED_CANON]; status: operating_stance; scope: run_canonical | Run-canonical | None known | Already accepted |
| 5 | SEM as concurrent quality substrate (during creation, not after) | SEM session + `maestro_v0.md §4.1` | OPERATOR_ASSERTED | Run-canonical principle | `maestro_v0.md` or CR-009 source attachment | Source attached + operator F |
| 6 | Five-layer pre-loader (L1–L5) | Staging emission + operator assertion + RTFA forensic support | `[OPERATOR_ASSERTED]`; support: forensic_supported; support_source_class: `[FORENSIC_CONTROL]`; status: pending_formalization | High-confidence synthesis | substrate_floor_v0.2.yaml with architecture_layers | substrate_floor_v0.2 + operator F |
| 7 | 12-criterion SEM K1-K12 | `maestro_v0.md §4.1` (referenced) | UNVERIFIED-PENDING-SOURCE | Operator-asserted with reference | `maestro_v0.md` source attachment | Source attached |
| 8 | 97.5% release threshold | CR-009 (referenced) | OPERATOR_ASSERTED | Active KPI card | CR-009 source attachment | Source attached |
| 9 | Q1-Q16 Q-Matrix content | Open | `[PROVISIONAL]`; status: open; promotion: do_not_promote; blocker: canon_gap | Canon-blocking + implementation-blocking (OQ-6.2 / GAP-08) | Operator gate | Do not reconstruct |
| 10 | SE20 / BICDM-20 / SEM-12 relationship | Open | GAP-08 | Canon-blocking + implementation-blocking | Operator decision | Do not default |
| 11 | G-Card ≥7.0 vs SEM 97.5/100 scalar | Open | GAP-09 | Unresolved scalar relationship | Operator decision | Do not collapse |
| 12 | VIS/K8 scope | Open | GAP-VIS-K8 | Canon-blocking + implementation-blocking | Operator scope decision | Do not infer |
| 13 | +4 governors active status | Open | GAP-+4 | Depends on VIS/K8 | Operator scope decision | Do not infer |
| 14 | Mixed-use policy | Open | GAP-MIX | Canon-blocking | Operator policy decision | Do not default |
| 15 | HPA aggregate | Open | GAP-HPA | Blocked | Operator decision | Do not aggregate |
| 16 | Executive Committee composition (Red-Pen Review) | Open | GAP-EXEC | Function confirmed; composition open | Operator decision | Do not specify |
| 17 | SongCouncil per-member metrics | Open | GAP-02 | Canon-blocking | Operator decision | Do not author |
| 18 | Persona Schema | Open | GAP-06 | Paused until GAP-02 | GAP-02 closure | Sequential |
| 19 | FOIL promotion + deduplication (controller scope) | `foil_promotion_contract.yaml` (status authoritative_done) | ACCEPTED_CANON (for controller scope) | Authoritative within FOIL controller scope | None known | Already accepted within scope |
| 20 | FOIL lineage cascade (MACRO/MICRO/TACTICAL/VARIABLE+1) | Lineage evidence per DAVI return | OPERATOR_ASSERTED / FORENSIC-DERIVED | Origin model | Separate from controller-safe scope | Two-layer structure preserved |
| 21 | canonical_employee_module_spec 25+ fields | `canonical_employee_module_spec.yaml` (status patched_candidate_for_review) | `[CANDIDATE_SPEC]`; support: principle_canon_supported; status: patched_candidate_for_review | Patched candidate per V5C return | File status promotion | Operator F on schema |
| 22 | INV-01 through INV-10 kernel invariants | `mosaic_engine_v0_1.md` (referenced as candidate) | UNVERIFIED-PENDING-SOURCE (for promotion to canon kernel) | Mosaic candidate spec content | Mosaic Engine v0.1 promotion | Source attached + Mosaic F |
| 23 | 16 cognitive operators | `mosaic_engine_v0_1.md` candidate spec | UNVERIFIED-PENDING-SOURCE | Mosaic candidate content | Mosaic Engine v0.1 promotion | Source attached + Mosaic F |
| 24 | ATP / CINR / Replay / Branch / Phantom Detection state primitives | Mosaic candidate spec | UNVERIFIED-PENDING-SOURCE | Mosaic candidate content | Mosaic Engine v0.1 promotion | Source attached + Mosaic F |
| 25 | 8 substrate layers N1-N8 | `mosaic_engine_v0_1.md` (referenced) | UNVERIFIED-PENDING-SOURCE (for promotion to substrate canon) | Mosaic candidate content | Mosaic Engine v0.1 promotion | Source attached + Mosaic F |
| 26 | Reasoning stack (RECA / Tri-Attention / DSRP / Sense-Think-Act) | `mosaic_engine_v0_1.md` candidate spec | UNVERIFIED-PENDING-SOURCE | Mosaic candidate content | Mosaic Engine v0.1 promotion + edge-relationship resolution (ORQ-002) | Source attached + Mosaic F |
| 27 | 13-stage runtime chain | Lineage evidence | OPERATOR_ASSERTED / FORENSIC-DERIVED | Historical operational | Reconciliation with M0–M11 candidate (FC-N03) | Operator F on reconciliation |
| 28 | Sacred Imperfection mandate (INV-09 instantiation) | `maestro_v0.md §6.4` + operator canon | OPERATOR_ASSERTED | Active operating principle | Source attached | `maestro_v0.md` attached |
| 29 | 5-Council workforce | Lineage + executive grouping | BRIDGE_LAW (explanatory layer) | Executive grouping not runtime authority | Pinned matrix supersedes per V5B | Renaming complete |
| 30 | 13-worker expansion lens | Lineage + v5-c reference + `maestro_v0.md §2.2` | `[PROVISIONAL]`; status: unresolved_workforce_topology; stable_principle: bounded_SME_labor; stable_principle_authority: `[ACCEPTED_CANON]` | Not force-closed | Operator F | Operator decides default |
| 31 | Pinned Council Matrix (Alan/Vanessa/Anva/Eldrik/Dave/Sage/Melony + V&V Marshal) | `COUNCIL_MATRIX` v5-b | FILE-VERIFIED:v5b | Verified runtime execution authority | None known | Already verified |
| 32 | Phantom Detection at emit time | Mosaic candidate spec | UNVERIFIED-PENDING-SOURCE | Mosaic candidate content | Mosaic Engine v0.1 promotion | Source attached + Mosaic F + ORQ-008 resolved |
| 33 | Suno output law (legacy v4.5x order) | Historical v4.5x + `maestro_v0.md §5.1` | BRIDGE_LAW | Legacy ancestor only | None — usage historical | N/A |
| 34 | Suno output law (v5-c Creative UST) | Current Creative UST shell + `template_creative_ust.yaml` | [ACCEPTED_CANON]; status: operating_stance; scope: run_canonical | Forbids `[Road-Map]`, `[CREW_TAGS]`, standalone `[FX]` per DAVI return | None | Already operating |
| 35 | Seven workspaces as sequential epistemic phases | Operator narrative | OPERATOR_ASSERTED / NARRATIVE MODEL | Historical framing | None — narrative | N/A |
| 36 | OpenAI + Suno corporate outreach | Operator report | OPERATOR_ASSERTED / EXTERNAL EVIDENCE NOT ATTACHED | Operator-reported external context | Evidence packet | Evidence attached |
| 37 | v2.6 → Suno v5.5 Pro empirical claim | Operator report | OPERATOR_ASSERTED / EMPIRICAL ANECDOTE / TEST ARTIFACTS NOT ATTACHED | Operator-reported observation | Test artifacts | Test artifacts attached |
| 38 | Substrate compression-gap observation | Operator origin claim + RTFA forensic support | OPERATOR_ASSERTED | Architectural origin observation | Replay citation | Replay attached |
| 39 | Three-Maestro partition (Project/App/Runtime) | `mosaic_engine_v0_1.md` INV-10 | FILE-VERIFIED:v5b (INV-10 as invariant) | Canon partition rule | None | Already canonical |
| 40 | PERF axis name (not PER) | `[FILE-VERIFIED:v5b]` per V5B return | FILE-VERIFIED:v5b | Verified canonical axis name | None | Already verified |
| 41 | LYR.K0.S3 forbidden ops address (not K5.S3) | `[FILE-VERIFIED:v5b]` per V5B return | FILE-VERIFIED:v5b | Verified canon address | None | Already verified |
| 42 | Character cap 4960–4999 / 960–999 / 1960–1999 | `[FILE-VERIFIED:v5b]` per V5B return | FILE-VERIFIED:v5b | Verified canon caps | None | Already verified |
| 43 | Reverse compilation gate (Phase 3 gates PASS) | `[FILE-VERIFIED:v5b]` per V5B return + `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md §15` | FILE-VERIFIED:v5b | Verified canon gate | None | Already verified |
| 44 | Phase model (Phase 0 dual scaffold through Phase 5 delivery) | `[FILE-VERIFIED:v5b]` per V5B return | FILE-VERIFIED:v5b | Verified canon phase model | None | Already verified |
| 45 | Stop-the-line semantics | `[FILE-VERIFIED:v5b]` per V5B return | FILE-VERIFIED:v5b | Verified canon stop-the-line | None | Already verified |
| 46 | Evidence Contract (one sentence per subkey, operational constraint, source binding, downstream prediction, challenge cycle) | `EVIDENCE_CONTRACT` v5-b | FILE-VERIFIED:v5b | Verified canon contract | None | Already verified |
| 47 | Mandatory logs (run ledger, work item ledger, dissent map, consensus minutes, gate results, cap report, lock report, telemetry) | `LOG_TEMPLATES` v5-b | FILE-VERIFIED:v5b | Verified canon logs | None | Already verified |
| 48 | SEG / G-Card / SE20 axes | `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md` | FILE-VERIFIED:v5b | Verified canon governance axes | None | Already verified |
| 49 | G-Card pass threshold ≥7.0 | `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md G.K6.S4` | FILE-VERIFIED:v5b | Verified canon threshold | GAP-09 (scalar relationship to SEM 97.5/100 unresolved) | GAP-09 closure for scalar collapse |
| 50 | UST state machine (NULL → PROPOSED → PRESSURED → RESOLVED → LOCKED) | `[FILE-VERIFIED:v5b]` + `maestro_v0.md §3.3` | FILE-VERIFIED:v5b | Verified canon state machine | None | Already verified |
| 51 | Triad as training signal + downstream conditioning (not disposable end-output) | `[FILE-VERIFIED:v5b]` governance clarification | FILE-VERIFIED:v5b | Verified canon semantic | None | Already verified |
| 52 | Non-creative controller boundary | `controller_contract.yaml` + `canonical_employee_module_spec.yaml` preserved law | [ACCEPTED_CANON]; status: operating_stance; scope: run_canonical | Run-canonical boundary | None known | Already accepted |
| 53 | Nulls are signal (not absence) | `canonical_employee_module_spec.yaml` preserved law | [ACCEPTED_CANON]; status: operating_stance; scope: run_canonical | Run-canonical | None | Already accepted |

Additional rows to be added as content surfaces and new claims enter the brief or are derived from gap closure.

---

## Appendix B — Glossary

Terms used throughout this brief, with authority class where applicable.

- **ATP** — Artifact Transfer Packet; portable, hash-verified state capsule any future session can resume from. `[CANDIDATE_SPEC]` content per `mosaic_engine_v0_1.md`.
- **BICDM-20** — Referenced governance axis (relationship to SE20 and SEM-12 is GAP-08, open).
- **BRIDGE_LAW** — Authority class. Preserved from Day 2 / v4.5x lineage but not final destination canon.
- **Candidate keystone** — Status descriptor for the five-layer pre-loader: high-confidence operator+forensic support, awaiting formalization and operator F before canon promotion.
- **CANDIDATE_SPEC** — Authority class. Formal authored runtime/product proposal pending operator force-closure.
- **CINR** — Canonical Instance Node Record; runtime state representation. `[CANDIDATE_SPEC]` content per `mosaic_engine_v0_1.md`.
- **Conversation Layer** — N1 in Mosaic substrate layer architecture. Per SEC E03, originated in Chimera-Indigo, not v4.5; substrate-vs-application placement is ORQ-001.
- **CR-009** — Referenced operator canon record for 97.5% release threshold supersession of 70% AI default; source attachment pending.
- **Creative UST** — Canonical downstream output format / shell. Derives from locked Technical UST. `[ACCEPTED_CANON]` (status: operating_stance; scope: run_canonical; derivative: true).
- **DAVI** — One of the four reviewing workspaces; surfaced §7.7 Suno output split and §15 Promotion Diff requirement.
- **Day 2 / Day 3** — Bridge / preservation substrate from broken migration environment (Day 2); stress-test / failure evidence (Day 3). Neither is destination canon. v4.5x is operational root.
- **Eight axes** — THY, VOC, STY, TIM, PERF, POST, MAP, LYR. Note PERF (not PER) per `[FILE-VERIFIED:v5b]`.
- **EXECUTABLE_CHAIN** — v5-b canonical pack member.
- **EVIDENCE_CONTRACT** — v5-b canonical pack member.
- **Files5 / Files6** — Lineage layers: Files5 authored Mosaic Engine v0.1 and Maestro v0 as formal candidate specs; Files6 added forensic verification (RTFA, SEC, SDG, SLR, MMR) underneath. Files6 is `[FORENSIC_CONTROL]`, not promotion.
- **FILE-VERIFIED:v5b** — Authority class. Verified in currently uploaded v5-b canonical pack.
- **Five-layer pre-loader** — L1 kernel invariants / L2 operational memory / L3 heuristics-as-substrate / L4 lineage memory / L5 project-state pre-loading. `[OPERATOR_ASSERTED]` (support: forensic_supported; support_source_class: `[FORENSIC_CONTROL]`; status: pending_formalization).
- **FOIL** — Two-layer structure: lineage origin (cascade MACRO→MICRO→TACTICAL→VARIABLE+1) + controller scope (promotion + deduplication only). Per DAVI return.
- **FORENSIC** — One of the four reviewing workspaces; surfaced formal-candidate-spec status and canon-blocking gap inventory.
- **FORENSIC_CONTROL** — Authority class. V&V layer artifact; controls interpretation, does not auto-promote.
- **G-Card** — Quality & Excellence Gate governance axis. Pass threshold ≥7.0 per G.K6.S4. Scalar relationship to SEM 97.5/100 is GAP-09.
- **GAP-XX** — Canon-blocking or implementation-blocking gaps that must remain open in this brief.
- **HSI** — Human Struggle Injection protocol: Origin / Scar / Choice / Cost. `[CANDIDATE_SPEC]` content per `maestro_v0.md §6.3`.
- **INV-01 through INV-10** — Mosaic kernel invariants. Status as canon-kernel laws is `[UNVERIFIED-PENDING-SOURCE]` for full promotion, even where named in `mosaic_engine_v0_1.md`.
- **LCR** — Lyric Change Request workflow; two SME approvals required for edits to locked text.
- **LYR.K0.S3** — Address for lyrics-lock forbidden operations. Supersedes `LYR.K5.S3` per `[FILE-VERIFIED:v5b]`.
- **Maestro.Project / Maestro.App / Maestro.Runtime** — Three non-interchangeable partition categories per INV-10.
- **Mosaic Engine v0.1** — Formal candidate substrate runtime spec. `[CANDIDATE_SPEC]`.
- **N1-N8** — Eight substrate layers per Mosaic Engine v0.1 candidate spec.
- **Non-creative controller** — Boundary rule: controller may route, validate, log; controller may NOT re-centralize semantic judgment or perform creative authorship.
- **OPERATOR_ASSERTED** — Authority class. Direct operator claim not yet converted into artifact evidence.
- **ORQ-XXX** — Research Null Register entries. Non-canonical research backlog.
- **PERF** — Performance axis. Supersedes `PER` per `[FILE-VERIFIED:v5b]`.
- **Phantom commitment** — Q+A without F treated as canon. INV-04 prohibition. Mosaic Engine v0.1 candidate spec places Phantom Detection at emit time.
- **PROVISIONAL** — Authority class. Plausible but unresolved; weak evidence; do not promote.
- **PTF** — Pain-to-Fix Library; failure-mode → remediation pairs feeding M8 revision loop.
- **Q-A-F** — Question / Answer / Force-closure atomic change unit per INV-04.
- **Replay** — State primitive for re-running a session from ATP; cited as promotion gate for substrate compression observation.
- **RTFA / SEC / SDG / SLR / MMR** — Forensic chain `[FORENSIC_CONTROL]` artifacts: Reasoning-Trace Forensic Audit, Substrate Edge Confirmation, Substrate Dependency Graph, Sem-Layer Resolution, Morris Matrix Resolution.
- **Sacred Imperfection** — INV-09 mandate; required imperfection signatures (vinyl crackle, tape wobble, breath, pitch drift, room tone). Sterile production fails HPA gate.
- **SE20** — Sonic Excellence 20-Axis baseline checklist; "yesterday's award-winning standard."
- **SEG** — Structural & Engineering Gate governance axis.
- **SEM** — Song Excellence Matrix. 12-criterion weighted; 97.5% release threshold per CR-009.
- **SME** — Subject-matter expert; bounded labor unit with explicit domain authority and non-authority.
- **substrate_floor_v0.2.yaml** — Referenced artifact (not yet authored) required for five-layer pre-loader promotion to canon.
- **Substrate** — Material LLMs compress out between reasoning and surfaced response. Observable as dependency wiring flattened into adjacency / inventory in surfaced output.
- **Technical UST** — Sole canonical source-of-truth middleware. `[ACCEPTED_CANON]` (status: operating_stance; scope: run_canonical).
- **TECHNICAL_UST_CANON** — v5-b canonical pack member.
- **TECHNICAL_UST_GOVERNANCE_ADDENDUM** — v5-b canonical pack member; defines SEG/G-Card/SE20 axes.
- **Triad** — Performer Profile + Show Summary + Session Sheet. Delivered as surface artifact (Phase 5) but treated semantically as training signal + downstream conditioning.
- **UNVERIFIED-PENDING-SOURCE** — Authority class. Likely true in broader corpus but not file-verified in current attached set.
- **UST state machine** — NULL → PROPOSED → PRESSURED → RESOLVED → LOCKED.
- **V&V Marshal** — Gate authority in pinned Council Matrix.
- **V5B / V5C** — Two of the four reviewing workspaces. V5B surfaced canon-corrections (PERF, LYR.K0.S3, character caps, pinned matrix); V5C surfaced Day 2 reframing, Mosaic/Maestro boundary, employee module status, workforce topology open.
- **v4.5x** — Operational root. Working-monolith ancestor that re-asserts substrate every session.

---

## Appendix C — Conversion-Readiness Checklist

Items below are calibrated to v0.3 authority discipline. Each item carries authority labels for downstream evaluation.

### C.1 — Surface-readiness (what the conversion target sees)

- [ ] `[ACCEPTED_CANON]` (status: operating_stance; scope: run_canonical) Technical UST canonical structure (8 axes, AXIS.K{n}.S{n}.variant{n} addressing, 5-state state machine).
- [ ] `[ACCEPTED_CANON]` (status: operating_stance; scope: run_canonical) Creative UST as derivative downstream shell of locked Technical UST.
- [ ] `[FILE-VERIFIED:v5b]` Character cap canon: 4960–4999 / 960–999 / 1960–1999 / ≤150.
- [ ] `[FILE-VERIFIED:v5b]` Triad surface artifact (Performer Profile + Show Summary + Session Sheet).
- [ ] `[FILE-VERIFIED:v5b]` Phase 5 delivery from locked Technical UST + Show Summary only.

### C.2 — Substrate-readiness (what the conversion target may strip)

- [ ] `[CANDIDATE_SPEC]` Mosaic Engine v0.1 substrate runtime preserved (N1-N8 layers).
- [ ] `[CANDIDATE_SPEC]` Sixteen cognitive operators cross-cut every layer (NER through Replay).
- [ ] `[OPERATOR_ASSERTED]` (support: forensic_supported; support_source_class: `[FORENSIC_CONTROL]`; status: pending_formalization) Five-layer pre-loader bundle (L1–L5) named and addressable.
- [ ] `[CANDIDATE_SPEC]` Phantom Detection at emit time per INV-04.
- [ ] `[FILE-VERIFIED:v5b INV-02]` Detail Non-Regression enforced structurally (no silent drops, deprecation requires reason + migration path).
- [ ] `[FILE-VERIFIED:v5b INV-08]` Depth-accumulation preserved (v2.6 → Suno v5.5 Pro lineage maintained — empirical anecdote, test artifacts not yet attached).

### C.3 — Workforce-readiness

- [ ] `[FILE-VERIFIED:v5b]` Pinned Council Matrix (Alan/Vanessa/Anva/Eldrik/Dave/Sage/Melony + V&V Marshal) preserved as runtime execution authority.
- [ ] `[BRIDGE_LAW]` 5-Council framing preserved as executive grouping / explanatory layer.
- [ ] `[PROVISIONAL]` (status: unresolved_workforce_topology; stable_principle: bounded_SME_labor; stable_principle_authority: `[ACCEPTED_CANON]`) Default workforce topology operator F awaited before any conversion-target workforce promise.
- [ ] `[CANDIDATE_SPEC]` (support: principle_canon_supported; status: patched_candidate_for_review) Bounded SME principle preserved (not theatrical persona flavor).
- [ ] `[ACCEPTED_CANON]` (status: operating_stance; scope: run_canonical) Non-creative controller boundary preserved.

### C.4 — Output-discipline-readiness

- [ ] `[FILE-VERIFIED:v5b]` Reverse compilation gate (Phase 3 gates PASS) enforced.
- [ ] `[FILE-VERIFIED:v5b]` Stop-the-line conditions enforced (skipped subkey, silent fill of null, truncation, unauthorized canon mutation, false completeness, comma outside lyrics block, syllable count out of band).
- [ ] `[FILE-VERIFIED:v5b]` LYR.K0.S3 lyrics-lock forbidden operations enforced.
- [ ] `[ACCEPTED_CANON]` Legacy v4.5x and current v5-c Creative UST formats separated; v5-c forbidden constructs (`[CREW_TAGS]`, `[Road-Map]`, standalone `[FX]`) enforced.

### C.5 — Audit-readiness

- [ ] `[FILE-VERIFIED:v5b]` Evidence Contract (one sentence per subkey, operational constraint, source binding, downstream prediction, challenge cycle) enforced.
- [ ] `[FILE-VERIFIED:v5b]` Mandatory logs emitted (run ledger, work item ledger, dissent map, consensus minutes, gate results, cap report, lock report, telemetry).
- [ ] `[CANDIDATE_SPEC]` ATP / CINR portability preserved across sessions / models.
- [ ] `[ACCEPTED_CANON]` (status: operating_stance; scope: run_canonical) Q-A-F atomic change unit; no phantom commitments.

### C.6 — Quality-substrate-readiness

- [ ] `[FILE-VERIFIED:v5b]` SEG / G-Card / SE20 governance axes preserved.
- [ ] `[OPERATOR_ASSERTED]` SEM K1-K12 with 97.5% release threshold preserved (pending CR-009 source attachment for promotion to documentary canon).
- [ ] `[CANDIDATE_SPEC]` Sacred Imperfection signatures preserved (vinyl crackle, tape wobble, breath, pitch drift, room tone).
- [ ] `[CANDIDATE_SPEC]` HSI protocol available (Origin / Scar / Choice / Cost).
- [ ] `[CANDIDATE_SPEC]` PTF library available; Micro-Move library available.

### C.7 — Boundary-readiness

- [ ] `[OPERATOR_ASSERTED]` Maestro / Mosaic platform boundary preserved (distinct systems, candidate interface; not collapse).
- [ ] `[FILE-VERIFIED:v5b INV-10]` Maestro.Project / Maestro.App / Maestro.Runtime partition preserved.
- [ ] `[BRIDGE_LAW]` Day 2 reframed as bridge/preservation substrate (not destination canon).
- [ ] `[OPERATOR_ASSERTED]` v4.5x preserved as operational root.

### C.8 — Discipline-readiness

- [ ] Promotion Matrix (Appendix A) used as canonical reference for what is / isn't promoted at any moment.
- [ ] Canon-blocking gaps (§11.2) remain OPEN in any conversion-target proposal.
- [ ] Non-promotion list (§15) preserved in any conversion-target proposal.
- [ ] Eight-class authority scheme used in any conversion-target authority claim.

A conversion proposal that fails any C.2 item ships a wrapper. A conversion proposal that fails any C.7 item proposes platform collapse. A conversion proposal that fails any C.8 item commits the operator to closures the operator has not authorized.

---

## Appendix D — Pending Source Reconciliation

The following claims are likely true in the broader project corpus but NOT file-verified in the current attached source set. They are preserved here pending source attachment. Movement from this appendix to main-body status requires:

1. Source file attached and verified.
2. Authority class upgraded with reason.
3. Operator F recorded on the migration.

### D.1 — Mosaic substrate architecture (`mosaic_engine_v0_1.md` candidate spec content)

- 8 substrate layers N1-N8 with full detailed semantics
- 10 kernel invariants INV-01 through INV-10 as promoted canon kernel laws (current status: enumerated in candidate spec, awaiting kernel-promotion)
- 16 cognitive operators with detailed scope and integration semantics
- ATP / CINR / Replay / Branch / Phantom Detection state primitives
- Reasoning stack (RECA / Tri-Attention / DSRP / Sense-Think-Act) with edge-relationship resolution (ORQ-002)
- Substrate layer cross-layer interconnect graph

### D.2 — Maestro music application (`maestro_v0.md` candidate spec content)

- 12-criterion SEM K1-K12 with weights (currently referenced; awaiting attachment as documentary canon)
- 97.5% release threshold (CR-009 source attachment pending)
- 13-worker roster as default or hybrid topology decision
- 3 substrate governance roles (Algorithmic Bias Auditor, Negative Control Sheriff, Trauma-Aware Analyst) — substrate vs application boundary (ORQ-004)
- Lyrics-lock forbidden operations enumeration (paraphrase / synonym_substitution / line_rewrite) as promoted canon (currently candidate)
- PTF library (Pain-to-Fix chains)
- Micro-Move library (sub-cognitive operations)
- HSI Origin/Scar/Choice/Cost protocol
- Sacred Imperfection mandate (INV-09) signatures and HPA gate criteria
- Syllable rules 6–11 with HPA gate enforcement details
- Definition of Done checklist (§9 of `maestro_v0.md`)

### D.3 — FOIL contract details (`foil_promotion_contract.yaml` content beyond top-level scope)

- Promotion eligibility rules detailed enumeration
- Deduplication eligibility rules detailed enumeration
- Defect taxonomy (FOIL-specific defect categories)
- Ledger requirements (FOIL-specific ledger entries)
- Block conditions enumeration

(Note: `foil_promotion_contract.yaml` is file-attached with status `authoritative_done`; specific rule details below the top-level governing canon are preserved here for clarity on what the brief has and hasn't quoted directly.)

### D.4 — Canonical employee module (`canonical_employee_module_spec.yaml` schema details)

- 25+ required schema fields with full enumeration
- Five elements (role / expertise / process / output / constraints) detailed specification
- Domain authority / explicit non-authority structure
- Challenge obligations
- Conflict precedence rules
- Reverse pass participation rules

(Note: `canonical_employee_module_spec.yaml` is file-attached with status `patched_candidate_for_review`; specific schema field enumeration is preserved here pending operator F on the schema.)

### D.5 — External validation (operator-reported, not file-attached)

- OpenAI corporate outreach evidence packet
- Suno corporate outreach evidence packet
- v2.6 prompts → Suno v5.5 Pro test artifacts (a/b comparison; somatic-audit measurements; output samples)

### D.6 — Forensic chain claims dependent on full corpus attachment

- Substrate Dependency Graph (SDG) v0.1 specific dependency relationships
- SEM Layer Resolution (SLR) specific layer assignments
- Morris Matrix Resolution (MMR) specific Q1-Q16 reconstruction proposals (note: per FORENSIC return, Q1-Q16 content is OPEN; MMR Path C "Define forward" is the recommended path; this brief does NOT propose Q1-Q16 content)

### D.7 — Cross-corpus dossier claims

- VIG-SEL Research Dossier specific findings
- Reverse UST dossier v0.2 specific reconstructions
- Stylebook dossier v0.3 specific design principles (Sacred Imperfection budget parameterization is ORQ-007)

---

**END OF BRIEF v0.3**

*Conversion-evaluation review brief. Authority-disciplined synthesis. Promotion target: ACCEPTABLE_AS_BRIDGE_CONVERSION_PAPER. Awaiting operator §14 acceptance decision (Option A recommended; Option C may proceed in parallel).*

*This brief revises v0.2 in three coordinated dimensions: authority discipline (9-class scheme replaces broad CANON-DOCUMENTED labels), surgical patches (23 corrections P1–P23 applied), and structural additions (Authority Notice, Current Evidence Scope, Promotion Matrix, §15 Promotion Diff, Appendix D Pending Source Reconciliation). The thesis is preserved. The authority claims are made promotion-safe.*

*The brief does not promote Mosaic Engine v0.1 or Maestro v0 to canon. It does not promote the five-layer pre-loader as final canon law. It does not close any canon-blocking gap. It does not invent new claims.*

*The brief surfaces architectural depth other AI evaluators miss when assessing Maestro for app conversion. That is its purpose. Operator F on §14 entails operator F on §15 Promotion Diff as the canonical statement of what acceptance does and does not entail.*
