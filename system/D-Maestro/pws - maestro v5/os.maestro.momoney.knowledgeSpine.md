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
