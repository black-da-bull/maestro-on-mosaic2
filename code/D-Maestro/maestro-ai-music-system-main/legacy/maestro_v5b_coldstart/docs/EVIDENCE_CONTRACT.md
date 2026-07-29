# Evidence Contract — PIN.V5B.EVIDENCE.CONTRACT.V1

## Evidence: Valid Fill (per Technical UST subkey)
- **rule.one_sentence_per_subkey:** Each subkey value is a single concise sentence.
- **rule.constraint_form:** Each sentence must encode at least one operational constraint (range, target, rule, exclusion, or precedence).
- **rule.source_binding:** Each sentence must cite its source anchor as one of:
  - a Creative UST field tag (e.g., `[tempo]`, `[genre]`, `[fx_palette]`), or
  - a v0.raw quote fragment identifier (e.g., `raw:L12`), or
  - a downstream-binding justification (e.g., `binds:POST.K2.S4`).
- **rule.downstream_prediction_required:** Each owner must attach at least one “if X then Y” downstream sensitivity note per key group.
- **rule.challenge_cycle_required:** Each meaningful fill must survive at least one peer challenge cycle; dissent must be logged.

- **rule.lyrics_lock_scope:** Lyrics lock applies to quoted lyric text only; meta tags and sFX remain editable.

## Evidence: Pass Record (per Phase Gate)
- **SEG PASS record:** All feasibility checks in scope pass; contradictions are either resolved or explicitly routed back to Phase 2 work items.
- **G-Card PASS record:** Scores recorded at address level; threshold enforcement uses the canon threshold where stated (e.g., `G.K6.S4 pass_threshold (≥7.0)`).
- **SE20 PASS record:** Checklist pass/fail recorded; failures trigger Phase 2 re-meeting per binding rules.
- **CAP PASS record:** Character counts validated for each deliverable; overflow triggers Phase 4 re-promotion/dedup loop.
- **LOCK PASS record:** Lyrics lock compliance verified; forbidden ops detected ⇒ stop-the-line.

## Mandatory Logs (Existence is enforced)
- **log.run_ledger:** Run header; timestamps; phase transitions; responsible persona per work item.
- **log.work_item_ledger:** Work items created, executed, challenged, revised, closed; includes definitions of done.
- **log.dissent_map:** Disagreements preserved; split decisions recorded with tie-break justification.
- **log.consensus_minutes:** Phase 3 meeting notes; binding checks; decisions promoted to macro.
- **log.gate_results:** SEG + G + SE20 results with address references.
- **log.cap_report:** Character counts per deliverable; promotion actions taken.
- **log.lock_report:** Lock compliance scan results; any violations with location pointers.
- **log.telemetry:** Observed KPI values only when the metric contract exists in artifacts (e.g., `metrics.hpa.v4.2.3.yaml`).
