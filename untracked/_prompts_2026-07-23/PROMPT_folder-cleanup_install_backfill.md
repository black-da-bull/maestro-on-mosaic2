PROJECT MAESTRO — install the harvest suite + autonomous Downloads → untracked backfill + check-in
(prerequisite: the next replay-backed-build-harvest FULL run must not execute until this completes)

Load _PROVENANCE/STATE.md, LEDGER.md, OPEN.md first (folder CLAUDE.md auto-loads state per M11/DEC-29).
Resume the folder-cleanup workstream (lineage c6dfad39 / O-11). Fix: AI/Cowork deliverables have been
downloading to C:\Users\gamer\Downloads and never flowing through D:\maestro-on-mosaic\untracked\, so they
sit outside the SSOT, invisible to the ledger (M1 limbo). Route the pile in, check it in, and install the
new harvest tooling.

MODE — AUTONOMOUS. Do NOT pause for scope approval; proceed on your own judgment and report at the end.
Hard rails that still hold (these are canon, not gates): non-destructive — NEVER permanently delete
(M18: deletion needs my explicit statement); append-only ledger (M2, never rewrite); provenance-complete
(no skeletons, F2); dedup by content hash, don't discard (M7/DEC-02); park genuinely-ambiguous items,
don't guess (M16). "No approval pause" means you run start-to-finish without checking in; it does not mean
delete or overwrite.

PRECONDITION (the only stop, and only if blocked): confirm both C:\Users\gamer\Downloads and
D:\maestro-on-mosaic are reachable this session. If Downloads is not connected, say so and ask me to add it
— then continue. Do not guess paths.

PART A — INSTALL the replay-backed-build-harvest suite (2026-07-23 calibration deliverable)
From Downloads, take the LATEST replay-backed-build-harvest-suite-*.zip (highest version — currently v0.2,
which adds the D1/D2/D3 gates the corpus run-book requires; supersede any v0.1 by pointer, M2; the 6 loose
*.skill files are the same units, use only if the zip is missing). Then:
1. Extract it to a canonical home in the store (the tooling lane your M19 contracts designate, e.g.
   code\replay-backed-build-harvest-suite\). Keep this extracted suite as the SSOT record.
2. Install: copy skills\* -> .claude\skills\  and  agents\*.md (incl. AGENT_REGISTRY.yaml) -> .claude\agents\.
   The maestro-mosaic binding, schemas, and scripts already live inside the orchestrator skill — keep them
   with it. If a prior version of any skill/agent exists, supersede BY POINTER (M2), do not rewrite; archive
   the prior build.
3. VERIFY the install before claiming success (SKILL-REPKG-1 — a skill isn't installed until its tests pass):
   run  .claude\skills\replay-backed-build-harvest\scripts\selftest.py  (expect ALL SELFTESTS PASS; it now
   runs 13 checks incl. check_supersession_propagation) and  scripts\validate_package.py --suite <suite home>
   (expect ALL PASS). If either fails, log a defect in OPEN.md and STOP the install step (still do Part B).
4. Register: append LEDGER entry HARVEST-INSTALL-1 (suite v0.2 installed + Calibration-1 ingested; list the
   skill/agent IDs and the selftest result). The suite is PROVISIONAL pending my review of
   CALIBRATION_REPORT.md — record in STATE that the promotion decision (authorize a FULL harvest run) is the
   open next action, and add OR-STRATA-O18-RESIDUE to OPEN.md (live defect: maestro-current\
   STRATA_MIGRATION_MAP.md still ships the DEC-27-withdrawn "competing detail stratum / O-18" line, unstruck
   — do not fix it here; it's my ruling).

PART B — BACKFILL Downloads (automated)
1. Inventory all of Downloads. Classify each item MAESTRO / UNRELATED / AMBIGUOUS with a recorded basis (M16).
   Recognize project families by name AND content, e.g. MAESTRO*/maestro*, MOSAIC*, SESSION13_*, PATCH-0*,
   O16E_*, BRIDGE_*, P1_NARROW*, R2_*, MUT26*, momoney*/MoMoney*, run-it-to-me*/Ayo*, forensic_*,
   VERSION_1_ORIGIN*, EXECUTABLE_APP_DESIGN*, MAESTRO_VV_REPORT*, intent-compiler-skill*,
   maestro_evidence_classification_register*, CALIBRATION_REPORT*, REPLAY_BACKED_BUILD_HARVEST*. Guidance,
   not an exhaustive whitelist.
2. COPY every MAESTRO item into untracked\ and check it in (Part C). Leave UNRELATED items untouched. Park
   AMBIGUOUS items in untracked\_INTAKE_QUARANTINE.md with your best guess + why (don't force-classify,
   don't delete) — parking is not a stop.
3. After an item is checked in AND hash-verified present in the store, relocate its Downloads original into
   C:\Users\gamer\Downloads\_maestro_ingested_<YYYYMMDD>\ (a move, fully reversible — NOT a delete). This
   tidies Downloads and makes re-runs obvious. Permanent deletion of that holding folder remains my call.

PART C — CHECK-IN mechanics (per item in untracked\)
- hash (md5 + sha256); size; internal date where present (mtimes unreliable post-consolidation — M7).
- dedup vs the existing store by content hash; on duplicates select the primary (DEC-02) and record the rest
  as dated-context duplicates (keep, don't delete).
- classify lane (M16: KNOWN/PROBABLE/HISTORICAL/UNVERIFIED) and M19 axes (ROLE + SOURCE-ORIGIN + rung +
  domain); unzip archives and register MEMBERS, not just the zip.
- route from untracked\ to its proper home per the folder contracts (M19); nothing operative left only in
  Downloads or conversation (M1).
- append a LEDGER entry per batch (M2); update STATE next-actions; add unresolved items to OPEN.md with an
  owner (nulls are reserved addresses, not stops).
- idempotent: hash-key everything so a re-run does not double-register and can report what it did.

DEFINITION OF DONE
- Suite v0.2 installed to .claude\ and self-tests PASS (or a defect is logged); HARVEST-INSTALL-1 in the ledger.
- Every MAESTRO Downloads item checked in (hashed, deduped, lane+axis classified, routed, registered) or
  parked in quarantine with an owner; originals relocated to _maestro_ingested_<date>\ (none deleted).
- untracked\ drained of processed items; STATE/LEDGER/OPEN reflect both the install and the ingest.
- Write _PROVENANCE\INTAKE_REPORT_<date>.md: counts (installed / moved / deduped / routed / quarantined /
  unrelated-skipped), the ledger IDs created, the selftest result, and the relocation holding-folder path.
- State plainly that the blocker is cleared: the next replay-backed-build-harvest FULL run can now source
  from the filestore, and its go/no-go is my review of CALIBRATION_REPORT.md.
