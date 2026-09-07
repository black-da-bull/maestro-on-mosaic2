# Maestro P0 Workforce + Technical UST Runtime

This directory materializes the accepted **13 audio workers**, the P0.2 Technical UST ownership/dependency overlay, and the P0.3 executable structural-interpretation layer.

The runtime keeps two things separate on purpose:
- employee descriptors define bounded worker identity, domain authority, writable lanes, challenges, and non-authority;
- `technical_ust_ownership_dependency_overlay.yaml` binds actual Technical UST axes/keys/subkeys and crossstream dependencies.

A broad worker dispatch is **not** proof of canonical address ownership. `technical_ust_runtime.py` must resolve the requested Technical UST address through the overlay before an address-authorized dispatch or mutation can occur.

## Files
- `canonical_employee_module_spec.yaml` — schema for one bounded employee module.
- `canonical_13_employee_instances.yaml` — exactly 13 current audio-worker instances.
- `employee_workforce_registry_contract.yaml` — registry/runtime boundary after P0.2 integration.
- `technical_ust_ownership_dependency_overlay.yaml` — materialized address ownership, required reviewers, and dependency edges.
- `workforce_runtime.py` — list/show/broad dispatch-envelope runtime.
- `technical_ust_runtime.py` — address dispatch, state mutation guard, dependency propagation, lawful peer blocking, lyric lock, and `MAP.K3` reference invalidation.
- `golden_structural_interpretation_fixture.py` — P0.3 executable proof fixture.
- `validate_workforce.py` — fail-closed integrated validator.
- `requirements.txt` — runtime Python dependency for YAML parsing.

## P0.3 golden fixture

The fixture executes a controlled structural delta and must prove all five behaviors:
1. `THY.K3.S2` dispatches to Dave from explicit overlay ownership rather than role-name inference.
2. A Dave-owned rhythmic-theory change reopens the supported `THY.K3 -> LYR.K4` dependency.
3. Vanessa can own integrated `PER.K2`, while Dave's lawful rhythmic objection still blocks final acceptance.
4. Dependency review does not authorize a lyric rewrite: locked `LYR` state remains unchanged without explicit operator authorization.
5. When `MAP.K3.S1` references `THY.K3.S2`, changing that upstream address reopens the exact referenced section entry (`MAP.K3.S1@Chorus`).

## Run
```bash
cd runtime/maestro-workforce
python -m pip install -r requirements.txt
python validate_workforce.py
python golden_structural_interpretation_fixture.py
python workforce_runtime.py list
python workforce_runtime.py dispatch Dave --task "evaluate pocket readability"
```

The four visual-module roles remain outside this audio runtime. Historical Isla/Huan and Melony records remain historical strata and are not silently added or conflated.

Model/provider invocation is still outside P0.3. This runtime proves routing and state/governance behavior; it does not claim 13 autonomous LLM processes.
