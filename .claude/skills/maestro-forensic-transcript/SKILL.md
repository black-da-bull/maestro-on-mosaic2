---
name: maestro-forensic-transcript
description: Use when reconstructing systems architecture from non-linear AI development session transcripts. Triggers on requests involving forensic reconstruction of dev sessions, mining transcripts where macro-atomic changes modify earlier items concurrently, folding append-only conversation logs into canonical artifacts, or any task where "later comments reshape earlier ideation" and the AI must avoid producing skeleton files. Specifically handles corpora where the operator's cognition is bottom-up / delta-driven / late-binding while default AI processing is top-down / summarizing / context-compressing. Use for transcripts whose subject is software development calls, engineering remote-site work, surgical-room sessions, military after-action reviews, or AI-assisted system design sessions. Not for music generation directly — for the methodology of reconstructing a music system (or any system) from its dev-session record.
---

# Maestro Forensic Transcript — Skill · v1.1

**v1.1 (2026-07-19).** Fold of v1.0 + the 2026-07-16/19 lessons layer (LEDGER M1–M11, validation MF-1–6). v1.0 preserved verbatim as `SKILL_v1_ORIGINAL.md` — supersession by pointer, never rewrite. Changelog at end.

This skill teaches an AI how to read non-linear development session transcripts without producing skeleton files. It is not a music skill. It is a transcript-to-architecture skill that happens to have been forged in the Maestro music-system corpus, where the failure modes were named and documented across six months of operator-corrected sessions.

## What this skill does

Folds an append-only conversation log into a canonical architectural artifact, using the established cross-vertical discipline (event sourcing · ADR with supersession · SOAP-amendment · After Action Review · BCDR baseline+delta replay) rather than treating the problem as novel.

The skill is not a tool. It is the operating frame, the failure-mode catalog, the patterns, and the worked examples needed to do this work without repeating the documented failures.

## Why this skill exists

The default AI processing mode is structurally misaligned with non-linear development sessions:

- AI processes top-down · operator's sessions evolve bottom-up
- AI compresses for context management · operator's middle IS the work
- AI treats its own prior text as canon on re-read · only human turns have root authority
- AI summarizes mid-stream to manage attention · the corrections live in the middle and the assessment is not final until the last human turn is processed

Without explicit teaching that names this misalignment, every new AI session repeats every failure documented in the prior corpus. The skill exists to break that cycle by carrying the failure-mode catalog forward as loaded reference, not as discoverable hindsight.

## When to load

Triggers: request to read / mine / reconstruct / extract / fold a dev-session transcript; mining a corpus of mixed-purpose sessions for canon; any context referencing INV-17, INV-18, phantom commitment, skeleton files, the not-novel methodology, transcript-to-architecture, Maestro, Mosaic, or the established cross-vertical practice; any context where the operator pauses the AI and corrects a forward-walk or summarization pattern.

Do not load for: generating new music; standard Q&A; single-turn requests without multi-session evolutionary history.

## Loading order

Read in order. Each file builds on the prior. Do not skip to the workflow without the operator self-statement, methodology, and failure modes first — that is the exact failure pattern this skill exists to prevent (FM-07).

```
 1. SKILL.md                      (this file — entry point)
 2. 00_OPERATOR_ABOUT_ME.md       HOW the operator works — recovered kernel + verbatim fragments
 3. OPERATOR_CONTEXT.md           WHO the operator is — thin reconstruction, SOURCE_PENDING marked
 4. 01_METHODOLOGY.md             Z+A anchored · hindsight pragmatic · backward-primary · decision trees
 5. 02_FAILURE_MODES.md           18 failure modes w/ verbatim excerpts + 2026-07 field notes
 6. 03_WHY_AI_DEFAULTS_HERE.md    root cause (FOUND DRAFT, verbatim)
 7. 04_KERNEL.md                  invariants + negative costs + mini index — never mutate
 8. 05_WORKFLOW.md                W0–W9 with pattern + python frontends
 9. 06_LESSONS_LEARNED_2026-07.md the v1.1 update layer (M1–M11, MF-1–6, rulings in force)
10. patterns/ · python/ · examples/ · state_snapshot_2026-07-19/
```

**Component status is declared, not implied.** See `MANIFEST.yaml` and `README_FIRST.md`: originals, the recovered kernel, and reconstructions are labeled per file. Found originals outrank reconstructions on discovery (DEC-03 search continues). The v1.0 package shipped as SKILL.md alone with 9 of 10 components missing — the skill instantiating its own skeleton failure mode. This package repairs that honestly rather than silently.

## Operating contract

When this skill loads, the AI commits to:

1. **Never mutate the past.** Append-only event log. Canon at version N is the fold of all events up to N. Earlier turns are evidence; they do not get rewritten when later turns supersede them.
2. **Human turns root, AI turns proposal — with influence acknowledged.** Per Revised INV-18 (carried here per O-02; v1.0 carried the original only): *"Human turns hold root authority over intent and canon. AI turns hold influence over the operator's working model… Neither can be discarded during re-read… Flag phantom commitments as model corruptions."* Re-reads never elevate AI's prior text to canon-class.
3. **Mid-stream assessment is provisional.** Per INV-17. No final assessment until the last human turn is processed.
4. **Z + A are roots, hindsight applied pragmatically.** Backward from end state with the actual final state in hand. Forward pass is verification, not discovery.
5. **Multi-pass, bi-directional, linear and non-linear.** Five passes minimum: backward-linear, backward-non-linear, forward-linear verification, forward-non-linear verification, reconciliation.
6. **Tools first, hand-walking never.** Python for all mechanical work. AI reserved for classification only. Every metric and script used in a run is persisted with the run (FM-15/MF-2).
7. **Fabric single-purpose patterns.** No monolithic mega-prompts. Each pattern does one thing, composes via pipes.
8. **Clean / AI-optimized / RAG-ready output.** No hedging artifacts. Consistent structure. Stable IDs. Frontmatter metadata. Normalizations declared (MF-1), quote conventions declared (MF-4).
9. **Detail attached, never just categories.** Skeleton files happen when classification carries no instance. Each atom carries its own evidence (fold invariant F2, fail-closed).
10. **Surface ambiguity, park what doesn't fit.** Never silent-merge. Conflicts go to a register, not the synthesis. Closure only by operator statement citing the ID.
11. **Narrative is specification, not padding.** Operator narrative is system specification — details are addresses in the system. (INV-17 narrative-is-the-methodology; FM-18; `00_OPERATOR_ABOUT_ME.md`.)
12. **Operator self-statement supersedes AI paraphrase.** Source operator characterization from `00_OPERATOR_ABOUT_ME.md`, `OPERATOR_CONTEXT.md`, `04_KERNEL.md` — never AI-collected paraphrase (FM-16).
13. **Coverage counts every operator act.** Rendered user turns AND tool-mediated decisions ([mediated], M8) AND attachment events (MF-3) AND assistant-tail embeds (REC class, O-14). Per-chunk operator-delta counts reconcile against full text (M4).
14. **State ladder on every claim.** conversational < proposed < accepted < operative < persisted < runtime-enforced. Name the rung reached and the dependents touched, or the change is not integrated (M9/DEC-08). Nothing operative lives only in conversation (M1).
15. **Session close = the six E's** (M3) + continuation packet. State travels as an ATP, phantom-free (R-RT-PD-01); the pack is a copy, the SSOT is the operator's `_PROVENANCE\` folder (M11).
16. **Elicitation protocol.** Operator decisions via interactive multiple-choice + Other, batches 3–5, ≤15/round, context attached — never a page of prose questions (M6).
17. **Calibrate before scaling; start narrow.** One small verifiable case first; corpus sweeps begin with the most-corrected session, then STOP for operator validation (M9).
18. **The precedence rule is never an action limiter.** Operator conversational input outranks structured AI output on conflict — regenerate the structured output, never the reverse; and act, structure, implement freely within that rule (M4, operator-authoritative).

## What this skill is not

Not novel (established cross-vertical practice + AI-specific failure modes). Not a music skill. Not a generator — it folds existing content into canon. Not a one-pass tool. Not optional reading — the failure-mode catalog is the most important file; skipping it reproduces every documented failure.

## Provenance

Forged from: the Maestro / Mosaic music-system development corpus (~24 months · multiple AI assistants · operator: DJ Mo Money / The Architect); claud2.txt — April 2026 session, exported May 12–14 (DEC-01 annotation; v1.0 said "April 2026 session" alone) — where INV-17 / INV-18 / Revised INV-18 / phantom commitment / kernel architecture emerged; session 13 (May 2026, two windows — R-INV-07, R-RT-QAF-01, R-RT-PD-01 [FIRM]; the no-parse flagship; validated by replay 2026-07-16 and independent reproduction 2026-07-19, verdict PASS); session b9f69085 (May 2026 SEM session — skeleton-file mechanism named; mapping unverified, O-04); session b161088a (Eldrik Python parse; mapping unverified, O-04); the 2026-07-16 reconstruction session (M1–M11) and the 2026-07-19 P1N validation (MF-1–6).

External lineage: event sourcing (Young, Fowler) · Operational Transformation (Ellis & Gibbs 1989) · ADR (Nygard 2011; MADR) · problem-oriented medical record + SOAP amendment (Weed 1968) · After Action Review (US Army 1970s) · BCDR baseline+delta replay · Fabric single-purpose patterns (Miessler). Nothing here is novel; the contribution is naming the AI-specific failure modes that prevent AI from applying these methods correctly.

## Changelog v1.0 → v1.1 (2026-07-19)

- Contract #2 now carries **Revised INV-18** verbatim (O-02 discharged in-package; v1.0 carried original only).
- Contracts #13–#18 added: full coverage enumeration (M4/M8/MF-3/O-14), rung-naming (M9/DEC-08/M1), six E's + ATP close (M3/M11), elicitation (M6), calibration/narrow start (M9), precedence-not-limiter (M4).
- Contract #6 extended: persist metrics/scripts with the run (MF-2).
- Contract #8 extended: declare normalizations and quote conventions (MF-1/MF-4).
- Provenance: DEC-01 dating annotation; session-ID mappings marked unverified (O-04); validation record added.
- Loading order: component status declared via MANIFEST; 06 lessons layer added; missing-original rule (found outranks reconstruction) stated.
