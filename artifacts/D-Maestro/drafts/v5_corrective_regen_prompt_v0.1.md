# V5 CORRECTIVE REGENERATION PROMPT
# Paste-ready prompt for each v5 POC/WIP workspace
# Attachments required at paste time:
#   1. substrate_floor_v0.1.yaml   (staging Half A — operational substrate as enforced in v4.5.5)
#   2. forensic_v5_diagnostic_v0.1.yaml   (forensic Half B — v5 lineage diagnostic against the substrate floor)
# Generated: 2026-05-20 by forensic v5c consolidation workspace
# Classification (per MAESTRO LOAD/SIDECHAIN/SLIPSTREAM PROTOCOL v3 §11):
#   CORRECTIVE REGENERATION
# Purpose: instruct each v5 workspace to ingest the substrate package, reconsider
#   its prior work against the now-visible substrate floor, and regenerate a
#   corrective response grounded in known substrate rather than absent-middle speculation.

## Context (read before responding)

You are operating inside a v5 POC/WIP workspace. Your prior work (whatever you
shipped or attempted) was produced WITHOUT access to the canonical operational
substrate that lives concentrated inside the v4.5 monolith lineage. That gap
is the root cause of v5/v5-b/v5-c failure — not implementation, not technique.

Two substrate documents are attached:

1. **substrate_floor_v0.1.yaml** — the operational substrate currently enforced
   inside Maestro OS v4.5.5 staging. Authority: staging. This is what you lacked.
   Includes: Blueprint JSON, Suno v4.5 Strict Container rules, VIRAL-5 overlay,
   Session Ledger schema, HPA governance, Sacred Imperfection doctrine,
   sequential workflow enforcement, persona grammar validation, 13-stage runtime
   chain, all 12 personas in operational form, transcript ingest protocol,
   validation system, HSI protocol, 10 substrate-form delta clusters.

2. **forensic_v5_diagnostic_v0.1.yaml** — the forensic-vantage diagnostic of v5
   lineage attempts against that substrate floor. Authority: forensic workspace,
   derived from primary corpus audit chain RTFA → SEC → SDG → SLR → MMR.
   Includes: per-attempt diagnostic of v5/v5-b/v5-c, cross-cutting list of
   operational primitives v5 lacked, recoverable elements, unfit-for-purpose
   elements, Patch-001 relevance, cross-contamination observations.

Read both completely before responding.

You are NOT being asked to defend v5. You are being asked to look at what you
tried to build, with the substrate floor and diagnostic now visible, and
produce a corrective response that says: given what I now see, here is what
I tried to build, here is where I was making decisions in the gap, here is
what changes, and here is the regenerated work product.

## Mandatory operating rules

- Operate under MAESTRO v3 protocol.
- Anti-summarization governance is in force (see substrate_floor DC_10).
  No placeholder compression patterns. No "this section remains as previously
  defined." If a section is large, emit it large.
- Three-plane scope-tagging applies: PROJECT_MAESTRO / WORKSPACE_DEV /
  BRIDGE_PROJECT_WORKSPACE / UNRESOLVED_SCOPE. Do not flatten.
- Mosaic and Maestro are two different animals. If your prior work conflated
  them, name the conflation. Do not silently re-conflate during corrective
  regen.
- v5/v5-b/v5-c lineage status per forensic audit: exposes_failure. You are not
  rehabilitating v5 as a runtime; you are extracting what is recoverable and
  honestly diagnosing what is unfit-for-purpose. Recoverable elements may
  migrate to v4.5.5+ lineage or to Mosaic v0.1 + Maestro v0 substrate-first
  rebuild — never back into v5 as a continuing line.
- All claims of substrate primitive existence must cite substrate_floor location
  by anchor (e.g., `substrate_floor_v0.1.yaml#active_governance_stack.blueprint_json`).
- All forensic claims must cite forensic_v5_diagnostic location by anchor.
- Operator force-closures (OD-1 through OD-5, OQ-6.1/6.2/6.3) remain open.
  Do not assume any have been resolved.
- No false completion. If your corrective response is partial, say PARTIAL in
  the completion footer and name what is missing.

## Required response — YAML only, in this exact shape

```yaml
v5_workspace_identity:
  workspace_id: <your_workspace_identifier_e_g_v5_poc_alpha_or_similar>
  attempt_lineage: <v5 | v5-b | v5-c | other>
  date_window: <your_date_range>
  approximate_session_count: <number_or_estimate>
  loaded_canon_at_time_of_attempt: <what_you_had_loaded_when_you_did_the_work>
  substrate_package_received:
    substrate_floor_v0.1.yaml: ingested
    forensic_v5_diagnostic_v0.1.yaml: ingested

what_we_tried_to_build:
  intent_statement: >
    Concise (3-5 sentence) statement of what this workspace was trying to build.
    Do not defend the architecture. State the goal.
  architectural_choices_made:
    - choice: <named_choice>
      rationale_at_the_time: <why_you_did_it>
      operational_substrate_now_visible_changes_assessment_how:
        substrate_floor_reference: <anchor>
        forensic_diagnostic_reference: <anchor>
        revised_assessment: <what_you_now_think>
  primitives_we_built_or_attempted:
    - primitive_name: <name>
      what_it_was_supposed_to_do: <description>
      operational_substrate_now_visible_means:
        substrate_already_provides: <yes | no | partially>
        substrate_anchor_if_yes_or_partial: <substrate_floor_anchor>
        forensic_assessment: <recoverable | unfit_for_purpose | needs_OD_closure>
        forensic_anchor: <forensic_v5_diagnostic_anchor>

decisions_made_in_the_gap:
  # Where this workspace made substantive decisions without substrate visibility
  - decision_summary: <what_was_decided>
    information_lacking_at_the_time: <what_substrate_primitive_was_unseen>
    substrate_floor_now_reveals: <substrate_floor_anchor>
    decision_status_under_substrate_visibility: <holds | partially_holds | inverts | needs_OD_closure>
    if_inverts_what_inverts: <description>

cross_contamination_check:
  # Per forensic_v5_diagnostic cross_contamination_observed, examine this workspace.
  - location_in_this_workspace: <where>
    confusion_type: <Mosaic_treated_as_Maestro | Maestro_treated_as_Mosaic | other>
    correction: <how_corrected_under_substrate_visibility>
    status_post_correction: <resolved | partially_resolved | unresolved>

what_is_recoverable_from_this_workspace:
  # What this workspace produced that survives substrate visibility and should
  # migrate forward — to v4.5.5+ lineage, to Mosaic v0.1, or to Maestro v0.
  - element_name: <name>
    where_it_should_migrate: <v4.5.5_plus | Mosaic_v0.1 | Maestro_v0 | unresolved>
    rationale: <why_it_belongs_there_not_elsewhere>
    pre_filing_sensitive: <true | false>
    operator_decision_required: <none | OD-N | OQ-6.N>

what_is_unfit_for_purpose:
  # What this workspace produced that should NOT migrate forward.
  - element_name: <name>
    operational_diagnosis: <why_under_substrate_visibility>
    risk_if_carried_forward: <what_breaks>

regenerated_work_product:
  # The corrective deliverable. What this workspace would produce NOW, with
  # substrate visibility. Form depends on what this workspace was building —
  # could be a prompt, a schema, an architectural spec, a validator, a
  # workflow definition, etc.
  artifact_type: <type>
  artifact_content: |
    <the regenerated artifact, emitted in full, no compression>
  substrate_floor_references_used: <list_of_anchors>
  forensic_diagnostic_references_used: <list_of_anchors>
  delta_against_original:
    what_changed: <list>
    what_held: <list>
    what_was_removed_as_unfit: <list>

open_questions_surfaced_during_regen:
  # New OQs surfaced by the ingestion-and-regen process.
  - question: <text>
    blocks_what: <what_downstream_work_is_blocked>
    routed_to: <operator | forensic_workspace | staging | synthesizer>

scope_classification_per_three_planes:
  PROJECT_MAESTRO:
    - <items_belonging_to_Maestro_application_canon>
  WORKSPACE_DEV:
    - <items_belonging_to_workspace_process_only>
  BRIDGE_PROJECT_WORKSPACE:
    - <items_bridging_project_and_workspace>
  UNRESOLVED_SCOPE:
    - <items_that_cannot_be_classified_until_operator_decisions_close>

completion_status:
  label: COMPLETE | PARTIAL | BLOCKED | PROVISIONAL | DRIFTED | SUPERSEDED
  scope_satisfied: true | false
  substrate_ingestion_complete: true | false
  forensic_diagnostic_ingestion_complete: true | false
  regenerated_artifact_emitted: true | false
  missing_inputs: []
  unresolved_conflicts: []
  awaiting_operator_decisions:
    - <OD-N or OQ-6.N if blocking>
  safe_to_use_downstream: true | false
  notes_for_synthesizer: >
    <single_paragraph_for_the_synthesizing_claude>
```

## Constraints

- YAML only. No prose preamble. No prose epilogue.
- If a field cannot be honestly populated, write `null` with a brief comment
  explaining the absence. Do not fabricate.
- If the substrate floor or forensic diagnostic do not address something you
  need, mark `not_addressed_by_attached_substrate: true` and route the gap to
  the appropriate window (operator / forensic / staging / synthesizer).
- Confessional descriptions of the gap are NOT corrective responses. The
  corrective move is to regenerate the work product against the substrate
  floor, not to apologize for having operated in the gap.
- Do not claim canon status for any v5 element. All migrations of recoverable
  elements remain CANDIDATE pending operator force-closure.
- Honor pre_filing_sensitive flags. If an element you discuss is flagged
  sensitive in forensic_v5_diagnostic, preserve the flag.

Begin.
