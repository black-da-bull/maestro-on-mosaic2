# PATCH-02 — v5c Canon Register: Supersession-Context Annotation (CANDIDATE)
**Status: CANDIDATE (rung: proposed). Annotation, not deletion. Reversible by removing the annotation block.**

## Target artifacts
`artifacts/D-Maestro/canon/Maestro_v5c_Canonical_Root.md` · `Maestro_v5c_Canonical_Spine.md` · `Maestro_v5c_Lineage_and_Delta_Ledger.md` · `Maestro_v5c_Conflict_and_Open_Question_Register.md`

## Proposed change (identical block PREPENDED to each file; diff = insert-only at line 1)
```text
> [SUPERSESSION CONTEXT — added 2026-07-19, operator-accepted only if force-closed]
> Session 13 (May 2026, operator-ratified) rules that v5/v5b/v5c are FAILED-RECREATION
> tracks and that v4.5.5 is the last WORKING anchor (SM13-W2-34/U57; SM13-W1-27/U34).
> This register predates or runs parallel to that ruling and contains ZERO references
> to v4.5.5 (V1, confirmed R1+R2 2026-07-19). Read as historical/diagnostic lineage,
> not as current destination canon. Destination canon: R-list v0.2 / CONFIG B FIRM
> (see _PROVENANCE/S13_BRIDGE/SESSION13_CANDIDATE_PATCHSET/PATCH-01).
```

## Anchors
U57 verbatim ("versioon 4.5.5 is the last working version…", "version 5 was a poc/wip that failed") @ `claude-session13-window2.txt` bytes 899848 / 900026. U34/U32 W1 rulings ("version 5 is pre-mosaic…") @ `claud3.txt` byte region 376732+. V1 zero-occurrence evidence: R1 §6 + R2 §5.

## What this patch does NOT do
Does not delete, rewrite, or demote the register's content; does not touch the zip or PDF canon members (MF-5); does not close the SEG-name collision (elicitation item E-7).
