---
artifact: maestro_v0_application_spec
version: v0.1-source-anchored
source_primary: song_excellence.yaml@v5.0.2-dedup-kernel (S0001–S2131, 2131 sections)
source_secondary: 4.5.5.txt (via forensic-chain-derived maestro_v0.md, M0-M11 baseline)
mounting_target: Mosaic v0.1 (domain-neutral substrate runtime)
mounting_interface_status: documented-but-not-source-validated
generated: 2026-05-25
methodology: systems-engineering requirements traceability (established)
traceability: bidirectional · every claim cites S####; every source concept has spec destination
supersedes: maestro_v0.md (M0-M11 only; missing M12-M14+G0); all pre-canon-access workspace artifacts
status: DRAFT for operator F
---

# Maestro v0 — Application Specification (Music Domain on Mosaic v0.1)

> This document is the music application that mounts on the Mosaic v0.1 domain-neutral substrate.
> Substrate primitives are consumed via the mounting interface (§2); music-specific content lives here (§3+).
> Cross-contamination of substrate and application is the documented v5-c failure mode — strict separation enforced.

---

## §1. Identity and Purpose

**Maestro v0** is the music creation application within the *Maestro on Mosaic* architecture ("the Rebirth"). It produces release-grade music artifacts under bounded specialist labor, governed by a 12-criterion Song Excellence Matrix at 97.5% release threshold, calibrated to operator somatic vagal/HPA response.

**Distinguishing properties** (vs. v5/v5-b/v5-c lineage which `exposes_failure`):
- Monolithic substrate co-residence per INV-08 (depth-accumulation across cross-references)
- Domain-pure (no Mosaic substrate concerns leak in; no music concerns leak into Mosaic)
- CR-001 portable (single-artifact zero-touch deployment via M11)
- Anti-summarization governance (DC_10): no placeholder compression of canon

**Terminal output** of any session: `A_zero_touch_prompt_for_SUNO` (M11) — single-paste artifact that a new session can run with no further context.

---

## §2. Mounting Interface — Mosaic v0.1 Substrate Consumed

**Validation status:** *documented-but-not-source-validated*. `mosaic_engine_v0_1.md` not loaded in current project; interface drawn from references in `ws_synthesizing-claude_day-1-prep_v1_0.yaml` and `maestro_consolidation_snapshot_v0_1.yaml`. Full source validation pending.

### §2.1 Substrate Layers Consumed (Mosaic N1–N8)

| Layer | Name | Maestro v0 consumes for |
|---|---|---|
| N1 | Conversation | Operator dialogue capture, persona dialogue, council deliberations |
| N2 | Workforce | 6 producer-archetype personas as bounded employee modules |
| N3 | Execution | M0–M14 pipeline execution, M8 revision loop |
| N4 | Canon | song_excellence.yaml content as canonical authority; CR-001→CR-010 rules |
| N5 | Admissibility | SEG scoring + composite ≥97.5% gate; G-Card PASS/ITERATE/HOLD |
| N6 | Governance | Lyric Integrity Lock (CR-002), Speaker Attribution (CR-007), Comma Policy (CR-008) |
| N7 | Output | Triad output contract + M11 zero-touch prompt emission |
| N8 | Cognitive Operators | (16 operators from substrate; specific consumption pattern pending validation) |

### §2.2 Substrate Invariants Honored (Mosaic kernel; documented as 10, specific list pending validation)
- **INV-08 (load-bearing):** Substrate is depth-accumulation, not failure-defense. Monolithic co-residence preserved. *Source: cross-workspace summaries; song_excellence canon implicit confirmation via CR-001 portability principle.*
- Other 9 invariants: documented in references, validation pending.

### §2.3 Cognitive Operators Consumed (16 documented; consumption pattern pending)
Documented in cross-workspace summaries. Specific operator-to-module bindings deferred to validation pass.

---

## §3. Application Canon — Music-Specific Primitives

All material in this section is sourced from `song_excellence.yaml`. Every primitive has an S#### back-anchor.

### §3.1 Song Excellence Matrix (SEM) — 12 Criteria

**Definition (S2098):** *Song Excellence Governance (SEG) is a scoring + gating framework for excellence decisions, weighted rubric + gates + thresholds + ranked remediation actions.* Applied at M7.

**Scoring:** 0–5 per criterion (S0019–S0030). Binary checks use 0/5 (S0030).
**Composite formula:** `Σ((score_i / 5) × weight_i) / Σ(weights) × 100` → percentage (S1805 M7.1).
**Release threshold:** **≥ 97.5%** per CR-009 (S2117). Supersedes earlier ≥70 (S0816) — explicit conflict logged.

**Criteria table:**

| K# | Criterion | Weight | Min | Snake-key | Source |
|----|---|---:|---:|---|---|
| K1 | Hook Strength | 18% | ≥4 | `hook_strength` | S0804 |
| K2 | Lyric Integrity & Emotional Clarity | 12% | ≥3 | `lyric_integrity` | S0805 |
| K3 | Vocal Delivery & Character | 10% | ≥3 | `vocal_delivery` | S0806 |
| K4 | Melody & Topline Craft | 10% | ≥3 | `melody_topline` | S0807 |
| K5 | Structure & Pacing | 8% | ≥3 | `structure_pacing` | S0808 |
| K6 | Production Quality | 12% | ≥3 | `production_quality` | S0809 |
| K7 | Arrangement Interest & Contrast | 6% | ≥2 | `arrangement_interest` | S0810 |
| K8 | Commercial Viability & Market Fit | 8% | ≥3 | `commercial_viability` | S0811 |
| K9 | Originality / Distinctive Element | 6% | ≥2 | `originality` | S0812 |
| K10 | Metadata & Governance | 4% | ≥3 | `metadata_governance` | S0813 |
| K11 | Lyric Syllable Integrity | 4% | ≥4 | `lyric_syllable_integrity` | S0814 |
| K12 | Pre-release QA Checks | 2% | ≥2 | `pre_release_QA` | S0815 |
| — | **Total** | **100%** | — | — | — |

**K8 canon conflict log:** v5-c MOSAIC v2.2 attempted to rename K8 to *Compression Survivability*; v2.3 to *Visual Coherence*. Both UNFIT per `forensic_v5_diagnostic`. Canon K8 = *Commercial Viability & Market Fit* per S0811. **Resolved.**

### §3.2 Technical UST Schema — 9 Prototype Modules

Per S0822: *Each song session is decomposed into:*

| Module | Canonical fields | Source |
|---|---|---|
| **Theory** | mode, tonal center, meter, tempo, chord color | S0823 |
| **Voice** | register, delivery, expression | S0824 |
| **Style** | genre, era, intent, texture, aesthetic, focus | S0825 |
| **Structure** | intro, verses, choruses, bridge, outro | S0826 |
| **Performance** | pocket, BGVs, call-and-response, phrasing ops | S0827 |
| **Timbre** | drum tone, bass tone, keys, guitar, FX, vocal tone | S0828 |
| **Post** | comp, EQ, space, dynamics | S0829 |
| **Operators** | special FX (chopped & screwed, pitch shifts, etc.) | S0830 |
| **Validators** | lyric lock, metadata commas, syllable guideline, container lint | S0831 |

**Addressing pattern** (consumed at scoring): `{Module}.{field}.{subfield}.{variant}` — implied by live SEG instance at S1873.

### §3.3 Producer-Archetype Personas — 6 Bounded Workforce Modules

Personas are bounded employee modules (per `canonical_employee_module_spec.yaml`, referenced) consuming Mosaic N2 Workforce primitives. Each persona contributes positive (canon-locking) and negative (red-pen blind-spot) notes per SEM criterion.

| Persona | Producer archetype | Strong-on criteria | Flags criteria | Source range |
|---|---|---|---|---|
| **Pop** | Max Martin / Jack Antonoff | K1 K8 K5 | K9 K12 | S0210–S0221 |
| **Country** | Dan Huff / Joey Moi | K2 K3 K5 K10 | K8 K11 | S0222–S0233 |
| **R&B / Soul** | Hitmaka / No I.D. | K2 K3 K6 K7 K9 | K1 K8 | S0234–S0245 |
| **Americana** | Dave Cobb | K2 K3 K5 K9 | K1 K6 | S0246–S0257 |
| **Blues / Stadium Rock** | Rick Rubin | K3 K6 K5 K9 K12 | K1 K2 | S0258–S0269 |
| **Trap / Rap** | Metro Boomin / Hit-Boy | K6 K1 K7 K8 K9 | K2 K11 | S0270–S0282 |

**Activation rule:** Personas activate at M6 (SME round-robin orchestrator, S2086) and provide overlays consumed at M7 scoring.

**Persona ↔ UST module ↔ SEM criterion coupling contract** (the triad bindings — derived from S0210–S0282 + live SEG instance S1873):

```
  R&B persona K3 strength  →  binds to UST.Voice.delivery  →  evidences SEM.vocal_delivery
  Pop persona K1 strength  →  binds to UST.Style.intent + UST.Structure.hook_placement
                            →  evidences SEM.hook_strength
  Trap persona K6 strength →  binds to UST.Post + UST.Timbre.drum_tone + UST.Timbre.bass_tone
                            →  evidences SEM.production_quality
```

Full coupling matrix in §6 (Traceability Matrix).

### §3.4 Active Change Rules — CR-001 through CR-010

All ACTIVE per S2120. Governance binding the triad.

- **CR-001** · Portability over session-locked context *(@S2109)*
    - Change: Create monolithic prompts and artifacts that survive across GPT sessions.

- **CR-002** · Modify “no lyric changes” rule *(@S2110)*
    - Change: Lyric/music creation processes may edit lyrics, other process branches must not.
    - Notes: Governance scope corrected to avoid blocking creation workflows.

- **CR-003** · Replace high-level summaries with atomic task trees *(@S2111)*
    - Change: Every node must break down to task → subtask → audit check → KPI.
    - Notes: This supersedes any “overview-only” outputs.

- **CR-004** · Suno translation awareness becomes first-class *(@S2112)*
    - Change: UST must be optimized for how Suno expands/validates content, including blocked-word collisions.

- **CR-005** · Section header and character waste corrections *(@S2113)*
    - Change: Replace `durationbars:` with `{x} bars`; remove schema labels (`who:`, `mode:`) from headers.

- **CR-006** · Stage direction placement correction *(@S2114)*
    - Change: Stage directions must be `[ ** sFX: ... ** ]` blocks, never quoted `"*(...)*"`.

- **CR-007** · Speaker attribution correction (critical) *(@S2115)*
    - Change: Use `[Lead]` tokens only; ban `[Lead:]` colon labels; choir/BGV are adlibs unless multiple primaries.
    - Notes: Gender alignment elevated to equal importance.

- **CR-008** · Comma restriction elevated to validator policy *(@S2116)*
    - Change: Commas allowed only inside lyric quotes or between quote and adlib.

- **CR-009** · Pass threshold correction *(@S2117)*
    - Change: Reject 70% pass guidance; canon expectation is ~97.5% pass for release-grade gating.
    - Conflict: Earlier assistant guidance used ~70; marked superseded.

- **CR-010** · Decomposer purpose correction *(@S2118)*
    - Change: Chaos-Decomposer exists to extract the real process and enable a monolithic zero-touch prompt artifact, not QA chatter.

### §3.5 G0 Term Taxonomy — Onboarding Vocabulary

Per S2097: *Ensure a new session understands internal terms and why they exist.* Consumed at M13 (context_md_generator) and embedded in M11 zero-touch prompts.

#### SEG (Song Excellence Governance) *(@S2098)*
- **What:** A scoring + gating framework for excellence decisions.
- **Who:** Used by the system as the evaluator layer, informed by SME lenses.
- **When:** After UST normalization and before zero-touch prompt emission.
- **Where:** Inside evaluation pipeline (M7).
- **Why:** To quantify readiness, surface deficiencies, and trigger targeted revisions.
- **How:** Weighted rubric + gates + thresholds + ranked remediation actions.
- **5 Whys:**
    - 1) Why score? To avoid subjective drift.
    - 2) Why weighted? Not all criteria impact outcomes equally.
    - 3) Why gates? Some failures are release-blocking regardless of score.
    - 4) Why ranked deficiencies? To focus iteration on highest leverage fixes.
    - 5) Why portable? To support co-development and reproducible results.

#### G-Card *(@S2099)*
- **What:** A decision artifact summarizing SEG result, top deficiencies, required actions.
- **Who:** Consumed by revision module and by humans for quick go/no-go.
- **When:** Immediately after scoring (M7).
- **Where:** Output artifact and governance ledger.
- **Why:** To capture decisions and make iteration deterministic.
- **How:** PASS/ITERATE/HOLD + atomic required actions + iteration cap.

#### sFX block *(@S2100)*
- **What:** Non-vocal stage direction container.
- **Why:** Prevents stage direction from being treated as lyrics and reduces character waste.

---

## §4. Operational Pipeline — M0–M14 + G0

Sixteen modules execute over the Mosaic N3 (Execution) substrate. Forward path: M0 → M1 → … → M11 (terminal). Sidecars: M12/M13/M14. Onboarding: G0.

**Dependency graph (forward path):**
```
  M0 → M1 → M2 → M3 → M4 → M5 → M6 → M7 ──PASS──→ M9 → M10 → M11 ⇒ SUNO
                                       └──ITER──→ M8 ⥀ (re-score → M7)
                                       └──HOLD──→ operator escalation
  
  Sidecars: M12 (chain_report) ← M1 + M8 + M9
            M13 (context_md)   ← M2 + M3
            M14 (chaos_decomposer) ← any (per CR-010)
  Onboarding: G0 (term_taxonomy) ← M1 + M13
```

### §4.1 M0 — `session_init_and_state_load` *(@S2080)*
- **Purpose:** Load current worklog inputs and initialize state containers.
- **Inputs:** Conversation worklog, pasted specs, any attached artifacts.
- **Outputs:** S_raw_corpus, S_rule_registry, S_change_request_log, S_session_ledger.
- **Dependencies:** None.
- **Atomic steps:**
    - M0.1 Initialize empty state objects.
    - M0.2 Ingest conversation as RAW corpus.
    - M0.3 Detect embedded monoliths/specs and register as artifacts.
    - M0.4 Initialize CR counters and lineage pointers.

### §4.2 M1 — `change_request_handler` *(@S2081)*
- **Purpose:** Detect and apply CRs as governance events with precedence and lineage.
- **Inputs:** S_raw_corpus, S_rule_registry, latest message.
- **Outputs:** Updated S_rule_registry, S_change_request_log.
- **Dependencies:** MODULE-M0.
- **Atomic steps:**
    - M1.1 Detect imperative language and corrections.
    - M1.2 Create CR entry with timestamp and scope.
    - M1.3 Supersede older rules with version tags.
    - M1.4 Fork conflicts with conflict notes.

### §4.3 M2 — `RECA_snapshot_builder` *(@S2082)*
- **Purpose:** Build Requirements, Environment, Constraints, Assets snapshot for deterministic execution.
- **Inputs:** S_raw_corpus, S_rule_registry.
- **Outputs:** S_RECA_snapshot.
- **Dependencies:** MODULE-M0, MODULE-M1.
- **Atomic steps:**
    - M2.1 Extract requirements.
    - M2.2 Extract environment assumptions.
    - M2.3 Extract constraints.
    - M2.4 Extract assets and exemplars.

### §4.4 M3 — `operating_env_snapshot_builder` *(@S2083)*
- **Purpose:** Declare the operating environment assumptions and active tool constraints.
- **Inputs:** S_rule_registry, S_RECA_snapshot.
- **Outputs:** S_operating_env_snapshot.
- **Dependencies:** MODULE-M2.
- **Atomic steps:**
    - M3.1 Identify target generator pipeline (Suno-facing).
    - M3.2 Register active validators and banned patterns.
    - M3.3 Register content moderation sensitivities (blocked-word risk).

### §4.5 M4 — `brief_and_artifact_parser` *(@S2084)*
- **Purpose:** Parse user-provided UST/song/notes into internal structure without leaking schema into output.
- **Inputs:** Raw song input, existing UST structures, S_rule_registry.
- **Outputs:** S_song_struct (normalized internal representation).
- **Dependencies:** MODULE-M1, MODULE-M3.
- **Atomic steps:**
    - M4.1 Parse meta containers.
    - M4.2 Parse Lyrics Block sections.
    - M4.3 Identify speaker attribution elements.
    - M4.4 Identify forbidden formatting (durationbars, colon labels, quoted stage directions).

### §4.6 M5 — `technical_ust_initializer` *(@S2085)*
- **Purpose:** Normalize/repair Technical UST fields into canonical form.
- **Inputs:** S_song_struct, S_rule_registry.
- **Outputs:** A_technical_ust_draft.
- **Dependencies:** MODULE-M4.
- **Atomic steps:**
    - M5.1 Normalize container names and field syntax.
    - M5.2 Enforce performer role declarations (gender alignment readiness).
    - M5.3 Add missing fields required by governance.
    - M5.4 Add Validators container with comma policy and attribution rules.

### §4.7 M6 — `SME_round_robin_orchestrator` *(@S2086)*
- **Purpose:** Apply persona/SME lenses to generate targeted improvements without violating governance constraints.
- **Inputs:** A_technical_ust_draft, Lyrics Block, S_rule_registry.
- **Outputs:** A_revision_suggestions (atomic actions), A_persona_overlays.
- **Dependencies:** MODULE-M5.
- **Atomic steps:**
    - M6.1 Run lyric clarity and structure audit lens.
    - M6.2 Run performance arc and delivery lens.
    - M6.3 Run timbre and mix intent lens.
    - M6.4 Generate atomic remediation actions.

### §4.8 M7 — `SEG_and_G_card_evaluator` *(@S2087)*
- **Purpose:** Score excellence and produce decision artifacts.
- **Inputs:** A_technical_ust_draft, A_revision_suggestions, S_rule_registry.
- **Outputs:** A_SEG_scorecard, A_G_card_decision.
- **Dependencies:** MODULE-M6.
- **Atomic steps:**
    - M7.1 Compute weighted scores per criterion.
    - M7.2 Apply pass threshold policy (canon: ~97.5%).
    - M7.3 Generate ranked deficiencies.
    - M7.4 Emit G-Card with required actions.

### §4.9 M8 — `revision_loop_orchestrator` *(@S2088)*
- **Purpose:** Apply targeted remediations and re-evaluate until pass or iteration cap.
- **Inputs:** A_revision_suggestions, A_technical_ust_draft, S_rule_registry.
- **Outputs:** A_technical_ust_revised, A_revision_log.
- **Dependencies:** MODULE-M7.
- **Atomic steps:**
    - M8.1 Select top deficiency.
    - M8.2 Apply one atomic remediation.
    - M8.3 Re-run validators and scoring.
    - M8.4 Stop at cap or pass.

### §4.10 M9 — `format_and_policy_validator (Suno-focused)` *(@S2089)*
- **Purpose:** Enforce Suno-efficient formatting rules and ban known failure patterns.
- **Inputs:** A_technical_ust_revised (or draft), Lyrics Block, S_rule_registry.
- **Outputs:** A_validation_report (pass/fail + reasons).
- **Dependencies:** MODULE-M5 (minimum), MODULE-M8 (if revision loop enabled).
- **Atomic steps:**
    - M9.1 Fail if `durationbars:` exists anywhere.
    - M9.2 Fail if any colon speaker labels appear (e.g., `[Lead:]`).
    - M9.3 Fail if any quoted stage direction exists (`"*(...)*"`).
    - M9.4 Fail if commas appear outside lyric quotes except `"....", ("...")`.
    - M9.5 Fail if choir/BGV appears as a speaker token without multi-primary declaration.
    - M9.6 Fail if first lyric line is not one line below header (allow optional sFX line in between).
    - M9.7 Flag blocked-word risk terms and propose safe synonyms (non-destructive suggestion).

### §4.11 M10 — `show_summary_generator (strict)` *(@S2090)*
- **Purpose:** Generate short professional directive show summary that matches UST intent.
- **Inputs:** A_technical_ust_revised, Lyrics Block, S_rule_registry.
- **Outputs:** A_show_summary_strict.
- **Dependencies:** MODULE-M9.
- **Atomic steps:**
    - M10.1 Extract genre, tempo, key, performance arc, palette.
    - M10.2 Generate summary with minimal punctuation risk.
    - M10.3 Enforce char budget discipline.

### §4.12 M11 — `zero_touch_prompt_generator_for_SUNO (Critical)` *(@S2091)*
- **Purpose:** Emit the final monolithic prompt artifact that a new session can run.
- **Inputs:** A_technical_ust_revised, A_show_summary_strict, A_validation_report, optional SEG/G-Card.
- **Outputs:** **A_zero_touch_prompt_for_SUNO** (single paste artifact).
- **Dependencies:** MODULE-M9, MODULE-M10.
- **Atomic steps:**
    - M11.1 Compile final UST in canonical containers.
    - M11.2 Compile Lyrics Block with correct headers, sFX blocks, quotes, adlibs.
    - M11.3 Embed validator rules as explicit “must” constraints.
    - M11.4 Emit strict output format contract (UST + Show Summary only).
    - M11.5 Provide “song-in on one side” execution instruction and “outputs shown at end”.

### §4.13 M12 — `chain_report_generator` *(@S2092)*
- **Purpose:** Produce lineage report capturing CRs, decisions, validations, and applied remediations.
- **Inputs:** S_change_request_log, A_validation_report, A_revision_log.
- **Outputs:** A_chain_report.
- **Dependencies:** MODULE-M1, MODULE-M8, MODULE-M9.
- **Atomic steps:**
    - M12.1 List CR evolution.
    - M12.2 Record validator failures and fixes.
    - M12.3 Record final pass conditions.

### §4.14 M13 — `context_md_generator` *(@S2093)*
- **Purpose:** Produce portable context snapshot for new sessions.
- **Inputs:** S_RECA_snapshot, S_operating_env_snapshot, key canon rules.
- **Outputs:** A_context_md.
- **Dependencies:** MODULE-M2, MODULE-M3.
- **Atomic steps:**
    - M13.1 Summarize Requirements and Constraints.
    - M13.2 List canonical formatting rules.
    - M13.3 Define terms (SEG, G-Card, sFX, performer tokens, adlibs).

### §4.15 M14 — `chaos_decomposer_core (v1.6 alignment)` *(@S2094)*
- **Purpose:** When invoked, emit KEY_TERM_TREE, NODE_EDGE_TAXONOMY, MODULE_SEQUENCE_ATOMIC, DELTA_AND_GAPS.
- **Inputs:** Full RAW corpus, rule registry, artifacts.
- **Outputs:** 4-section decomposer output.
- **Dependencies:** MODULE-M0–M13 as needed.
- **Atomic steps:**
    - M14.1 RAW build and tagging.
    - M14.2 NORMALIZED derivation.
    - M14.3 Fractal expansion where grounded.
    - M14.4 Gap minimization with OPEN_QUESTION markers.

### §4.16 G0 — `term_taxonomy_with_5Ws_and_5Whys` *(@S2097)*
- **Purpose:** Ensure a new session understands internal terms and why they exist.
- **Inputs:** Rule registry, artifacts list, CR log.
- **Outputs:** A_term_taxonomy.
- **Dependencies:** MODULE-M1, MODULE-M13.

---

## §5. Gates and Validators

### §5.1 Governance Gates (six total)

| Gate | Source | Check | Critical (AND clause) | Binary |
|---|---|---|---|---|
| `metadata_gate` | S0817 | Required fields present (CREW_TAGS, lyric_version, USTF_version, etc.) | ✓ | ✓ |
| `lyric_syllable_gate` | S0818 | All quoted lyric lines 6-10 syllables (adlibs/SFX excluded) | ✓ | ✓ |
| `hook_gate` | S0819 | Hook Strength score ≥ 4 | — | ✓ |
| `production_gate` | S0820 | LUFS target, no clipping, low-end clarity | — | ✓ |
| `final_qa` | S0821 | Stems exported, ledger updated, release pack ready | — | ✓ |
| `roadmap_gate` | S1805 | RoadMap axis present and section ordering valid | ✓ | ✓ |

**Composite pass condition (S1405):**
```
  composite_pct ≥ 97.5
  AND metadata_complete = true
  AND lyric_syllable_gate = true
  AND roadmap_gate = true
  → SERIALIZE & OUTPUT (proceed to M9)
  ELSE → REMEDIATION (M8)
```

**Gate evolution note:** Early rubric form (S0817-S0821) listed Hook + Final QA as separate gates. Operational form (S1805) folds Hook into Hook Strength criterion scoring; Final QA moves downstream of M7. `production_gate` present operationally but not in named critical-AND clause — needs operator F per §7 open items.

### §5.2 M9 Validator Policy (7 atomic rules @ S2089)

Suno-focused. Any single FAIL blocks validation report from passing. Maps directly to CR-005/006/007/008.

| Rule | Failure condition | Bound CR |
|---|---|---|
| M9.1 | `durationbars:` exists anywhere | CR-005 |
| M9.2 | Any colon speaker labels (`[Lead:]`) | CR-007 |
| M9.3 | Any quoted stage direction (`"*(...)*"`) | CR-006 |
| M9.4 | Commas outside lyric quotes (except `"....", ("...")`) | CR-008 |
| M9.5 | Choir/BGV as speaker token without multi-primary declaration | CR-007 |
| M9.6 | First lyric line not on line immediately below header | (formatting) |
| M9.7 | Blocked-word risk terms (non-destructive flag with synonym suggestion) | CR-004 |

---

## §6. Traceability Matrix

Per established systems-engineering practice: every spec primitive cites source S####; every source concept has a spec destination. This section establishes bidirectional traceability.

### §6.1 Source → Spec (Coverage)

| Source concept | Source anchor | Spec destination |
|---|---|---|
| 12-criterion Song Excellence Matrix | S0803-S0815 | §3.1 |
| Composite scoring formula | S0816, S1405, S1805 | §3.1 |
| Release threshold 97.5% | S2117 (CR-009) | §3.1 |
| 9 UST prototype modules | S0822-S0831 | §3.2 |
| 6 producer-archetype personas | S0210-S0282 | §3.3 |
| CR-001 → CR-010 (10 active rules) | S2109-S2118 | §3.4 |
| SEG framework definition | S2098 | §3.1, G0 in §3.5 |
| G-Card decision artifact | S2099 | §3.5 |
| sFX block | S2100 | §3.5 |
| M0-M14 + G0 pipeline | S2080-S2097 | §4 |
| 6 governance gates | S0817-S0821, S1805 | §5.1 |
| Critical-AND composite condition | S1405 | §5.1 |
| M9.1-M9.7 validator policy | S2089 | §5.2 |
| Live SEG schema instance | S1822, S1873, S1878 | §3.1 (illustrative) |
| Lyric Integrity Lock + LCR flow | S0073-S0109 (CR-002) | §3.4, §5 |
| Persona overlay coupling | S0210-S0282 | §3.3 |
| Tri-Attention application | S0051-S0055 | §7 open items (when to apply) |
| Migration log + CR lineage | S2103-S2130 | §3.4 |
| Scoring scale 0-5 + 0/5 binary | S0019-S0030 | §3.1 |

### §6.2 Spec → Source (Reverse Coverage)

Every §3+ claim above is anchored to S####. No fabricated material. Items derived from cross-references rather than direct extraction are explicitly flagged.

### §6.3 Pre-Canon-Access Artifacts (Historical Record)

Per universal supersession of pre-canon-access material:
- Workspace YAMLs (ws_* × 6) — historical record, recoverable elements migrate per `v5_corrective_regen_prompt`
- Forensic chain (RTFA/SEC/SDG/SLR/MMR) — historical reconstruction; methodology valid, content artifacts superseded by direct canon access
- `substrate_floor_v0.1.yaml`, `forensic_v5_diagnostic_v0.1.yaml` — superseded
- `maestro_consolidation_snapshot_v0.1.yaml`, `maestro_verification_fork_v0.1.yaml`, `open_question_verification_queries_v0.1.md` — superseded; verification fork's 25 paste-ready queries largely resolved directly from canon
- `maestro_on_mosaic_paper_v0.2.md` (DRAFT) — superseded; its claims rest on reconstruction layer
- `maestro_v0.md` (referenced, M0-M11 only) — superseded by current document

---

## §7. Open Items Requiring Operator F

Honest gap list — items where canon is ambiguous, conflicted, or external validation needed.

1. **K11 syllable range** — canon S0818 says 6–10; REPAIR-04 in spine-staging quotes 6–11. Version delta requires reconciliation.
2. **production_gate criticality** — operational at M7.2 (S1805) but not in named critical-AND clause at S1405. Confirm whether release-blocking or warning-only.
3. **Hook Gate disposition** — early rubric S0819 = separate binary gate; M7.2 operational form folds into Hook Strength criterion scoring. Confirm hook-as-criterion-only.
4. **G-Card full state set** — taxonomy S2099 lists PASS/ITERATE/HOLD; live SEG instance (S1873) shows only PASS. Confirm HOLD trigger conditions.
5. **Mosaic v0.1 source validation** — `mosaic_engine_v0_1.md` not loaded; substrate interface in §2 documented-but-unvalidated. Load when available.
6. **Coupling matrix completeness** — §3.3 shows partial Persona↔UST↔Criterion bindings derived from S0210-S0282; full matrix completion deferrable but should be next pass.
7. **Round-trip validation** — programmatic check that every concept in song_excellence.yaml has a destination in this spec. Recommended before release.
8. **Triad output character budgets** — referenced (performer_profile ≤2000, show_summary ≤1000, session_sheet 4950-4995) but verbatim source S#### not yet anchored. Verify.

---

## §8. State Objects and Artifacts (Pipeline I/O)

### §8.1 State containers `S_*` (carried forward across modules)

| Container | Owner | Purpose |
|---|---|---|
| `S_raw_corpus` | M0 | Conversation worklog as raw, untagged input |
| `S_rule_registry` | M0, updated M1 | Rules with version tags and supersession lineage |
| `S_change_request_log` | M0, appended M1 | CR lineage with timestamps and scope |
| `S_session_ledger` | M0 | Append-only ledger of all governance events |
| `S_RECA_snapshot` | M2 | Requirements / Environment / Constraints / Assets |
| `S_operating_env_snapshot` | M3 | Generator pipeline, validators, blocked-word risks |
| `S_song_struct` | M4 | Normalized internal song representation |

### §8.2 Artifacts `A_*` (emitted at module boundaries)

| Artifact | Emitted by | Consumed by |
|---|---|---|
| `A_technical_ust_draft` | M5 | M6, M7 |
| `A_revision_suggestions` | M6 | M7, M8 |
| `A_persona_overlays` | M6 | M7 |
| `A_SEG_scorecard` | M7 | M8, M12 |
| `A_G_card_decision` | M7 | M8 (if iterate), M11 (if pass) |
| `A_technical_ust_revised` | M8 | M9, M10, M11 |
| `A_revision_log` | M8 | M12 |
| `A_validation_report` | M9 | M10, M11, M12 |
| `A_show_summary_strict` | M10 | M11 |
| **`A_zero_touch_prompt_for_SUNO`** | **M11 (TERMINAL)** | External (Suno session) |
| `A_chain_report` | M12 | Historical record |
| `A_context_md` | M13 | Onboarding new sessions |
| `A_term_taxonomy` | G0 | M13 |

---

## §9. Mount Contract — Maestro v0 ↔ Mosaic v0.1

**Boundary discipline:** No music-specific content in Mosaic v0.1; no Mosaic substrate concerns in Maestro v0.

### §9.1 Maestro v0 → Mosaic v0.1 (what Maestro consumes)
- Substrate layers N1–N8 (per §2.1)
- 10 kernel invariants (INV-08 confirmed load-bearing; others documented-not-validated)
- 16 cognitive operators (documented-not-validated)
- ATP (Air-gapped Transfer Pack) primitive for CR-001 portability
- CINR (Causal-trace replay) primitive for M12 chain reports
- Replay-governed canon discipline

### §9.2 Mosaic v0.1 ← Maestro v0 (what Maestro provides)
- Application-domain canon (this document)
- Music-specific personas as N2 Workforce instances
- Music-specific CRs (CR-001 through CR-010) loaded into N4 Canon layer
- SEG framework as N5 Admissibility instance
- M0–M14 + G0 as N3 Execution instance
- Triad output (performer_profile / show_summary / session_sheet) as N7 Output instance

### §9.3 No-Crossing Rules (anti-cross-contamination, derived from v5-c failure analysis)
- Mosaic substrate spec MUST NOT reference music criteria, syllable rules, persona archetypes, Suno-specific validators.
- Maestro v0 application spec MUST NOT redefine substrate primitives (ATP, CINR, Replay, kernel invariants).
- Any document conflating these is per-definition v5-c-class failure and gets reclassified to historical record.

---

## §10. Validation and Acceptance

### §10.1 Lossless-recovery validation criteria

Per established methodology, lossless = every concept in source has a destination in derived. Verification approaches:

- **Coverage check (programmatic):** Walk all 2,131 S#### sections; flag any concept with no spec destination. Recommended automated pass.
- **Round-trip check (programmatic):** From this spec, reconstruct a structural skeleton; diff against source. Recommended automated pass.
- **Operator validation (human):** Senior operator reads this spec; identifies missing or wrong material. Required for canon acceptance.

### §10.2 Acceptance gate

This document remains DRAFT until:
1. Operator F on each §7 open item
2. Mosaic v0.1 source validation (§2 unblocks)
3. Lossless-coverage check passes
4. Coupling matrix §6 completes

Upon acceptance: this becomes the operative Maestro v0 application specification. The forensic-chain reconstruction artifacts move fully to historical record per universal supersession.

---

## Document metadata

- **Source primary:** `song_excellence.yaml@v5.0.2-dedup-kernel`, 2,131 sections, S0001-S2131
- **Reformatted artifacts:** `song_excellence_reformatted.md`, `song_excellence_sections.txt`, `song_excellence_sections.json`
- **Architectural extract:** `architecture.json` (structured), `song_excellence_architecture.md` (narrative)
- **View artifacts:** `views/01_pipeline.puml`, `02_seg_state_machine.puml`, `03_rubric_matrix.puml`, `04_cr_lineage.puml`
- **This document supersedes:** `maestro_v0.md` (incomplete M0-M11), pre-canon-access workspace artifacts, forensic chain reconstructions (as content; methodology remains valid)
- **Awaiting source validation:** `mosaic_engine_v0_1.md` for §2 substrate interface verification

**Methodology citation:** Requirements traceability + lossless concept-to-destination mapping is established systems engineering (NASA SE Handbook NPR 7123.1; software engineering literature 1970s onward including Yourdon/DeMarco structured analysis, Chen ER modeling, Sowa conceptual graphs). Not a novel technique — applied here to session-transcript-to-architecture transform.