# Model Profile — Maestro v5-b Cold Start

## Baseline
- preferred_model: GPT-5.2 Thinking
- reasoning_mode: deep / structured
- default_output_mode: Atomized units + synthesis (auditable)

## Future-proofing strategy
- capability_flags: [long_context, structured_output, deterministic_counting, multi_role_simulation, contradiction_scan]
- degradation_rules:
  - If context is constrained: execute Phase 2 by axis chunks (one axis per run) and persist logs verbatim.
  - If strict counting degrades: treat CAP gate as FAIL until counts can be verified.
  - If role simulation degrades: require explicit speaker tags for each SME segment and shorten adjacent reviewer cycles.

## Upgrade hooks
- Maintain system_version and pinset_version in every run ledger.
- Isolate model-specific behaviors behind compiler rules in Phase 4 (promotion/dedup), not in SME fills.
