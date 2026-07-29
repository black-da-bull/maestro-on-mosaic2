# TRACE_MAP (source → rule → dependent artifacts)

SYSTEM_PROMPT_CoSTAR_v4.2.3.md
  → [USTF rules; stop-ship set]
  → artifacts/state/ust_prompt.valid.txt
  → artifacts/state/verification_log.json
  → Validation_Report_Template.md

os.maestro.momoney.knowledgeSpine.v4.2.3.md
  → [USTF detail; narrative governance]
  → artifacts/state/ust_prompt.valid.txt
  → artifacts/state/persona_usage.log

os.maestro.momoney.customInstructions.v4.2.3.md
  → [SME round-robin, output contract]
  → artifacts/state/persona_usage.log
  → artifacts/state/verification_log.json

os.maestro.momoney.configuration.v4.2.3.json
  → [DAG nodes/edges]
  → E2E_TestPlan_v4.2.3.md
  → artifacts/state/verification_log.json

E2E_TestPlan_v4.2.3.md
  → [E2E lane]
  → all artifacts/state/*

metrics.hpa.v4.2.3.yaml
  → [HPA thresholds]
  → artifacts/state/hpa_score.log
  → Validation_Report_Template.md

benchmark.audio_models.v4.2.3.md
  → [A→T→A protocol]
  → artifacts/state/verification_log.json
  → artifacts/state/hpa_feedback.json
