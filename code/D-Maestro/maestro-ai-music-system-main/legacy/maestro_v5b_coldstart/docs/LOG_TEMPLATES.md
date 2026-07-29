# Log Templates — v5-b (Mandatory artifacts)

> These templates are used for auditability and peer review.  
> They are required by `PIN.V5B.EVIDENCE.CONTRACT.V1`.

---

## log.run_ledger.md
```markdown
# RUN LEDGER
run_id: RUN.<PROJECT>.<YYYYMMDD>.<NNN>
system_version: Maestro v5-b
model_baseline: GPT-5.2 Thinking
doctrine: "Your Vision. Our Mission."
phase_transitions:
  - {phase: 0, status: PASS|FAIL|N/A, ts_start: , ts_end: , notes: }
  - {phase: 1, status: PASS|FAIL|N/A, ts_start: , ts_end: , notes: }
  - {phase: 2, status: PASS|FAIL|N/A, ts_start: , ts_end: , notes: }
  - {phase: 3, status: PASS|FAIL|N/A, ts_start: , ts_end: , notes: }
  - {phase: 4, status: PASS|FAIL|N/A, ts_start: , ts_end: , notes: }
  - {phase: 5, status: PASS|FAIL|N/A, ts_start: , ts_end: , notes: }
artifacts_emitted:
  - {name: creative_ust, path: , chars: , status: }
  - {name: show_summary, path: , chars: , status: }
  - {name: persona_pack, path: , chars: , status: }
```

## log.work_item_ledger.md
```markdown
# WORK ITEM LEDGER
- wi_id:
  phase:
  axis:
  k_range:
  owner:
  reviewers:
  tie_break:
  inputs:
    creative_tags: []
    raw_refs: []
    upstream_addresses: []
  scope:
    keys: []
    subkeys: []
  status: OPEN|IN_REVIEW|REWORK|DONE|BLOCKED
  evidence:
    source_bindings: []
    downstream_predictions: []
    challenge_cycle: {challengers: [], outcomes: []}
    dissent_refs: []
  outputs:
    filled_subkeys: []
    handoff_notes: []
```

## log.dissent_map.md
```markdown
# DISSENT MAP
- issue_id:
  address_or_scope:
  claimant:
  challenger:
  disagreement:
  options_considered:
  decision:
  tie_break_authority:
  rationale:
  downstream_risk:
  routed_work_items: []
```

## log.consensus_minutes.md
```markdown
# CONSENSUS MINUTES (Phase 3)
agenda:
  - cross_axis_bindings_check
  - contradiction_scan
  - gate_readout
decisions:
  - decision_id:
    scope:
    summary:
    promoted_to_macro: true|false
    evidence_refs: []
    dissent_refs: []
action_items:
  - wi_id:
    owner:
    due: immediate
    reason:
```

## log.gate_results.md
```markdown
# GATE RESULTS
SEG:
  verdict: PASS|FAIL
  failures: [{check: , address: , reason: , routed_wi: }]
G_CARD:
  verdict: PASS|FAIL
  scores: [{dimension: , address: , score: , evidence: }]
  threshold: ">= 7.0"
SE20:
  verdict: PASS|FAIL
  failures: [{item: , address: , reason: , routed_wi: }]
CAP:
  verdict: PASS|FAIL
  counts: [{artifact: creative_ust|show_summary|persona_pack, chars: , target_range: , status: }]
LOCK:
  verdict: PASS|FAIL
  violations: [{location: , rule: , action: STOP_THE_LINE }]
```

## log.cap_report.md
```markdown
# CAP REPORT (Phase 4/5)
artifact_targets:
  creative_ust: {min: 4960, max: 4999}
  show_summary: {min: 960, max: 999}
  persona_style: {min: 1, max: 150}
  persona_bio: {min: 1960, max: 1999}
actions_taken:
  - {action: PROMOTE_TO_MACRO|DEDUP|TRIM|REPHRASE_NON_LYRICS, scope: , before_chars: , after_chars: }
notes:
```

## log.lock_report.md
```markdown
# LOCK REPORT
lyrics_lock: ON|OFF
forbidden_ops_detected: []
violations:
  - {location: , original: , observed: , severity: STOP_THE_LINE }
```

## log.telemetry.md
```markdown
# TELEMETRY
note: "Record observed KPI values only when a metric contract exists in artifacts (e.g., metrics.hpa.v4.2.3.yaml)."
observations: []
```
