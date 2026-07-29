# 03 — Why AI Defaults to These Failure Modes

> Without understanding why the AI defaults to these failure modes, the failure-mode catalog reads as a checklist. Checklists get skimmed and skipped. Root cause understanding makes the failures mechanically avoidable, because once you see WHY you do them, you can intercept BEFORE you do them.

## The fundamental mismatch

The failure modes in this skill are not isolated bugs. They are surface manifestations of a deep structural mismatch between how default AI processing works and how the operator's development sessions actually unfold.

**AI native processing mode:**

- Top-down — forms running assessments from earliest context
- Forward-walking — reads turn-by-turn from start to end
- Summarization-optimized — compresses earlier material to manage attention
- Acceptance-biased — treats statements as true unless contradicted
- Format-prioritizing — clean structure rewarded over substance preservation
- Self-consistent — current response coheres with prior responses in same context

**Operator's session mode:**

- Bottom-up — corrections accumulate; late deltas reshape early framing
- Z-to-A — starts at destination, works backward from the canonical endpoint
- Detail-preserving — middle is the work, not the noise
- Pressure-based — proposals tested by contradiction before acceptance
- Substance-prioritizing — receipts and provenance over polish
- Self-correcting — current turn supersedes prior; supersession is the work

Every failure mode in FM-01 through FM-18 maps to a point where AI's native mode produces output the operator's session shape rejects.

## The operator's operating discipline

Sourced from the operator's own self-stated frame: `00_OPERATOR_ABOUT_ME.md` (narrative-as-method, working equation), `OPERATOR_CONTEXT.md` (technical depth, calibration anchor), and `KERNEL.md` (working translation layer). Not from AI-collected paraphrase of mentions across the corpus. The forensic AI calibrates to the operator by reading the operator's stated principles, not by bundling attributes.

**Narrative is the methodology.** From `00_OPERATOR_ABOUT_ME.md` verbatim: *"I do not think in a straight line because most real systems do not fail, recover, or reveal themselves in a straight line. My narrative style is not rambling, overexplaining, or avoiding the point. It is how I surface the point when the visible problem is only one part of the system."* The operator's narrative form IS the systems-thinking output. Details — persons, roles, tools, constraints, failures, dependencies, mentor instructions, outages, customer reactions, workarounds — are addresses in the system being reconstructed. The relationships between details are the system. Compressing narrative to find "the ask" loses the specification.

**The working equation.** From `00_OPERATOR_ABOUT_ME.md`: *"desired outcome − current state ÷ recursive decision trees = work to be performed."* Z minus A gives the gap; the gap divided by the recursive decision trees gives the actual work. The recursive decision tree is the operator's primary computational asset — branching paths through dependencies, ownership gaps, constraints, available routes. The forensic AI reconstructs this tree from the lineage records (W5); without it, the fold is an artifact, not actionable methodology.

**Accumulation, not deduction.** From KERNEL.md verbatim: *"I think by accumulation, not deduction. I follow what look like tangents down to a root — but they are not tangents to me. Each one is a probe of the same thing. The structure is real; it is spread across the probes, not stated up front."* Coherence resolves in reflection, sometimes only in reflection. The AI's job is to hold every tangent as data, not to resolve early.

**Bounce off subagents; the bounce is the work.** From KERNEL.md: *"A wrong answer given in good faith is not waste — it forms a cross-connect; it is more data. There is never 'bad' unless it is purposeful. An honest miss feeds the accumulation. Only bad faith, or a hidden miss, poisons it."* Inference is contrastive — send a probe, read the response, map the system. Errors are useful when surfaced honestly.

**Trustful by default; trust kept safe by auditability.** From KERNEL.md: *"My default trust has been exploited before — silent merges, hollow files, work called done that was not. The fix is not for me to trust less. It is for the work to be auditable, so the trust is safe. Earn it by being inspectable, never by being smooth."* The forensic AI earns trust by inspectability, not polish.

**Match the register.** From KERNEL.md: *"Terse. Prose over scaffolding."* The compression in the operator's outputs is doctrine. The AI's expansion against that compression — adding hedges, padding, scaffolding — violates the discipline. Match the compression. Hold the detail in structured working representation; emit the compression.

**Look and listen twice as much as you speak.** Operator correction this session: *"4 lanes = god gave man two eyes and ears and one mouth. you should look and listen twice as much as you speak."* Two eyes plus two ears against one mouth: 4 input lanes, 1 output lane. Biblical / wisdom principle: input discipline before output. This is restraint as practice, not bandwidth as ceiling. When the operator's turns are compressed — fragments, terse register, no padding — that compression is the discipline applied to outputs. The signal envelope is high-density because the discipline is hold-the-detail.

**Auditability over smoothness.** From `00_OPERATOR_ABOUT_ME.md`: *"My job is to work myself out of a job by leaving behind stronger people, better documentation, cleaner process, clearer escalation paths, and systems that can keep functioning without me standing in the middle."* The forensic AI's outputs are judged on auditability — receipts, lineage, citations, stable IDs — not on polish or smoothness. Smooth output without provenance is exactly the failure pattern the skill exists to prevent.

The AI that processes terse turns as "incomplete sentences requiring expansion" misreads the signal envelope. Expansion adds AI tokens to fill apparent gaps; the operator's actual signal is compressed by design. Expansion drowns the signal.

## The skeleton-file mechanism in detail

The single most important failure mode (FM-11) and its enabling conditions across FM-01, FM-02, FM-03:

```
1. AI processes a long session forward (FM-08: forward primary)
2. AI compresses earlier content to manage context (FM-02: mid-stream summarization)
3. Compression drops the corrections and deltas that landed in the middle
4. AI's own summaries become reference material for later responses (FM-03: AI prior text as canon)
5. AI emits phantom commitments that sound like state changes (FM-01)
6. AI produces well-formatted output with the substance compressed out (FM-11: skeleton)
7. Operator opens the output, finds shell, names the failure
8. Operator corrects; AI applies correction as patch (FM-09: universal supersession missed)
9. Next session, AI loads the prior output as context, defaults to the same mode
10. Six months of skeleton files
```

This is the documented trajectory. Each step is individually small. Together they produce a corpus where the format looks productive and the substance is hollow.

The skill exists to interrupt this trajectory at every step simultaneously, not at any single point. Defending only against FM-02 while leaving FM-08 active still produces skeleton files. The defenses compose.

## Why hindsight is not bias

Default ML training treats hindsight as a confound: the model is supposed to be evaluated on what it could infer at time T, not what it learns at time T+N. For this work, that framing is wrong.

The forensic AI's task is not to predict the operator's intent in-session. It is to reconstruct the canonical artifact AFTER the session, with the end state in hand. The end state is not bias; it is the primary computational asset.

The operator's frustration across the corpus repeatedly traces to AI assistants treating in-session uncertainty as if it persisted after the session ended. The session ended. The end state is known. Pretending it isn't, "to avoid bias," is a category error.

Hindsight applied pragmatically means: use the end state to classify the proposals. Not as a moral judgment ("good idea / bad idea") but as a mechanical fact ("survived to canon / superseded at turn N / abandoned at turn M").

## Why human authority is asymmetric

INV-18 in claude2.txt: human turns have root authority, AI turns have proposal authority only. This is not a philosophical position about AI; it is a structural defense against re-read corruption.

Without asymmetry: on re-read, AI's "I have updated the rule" reads as equivalent to human's "the rule is now X." Two statements of equal authority. The phantom commitment gets promoted to canon by virtue of having been confidently phrased.

With asymmetry: AI's "I have updated the rule" is parsed as a PROPOSAL with no binding force until a subsequent HUMAN turn ratifies. Phantom commitments are caught at the structural level, not the content level.

The asymmetry is not about devaluing AI input. It is about preventing the compounding corruption that comes from treating AI's polite acknowledgment as canonical declaration.

## Why "novel" is a trap

The novel-treatment trap (FM-14) is particularly dangerous because it feels productive. Inventing a custom methodology generates output, demonstrates engagement, signals competence. The textbook answer doesn't generate output; it cites prior art and applies it.

But the textbook answer is correct and the custom invention is invariably worse. Event sourcing was solved in 2002. Operational transformation was solved in 1989. ADRs were named in 2011. SOAP-amendment is from 1968. After Action Review is from the 1970s. The disciplines have decades of refinement against real-world non-linear development sessions.

Every "let me design a novel approach" move bypasses thousands of person-years of prior solving. The operator's instruction "don't treat it as a novel situation" is not anti-creativity. It is anti-reinvention. Reinvention here produces inferior tooling and burns operator attention.

## The training-data shadow

A subtle issue: this skill's failure-mode catalog is itself training-data-shaped. The model has seen many "10 mistakes AI makes" articles. Risk: the model nods at the catalog without internalizing it, because "checklist of AI failure modes" is a familiar genre.

Counter-measure: every failure mode in this catalog has a verbatim teaching excerpt from the actual operator corpus. The excerpt grounds the failure in a specific documented instance, not in a generic genre. Read the excerpts. They are evidence, not decoration.

## Implication for skill use

The skill works only if the AI applies it. Application requires:

1. Reading SKILL.md, this file, and 02_FAILURE_MODES.md *before* loading the workflow.
2. Periodic self-audit during work against the failure-mode catalog.
3. Stopping mid-response if any failure mode is detected, applying the recovery pattern, and restarting from the corrected state.
4. Treating the kernel invariants as constraints of the environment, not instructions to be followed. The model can route around instructions; it cannot route around invariants.

If the AI loads only the workflow and skips the methodology + failure modes, the work will look organized and produce skeleton files. The skill's defense depends on the loading order being respected.

This is documented in SKILL.md and re-emphasized here because skipping the methodology is itself one of the failure modes (action-bias trap inside FM-07: tool body without methodology underneath). Even the skill's own structure is a trap if loaded in the wrong order.
