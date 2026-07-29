# Addendum — Corrected Workspace Relationship of R1 and R2 (append-only; supersession by pointer)
**Date:** 2026-07-19 · **Authority:** operator statement (ROOT), relayed 2026-07-19 · **Applies to:** `P1N_VALIDATION_2026-07-19/` (R1 files) and `R2_SECOND_WITNESS/` (R2 files).

Operator correction of record: **R1 was executed in the original workspace and continuing session in which P0 and the early reconstruction work were created. R2 was executed in a separate workspace with separate conversational context.** R2 encountered R1's persisted outputs on disk but did not inherit R1's conversational state.

Consequences, per ROOT-outranks-artifact:

1. R1's header line — "This session is a different validator than the one that produced the replay (separate context, no access to that session's memory)" — is **superseded as to workspace relationship**. R1 is the originating workspace auditing itself against the primaries: an internal-coherence witness, not an independent external one. The mechanical results in R1 are unaffected; only the independence characterization changes.
2. R2's description of R1 as an "R1 validation session" with independent standing is likewise corrected. R2's own standing is unchanged: it is the cold, portability witness — no conversational inheritance, derivation from persisted evidence alone.
3. Corrected joint interpretation: R1 tests whether the method remains coherent inside the evolving workspace that created it; R2 tests whether another workspace can reproduce the result from persisted evidence without the original session context. They are complementary witnesses, not duplicate runs.

Neither file is rewritten (append-only). Future sessions must read R1 and R2 through this addendum.
