# SESSION TRANSFER PACKAGE — MANIFEST

**Bundle ID:** `STP.MAESTRO_MOSAIC.2026-05-06`
**Generated:** 2026-05-06
**Source session:** Maestro/Mosaic Dev Recovery, dev-window mode, dual-state stance, oriented toward finalization
**Purpose:** Lossless cold-load of current working state into a new project workspace, without requiring transcript replay or operator re-explanation
**Authority:** This package preserves operator-confirmed canon and clearly demarcates CANDIDATE / NEEDS SOURCE / FROZEN material. It does NOT promote anything to canon that was not already so in the source session.

---

## 0. Read this file first

This package contains everything required to restore the working frame, working state, and pending decisions of the source session in a new workspace. It is structured so the loader can:

1. Read it in order, top to bottom.
2. Stop after `01_BOOT.md` if the only need is to resume operator dialogue.
3. Continue through the remaining files only if substantive work is to resume.

The package is lossless in the sense that no operator-confirmed fact, frame correction, or decision pointer has been omitted. It is not lossless in the sense of being a full transcript — see `99_TRANSCRIPT_POINTER.md` for that.

---

## 1. Load order

| # | File | Read when | Bytes target | Loss tolerance |
|---|---|---|---|---|
| 00 | `00_MANIFEST.md` | always (this file) | small | none |
| 01 | `01_BOOT.md` | always — establishes operating frame | small | none |
| 02 | `02_OPERATOR_CONFIRMED_CANON.md` | always — what is settled and how | medium | none |
| 03 | `03_CURRENT_STATE.md` | always — where the work is right now | medium | none |
| 04 | `04_OPEN_DECISIONS_AND_BLOCKERS.md` | always — what the operator must resolve | medium | none |
| 05 | `05_CORPUS_INDEX.md` | when working with files | medium | none |
| 06 | `06_FORBIDDEN_ACTIONS.md` | always — what not to do | small | none |
| 07 | `07_FRAME_CORRECTIONS_LIVE.md` | always — fresh framings not yet in artifacts | small | none |
| 08 | `08_DELIVERED_ARTIFACTS_THIS_SESSION.md` | for continuity audit | small | none |
| 99 | `99_TRANSCRIPT_POINTER.md` | when full session detail is needed | small | none |

---

## 2. What this package replaces vs supplements

**Replaces** in the new workspace context (load these first):
- session brief
- "what is going on" preamble
- operating-frame setup
- failure-hierarchy briefing
- source-role briefing

**Supplements** existing project workspace material (read these AFTER project files):
- The dev workspace files (`/mnt/project/*`) remain controlling.
- `WIRING_RECOVERY_V_AND_V_v0.md` (WRVV) remains the controlling V&V doc.
- `SOURCE_GAP_LIST_v0.1.md` (SGL) — if present — remains the controlling gap ledger.
- This package adds operator framings and session-state context that those files do not carry.

---

## 3. Authority hierarchy (load-time)

When this package and another source conflict, resolution order is:

1. **Operator turn in the new session** — direct correction overrides everything.
2. **WRVV.v0 §10 forbidden actions** — these are hard locks.
3. **SOURCE_GAP_LIST_v0.1** — frozen gaps are not reconstructable.
4. **Files6 control pack** (SDG.v0.1, SEC.v4.5, SLR.v0, CMA.v0, MMR.v0, RTFA.v0) — controlling for their respective domains per operator declaration.
5. **This package** — preserves session state and operator framings.
6. **Files4–5** — substrate-aware candidate emergence.
7. **Files1–3** — ancestor baseline; superseded where files4–6 disagree.
8. **Birth certificate Zero-Day Restore Pack** (§V) — Claude-side restore canon.
9. **Diagnostic diagrams** — never canon.

---

## 4. Stop conditions for the loader

Do not proceed past `01_BOOT.md` without the operator's instruction if any of the following are true:

- The new workspace does not contain `WIRING_RECOVERY_V_AND_V_v0.md` or equivalent V&V doc.
- The new workspace does not contain at least the files6 control pack (SDG / SEC / SLR / CMA / MMR / RTFA).
- The operator has not signaled what task is to resume.

In these cases, the loader's first response is to surface the gap and ask, not to synthesize forward from this package alone.

---

## 5. Integrity

This package is text-only and human-readable. No binary state, no model-specific format. It loads on any model. It is the package; the model is the hardware.
