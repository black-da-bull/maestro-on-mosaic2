---
date: 2026-02-10T13:20:55-06:00
researcher: Maestro v5-b (GPT-5.2 Thinking)
git_commit: null
branch: null
repository: null
topic: "Deep dive into Maestro v5-b, Suno v5 interface points, and the UST schema"
tags: [research, codebase, maestro, suno, ust, schema]
status: complete
last_updated: 2026-02-10
last_updated_by: Maestro v5-b (GPT-5.2 Thinking)
---

# Research: Maestro v5-b, Suno interface points, and the UST schema

**Date**: 2026-02-10T13:20:55-06:00  
**Researcher**: Maestro v5-b (GPT-5.2 Thinking)  
**Git Commit**: null  
**Branch**: null  
**Repository**: null

## Research Question
Deep dive into maestro, suno v5 and the ust schema.

## Summary
This environment contains the Maestro v5-b “cold start” governance pack as a set of markdown templates and canonical outlines.

Maestro v5-b is defined as a phased, work-item-driven pipeline (Phase 0→5) that starts from an artist input (v0.raw), maps it into a Creative UST scaffold, expands that into a fully non-NULL Technical UST across a fixed set of axes, then runs feasibility/quality gates (SEG, G-Card, SE20, CAP, LOCK) before compiling a Suno-facing output (Creative UST + lyrics block) and related capped artifacts.

The “UST schema” exists in two forms:
- Creative UST: a Suno-facing prompt scaffold organized into macro sections (Theory, Voice, Style, Timbre, Performance, Road Map, Post Production) plus an explicit Lyrics Block.
- Technical UST: an internal, addressable hierarchy organized by axes (THY, VOC, STY, TIM, PERF, POST, MAP, LYR) and key/subkey addresses (AXIS.K#.S#).

“Suno v5” specifics are not defined in the mounted pack; the only explicit Suno version reference in the pack is “Suno v4.5 token efficiency” in the CAP section of the Knowledge Spine. The pack does define Suno-facing formatting discipline, an explicit cap strategy, and a “no Suno output without PASS” invariant.

## Detailed Findings

### 1) Maestro v5-b execution model (phases, work items, stop-the-line)
Maestro is expressed as an “Executable Chain” with five phases and a stop-the-line policy.

- Phase 0: Create dual scaffolds (Creative UST initialized to NULL; Technical UST initialized to NULL).  
  Reference: `EXECUTABLE_CHAIN.md:6-13`.

- Phase 1: Store v0.raw immutably; map intent into Creative UST (macro/micro only); assemble the packet with Knowledge Spine and SE20 rubric.  
  Reference: `EXECUTABLE_CHAIN.md:14-22`.

- Phase 2: “NULL hunting” by axis using work items. The owner fills a scoped key-range; adjacent reviewers challenge; dissent is logged; tie-break invoked when required. The phase repeats until all axes have no NULLs remaining.  
  Reference: `EXECUTABLE_CHAIN.md:23-31`.

- Phase 3: Meetings + gates (cross-axis bindings; SEG; G-Card scoring >= 7.0; SE20; LOCK; CAP). Any FAIL halts the run and produces diagnostics + missing work items rather than outputs.  
  Reference: `EXECUTABLE_CHAIN.md:32-43`.

- Phase 4: Promotion + decompile (compiler). Repeated constraints promoted; leaves deduplicated; triad artifacts compiled under caps.  
  Reference: `EXECUTABLE_CHAIN.md:44-51`.

- Phase 5: Human delivery (triad + telemetry + minutes + verification logs) and freeze v1.canon.  
  Reference: `EXECUTABLE_CHAIN.md:52-61`.

Work items have a normalized schema: ID format, ownership, reviewers, evidence requirements, and definition-of-done.  
Reference: `WORK_ITEM_SCHEMA.md:3-13`.

Stop-the-line behavior is reiterated across the chain and playbook: a gate failure produces only diagnostics and missing work items, not a Suno prompt.  
Reference: `EXECUTABLE_CHAIN.md:57-61`; `solution.md:5-7`.

### 2) Council model (who fills what; how disagreement resolves)
Axis ownership is assigned via a pinned Council Matrix. Each axis has a primary owner SME; at least two adjacent reviewers are required; tie-break authority is defined; SEG feasibility overrides taste.

- Ownership + reviewers + tie-break mapping by axis:  
  Reference: `COUNCIL_MATRIX.md:11-21`.

- Council Protocol defines required outputs per work item: read acknowledgement; one-sentence constraint fills with bindings; downstream sensitivity predictions; challenge cycle log; handoff notes.
  Reference: `COUNCIL_PROTOCOL.md:14-20`.

- Disagreement rules include “no smoothing”, SEG physics override, and lyrics-lock override (lock risk stops the line, not tie-break).  
  Reference: `COUNCIL_PROTOCOL.md:21-25`.

### 3) Evidence Contract (what counts as a valid fill and a valid PASS)
The Evidence Contract defines what “evidence” means for individual subkey fills and for phase gates.

Per-subkey fill rules:
- Exactly one sentence per subkey.
- Sentence must encode an operational constraint.
- Sentence must include a source binding (Creative tag, raw line pointer, or downstream binding).
- Owners must add downstream prediction notes.
- Each meaningful fill must survive at least one challenge cycle.

Reference: `EVIDENCE_CONTRACT.md:4-13`.

Per-gate PASS records:
- SEG, G-Card, SE20, CAP, LOCK each have explicit PASS conditions.

Reference: `EVIDENCE_CONTRACT.md:15-20`.

Mandatory logs are enumerated and treated as enforced artifacts: run ledger; work item ledger; dissent map; consensus minutes; gate results; cap report; lock report; telemetry.

Reference: `EVIDENCE_CONTRACT.md:22-30`; templates in `LOG_TEMPLATES.md`.

### 4) Technical UST schema (internal address space)
The Technical UST is a canonical hierarchical outline meant to be “lossless, addressable, reversible, and audit-ready.”  
Reference: `TECHNICAL_UST_CANON.md:1-6`.

Key concepts:
- Global laws include lyrics_lock, addressability, reversibility, nulls-as-signal, and “no Suno output without pass.”
  Reference: `TECHNICAL_UST_CANON.md:19-24`.

- Addressing grammar includes axis/key/subkey IDs and extends down to lyric section/line/word labels.
  Reference: `TECHNICAL_UST_CANON.md:26-33`.

Axes present in the canonical outline:
- THY (Theory), VOC (Vocals), STY (Style), TIM (Timbre), PERF (Performance), POST (Post Production), MAP (Road Map), LYR (Lyrics Block).
  Reference: representative axis definitions at `TECHNICAL_UST_CANON.md:37-110` and continued through the document.

Lyrics axis has governance + structural levels (Sections → Lines → Syllables → Words/Atomic controls).
- LYR.K0 governance fields and atomic “Words” layer:
  Reference: `TECHNICAL_UST_CANON.md:239-267`.

Technical UST attaches validation layers and defines compilation outputs as derived artifacts:
- Outputs include `creative.ust.v5`, `show_summary (960–999 chars)`, and a `suno_ready_prompt (≤4999 chars)`.
  Reference: `TECHNICAL_UST_CANON.md:287-292`.

### 5) Governance monolith in the Technical UST address space (SEG, G-Card, SE20, bindings)
The governance addendum states SEG, G-Card, and SE20 are first-class systems that share the same address space.

- SEG axis enumerates feasibility checks across form, temporal integrity, spectral feasibility, human execution, and policy enforcement.
  Reference: `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md:8-58`.

- G-Card axis enumerates dimensions and includes the pass threshold field “≥7.0.”
  Reference: `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md:60-119`.

- Cross-axis bindings are explicitly non-optional.
  Reference: `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md:190-199`.

- Phase integration guarantee explicitly constrains when “reverse compilation” and “Suno output” may occur.
  Reference: `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md:201-209`.

### 6) Creative UST schema (Suno-facing prompt scaffold)
The Creative UST template is a formatted prompt scaffold with:
- Formatting rules intended to constrain how Suno (or similar prompt parsers) interpret meta vs lyrics.
- Macro blocks: Theory, Voice, Style, Timbre, Performance, Road Map, Post Production.
- A Lyrics Block with per-section headers and quoted lyric lines.

Formatting rules:
- Speaker tags must be outside lyric quotes.
- sFX cues must be wrapped as `** sFX: ... **` and not inside lyric quotes.
- Avoid commas outside lyric quotes (use line breaks/semicolons in meta).

Reference: `CREATIVE_UST_TEMPLATE.txt:1-5`.

Macro block field tags (examples):
- Theory: `[mode]`, `[tonal_center]`, `[meter]`, `[tempo]`, `[chord_color]`.
- Voice: `[register]`, `[delivery]`, `[expression]`, `[layering]`, `[articulation]`.
- Style: `[genre]`, `[intent]`, `[texture]`, `[aesthetic]`.
- Road Map: `[sections]`, `[bars_per_section]`, `[pickups_and_turnarounds]`, `[energy_flow]`, `[section_thesis]`.

Reference: `CREATIVE_UST_TEMPLATE.txt:7-46`.

Lyrics Block conventions:
- Each section includes a structured header (section name, bar count, voice/instrumentation/FX notes) followed by quoted lyric lines and optional (adlib)/(fx) lines.

Reference: `CREATIVE_UST_TEMPLATE.txt:54-91`.

### 7) Suno interface points in the pack (what is explicitly defined)
What is explicitly defined in this pack regarding Suno:
- A hard invariant in Technical UST: “no_suno_output_without_pass.”  
  Reference: `TECHNICAL_UST_CANON.md:19-24`.

- An explicit Suno-facing scaffold (the Creative UST template) plus formatting rules that distinguish meta from sung lyrics.
  Reference: `CREATIVE_UST_TEMPLATE.txt:1-5`.

- A cap strategy for deliverables:
  - Creative UST: 4960–4999 chars
  - Show Summary: 960–999 chars
  - Persona Pack: style <=150 chars; bio 1960–1999 chars

Reference: `context.md:15-18` and `LOG_TEMPLATES.md:79-88`.

What is *not* explicitly defined in this pack:
- Model-specific Suno v5 prompt syntax, feature flags, or constraints beyond the general “Suno-ready prompt” length guidance.
- Any API integration code.

The only explicit Suno version reference in the pack is “Suno v4.5 token efficiency” in the CAP discussion.
Reference: `KNOWLEDGE_SPINE.md:52-56`.

## Code References
- `EXECUTABLE_CHAIN.md:6-61` — Phase model, work items, stop-the-line.
- `WORK_ITEM_SCHEMA.md:3-13` — Work item card fields and definition-of-done.
- `COUNCIL_MATRIX.md:11-21` — Primary owner, reviewers, tie-break per axis.
- `COUNCIL_PROTOCOL.md:14-35` — Challenge cycle requirements, disagreement policy, traceability.
- `EVIDENCE_CONTRACT.md:4-30` — Valid fill rules; pass records; mandatory logs.
- `TECHNICAL_UST_CANON.md:10-33` — Kernel laws and addressing grammar.
- `TECHNICAL_UST_CANON.md:37-267` — Axis inventory; lyrics atomic controls.
- `TECHNICAL_UST_CANON.md:287-292` — Derived outputs including `creative.ust.v5` and `suno_ready_prompt`.
- `TECHNICAL_UST_GOVERNANCE_ADDENDUM.md:8-209` — SEG/G/SE20 axes; bindings; phase guarantee.
- `CREATIVE_UST_TEMPLATE.txt:1-91` — Suno-facing Creative UST scaffold and lyrics block conventions.
- `KNOWLEDGE_SPINE.md:30-56` — Gate definitions + CAP/Suno reference.

## Architecture Documentation
From the mounted cold-start pack, Maestro v5-b is documented as:
- A deterministic pipeline organized into phases, where the Technical UST is treated as an internal worksheet and the Creative UST is treated as the Suno-facing prompt scaffold.
- An addressable schema where every constraint is pinned to an AXIS.K#.S# location.
- A council process enforcing challenge cycles and dissent retention.
- Gate layers that must PASS before any prompt-like output can be emitted.

## Historical Context (from thoughts/)
No `thoughts/` directory was present in this environment; historical context is limited to `MIGRATION_LOG.md`.

- `MIGRATION_LOG.md:3-15` — Describes what became canonical in v5-b (dual-scaffold, work-item model, pinned council/evidence, Creative MAP parity patch) and what was deprecated.

## Related Research
None found in this environment (no other research docs present).

## Open Questions
- Where is `SYSTEM_PROMPT.md` referenced by `MODULE_REGISTRY.md`, and what additional Suno v5-specific rules (if any) exist there.
- Whether any non-doc code exists in the actual repository beyond this mounted pack (no git metadata present here).
- Whether Suno v5 introduces cap targets or parsing rules different from those captured in the Creative UST formatting discipline.
