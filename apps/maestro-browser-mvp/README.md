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
