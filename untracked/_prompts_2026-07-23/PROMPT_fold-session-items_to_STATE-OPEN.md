PROJECT MAESTRO — fold the 2026-07-23 harvest session's open items into STATE + OPEN (append-only)
Run in the folder-cleanup / provenance session (filesystem authority). Load _PROVENANCE/STATE.md, LEDGER.md,
OPEN.md first.

PURPOSE: close the M1 gap — this session's action items currently live only in untracked/_prompts_2026-07-23/
+ the suite COMPOSITION_MANIFEST. Persist them into the SSOT state register. Append-only (M2); supersede by
pointer, never rewrite; do NOT resolve any O-item (operator authority). Idempotent: if a block below already
exists by its ID, skip it — do not double-append. This is NOT a new TASKS.md; STATE + OPEN are the task system.

AUTHORITY: these are AI-proposed this session; they become operative when the operator acts on them. The three
O-items are evidence-backed FINDINGS whose RESOLUTION is operator authority.

1) STATE.md — append a new dated block (do NOT rewrite the 0.7 ordering):
## 2026-07-23 — replay-backed-build-harvest suite folded; next-actions (proposed)
The harvest suite (v0.2) was authored, calibrated (Calibration-1: externally_blocked, 15/15) and independently
V&V'd (LAWFUL-WITH-NITS). Proposed next-actions, in order:
1. Run untracked/_prompts_2026-07-23/PROMPT_folder-cleanup_install_backfill.md — clears the Downloads→untracked
   blocker (deliverables were landing in C:\Users\gamer\Downloads, outside the SSOT) and installs the suite
   v0.2 to .claude/. Gate: LEDGER HARVEST-INSTALL-1 + suite selftest PASS.
2. Review CALIBRATION_REPORT.md → operator go/no-go on the full harvest.
3. Run untracked/_prompts_2026-07-23/PROMPT_corpus-harvest_runbook.md — this OPERATIONALIZES STATE 0.7
   next-action #1 (O16E HISTORY-GROUNDED-DERIVATION) via the installed suite: narrow-start batch, STOP for
   operator validation before widening (M9). It EXTENDS #1; it does not replace it.
Deferred (later, not-now): price the adversarial pass — Experiment C on >=3 slices; non-Maestro Calibration 2
(the gate before the suite's portability may be called empirically validated).

2) OPEN.md — append three new items (confirm the next-free O-numbers before writing; proposed here as
   O-19..O-21; each cross-referenced to the harvest's OR- ID):
## O-19 · Technical-UST subkey granularity (sub-question of O16E) [harvest: OR-O16E-GRANULARITY]
Chimera-era template (compile source md5 eaf18e11; 33 keys / 165 subkeys) vs v5b coldstart canon monolith
(sha256 bfe0b238; 28 keys / ~128 subkeys + LYR.K0 governance keys + THY.K5 tension-release) — which feeds
compiled SUBKEY granularity, or do they layer (DEC-22 later-speaks-in-detail)? Keys stable; subkeys
provisional. Owner: operator (rides O16E). Inferred default: LAYER per DEC-22 with a subkey-provenance ledger.
Do not resolve. Evidence: CALIBRATION_REPORT §6; harvest OR-O16E-GRANULARITY.
## O-20 · Correction-propagation residue in STRATA_MIGRATION_MAP.md [harvest: OR-STRATA-O18-RESIDUE]
maestro-current/STRATA_MIGRATION_MAP.md still ships the DEC-27-withdrawn "competing detail stratum —
adjudication = O-18" framing, unstruck (~lines 36-37), while every peer site was struck — a byte-identical,
MANIFEST-listed, validator-passing v0.5 member (registration != application; byte-identity != currency). Now
catchable deterministically by check_supersession_propagation.py. Owner: operator (strike the line / re-run
propagation with a widened flag set). Do NOT edit here without an explicit operator statement (M18). Evidence:
CALIBRATION_REPORT §11 (FN-1) + the D1 gate proof.
## O-21 · Named-only sources unstaged [harvest: OR-SOURCES-UNSTAGED]
The compile predecessor md5 eaf18e11 (technical.ust.template.txt) and the v5b canon monolith sha256 bfe0b238
are referenced by hash but not located/staged in the reached material; both legs of O-19 stay unverifiable
until staged. Owner: operator (stage them / record a repo-wide search per M16 before any "missing" verdict).
Relates to O-17 (CONS). Evidence: reconstruction_handoff limitations; CALIBRATION_REPORT §7.

3) LEDGER.md — append (append-only):
## HARVEST-SUITE-1 — replay-backed-build-harvest v0.2 built + calibrated + V&V'd; session items folded (2026-07-23)
2026-07-23 · claude (cowork) · registration · tooling/method · persisted (prompts + suite in untracked;
STATE/OPEN append = this entry). Authored the replay-backed-build-harvest suite (thin orchestrator + 5 method
skills + 6 agents + maestro-mosaic binding + schemas + 13 self-tested scripts) composing
maestro-forensic-transcript BY POINTER (not modified, not v2). Calibration-1 on the Technical-UST adjudication
slice: externally_blocked, 15/15; independent V&V verdict LAWFUL-WITH-NITS; 3 scale-breaking nits closed with
proven deterministic gates (D1 check_supersession_propagation, D2 reconcile_coverage --contradictions, D3
evidence-ref lint). Agent-necessity verdict: evidence-authority DEMOTE_TO_SKILL; 5 agents necessary. Two
run-book prompts + the suite filed to untracked/_prompts_2026-07-23/ and untracked/ (pending the install
prompt). Opened O-19 / O-20 / O-21. Suite PROVISIONAL pending operator review of CALIBRATION_REPORT.md +
Calibration-2. Rung: persisted (staging) / proposed (STATE next-actions). Authority: AI-proposed; operator
accepts on execution.

VERIFY + REPORT: after appending, confirm STATE next-actions + OPEN O-19..O-21 + the LEDGER entry are present
and parse; confirm nothing operative now lives ONLY in the untracked prompts; write a one-line FOLD_NOTE (or a
line in the INTAKE_REPORT) recording the fold. Idempotent: skip any block whose ID already exists.
