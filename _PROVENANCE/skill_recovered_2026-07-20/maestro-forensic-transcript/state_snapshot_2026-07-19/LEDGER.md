# LEDGER — Mutation Record (append-only)
Method-level ledger per the future session mutation protocol. Human turns = root authority; AI entries = proposal until operator-accepted. Never rewrite an entry — supersede by pointer. Runtime canon (UST/SEM/SEG/FOIL) is NOT modified by entries typed `method`.

Entry fields: id · date · author · type (correction/extension/enhancement/example/explanation/defect) · scope (method/runtime/reconstruction) · status (proposed/accepted/authoritative/operative/superseded/rejected/unresolved) · origin (verbatim or pointer) · impacts · artifacts-to-patch · validation.

---

## M1 — Dialogue is not a persistent mutation engine
2026-07-16 · operator · correction+explanation · method · **authoritative**
Origin: session 2026-07-16, opening statement ("I understood each AI session as beginning with an initial working state that was progressively mutated…I now understand that this assumption was at least incomplete").
State exists only when externalized (files consumed next session). Prior sessions = evidence-grade mutation record, not applied state.
Impacts: weighting of all prior summaries/artifacts; inter-session handoff method. Validation: P1 replay will surface losses caused by the old assumption.

## M2 — Canon = reconciled working state (fold of events), not doctrine document
2026-07-16 · operator · clarification · method · **authoritative**
Origin: "Canon meant the reconciled working state produced by the session."
Converges with existing fold definition (SKILL.md: "Canon at version N is the fold of all events up to N"). No contradiction.

## M3 — Session-conclusion requirement: the six E's
2026-07-16 · operator · extension · method · **operative** (persisted here + STATE.md)
Origin: "Each meaningful session should result in some combination of: Extension… Enhancement… Exemplification… Explanation… Impact propagation… Application re-optimization."
Impacts: end-of-session reconciliation; continuation packet format. Artifacts-to-patch: future skill revision.

## M4 — INV-18 lineage = precedence + coverage rule, NOT action limiter
2026-07-16 · operator · correction (of prior mutation's interpretation) · method · **authoritative**
Origin: "it was never intended to prevent or limit the ai from action… when it chunked and parsed it was missing hundreds of lines of changes (i.e. sem, foil, phases and agent interactions)."
Lineage located (P0-b): E1 eldrik.txt.txt ~L64399 (Mar 2026 raw standing instruction) → E2 INV-18 (claud2.txt ~b252444) → E3 Revised INV-18 + re-read protocol (claud2.txt ~b255834) → E4 R-INV-07 [FIRM] + R-RT-PD-01 [FIRM] (claud3/session13, May 2026).
Impacts: replay must run per-chunk operator-delta coverage checks; audit prior sessions for wrongly suppressed outputs. Artifacts-to-patch: SKILL.md carries original INV-18 only — Revised INV-18 never propagated (missed-propagation instance). Skill cache is read-only → patch = new skill version (reconstruction target). Validation: none pending on intent (operator self-statement is final); wording annotation pending skill rebuild.

## M5 — Skill package is a skeleton (9 of 10 components missing)
2026-07-16 · AI-observed, operator-confirmed · defect · reconstruction · **confirmed**
Evidence: installed skill contains only SKILL.md; corpus search found only `drafts/03_WHY_AI_DEFAULTS_HERE.md` + `code/forensic-pipeline/python/fold_laminate_v0_1.py`.
Update 2026-07-16: `_PROVENANCE/recovered/KERNEL_from_im_dead_kb_2026-05-20.md` recovered from `archive/im_dead_kb.zip` — ancestor candidate for 00_OPERATOR_ABOUT_ME.md / 04_KERNEL.md. Remaining components: pending operator search (DEC-03), then reconstruction from forging transcripts (T09–T11).

## M6 — Elicitation protocol
2026-07-16 · operator · extension · method · **operative** (in effect this session)
Origin: "it is much easier to respond to questions (as many as needed up to 15) when presented with context and multiple choice and an other fill box in batches of 3-5 in an interactive format."
Rule: operator decisions elicited via interactive multiple-choice + Other, batches 3–5, ≤15/round, context attached. Never a page of prose questions.

## M7 — Multi-machine consolidation provenance
2026-07-16 · operator · explanation · method · **authoritative**
Origin: "i had multiple pc's and windows accounts from school, work and home with onedrive and profile sync. the folder was an attempt to get everything in oneplace."
Impacts: duplicates/mtime flattening are expected consolidation artifacts, not errors; "missing" files may exist on other machines/accounts (drives DEC-03).

---

## Decisions (operator-answered, elicitation rounds 1–2, 2026-07-16)

- **DEC-01** claud2.txt dating: BOTH — April 2026 session, exported May 12–14. SKILL.md provenance line needs annotation (not deletion) at next skill rebuild.
- **DEC-02** Primary copies: per `_PROVENANCE/DEDUP_MANIFEST.json` → `artifacts/D-Maestro/sources/` is primary citation target; `archive/maestro_v3_documents051226-05142026/` copies are dated-context duplicates. Manifest also establishes: `claud3.txt` ≡ `claud3-window1.txt` ≡ `claude-session13-window1.txt` (one file, three names).
- **DEC-03** Missing skill files: possibly extant on other PCs/OneDrive accounts. Operator searches via `_PROVENANCE/SKILL_FILES_SEARCH_CHECKLIST.md`; those files are not reconstructed until search concludes (found originals outrank reconstruction).
- **DEC-04** Session IDs b9f69085 / b161088a: verify from content during P1 — do not assume proposed mapping (b9f69085≈T11, b161088a≈T07-parse).
- **DEC-05** Next work: T14 Cowork transcript extraction precedes P1 replay of the older corpus.
- **DEC-06** Method/state files live in `_PROVENANCE/` (this directory), separate from runtime canon.

## T14 execution record (DEC-05) — 2026-07-16
Five Cowork transcripts extracted to `T14_extractions/`, each with verbatim operator turns and coverage line (all 5 = full coverage, no truncation): `970d0a6b_forensic_reconstruction.md` (1 user turn, 12 candidate mutations), `bda23828_build_harvest.md` (4 turns incl. 1 machine-injected skill payload flagged, 18 CM: 7 accepted), `fc16fb1a_mvp_buildable_substance.md` (1 turn, 9 CM), `c6dfad39_folder_cleanup.md` (13 turns, 13 CM), `63122c11_cowork_continuation.md` (4 turns + 3 AskUserQuestion-mediated decisions, 7 CM). Candidate mutations remain PROVISIONAL until P2 classification.

## M8 — Coverage rule must include tool-mediated operator decisions
2026-07-16 · AI-observed · enhancement · method · **proposed** (needs operator acceptance)
Finding: AskUserQuestion answers do not render as user turns in transcripts — operator decisions made through interactive elicitation are invisible to a user-turns-only coverage count. Proposed rule: extraction and coverage checks must additionally enumerate tool-mediated operator decisions (cited via the assistant turn that carries them), marked [mediated], never paraphrased as verbatim.

## M8 status update — 2026-07-16, elicitation round 3
M8 **accepted → operative**. All future extractions enumerate [mediated] operator decisions alongside verbatim user turns.

## M9 — Design-session additions adopted
2026-07-16 · AI-proposed (design session), operator-accepted round 3 · enhancement · method · **operative**
Three additions to the method: (1) **Calibration step** — validate the frame on one small verifiable case before corpus-scale passes; (2) **Rung-naming rule** — every claim of change names the ladder rung reached and the dependents touched; (3) **Narrow P1 start** — P1 begins with the single most-corrected prior session (replay + impact map, stop, validate) before the full oldest→newest sweep.

## M10 — Ayo covers case = canonical calibration example
2026-07-16 · operator-supplied evidence · exemplification · method · **authoritative**
Origin: design-session transcript pasted 2026-07-16 ("we designed three album covers in that chat… i cannot locate them"). The three "Run It To Me" covers (45 A-side Radio Ready, 45 B-side Explicit, 12" Super Duper Sky-walking Mix) were operative AND persisted — in `campaigns/run-it-to-me/` of the "Copy of MoMoney Studios Design System" claude.ai project — but never propagated to the context where the operator's model placed them. M1 failure class, verifiable in minutes. Fills the M9 calibration slot.

## M11 — Cross-surface state architecture (DEC-07)
2026-07-16 · operator-directed · extension · method · **accepted; implementation partial**
Operator wish: design project physically inside d:\maestro-on-mosaic; fallback: tool-specific and account-level Claude config files. Reality: claude.ai projects cannot be live-mounted. Implemented equivalent: (a) this folder = SSOT; (b) `CLAUDE.md` at folder root auto-loads the state pointer for all folder-connected sessions; (c) `_PROVENANCE/POINTER_FOR_CLAUDE_PROJECTS.md` = paste-in pointer doc for both design projects' knowledge; (d) design-project contents (covers HTML + campaign assets) to be exported by operator into `projects/design-system/` register (OPEN O-12).

## DEC-08 — Terminology
2026-07-16 · operator · round 3: corpus-wide term = **"state ladder / rungs"** (supersedes "layer ladder" wording in STATE.md v0.1; STATE.md normalized).

## New evidence surfaces (inventory extension)
claude.ai projects "MoMoney Studios Design System" and "Copy of MoMoney Studios Design System" (incl. `campaigns/run-it-to-me/Cover Directions.html`) hold Maestro-adjacent state outside this folder and outside Cowork history. Registered in P0 inventory §2.

## P1-narrow execution record (M9) — 2026-07-16
Session selected by correction density: **session 13** (window2 ≈0.32 markers/KB vs claud3 0.25, eldrik 0.18). Byte-lossless mechanical split (coverage verified: segment sum == file length). 49 operator segments processed (17+32), +2 recovered from assistant tails. Output: `P1_narrow/` — two replay files (verbatim operator quotes, 61 classified mutations, 9 contradictions preserved) + `P1_NARROW_IMPACT_MAP.md`. Stopped at the M9 gate pending operator validation.

## V1 — Validation finding: session-13 FIRM canon never persisted
2026-07-16 · AI-verified against corpus · defect finding · reconstruction · **confirmed by grep, awaiting operator ruling on repair**
R-RT-QAF-01, R-RT-PD-01, Config B FIRM canon (R-list v0.2, 96 entries/92 FIRM), and the v4.5.5-anchor ruling appear in ZERO persisted artifacts — transcripts only. `canon/Maestro_v5c_*` never mentions v4.5.5 and predates/ignores the ruling that v5c is a failed-recreation track. Canon register staleness: CONFIRMED (upgrades OPEN O-06 from presumptive). Top repair candidate: reconstruct R-list v0.2 as persisted artifact from U20/U53/U56 verbatim record (rung: proposed).

*Append below this line only.*
