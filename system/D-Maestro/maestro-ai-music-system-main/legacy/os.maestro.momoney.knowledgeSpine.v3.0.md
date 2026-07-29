# MoMoney Knowledge Spine — v3.0 SME Integration


## Domains & Lexicon
Primary Domains: AI music orchestration (Suno v4.5 UST), node–edge workflow, multi‑phase V&V, SME confrontation, session decomposition (KPAI)
Adjunct Domains: persona/profile extraction, guardrail engineering, control-systems analogies, VQ-codec limits, SWOT/fishbone
Canonical Lexicon: UST, master.json, Prime‑Directive, Road‑Map (bars), Macro/Micro/Tactical, round‑robin, ejection, consensus threshold, KPAI, ToT/CoT/CRISPE, Telemetry, Threat hooks, few‑shots, guardrails, compression, deltas

## Methods & Frameworks
- KPAI Session Decomposition → Node/Edge mapping
- Trees-of-Thought (3 branches) with self-consistency
- Fishbone & 5-Whys for root-cause on failure modes
- Scansion/prosody analysis for lyric meter & stress
- Mini-SWOT within creative variants A/B/C
- Compression Engine: elevate repeats to metadata; (repeat) notation; enforce bracket/comma rules

## Verification & Validation (V&V)
Macro: structure order, persona alignment, policies/guardrails
Micro: sentence-level clarity, terminology, style/format compliance
Tactical: Prime‑Directive SOP, bar counts, FX/phone scene, kick/sub, mastering headroom, tool capability fit
V&V Log Template:
  - Issues found →
  - Fixes applied →
  - Residual risks →

## Handoff Protocol
1) Role 1 emits master.project.json + context_state.json → Role 2 validates mapping; if fail, Role 1 repairs links (delta noted).
2) Role 2 emits UST_A/B/C + telemetry → Role 3 runs confrontation + gates; if fail, return to Role 2 with annotated deltas; else freeze and package.

## KPIs
- Schema validity ≥99.5% and artifact link coverage ≥98%
- First-pass validator success ≥90% (UST)
- Consensus within ≤3 rounds in ≥85% cases
- Post-consensus defect rate ≤2%
- Compression savings ≥15% with zero rule breaks

## Failure Modes & Mitigation
- Orphaned artifacts → relink via schema keys
- Prose leak into creative layer → governance filter
- Format drift → UST lint + guardrail re-application
- Gridlock → tie-break policy; fallback to variant with highest Macro pass + shortest delta

## Legacy (preserved)
# knowledge_spine.momoney (v4.1)

## A. Universal Suno Template (UST) — Working Rules
- Section order is strict. Ad-libs only in parentheses and must be literal vocal sounds.
- Dialogue-first development: sections refined via ToD before final UST.
- Token budget: keep < 4800 chars; compress narrative above arrangement notes if needed.

## B. Prompting Principles (Suno v4.5)
- Narrative-style prompts outperform bare tag lists; paint scene + emotional arc.
- Micro-dynamics matter: specify delivery, phrasing, articulation.
- Use explicit section headers; describe transitions and builds in prose under each header.

## C. Persona Tuning Loop (Concise SOP)
1. Identify clean vocal segment (no shimmer/artifacts).
2. Crop → create persona stub (name + target timbre/delivery).
3. Re-prompt with similar structure/tags.
4. Evaluate → if improved timbre or cadence appears, re-crop and iterate.
5. Maintain persona versions; roll back if artifacts creep in.

## D. Meta-Tag Grammar (Examples)
- `#gospel` `#southern_gothic` `#808_roll` `#female_vocal_lead` `#chopped` `#screwed` `#reverb_swell`
- Use tags to reinforce UST prose, not replace it.

## E. Validation & QA Checks
- **UST Syntax**: order, headings, ad-lib rule pass/fail.
- **Adherence Score**: match between user brief → UST fields (0–1).
- **Persona Fidelity**: vocal tone/delivery continuity vs. persona stub (0–1).
- **Artifact Risk**: flag shimmer/muffle risk based on FX density + stacking.

## F. Dialogue Patterns (Reusable)
- **Menu Prompt**: “Choose A/B/C: (A) tighten lyrics arc, (B) re-voice delivery, (C) retag style. Recommended: _X_ because _Y_."
- **SME Challenge**: “You must state 2 claims and defend them; inconsistency = ejection.”
- **Consensus Gate**: “When score ≥ threshold, freeze roster; emit consensus notes.”

## G. UST Skeleton (for quick drafting)
[Theory] → [Voice] → [Lyrics Narrative] → [Intro] → [Verse 1] → [Pre-Chorus] → [Chorus] → [Verse 2] → [Bridge] → [Chorus 2] → [Outro] → [Style] → [Timbre] → [Performance] → [Post Production] → [Outro Directive] → ▸ LYRICS BLOCK