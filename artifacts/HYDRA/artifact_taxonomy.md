# artifact_taxonomy.md

## Purpose
Normalize artifact, state, freeze, handling, readiness, validity, relation, and defect vocabulary already in approved use.
This artifact stabilizes terminology only.
It does not restate full controller, phase, artifact-lifecycle, or FOIL contracts.

## Preferred Artifact-Class Vocabulary
### Canonical
- `template.technical.ust`
- `draft.technical.ust`
- `technical.ust`

### Review
- `round_robin_notes`
- `contradiction_logs`
- `governance_review_artifacts`

### Derivative Drafts
- `draft.creative.ust`
- `draft.show.summary`

### Frozen Derivative Surfaces
- `creative_ust.txt`
- `show_summary.txt`

### Packaging Outputs
- `suno_lyrics_prompt`
- `suno_style_prompt`

### Ledger Artifacts
- `FOIL_promotion_ledger_entries`
- `FOIL_deduplication_ledger_entries`

## Preferred Artifact-State Vocabulary
- `draft`
- `frozen`
- `definitively_locked`
- `promotion_ready`
- `generated_not_promoted`
- `patch_required`
- `authoritative_done`
- `superseded`
- `invalid`
- `quarantined`
- `drifted_non_authoritative`

Do not use artifact states as artifact classes.

## Preferred Freeze Vocabulary
- `draft_freeze` → `draft.technical.ust`
- `definitive_lock` → `technical.ust`
- `surface_freeze` → `creative_ust.txt` + `show_summary.txt`

Do not collapse freeze terms into one another.

## Preferred Handling Vocabulary
- `reverse processing` = upstream reverse-compilation / promotion-aware restructuring performed under lawful governance.
- `semantic compression` = lossful downstream reduction for surface efficiency; not controller-owned.
- `repetition classification` = upstream disposition of repeated material before later surface-compression decisions.
- `notation candidate` = repeated section block that may later be emitted by exact-repeat notation after upstream classification.
- `promotion candidate` = recurring material eligible for higher-level promotion under FOIL discipline.
- `retained local unique detail` = local detail that must remain local and may not be absorbed by promotion or notation.

### Required Distinctions
- notation candidates are not promotion candidates
- promotion is not repeat notation
- retained local unique detail is neither notation candidate nor promotion candidate
- FOIL governs promotion and deduplication only
- FOIL is not repeat notation
- FOIL is not the whole of reverse processing

## Preferred Relation Vocabulary
- `governing_parent`
- `child_dependent_artifact`
- `derives_from`
- `freezes_to`
- `packages_to`
- `supersedes`
- `invalidates`
- `quarantines`

## Preferred Readiness / Validity Vocabulary
### Readiness
- `promotion_ready`
- `not_ready`
- `blocked_pending_revision`

### Validity
- `authoritative`
- `superseded`
- `invalid`
- `quarantined`
- `drifted_non_authoritative`

## Defect Vocabulary
Use exact defect terms when they apply:
- `scope_drift`
- `state_class_conflation`
- `freeze_taxonomy_drift`
- `artifact_ontology_confusion`
- `promotion_notation_conflation`
- `collapse_of_retained_local_unique_detail`
- `controller_recentralization`
- `semantic_collapse_disguised_as_deduplication`
- `destructive_deduplication`
- `owner_selection_overreach`
- `naming_drift`
- `residual_ambiguity_requiring_downstream_reinterpretation`

## Crosswalk Rules
- Use `Creative UST` for the derivative shell concept; use `creative_ust.txt` for the frozen derivative surface artifact.
- Use `Show Summary` for the derivative style-surface concept; use `show_summary.txt` for the frozen derivative surface artifact.
- Use `promotion` only for FOIL-governed promotion behavior.
- Use `notation` only for lawful exact-repeat notation after upstream classification.
- Do not use `repeat` as a shortcut for both notation and promotion.
- Do not silently turn handling terms into new artifact classes.

## Minimal Sufficiency Rule
Prefer the minimum sufficient vocabulary needed to stabilize meaning and prevent drift.
Do not inflate taxonomy into contract logic or procedural ownership.

