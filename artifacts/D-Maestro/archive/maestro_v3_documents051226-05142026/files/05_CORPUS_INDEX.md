# 05_CORPUS_INDEX

Mapping of files in the dev workspace, their roles, and authority levels. Use this when working with the corpus.

---

## 1. Zip groupings (files 1–6 per operator framing)

| Group | Zip | Date | Files | Phase classification |
|---|---|---|---|---|
| 1 | files.zip | 2026-04-12 18:19 | maestro.md (kernel v1.1) · executor_window.md · controller_window.md · session_handoff_2026-04-11.md · ip_vault_extraction_v0.md | MAESTRO_SPECIFIC / ancestor baseline |
| 2 | files2.zip | 2026-04-12 18:36 | maestro_canon_v4_5_2.md · knowledge.md · skills.md · canon_enforcement_kit.md · maestro_knowledge_spine.md · session_handoff_2026-04-12.md | MAESTRO_SPECIFIC / ancestor baseline |
| 3 | files3.zip | 2026-04-12 18:52 | maestro_v5c_bootstrap.md · MAESTRO_V5C_COLDSTART_BOOTSTRAP.md · MOSAIC_system_architecture.svg · BASELINE_RECONSTRUCTION_LEDGER_v0.1.docx | MAESTRO_SPECIFIC / ancestor baseline (pre-substrate; MOSAIC SVG is visualization style only at this point) |
| 4 | files4.zip | 2026-04-27 23:54 | mosaic_maestro_transfer_pack.md · tangent_resumption_2026-04-27.md | SUBSTRATE_AWARE / split / tangent / bridge |
| 5 | files5.zip | 2026-04-28 00:38 | mosaic_engine_v0.1.md · maestro_v0.md · cumulative_deltas_qaf.md | SUBSTRATE_AWARE / candidate emergence |
| 6 | files6.zip | 2026-04-28 22:31 | substrate_dependency_graph_v0.1.md (SDG.v0.1) · substrate_edge_confirmation_v4.5.md (SEC.v4.5) · sem_layer_resolution.md (SLR.v0) · council_matrix_archaeology.md (CMA.v0) · morris_matrix_resolution.md (MMR.v0) · reasoning_trace_forensic_audit_v0.md (RTFA.v0) · (carried) mosaic_engine_v0.1.md · maestro_v0.md · cumulative_deltas_qaf.md | SUBSTRATE_AWARE / current forensic / control / V&V |

**Verification:** Per WRVV §3, files5 contents are bit-identical inside files6. files6 adds the forensic verification layer, does not revise files5 candidates.

---

## 2. Controlling artifacts (per WRVV §8)

| Domain | Controlling artifact | Authority basis |
|---|---|---|
| Source-gap inventory (frozen) | SOURCE_GAP_LIST_v0.1 | Operator: ACCEPTED current control. **NOTE: file not present in `/mnt/project`.** |
| Council / matrix lineage / Morris | CMA.v0 | Operator: controls this domain |
| Substrate dependency graph (working) | SDG.v0.1 | Operator: working dependency graph (not final substrate canon) |
| Layer 5 SEM internal architecture | SLR.v0 | Operator: current Layer 5, patched by CMA/MMR |
| Morris Matrix (purpose/position/mechanism) | MMR.v0 | Operator: PROVISIONALLY RESOLVED only |
| Edge confirmation against primary v4.5 corpus | SEC.v4.5 | Self-declared method; cited by SDG.v0.1 |
| Original session reasoning audit | RTFA.v0 | Self-declared; partially superseded by SDG.v0.1 |
| Q-A-F provenance audit trail | cumulative_deltas_qaf.md | Self-declared; binds Mosaic + Maestro v0 specs to operator-confirmed deltas |
| Substrate runtime specification | mosaic_engine_v0.1.md | CANDIDATE runtime frame |
| Music application specification | maestro_v0.md | CANDIDATE product frame |
| Wiring V&V chain | WIRING_RECOVERY_V_AND_V_v0.md | Operator declaration: ORIENTATION / V&V |

---

## 3. Reference layers (not controlling, useful)

| Category | Files |
|---|---|
| Canonical ancestors | MoMoney_Maestro_OS_v4_5_2___MONOLITHIC_PROMPT.md · MoMoney_Maestro_OS_Knowledge_Base_Heuristics.md · maestro_canon_v4_5_2.md |
| Knowledge / skills registries | knowledge.md · skills.md · canon_enforcement_kit.md · maestro_knowledge_spine.md |
| Output format specs | 02_TECHNICAL_UST_CANONICAL.txt · 03_CREATIVE_UST_CANONICAL.md |
| Persona corpus | Maestro_Personas_aka_the_subagents.md (128 KB) |
| Research dossiers | MAESTRO_v5_Dossier_v0_2_Reverse_UST.md · MAESTRO_v5_Dossier_v0_3_Stylebook.md · MAESTRO_v5_VIG_SEL_Research_Dossier.md |
| Operator session windows | today-dev_chat_window.md (729 KB) · today-work_window.md (377 KB) · longDevWorkLog.txt (342 KB) · Yesterday.md · session-ust.txt · todays_iterative_session_md.ajson |
| Operator memory / character | clarity_architect_ii__AKA_claire_itty__birth_certificate.txt (559 KB) · claude_sem_ust_persona_maestro_patent.txt (332 KB) |
| Forensic / handoffs | ip_vault_extraction_v0.md · controller_window.md · executor_window.md · session_handoff_2026-04-11.md · session_handoff_2026-04-12.md |
| FOIL / tiered system | conversation_foil-based-tiered-system_2026-04-03-1252.agi.md |

---

## 4. Diagnostic-only assets (never canon)

| Asset | Role |
|---|---|
| MOSAIC_v2_2.png | Architecture visualization |
| maestro_on_mosaic.png | Architecture visualization |
| mosaic_v23_aka_maestro_v0.png | "Candidate for Release" diagram |
| ChatGPT_Image_Apr_24_2026_03_09_06_AM.png | Narrative artifact "Maestro: The Middle" |
| ChatGPT_Image_Apr_16_2026_10_35_59_PM.png | Earlier diagram, role not surfaced |
| 35d889eb2f8840fbbb9f3136d2103685.png | Hash-named, no metadata |
| b6837cad2e0e4467a7663a6a4b616fdb.png | Hash-named, no metadata |
| MOSAIC_system_architecture.svg | Pre-substrate-formalization visualization |
| USTF_Consolidated_6Page_Report.pdf | Reference doc, not inspected |

Per WRVV §10: treating diagrams as canon is FORBIDDEN. Diagrams are diagnostic only.

---

## 5. Source-role classification (per birth certificate §II.3.1)

When working any source, classify before use:

| Role | Definition | Authority Level |
|---|---|---|
| `decides` | Source authoritatively settles a question | T1 (operator-confirmed) or T2 (corpus-direct) |
| `informs` | Source provides relevant evidence | T2 or T3 |
| `exemplifies` | Source demonstrates a pattern | T3 |
| `contrasts` | Source illustrates by counter-example | T3 |
| `preserves_lineage` | Source records evolution but not current canon | T3 |
| `exposes_failure` | Source documents a failure mode | T2 or T3 |

A source can be useful without being authoritative.

---

## 6. Authority hierarchy (when sources conflict)

1. T1 operator framing (current session)
2. T1 operator framing (prior, captured in cumulative_deltas_qaf.md)
3. WRVV §10 forbidden actions
4. SOURCE_GAP_LIST_v0.1
5. T2 readable from files (files6 control pack)
6. T2 readable from files (files4–5 candidate / split)
7. T2 readable from files (files1–3 ancestor)
8. Birth certificate Zero-Day Restore Pack §V (Claude-side restore canon)
9. T3 candidates / proposals / research dossiers
10. AI-generated synthesis (orientation only)
11. Diagrams (never canon)

---

## 7. Session typology (per birth certificate line 4891)

| Session type | Example | Extraction posture |
|---|---|---|
| Architecture-discussion | today/yesterday sessions | Highest density of rule content; worldbuilding incidental |
| Orchestration-refinement | Day 2 | Protocol and process content; world-entities operational not narrative |
| Meta-reflection | Day 3 | Commentary on prior sessions; useful for provenance |
| Staff-perspective | eldrik/ | Dense worldbuilding; entity voice and relationship content; simulation commenting on itself from inside |
| Production session | song generation sessions | Source for behavior and outputs |
| Handoff session | session_handoff_*.md | Diff before trust |
| World session | unhinged-gls / worldbuilding | Preserve entities and events |

Per Zero-Day Restore Pack §9, each branch needs different extraction posture.

---

## 8. Three-stream extraction targets (per Zero-Day Restore Pack §8)

For any session being mined, produce three parallel streams:

- **W (World):** entity | type (label/artist/staff/room/artifact) | first appearance | description | relationships | current status
- **E (Events):** event | session/turn | trigger (ideation/failure/decision) | participants | outcome | architectural consequence
- **R (Rules):** rule | originating event | coupled rules | tier | source role classification

Hierarchy: W constrains E. E reveals R. R is recovered, not imposed first.

---

## 9. Quick lookups

**Looking for...**
- Kernel invariants → `maestro.md` v1.1 (18 invariants)
- Substrate runtime invariants → `mosaic_engine_v0.1.md` (10 invariants, CANDIDATE)
- Worker definitions → `Maestro_Personas_aka_the_subagents.md` (128 KB, search ai_personas content)
- Output format → `02_TECHNICAL_UST_CANONICAL.txt`, `03_CREATIVE_UST_CANONICAL.md`
- Output law (Suno) → `maestro_v0.md` "Suno output law" section
- V&V status → `WIRING_RECOVERY_V_AND_V_v0.md`
- Frozen gaps → `SOURCE_GAP_LIST_v0.1` (when present); fallback to WRVV §9
- Q-A-F provenance log → `cumulative_deltas_qaf.md`
- Layer 5 SEM architecture → `sem_layer_resolution.md`
- Executive committee / Morris Matrix → `morris_matrix_resolution.md`
- Council / matrix lineage → `council_matrix_archaeology.md`
- Substrate dependency edges → `substrate_dependency_graph_v0.1.md` + `substrate_edge_confirmation_v4.5.md`
- Operating frame canon → `clarity_architect_ii__AKA_claire_itty__birth_certificate.txt` §II + §V
