# Maestro Browser MVP

A creator-facing vertical slice for one Maestro project: intake, axis working notes, runtime-resolved Technical UST dispatch, validation, lock state, JSON import/export, and renderer-adherence evidence inspection.

## Authority model

The browser does **not** decide who owns a Technical UST axis or address. It queries the accepted `runtime/maestro-workforce` Technical UST runtime, which resolves exact address ownership and required reviewers from `technical_ust_ownership_dependency_overlay.yaml`.

The browser therefore treats its eight visible axis cards as working-note/navigation surfaces only. They are not ownership declarations and cannot widen worker authority.

## Renderer evidence boundary

`/api/adherence-matrix` exposes a versioned empirical renderer-adherence matrix derived from the current P1 calibration state. Renderer observations remain adapter evidence. They cannot automatically mutate Technical UST or promote themselves into Maestro canon/runtime law.

## Runtime API

- `GET /api/health` — confirms runtime and renderer-adapter availability.
- `GET /api/addresses` — lists exact Technical UST address bindings with runtime-resolved owner/reviewers.
- `GET /api/resolve?address=...` — resolves one address through the accepted overlay.
- `POST /api/dispatch` — creates an address-authorized bounded workforce dispatch.
- `POST /api/change-preview` — exercises accepted authority, lyric-lock, and dependency-impact rules without committing browser state automatically.
- `GET /api/adherence-matrix` — returns versioned renderer-adherence controls and evidence status.
- `POST /api/evidence/validate` — validates an empirical observation while explicitly returning `technical_ust_mutation: false` and `canon_promotion: false`.

This application remains isolated from the historical corpus. It uses current repository/runtime state as evidence and does not promote recovered or empirical material into canon by itself.

## Intake drafting

`POST /api/compile` accepts project_name, song_title, vision, lyrics and instrumental.
The browser's Draft Technical UST action submits the current intake, displays per-address
proposals, owner/reviewer bindings and explicit nulls, and persists the draft locally
alongside the unchanged lyric source. Editing intake invalidates its draft. A response
for an older intake is discarded. Missing Gateway configuration returns 503 without
changing project state. Model responses are proposals, never a canon promotion or lock.

The server uses AI_GATEWAY_API_KEY (or VERCEL_OIDC_TOKEN) and the configured
MAESTRO_INTERPRETATION_MODEL. Credentials remain server-side. This MVP is a single-model
specialist simulation with ownership checks, not autonomous workers or completed musical
quality evaluation. The local lock is a browser snapshot, not Technical UST acceptance.

Repository-root app.py delegates to runtime/maestro-workforce/app.py. Both entry points
serve the same maintained browser. Run `python runtime/maestro-workforce/build_browser.py`
after browser edits to regenerate the standalone deployment's inline public/index.html;
CI checks parity. Run the MVP fixture and test_intake_contract.py for API checks.
