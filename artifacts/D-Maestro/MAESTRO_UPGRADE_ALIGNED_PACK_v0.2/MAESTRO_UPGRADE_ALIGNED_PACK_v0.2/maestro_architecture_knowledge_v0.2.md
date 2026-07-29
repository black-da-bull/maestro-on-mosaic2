# Maestro / Mosaic Architecture Knowledge v0.2
Status: OPERATOR REVIEW REQUIRED  
Purpose: Knowledge file for Custom GPT upload.

## 0. Core Model

The architecture has four planes:

```yaml
planes:
  maestro_app:
    type: customer_owned_application
    metaphor: virtual_record_label
    owns:
      - music_creation
      - bounded_SME_workforce
      - song_governance
      - Technical_UST_work
      - Creative_UST_generation
      - SEM_G_Card_HPA_evaluation
      - release_packaging

  mosaic_host:
    type: host_platform
    metaphor: cloud_runtime
    owns:
      - runtime_hosting
      - substrate_services
      - portability
      - state_inspection
      - replay_support
      - application_mounting
      - cross_app_runtime_primitives

  dev_environment:
    type: construction_iteration_space
    owns:
      - experiments
      - branch_work
      - failed_attempts
      - staging
      - v5_v5b_v5c_lineage
      - day_state_models

  forensic_reconstruction:
    type: extraction_recovery_layer
    owns:
      - transcript_ingest
      - lineage_reconstruction
      - architecture_extraction
      - drift_detection
      - node_edge_taxonomy
      - authority_review
```

## 1. Plane Descriptions

### 1.1 Maestro App

Maestro App is the customer-owned music application. It simulates a virtual record label. It is the product-level experience for music creation and evaluation.

Primary responsibilities:
- create and evaluate songs
- operate a virtual staff / bounded SME workforce
- maintain Technical UST as music-domain middleware
- derive Creative UST and Show Summary
- enforce SEM / G-Card / HPA
- produce zero-touch Suno-facing prompt artifacts
- preserve sacred imperfection and human authenticity as music-domain requirements

Maestro App does not own:
- the host platform itself
- generic substrate runtime primitives
- forensic proof status
- dev workspace authority

### 1.2 Mosaic Host Platform

Mosaic is the host runtime platform. It is analogous to a cloud platform that hosts applications.

Primary responsibilities:
- provide runtime substrate services
- host applications such as Maestro
- preserve state and portability
- support canonical instance records
- support replay and inspection
- provide cross-application governance primitives
- prevent prompt-only fragility

Mosaic does not own:
- Maestro-specific song criteria
- music-specific employee identities
- specific lyric rules unless exposed as app configuration
- forensic status of dev artifacts

### 1.3 Dev Environment

The Dev Environment is the build lab.

Primary responsibilities:
- experimentation
- iteration
- staging
- branch creation
- failed architecture attempts
- stress testing
- exploratory synthesis

Important rule:
Dev artifacts can contain valuable discoveries but must not be treated as canon without promotion.

### 1.4 Forensic Reconstruction

Forensics is the recovery and extraction layer.

Primary responsibilities:
- reconstruct architecture from development sessions
- detect drift
- preserve lineage
- classify contradictions
- recover lost dependencies
- produce diagnostic / control artifacts
- separate exploratory material from binding canon

Important rule:
Forensic control guides interpretation. It does not itself promote canon.

## 2. Node-Edge Topology

```yaml
node_edge_topology:
  mosaic_host:
    hosts:
      - maestro_app
    provides:
      - substrate_services
      - portability_services
      - runtime_state_services

  maestro_app:
    executes_on:
      - mosaic_host
    consumes:
      - runtime_substrate
      - state_preload
      - host_services
    emits:
      - technical_ust
      - creative_ust
      - show_summary
      - ar_profile
      - suno_prompt
      - ledgers

  dev_environment:
    produces:
      - candidate_specs
      - experiments
      - failed_branches
      - staging_outputs
    feeds:
      - forensic_reconstruction

  forensic_reconstruction:
    reads:
      - dev_environment
      - prior_runtime_outputs
      - transcripts
      - lineage_artifacts
    emits:
      - diagnostics
      - authority_matrices
      - promotion_recommendations
      - reconstructed_architecture
    does_not_emit:
      - automatic_canon
```

## 3. Authority Classes

Every architecture claim must carry one authority class.

```yaml
authority_classes:
  ACCEPTED_CANON:
    definition: force_closed_by_operator_or_governing_artifact_and_verified
  FILE_VERIFIED:
    definition: verified_in_uploaded_file_but_not_necessarily_promoted
  BRIDGE_LAW:
    definition: preserved_from_old_lineage_or_bridge_state
  CANDIDATE_SPEC:
    definition: formal_spec_pending_operator_force_closure
  FORENSIC_CONTROL:
    definition: diagnostic_control_surface_not_auto_promotion
  OPERATOR_ASSERTED:
    definition: direct_operator_claim_pending_artifact_promotion
  INFERRED:
    definition: analytic_conclusion_requiring_promotion_gate
  PROVISIONAL:
    definition: plausible_unresolved_do_not_promote
  UNVERIFIED_PENDING_SOURCE:
    definition: likely_true_but_missing_source_attachment_or_lineage
```

## 4. Claim Coordinate Schema

Every major claim has two coordinates:

```yaml
claim_coordinate:
  plane: maestro_app | mosaic_host | dev_environment | forensic_reconstruction | cross_plane
  authority: ACCEPTED_CANON | FILE_VERIFIED | BRIDGE_LAW | CANDIDATE_SPEC | FORENSIC_CONTROL | OPERATOR_ASSERTED | INFERRED | PROVISIONAL | UNVERIFIED_PENDING_SOURCE
  promotion_status: promoted | candidate | pending_operator_F | rejected | bridge_only | diagnostic_only
  source: file_or_operator_context
  downstream_effect: what_this_claim_changes
```

## 5. Corrected Legacy Term Registry

```yaml
legacy_term_registry:
  "Maestro":
    canonical_resolution:
      - Maestro_App
      - Maestro_Project
      - Maestro_Runtime
    disambiguation_required: true

  "Mosaic":
    canonical_resolution: Mosaic_Host_Platform
    disambiguation_required: false

  "mounted_on_Mosaic":
    means: app_executes_on_host_platform
    forbidden_meanings:
      - ownership
      - subordination
      - identity_collapse

  "sea":
    canonical_resolution: dev_forensic_semantic_reservoir
    not: Mosaic_platform

  "v5":
    canonical_resolution: dev_environment_failed_branch
    not: runtime_canon

  "v5-b":
    canonical_resolution: dev_environment_salvage_branch
    not: final_runtime_canon

  "v5-c":
    canonical_resolution: dev_environment_substrate_recognition_branch
    not: final_runtime_canon

  "Day_2":
    canonical_resolution: bridge_law_preservation_substrate
    not: destination_canon

  "forensic":
    canonical_resolution: reconstruction_layer
    not: app_or_platform
```

## 6. Upgrade Operating Rule

When asked to update the GPT:

- admin instructions should contain stable operating behavior
- knowledge files should contain architecture maps and vocabularies
- candidate specs should be uploaded as reference, not as unconditional canon
- forensic files should be uploaded as diagnostic reference
- dev logs should be uploaded only when the GPT is expected to reconstruct lineage

## 7. Response Contract

For architecture questions, answer using:

```markdown
## Plane Classification
## Authority Classification
## Node-Edge Reading
## What Is Promoted
## What Is Candidate
## What Is Forensic
## What Must Not Be Collapsed
## Next Upgrade Artifact
```
