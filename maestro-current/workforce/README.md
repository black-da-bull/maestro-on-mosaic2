# Maestro P0 Workforce Runtime

This directory materializes the accepted **13 audio workers** as bounded runtime employee descriptors plus a machine-callable registry and dispatch-envelope loader.

It intentionally does **not** implement the next P0 item: Technical UST axis/key ownership and crossstream dependency mapping. A dispatch envelope therefore names the selected worker and its broad domain but never proves canonical address ownership.

Files:
- `canonical_employee_module_spec.yaml` — source schema for one bounded employee module.
- `canonical_13_employee_instances.yaml` — exactly 13 current audio-worker instances.
- `employee_workforce_registry_contract.yaml` — registry law and runtime boundary.
- `workforce_runtime.py` — list/show/dispatch-envelope CLI.
- `validate_workforce.py` — fail-closed P0 validator.

Smoke:
```bash
python workforce/validate_workforce.py
python workforce/workforce_runtime.py list
python workforce/workforce_runtime.py show Anva
python workforce/workforce_runtime.py dispatch Dave --task "evaluate pocket readability" --output groove_objection
```

The four visual-module roles remain outside this audio runtime. Historical Isla/Huan and Melony records remain historical strata and are not silently added or conflated.
