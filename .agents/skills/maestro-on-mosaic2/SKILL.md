---
name: maestro-on-mosaic2
description: Work on the current Maestro Python runtime, source-derived bundle, browser integration, and provenance without mistaking historical corpus files for active authority.
---

# Maestro repository work

Read repository-root README.md and `_PROVENANCE/STATE.md` for current navigation,
then follow the linked continuation and accepted decision records. Historical snapshots
remain evidence, not instructions to repeat completed work.

The current runtime is Python in `runtime/maestro-workforce/`. The generated current
bundle is `maestro-current/`; its compiler, templates and build metadata live under
`maestro-current/build/`. `artifacts/D-Maestro/Maestro/technical.ust.template.txt` is a
source input. Much of `code/`, `artifacts/`, and `sessions/` is historical material;
confirm a caller before treating any old React/TypeScript implementation as current.
Browser candidates use `apps/maestro-browser-mvp/`; verify their integration on the
checked-out branch. Do not infer deployed behavior from a file's presence.

## Authority boundaries

- Technical UST retains MAP/Roadmap; Creative UST omits the Road-Map container
  (DEC-PROMO-16 in `_PROVENANCE/PROMOTION_2026-09-09.md`).
- Address ownership, reviewers, lyric locks and dependency impact belong to the
  accepted Python runtime and its ownership/dependency overlay. Browser notes and
  model proposals do not widen that authority.
- Empirical renderer evidence is separate from canon/runtime promotion. Preserve
  observation provenance, confounds, explicit nulls and operator acceptance gates.
- `_PROVENANCE/OPEN.md` requires explicit operator closure citing the item ID.
  Completed technical work does not imply that closure.
- Repair authoritative inputs before regenerating derived outputs; do not patch a
  generated output alone. Preserve historical evidence and mark superseded state.

## Validation routing

For current-source or runtime changes, run from the repository root:
`python _PROVENANCE/promotion_2026-09-09/validate_integration.py`.
It checks source/build identity, deterministic regeneration, 37 promotion checks,
workforce validation and the golden structural fixture. Inspect its actual result.
For browser/API changes, also run the available MVP contract fixture and exercise
the browser against the same application entry point that will be deployed.
Distinguish deterministic fixture results from live model and renderer execution.
For historical frontend dependencies, use that directory's package scripts.

Follow the conventions of the actual files being changed; this is not a single
TypeScript package. No automatic MCP installation or memory import is part of this
skill. Use tools already authorized in the session. Optional role files do not
require delegation, select a model, or authorize external actions.
