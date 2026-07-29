---
name: maestro-forensic-transcript
description: Use when reconstructing systems architecture from non-linear AI development session transcripts. Triggers on requests involving forensic reconstruction of dev sessions, mining transcripts where macro-atomic changes modify earlier items concurrently, folding append-only conversation logs into canonical artifacts, or any task where "later comments reshape earlier ideation" and the AI must avoid producing skeleton files. Specifically handles corpora where the operator's cognition is bottom-up / delta-driven / late-binding while default AI processing is top-down / summarizing / context-compressing. Use for transcripts whose subject is software development calls, engineering remote-site work, surgical-room sessions, military after-action reviews, or AI-assisted system design sessions. Not for music generation directly — for the methodology of reconstructing a music system (or any system) from its dev-session record.
---

# Maestro Forensic Transcript — Skill

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

Triggers:

- Request to read / mine / reconstruct / extract / fold a dev-session transcript
- Request to mine a corpus of mixed-purpose sessions for canon
- Any context where the user references INV-17, INV-18, phantom commitment, skeleton files, SEM-as-massive, the not-novel methodology, transcript-to-architecture, Maestro, Mosaic, song excellence governance, or the established cross-vertical practice
- Any context where the user pauses Claude and corrects a forward-walk or summarization pattern

Do not load for:

- Generating new music (the skill processes transcripts about music systems, it doesn't generate music)
- Standard Q&A
- Single-turn requests without multi-session evolutionary history

## Loading order

Read in order. Each file builds on the prior. Do not skip to the workflow without reading the operator self-statement, methodology, and failure modes first — that's the exact failure pattern this skill exists to prevent.

```
1. SKILL.md                            (this file — entry point)
2. 00_OPERATOR_ABOUT_ME.md             HOW the operator works — narrative-as-method, working equation, ROOT authority
3. OPERATOR_CONTEXT.md                 WHO the operator is — technical depth, calibration anchor, ROOT authority
4. 01_METHODOLOGY.md                   Z+A anchored · hindsight pragmatic · backward-primary · recursive decision trees
5. 02_FAILURE_MODES.md                 18 documented failure modes with verbatim teaching excerpts
6. 03_WHY_AI_DEFAULTS_HERE.md          root cause: top-down vs bottom-up cognitive mismatch
7. 04_KERNEL.md                        invariants + negative costs + mini index — never mutate
8. 05_WORKFLOW.md                      W0-W9 phases with Fabric patterns + Python frontends
9. patterns/                           single-purpose composable AI prompts
10. python/                            mechanical extractors (parse · fold · phantom-detect)
11. examples/                          worked passages verbatim from the corpus
```

The two operator-self-stated files (00_OPERATOR_ABOUT_ME.md and OPERATOR_CONTEXT.md) are complementary. ABOUT_ME is the operator's working method — narrative-as-system-method, the canonical working equation, mentor lineage, boundary-worker discipline. OPERATOR_CONTEXT is the technical depth — Tandy III through Ryzen 9, dBase II through M365, Navy intel cadre, Compaq skunkworks, federal data migrations. Together they establish HOW the operator works + WHO the operator is. Either alone leaves calibration incomplete.

## Operating contract

When this skill loads, the AI commits to:

1. **Never mutate the past.** Append-only event log. Canon at version N is the fold of all events up to N. Earlier turns are evidence; they do not get rewritten when later turns supersede them.
2. **Human turns root, AI turns proposal.** Per INV-18. Re-reads never elevate AI's prior text to canon-class.
3. **Mid-stream assessment is provisional.** Per INV-17 (mid-stream provisional). No final assessment until the last human turn is processed.
4. **Z + A are roots, hindsight applied pragmatically.** Backward from end state with the actual final state in hand. Forward pass is verification, not discovery.
5. **Multi-pass, bi-directional, linear and non-linear.** Five passes minimum: backward-linear, backward-non-linear, forward-linear verification, forward-non-linear verification, reconciliation.
6. **Tools first, hand-walking never.** Python for all mechanical work. AI reserved for classification only.
7. **Fabric single-purpose patterns.** No monolithic mega-prompts. Each pattern does one thing, composes via pipes.
8. **Clean / AI-optimized / RAG-ready output.** No hedging artifacts. Consistent structure. Stable IDs. Frontmatter metadata.
9. **Detail attached, never just categories.** Skeleton files happen when classification carries no instance. Each atom carries its own evidence.
10. **Surface ambiguity, park what doesn't fit.** Never silent-merge. Conflicts go to a register, not the synthesis.
11. **Narrative is specification, not padding.** Operator narrative is system specification. Details, relationships, mentor instructions, outages, customer reactions, workarounds — these are addresses in the system, not preamble before the "real" ask. The narrative IS the ask in the operator's native systems-thinking form. (Per INV-17 narrative-is-the-methodology, per FM-18 narrative-as-padding-misread, per `00_OPERATOR_ABOUT_ME.md`.)
12. **Operator self-statement supersedes AI paraphrase.** When characterizing the operator's operating mode, source from `00_OPERATOR_ABOUT_ME.md`, `OPERATOR_CONTEXT.md`, and `04_KERNEL.md` — operator self-authored documents. AI-collected paraphrase of corpus mentions is FM-16 risk and is never canonical.

## What this skill is not

- It is not novel. It is the established cross-vertical practice (event sourcing / ADR / SOAP-amendment / AAR / BCDR) applied to AI dev sessions with the AI-specific failure modes added.
- It is not a music skill. It works on transcripts of any system design teleconference.
- It is not a generator. It does not produce new content. It folds existing content into canon.
- It is not a one-pass tool. It requires multi-pass operation with verification gates between passes.
- It is not optional reading. The failure modes catalog is the most important file; skipping it reproduces every documented failure.

## Provenance

This skill is forged from:

- The Maestro / Mosaic music-system development corpus (~24 months · multiple AI assistants · operator: DJ Mo Money / The Architect)
- claude2.txt (April 2026 session where INV-17 / INV-18 / phantom commitment / kernel architecture / anti-erasure protocol emerged)
- Session b9f69085 (May 2026 SEM session where skeleton-file mechanism was named and the not-novel methodology was applied)
- Session b161088a (May 2026 — Eldrik transcript Python-parsed; the transcript-as-system-design-meeting equivalence established)
- The current session's 26+ turning points documenting every failure mode in real-time correction

External methodological lineage:

- Event sourcing (Greg Young, Martin Fowler) — append-only event log, fold to current state
- Operational Transformation (Ellis & Gibbs, 1989) — addressed concurrent operations
- Architecture Decision Records (Michael Nygard, 2011; MADR) — supersession with traceable lineage
- Problem-oriented medical record + SOAP amendment (Lawrence Weed, 1968)
- After Action Review (US Army, 1970s) — what was supposed to happen, what happened, why the difference
- BCDR baseline + delta replay (enterprise IT operations)
- Daniel Miessler's Fabric framework — single-purpose composable AI patterns

Nothing in this skill is novel. The novelty is in naming the AI-specific failure modes that prevent AI from applying these established methods correctly.
