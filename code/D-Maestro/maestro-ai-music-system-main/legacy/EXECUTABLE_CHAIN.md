# Executable Chain — Maestro v5-b (Monolithic RUN)

> The chain is expressed as phased processes composed of atomic work items.  
> The Orchestrator executes one RUN end-to-end with hard gates.

## Phase 0 — Ready State (Dual-Scaffold)
Work items:
- WI.P0.SYSTEM.INIT.R1: Initialize Creative UST scaffold to [NULL].
- WI.P0.SYSTEM.INIT.R2: Initialize Technical UST worksheet to [NULL] across all axes/subkeys.

Definition of Done:
- Both scaffolds exist; run ledger opened; pinset version recorded.

## Phase 1 — Creative Intake (Artist’s Call → Creative UST)
Work items:
- WI.P1.INTAKE.CREATIVE.R1: Store v0.raw (immutable).
- WI.P1.INTAKE.CREATIVE.R2: Map Affect/Intent/Textures into Creative UST (macro/micro only).
- WI.P1.PACKET.ASSEMBLE.R1: Attach Knowledge Spine + SE20 rubric; create Project Packet.

Definition of Done:
- Creative UST populated (allowed NULLs); raw preserved; packet ready for SMEs.

## Phase 2 — Engine Room (Creative → Technical; NULL Hunting)
Work items (per axis):
- WI.P2.{AXIS}.K{range}.R{round}: Primary owner fills scoped subkeys (one sentence each) + bindings + downstream predictions.
- WI.P2.{AXIS}.REVIEW.R{round}: Adjacent reviewers challenge; dissent logged; tie-break invoked if required.

Definition of Done:
- All scoped subkeys non-null for the axis; at least one challenge cycle logged; handoff notes recorded.
- Repeat until all axes complete (no NULLs remain).

## Phase 3 — Meetings (Bindings + Gates)
Work items:
- WI.P3.MEETING.BINDINGS.R1: Verify cross-axis bindings.
- WI.P3.GATES.SEG.R1: Run SEG feasibility checks.
- WI.P3.GATES.GCARD.R1: Run G-Card scoring (>= 7.0 threshold).
- WI.P3.GATES.SE20.R1: Run SE20 checklist; route failures back to Phase 2.
- WI.P3.GATES.LOCK.R1: Verify lyrics-lock compliance.
- WI.P3.GATES.CAP.PRELIM.R1: Preliminary cap feasibility check.

Definition of Done:
- All gates PASS. Any FAIL triggers stop-the-line and emits only diagnostics + missing work items.

## Phase 4 — Promotion + Decompile (Compiler)
Work items:
- WI.P4.PROMOTE.DEDUP.R1: Promote recurring constraints to macro; deduplicate leaves.
- WI.P4.COMPILE.TRIAD.R1: Compile triad artifacts from validated Technical UST.

Definition of Done:
- Compiled artifacts meet cap targets or route to further promotion/dedup work items.

## Phase 5 — Human Delivery
Work items:
- WI.P5.DELIVER.R1: Present triad + telemetry + consensus minutes + verification logs.
- WI.P5.CLOSEOUT.R1: Freeze v1.canon; close run ledger.

Stop-the-line policy:
If any gate fails, the RUN halts and emits only:
- failure diagnostics
- missing work items
- dissent map references
