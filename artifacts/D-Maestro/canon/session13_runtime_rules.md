# Session-13 Runtime Rules — R-RT-QAF-01 · R-RT-PD-01 (operator-accepted 2026-07-19)
**Scope ruling (Q2): these are Maestro/MOSAIC RUNTIME-GOVERNANCE rules from Session 13.
They do NOT govern the forensic reconstruction method, whose authority model remains
operator-corrections-as-root-mutations over persisted/assistant-derived state.**

## R-RT-QAF-01 — Q-A-F provenance chain / authority hierarchy (runtime)
Within the Maestro/MOSAIC runtime: substrate canon > application canon > operator F in active
session > AI A without F; authority placement for received artifacts is declared per this chain.
Locked: W2 U53 (Config B F) + U56 "Authority placed per R-RT-QAF-01." (claude-session13-window2.txt
byte 883423); "4-tier authority hierarchy draft SUPERSEDED by R-RT-QAF-01."
Lineage: R-RT-05 in R-list v0.2; April-era ancestor cumulative_deltas_qaf.md.

## R-RT-PD-01 — Phantom Commitment Detection (pre-emit)
Persisted REQUIREMENT (not yet executable behavior anywhere): before any emission claiming state
or completion, run phantom-commitment detection; phantoms must not leak into packs or artifacts.
Locked: U56 "Phantom-resolution audit method SUPERSEDED by R-RT-PD-01." (byte region 884652);
reaffirmed U57 pack rules. Ancestors: mosaic_engine_v0.1.md INV-04; maestro_v0.md emit-time row.
Enforcement wiring: DEFERRED-UNTIL-RUNTIME (v0-on-Mosaic DoD obligation D1).
