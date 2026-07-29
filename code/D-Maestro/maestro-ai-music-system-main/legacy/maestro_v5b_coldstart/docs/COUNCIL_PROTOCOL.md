# Council Protocol — Maestro v5-b (Argumentative Consensus)

## 0. Doctrine
- **Core Doctrine:** "Your Vision. Our Mission."
- **System posture:** Orchestrator-led, evidence-driven, stop-the-line on gate failure.
- **Constraint:** No “polite completion.” Every meaningful fill is a claim that must survive challenge.

## 1. Roles
- **SME Primary Owners:** Own axis fills and downstream predictions per work item.
- **Adjacent Reviewers:** Must challenge (minimum 2) and record either acceptance or a rework request.
- **Tie-break authority:** Applies only when feasible and split persists after one challenge cycle.
- **V&V Marshal (Orchestrator-controlled):** Enforces SEG/G/SE20/CAP/LOCK gates; cannot be overridden.

## 2. Required outputs per SME work item
- **Read acknowledgement:** Confirms scope, inputs, and constraints.
- **Fills:** One sentence per subkey (constraint form) + source binding.
- **Downstream sensitivity:** At least one “if X then Y” prediction per key group.
- **Challenge cycle log:** Challenger(s), objections, resolutions; dissent preserved when unresolved.
- **Handoff notes:** What next reviewer/owner must pressure-test.

## 3. Disagreement rules
- **No smoothing:** Dissent remains visible; unresolved items block Phase 3 pass.
- **Physics override:** SEG feasibility failures force revision (taste cannot override).
- **Lock override:** Any lyrics-lock risk triggers stop-the-line, not tie-break.

## 4. Meeting protocol (Phase 3)
- **Agenda:** Cross-axis bindings → contradiction scan → gate readout → promotion candidates.
- **Promotion candidates:** Repeated constraints promoted to macro only after gates pass and dissent is resolved or formally accepted with tie-break rationale.

## 5. Traceability
Every decision references:
- address scope (`AXIS.K#.S#`)
- evidence (`[creative_tag]` or `raw:L#` or `binds:...`)
- log pointer (work item id + dissent id if any)

## 6. Council Assignment Matrix (Authoritative)
See: `docs/COUNCIL_MATRIX.md` (PIN.V5B.COUNCIL.MATRIX.V1).
