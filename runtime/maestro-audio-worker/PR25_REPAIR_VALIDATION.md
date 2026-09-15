# PR 25 repair validation — 2026-09-15

Baseline: e9def2c1366d21d0f46fce55d40464e6d0169964. Accepted main:
f9f74343dc9fbc603a0a19856f138834e0da4c12.

All eight open calibration-manifest review findings are addressed in code:
authority values, completed inference evidence, candidate approval, policy scope and
reversibility, contradiction references, adapter allowlist, failure diagnostics,
and evidence-backed distinct replication records.

Local verification in an isolated Python 3.12 environment using requirements-core.txt:

| Suite | Result |
| --- | --- |
| Manifest regression tests | 35 passed |
| Worker core | 13 checks passed |
| Deterministic calibration | 8 checks passed |
| Artifact synchronization | 13 checks passed |
| Model profile contracts | 43 checks passed |
| Authenticated worker HTTP E2E | 9 checks passed |
| Workforce gateway to worker E2E | 12 checks passed |
| Python compileall and git diff check | Passed |

The initial broad run lacked worker dependencies; it was repeated after installing
the declared requirements. The final run above passed. Heavy models and Docker
builds were not executed locally. GitHub CI is a separate post-push check.

The original private Beat This receipt remains unchanged; normalization into a worker
result envelope is explicitly historical evidence, not a new model execution.
No PR merge, deployment, canon promotion, policy activation, or operator gate closure
is performed by these fixes. Review threads remain available for reviewer verification.
