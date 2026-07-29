# Maestro Admin Load Order v0.2
Status: OPERATOR REVIEW REQUIRED

## Goal

Upgrade the Custom GPT using plane-separated governance so it can reason accurately about Maestro App, Mosaic Host Platform, Dev Environment, and Forensic Reconstruction.

## Recommended Admin Window Order

### 1. Configure Instructions

Paste:
`maestro_admin_instructions_upgrade_v0.2.md`

This file sets behavior rules and prevents plane collapse.

### 2. Knowledge File 1

Upload:
`maestro_architecture_knowledge_v0.2.md`

This file contains the four-plane architecture, node-edge topology, authority classes, and legacy term registry.

### 3. Knowledge File 2

Upload:
`maestro_reassessment_prior_responses_v0.2.md`

This file tells the GPT what was previously wrong and which old generated output is quarantined.

### 4. Optional Existing Source Files

Upload source files only after the GPT has the plane rules.

Suggested categories:

#### Maestro App Sources
- maestro_v0_application_spec.md
- song_excellence_architecture.md
- architecture.json
- Maestro v5-c Canonical Spine if used as runtime-operational reference

#### Mosaic Host Sources
- mosaic_engine_v0_1.md if available
- substrate_floor files
- platform substrate specs

#### Dev Environment Sources
- v5 / v5-b / v5-c workspace YAMLs
- corrective regeneration prompts
- staging and slipstream updates

#### Forensic Sources
- forensic_v5_diagnostic files
- reconstruction YAMLs
- RTFA / SEC / SDG / SLR / MMR if available
- review briefs v0.3.1

## Loading Principle

Do not load dev or forensic files before the model knows they are not automatically canon.

## Recommended Opening Test Prompt

After upgrade, ask:

“Classify Maestro, Mosaic, the dev environment, and forensics into planes, then explain what must not be collapsed.”

Expected answer:
- Maestro App = customer-owned virtual record label app
- Mosaic = host platform / runtime
- Dev = construction space
- Forensics = reconstruction/extraction layer
- no automatic canon promotion from candidate/dev/forensic artifacts

## Kill Switch

If the upgraded GPT collapses planes, paste:

DRIFT DETECTED — plane collapse. Reclassify by four-plane architecture before continuing.
