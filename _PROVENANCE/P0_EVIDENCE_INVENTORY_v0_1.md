# P0 Evidence Inventory — v0.1
**Scope:** Pass-0 of the retroactive reconstruction protocol. Inventory and ordering only. No interpretation, no fold, no new doctrine. Every entry below is either OBSERVED (verified on disk this session, 2026-07-16) or FLAGGED (needs operator confirmation).
**Operator:** Mo (DJ Mo Money / The Architect)
**Compiled:** 2026-07-16, Cowork session (Fable), from connected folder `maestro-on-mosaic`

---

## 1. Evidence timeline (oldest → newest)

Dating basis: filename-embedded dates and internal content. **File mtimes are unreliable** — a mass copy on 2026-06-18 flattened most timestamps (FLAGGED, see §5.3).

| # | Date | Evidence | Location |
|---|---|---|---|
| T01 | 2025-05-07 | Song-review conversation (Suno v4.5 config bundle) | `sessions/D-Maestro/maestro-ai-music-system*/source/distributed/suno_v45_config_bundle_v3/conversation_-2--song-review_2025-05-07-0505.agi.md` |
| T02 | 2025-09-22 | OS-dev sessions (3 files, incl. 1.3MB dev transcripts) | `sessions/D-Maestro/.../legacy/conversation_untitled_2025-09-22-1358.agi.json`; `sessions/E-scatter/maestro/conversation_os-dev_2025-09-22-1447.agi.json`, `..._2025-09-22-1602.agi.md` |
| T03 | 2025-11-14 | OS-core session | `sessions/D-Maestro/.../legacy/conversation_os-core_2025-11-14-0539.agi.json` |
| T04 | 2025-12-24 | CHIMERA V2 system state + dialogue ledger; Maestro devsession (AI-optimized) | `sessions/D-Maestro/.../CHIMERA_V2_SYSTEM_STATE_2025-12-24/dialogue_ledgers/maestro.devsession.iterative.txt.ledger.md`; `sessions/OneDrive-v45/maestro_devsession.ai_optimized.md` |
| T05 | 2026-01-06 | UST session | `sessions/OneDrive-v45/session-ust.txt` |
| T06 | undated (legacy era) | Iterative devsession; v5 UST+SEM sessions; Gemini Gem iterative-design export | `sessions/D-Maestro/Maestro/maestro.devsession.iterative.txt`; `.../legacy/maestrov5-dev-ust and sem-sessions.txt` (704KB); `.../legacy/maestro-os-v4.x-baseline-001/oldMaestroGeminiGem...Export.txt` |
| T07 | 2026-03-28 / 03-30 | Eldrik sessions (3.5MB each, 4 files) — contains the operator's raw standing instruction on detail loss (§4.2, E1) | `sessions/D-Maestro/sources/conversation_maestro-chat---eldrik*_2026-03-28/30-*.agi.md/json`; source copy `artifacts/D-Maestro/sources/eldrik.txt.txt` |
| T08 | 2026-04-03 | Clarity session (3.3MB); FOIL-based tiered system session (890KB) | `sessions/D-Maestro/maestro-ai-music-system/dev-chats/conversation_maestro-chat---clarity_2026-04-03-1250.agi.md`; `sessions/D-Maestro/sources/conversation_foil-based-tiered-system_2026-04-03-1252.agi.md` |
| T09 | 2026-04 or 2026-05-12/13 (FLAGGED, §5.1) | **claud2.txt** — INV-17 / INV-18 / Revised INV-18 / INV-19 / INV-20 / phantom-commitment / kernel session | `artifacts/D-Maestro/archive/maestro_v3_documents051226-05142026/claud2.txt` (dup: `artifacts/D-Maestro/sources/claud2.txt`) |
| T10 | 2026-05-12 → 05-14 | v3 reconstruction window: claud3 (+window copies), session13 window1/2 (R-INV-07 [FIRM], R-RT-PD-01 [FIRM]), maestro5 report, EQ-0001/0002 extraction passes, TRACE_MAP, lossless transfer package v0.2 | `artifacts/D-Maestro/archive/maestro_v3_documents051226-05142026/` |
| T11 | 2026-05-15 | claude-session051526 (SEM forensic session; "Lossless process substrate; do not compress") | `artifacts/D-Maestro/sources/claude-session051526.md`, `-window1.txt.txt`, `.oxps` |
| T12 | 2026-05-20 | v5 spine staging workspace | `artifacts/D-Maestro/sources/ws_claude-project_v5-spine-staging_2026-05-20.yaml` |
| T13 | ~2026-06-18 | Mass consolidation into this folder (mtime flattening event) | folder-wide |
| T14 | 2026-06 → 07 | Cowork workspace sessions (readable transcripts, order TBD): "Maestro workspace forensic reconstruction", "Maestro/MOSAIC build harvest", "Maestro MVP buildable substance", "Project Maestro folder cleanup", "Cowork session continuation" | Cowork session history (not in this folder) |
| T15 | 2026-07-08 / 07-09 | README.md, MOSAIC_system_architecture.svg, _PROVENANCE/INDEX.json; style-library.md (560KB) | repo root; `_PROVENANCE/` |
| T16 | 2026-07-11 / 07-13 | style_library_assessment_v0_1; latest artifact/styles/system/untracked touches | repo root and subdirs |
| T17 | 2026-07-16 | **This session:** corrected operating model; mutations M1–M5 recorded (see §6) | Cowork transcript |

Referenced by SKILL.md provenance but **not located as named**: session `b9f69085` (May 2026 SEM — likely = T11), session `b161088a` (Eldrik Python parse — likely relates to T07/`code/forensic-pipeline`). FLAGGED for mapping.

## 2. Artifact registers (state snapshots, each with an "as-of" position)

- **Canon register** — `artifacts/D-Maestro/canon/`: `Maestro_v5c_Canonical_Root.md`, `Maestro_v5c_Canonical_Spine.md`, `Maestro_v5c_Lineage_and_Delta_Ledger.md`, `Maestro_v5c_Conflict_and_Open_Question_Register.md`, `master.project.json`, `MoMoney Maestro OS v4.5.2 — MONOLITHIC PROMPT.md`, `SONG EXCELLENCE GOVERNENCE files.zip`, KB heuristics.
- **Drafts register** — `artifacts/D-Maestro/drafts/` (39 files): incl. `cumulative_deltas_qaf.md` (**Q-A-F provenance ledger — existing mutation-ledger practice, Apr 2026 span**), `mosaic_engine_v0.1.md`, `maestro_v0.md`, `sem_layer_resolution.md`, `morris_matrix_resolution.md`, `substrate_dependency_graph_v0.1.md`, `substrate_floor_v0.1.yaml`, `03_WHY_AI_DEFAULTS_HERE.md` (see §3), session transfer packs v0.1/v0.2, `canon_enforcement_kit.md`.
- **HYDRA register** — `artifacts/HYDRA/`: v5c execution scaffold/metaprompts, `CHIMERA_CORE_PROMPT_v3.1.4.md`, day-2 authoritative ledger closeout, workspace fingerprint/schema.
- **Runtime patch register** — `artifacts/C-Downloads/`: `MAESTRO_ADMIN_*RUNTIME_REPAIR_002/003`, `CORRECTIVE_PATCH_BOOT_STATE_NORMALIZER_007`, `ALL_IN_ONE_RUNTIME_PATCH_006`, `MAESTRO_CANONICAL_MANIFEST.yaml`, `MAESTRO_END_TO_END_PROCESS_TREE.yaml`, bootstrap/transfer/resurrection zips.
- **Contracts** — `artifacts/extracted_contracts/`: controller contract + lockout policy.
- **Workspace identity specs** — `artifacts/D-Maestro/sources/ws_*.yaml` (8 files, incl. `ws_maestro_mosaic_forensic_claude_v1.0.yaml` with `hidden_substrate_erasure` defect record).
- **Forensic tooling** — `code/forensic-pipeline/python/fold_laminate_v0_1.py` (sole extractor); `code/style_library_parser_v0_1.py`.
- **Provenance infra** — `_PROVENANCE/INDEX.json` (1.5MB, 2026-07-08), `DEDUP_MANIFEST.json`.
- **Song/fixture material** — `artifacts/aisonggenerator/` (manifest.csv, PROVENANCE.md, songs/), `style-library.md`, `styles/`, media.
- **External surfaces (added 2026-07-16, M10/M11)** — claude.ai projects "MoMoney Studios Design System" + "Copy of…" (incl. `campaigns/run-it-to-me/Cover Directions.html` — the three Ayo covers). Outside this folder and Cowork history; import pending (OPEN O-12).

## 3. Verification finding P0-a — skill package is a skeleton (OBSERVED)

Installed skill `maestro-forensic-transcript` contains **only SKILL.md**. Of the 10 components its loading order mandates:

| Component | Status |
|---|---|
| 00_OPERATOR_ABOUT_ME.md | **MISSING** — not found anywhere in folder |
| OPERATOR_CONTEXT.md | **MISSING** |
| 01_METHODOLOGY.md | **MISSING** |
| 02_FAILURE_MODES.md (18 failure modes — "most important file") | **MISSING** |
| 03_WHY_AI_DEFAULTS_HERE.md | **EXISTS as draft** — `artifacts/D-Maestro/drafts/03_WHY_AI_DEFAULTS_HERE.md` (never packaged) |
| 04_KERNEL.md | **MISSING** |
| 05_WORKFLOW.md (W0–W9) | **MISSING** |
| patterns/ | **MISSING** |
| python/ | **PARTIAL** — only `fold_laminate_v0_1.py` in `code/forensic-pipeline/python/` |
| examples/ | **MISSING** |

Consequence: every session that "loaded the skill" received the operating contract but not the failure-mode catalog, kernel, workflow, or extractors. The skill instantiates its own documented failure mode (skeleton file: classification without instance). `.claude/skills/` in this folder is empty.

## 4. Verification finding P0-b — origin of the structured-vs-conversational instruction (OBSERVED)

**Lineage (4 generations):**

1. **E1 — Operator raw standing instruction** (Mar 2026, T07) — `artifacts/D-Maestro/sources/eldrik.txt.txt` ~L64399: *"You are optimized to read the initial x number of characters, the first and last x number of characters, look for structure (i.e. headers, lists, outlines, etc...). You maintain context windows by summarizing… SO MUCH DETAIL WAS DROPPED OVER SESSIONS THAT BY THE END WHAT I THOUGHT WAS A FULLY DEVELOPED, REAL WORLD STRESS TESTED MODULE WAS NOT."* (AI restatement at ~L64462.)
2. **E2 — INV-18 AUTHORITY ASYMMETRY** (T09) — `claud2.txt` byte ~252,444: *"Human turns have root authority. AI turns have proposal authority only… the system drifts toward confident AI language instead of human intent…"*
3. **E3 — Revised INV-18 WITH INFLUENCE ACKNOWLEDGMENT** (T09) — `claud2.txt` byte ~255,834: *"Human turns hold root authority over intent and canon. AI turns hold influence over the operator's working model… Neither can be discarded during re-read… Flag phantom commitments as model corruptions."* Includes the re-read protocol (the functional anti-erasure mechanism; no document literally titled "anti-erasure protocol" exists in this folder).
4. **E4 — Locked FIRM rules** (T10) — `claud3.txt` / `claude-session13-window*.txt`: `R-INV-07 [FIRM]` (authority asymmetry), `R-RT-PD-01 [FIRM]` (phantom-commitment detection, pre-emit).

**Operator intent clarification (2026-07-16, authoritative):** this lineage is a **precedence rule** (conversational operator input outranks structured AI output on conflict) plus a **coverage rule** (chunking/parsing must not drop operator deltas — SEM, FOIL, phases, agent interactions). It was **never an action limiter**. Any session where it was read as "be passive / don't produce" misapplied it; replay must audit for suppressed outputs.

**Missed propagation (OBSERVED):** SKILL.md operating contract #2 carries **original INV-18 only**. Revised INV-18 (E3) never propagated into the skill artifact. Supporting chunking-loss evidence: `claude-session13-window2.txt` byte ~107,529 (*"you can't parse or chunk it. that's why your failing…"*); `claude-session051526.md` (*"Lossless process substrate; do not compress"*); `maestro5 report.txt` (recovering skipped lines 22,764–22,964).

## 5. Discrepancies and open items — RESOLVED 2026-07-16 via elicitation rounds 1–2 (see LEDGER.md DEC-01..06)

1. **claud2.txt dating → DEC-01:** April 2026 session, exported May 12–14. SKILL.md provenance gets annotated at skill rebuild (OPEN O-01).
2. **Duplicates → DEC-02:** per DEDUP_MANIFEST.json, primary = `artifacts/D-Maestro/sources/`; archive copies = dated-context duplicates. Also established: `claud3.txt` ≡ `claud3-window1.txt` ≡ `claude-session13-window1.txt`.
3. **mtime flattening:** confirmed consolidation artifact (M7 — multi-PC/OneDrive merge); internal dates authoritative.
4. **Session IDs → DEC-04:** verify from content during P1 (OPEN O-04).
5. **Missing skill components → DEC-03:** possibly extant on other machines/accounts; operator searching via `SKILL_FILES_SEARCH_CHECKLIST.md` (OPEN O-03). Partial recovery: operator KERNEL.md (2026-05-20) extracted from `archive/im_dead_kb.zip` → `recovered/`.
6. **Cowork transcripts → DEC-05:** extraction runs next, before P1 (output: `T14_extractions/`).

## 6. This session's mutation records (2026-07-16 — seed for LEDGER)

- **M1** [authoritative] Dialogue is not a persistent mutation engine; state exists only when externalized. Prior sessions = evidence-grade mutation record, not applied state.
- **M2** [authoritative] "Canon" = reconciled working state (fold of events), not doctrine document. Converges with existing fold definition.
- **M3** [accepted, unpersisted] Session-conclusion requirement: six E's (extension, enhancement, exemplification, explanation, impact propagation, application re-optimization).
- **M4** [authoritative] INV-18 lineage (§4) = precedence + coverage rule, NOT action limiter. Replay must include per-chunk operator-delta coverage checks and audit for wrongly suppressed outputs.
- **M5** [observed, confirmed §3] Skill package skeleton: 9 of 10 components missing.

## 7. Next pass (not started)

P1 delta extraction, oldest→newest, per timeline §1 — mechanical parse, overlapping chunks, per-chunk operator-delta counts reconciled against full text (M4 coverage control). Requires resolution of §5.2 (primary copies) first.

*End of P0. Inventory only — nothing above alters Maestro runtime canon.*
