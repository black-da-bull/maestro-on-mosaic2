# P0 Workforce Registry — 2026-09-07

Doctrine: **Your Vision. Our Mission.**
Operator: Morris / Mo.
Parent state: promoted Maestro v5-c integration at `cfbe537e8175ac93aa857333d3c73f642d433da5`.
Work branch: `p0-workforce-registry-2026-09-07`.

## Objective

Materialize the first post-promotion P0 item: **the executable 13-audio-worker instances / workforce registry**.

This work item does not implement the next P0 item (Technical UST axis/key ownership + crossstream dependency overlay) and does not begin the golden structural-interpretation fixture.

## Authority and source basis

The current 13-audio-worker roster is taken from `maestro-current/04_COUNCIL_TOPOLOGY.md` and the current execution scaffold:

1. Mo
2. Canon Orchestrator
3. Megazord Orchestrator
4. Sibling Architect
5. Metro Craft
6. Melody Scout
7. Sage
8. Alan
9. Dave
10. Vanessa
11. Analog Confessor
12. Anva
13. Eldrik

The four visual roles remain outside the audio workforce. Historical Isla/Huan experiments remain historical. Historical `Melony` is not silently conflated with the current `Melody Scout` seat.

The employee shape is governed by the supplied `canonical_employee_module_spec.yaml`, whose safe sequence is employee schema -> canonical 13 instances -> workforce registry contract.

## Persisted runtime surface

`runtime/maestro-workforce/`

- `canonical_employee_module_spec.yaml` — the bounded employee-module schema.
- `canonical_13_employee_instances.yaml` — canonical roster/common contract and exact worker-file references.
- `employee_workforce_registry_contract.yaml` — executable registry law and dispatch boundary.
- `instances/01_mo.yaml` ... `instances/13_eldrik.yaml` — 13 bounded employee deltas.
- `workforce_runtime.py` — executable list/show/resolve/dispatch-envelope loader.
- `validate_workforce.py` — fail-closed P0 validator.
- `README.md` — invocation and scope boundary.

The runtime expands each worker delta against the common contract into the full employee schema, including domain authority, explicit non-authority, I/O, readable/writable zones, null handling, challenge/escalation, conflict precedence, reverse-pass limits, artifact duties, controller-substitution prohibitions, and Song Excellence reference duties.

## Runtime-enforced in this P0 slice

The executable Python runtime/validator enforces or exercises:

- exactly 13 audio workers;
- unique stable employee IDs;
- exact current roster/order;
- exclusion of the four visual-module roles;
- worker/controller separation;
- no direct worker phase-gating authority;
- reverse-pass participation only after definitive Technical UST lock;
- no inferred Technical UST axis/key ownership;
- registry count/roster consistency;
- explicit deferral of axis/key ownership and crossstream dependency overlay;
- exact controller action boundary (`route`, `validate`, `log`, `gate`, `freeze`, `promote`, `package`);
- Mo runtime worker may not impersonate the live operator;
- worker resolution by stable ID, role name, or declared alias;
- bounded dispatch-envelope construction;
- write-target rejection when outside the selected worker's declared writable zones.

A pre-persistence local smoke run returned:

`PASS: 13 bounded audio workers materialized; registry/runtime smoke clean; ownership overlay deferred`

The same staged semantic files were persisted. Repository-native post-persistence comparison verifies that the final branch delta is isolated to `runtime/maestro-workforce/` plus this provenance record; `maestro-current` was restored byte-for-byte to the promoted main tree after a temporary staging integration exposed a manifest-hash risk.

## Runtime truth — not overclaimed

Materialized now:

- bounded worker definitions;
- workforce registry;
- worker resolution;
- dispatch-envelope runtime;
- workforce validation.

Not materialized by this item:

- model/provider execution adapter that actually invokes independent worker models;
- Technical UST axis/key ownership overlay;
- crossstream dependency graph;
- autonomous multi-worker deliberation engine;
- golden structural-interpretation run.

Therefore "executable workers" in this checkpoint means executable, machine-loadable worker modules and dispatch contracts. It does **not** mean thirteen autonomous model processes have been launched.

## Integrity correction during this work item

The first staging commit placed the workforce inside `maestro-current` and modified builder/validator metadata before the generated bundle manifest had been regenerated from the exact committed bytes. That state was not promoted or merged.

The correction was architectural rather than cosmetic:

1. restore `maestro-current` exactly to the promoted main tree;
2. reuse the already-committed workforce subtree by Git tree identity;
3. relocate it to `runtime/maestro-workforce/`;
4. verify the branch diff no longer changes any `maestro-current` member.

This avoids a false PASS based on a stale generated-bundle manifest.

## Worker-level scope

The registry intentionally records broad lawful labor domains but **does not freeze Technical UST address ownership**. Exact axis/key/subkey ownership belongs to the next P0 item and must be derived against the current Technical UST topology rather than inferred from persona labels.

## P0 item verdict

**MATERIALIZED — REGISTRY/INSTANCE SLICE COMPLETE.**

Persistence rung: repository branch candidate.
Runtime-enforcement rung: executable registry/dispatch/validator only, as bounded above.
Production merge status: pending final branch review/merge.

## Next lawful action

**P0 item 2: materialize Technical UST ownership + crossstream dependency overlay.**

That next item must bind these 13 employee IDs to lawful Technical UST axes/keys/subkeys and dependency edges without changing their already-materialized identity/non-authority contract unless source evidence requires a patch.

Do not begin the golden structural-interpretation fixture until that overlay is materialized and validated.
