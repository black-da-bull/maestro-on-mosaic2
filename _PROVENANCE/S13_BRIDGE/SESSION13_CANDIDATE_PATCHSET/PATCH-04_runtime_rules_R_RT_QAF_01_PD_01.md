# PATCH-04 — Runtime Rule Cards: R-RT-QAF-01 and R-RT-PD-01 (CANDIDATE)
**Status: CANDIDATE (rung: proposed). New additive file; reversible by deletion.**
These two rules reached the runtime-enforced rung *within session 13's own governance* (SM13-W2-33) and were never persisted (V1). This file is their persisted rule-card form.

## R-RT-QAF-01 — Q-A-F provenance chain / authority hierarchy
- **Rule:** authority ordering = substrate canon > application canon > operator F in active session > AI A without F. Authority placement for any received artifact must be declared per this chain.
- **Locked by:** W2 U53 operator F (Config B → v0.2 becomes CONFIG B FIRM CANON) + W2 U56 live use: "Authority placed per R-RT-QAF-01." (`claude-session13-window2.txt` byte 883423) and "4-tier authority hierarchy draft SUPERSEDED by R-RT-QAF-01."
- **Lineage:** proposed as R-RT-05 in R-list v0.2 (U52 context); ancestors in persisted drafts: `cumulative_deltas_qaf.md` (Q-A-F ledger practice, April era).
- **Relation to method register:** consistent with M4 / ROOT-over-PROPOSAL; QAF adds the substrate>application ordering above the human/AI split.

## R-RT-PD-01 — Phantom Commitment Detection (pre-emit)
- **Rule:** before any emission claiming state or completion, run phantom-commitment detection; phantom commitments must not leak into packs or artifacts.
- **Locked by:** W2 U56: "Phantom-resolution audit method SUPERSEDED by R-RT-PD-01." (byte region 884652); reaffirmed U57 pack rules ("Phantom commitments must not leak into the pack … per R-RT-PD-01").
- **Lineage:** behavioral ancestry operator turns U31/U43/U45/U47; persisted ancestors: `mosaic_engine_v0.1.md` (INV-04 emit-time phantom detection), `maestro_v0.md` ("Phantom commitments blocked at emit time").

## Scope note
FIRM as members of R-list v0.2 CONFIG B canon (see PATCH-01 payload for the full R-RT group). Enforcement wiring into a running runtime is DEFERRED-UNTIL-RUNTIME (see SESSION13_TEST_PLAN.yaml); this file persists the rules, it does not claim they now execute anywhere.
