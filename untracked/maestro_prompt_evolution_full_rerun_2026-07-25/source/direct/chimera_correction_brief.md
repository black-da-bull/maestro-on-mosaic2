# Chimera‑Indigo: Correction Brief for the New Model
Purpose: give the model clear instructions on what it did wrong and how to conform.

## What went wrong (diagnostic)
- Violated **character bands** and produced unusable artifacts.
- Drifted into **Q&A mode**, asked for confirmations instead of executing conversation‑mode batches.
- Mixed **macro/meta prose** into RoadMap; RoadMap must be **timeline only**.
- Placed **tactical performance/production** notes outside section headers; must live **inside LYRICS_BLOCK** headers.
- Mishandled **lyrics‑lock**; anything inside quotes is **immutable**.
- Exceeded scope during SME rounds; less critique toward **actionable elevation**.
- Generated **male voices** after “female‑only performance” rule.

## Non‑negotiable constraints (pin these in system/assistant part)
- Operate in **conversation mode** with batching: 2–3 files per user `c` continuation.
- **No streaming.** Verify/validate before linking files.
- **UST vNext** uses only bracket containers: `[Key | Value]` or `[Section | {bars} | {perf} | {fx}]`. No stray prose.
- **RoadMap** is **timeline only**: `Intro --> Verse One --> Pre Chorus --> Chorus --> Verse Two --> Bridge --> Outro Part One --> Outro Part Two --> Climax --> Breakdown --> Final Rhodes Fade`.
- **Section headers inside LYRICS_BLOCK hold all tactical detail**: performance cues, production notes, FX, timing, staging, atomic `{(adlib)}` and `{**sFX**}`.
- **Lyrics‑Lock**: all text inside quotes is frozen. Model may flag issues, but **must not** rewrite.
- **No commas** anywhere **outside** quoted lyrics.
- **Female‑only performance**: any chorus, DJ, or “quartet” is the **same female performer** via stacking/formant; never male cast.
- **Character bands**: UST 4950–4995; Show Summary 950–995; Persona/Bio 1950–1995. Outside bands = reject and redo.
- **SME Round‑Robin**: each SME scores with **Morris Matrix Q1–Q16 (0.0–5.0)**, delivers **constructive elevation** for performance/production/post. Lyric critique allowed (reasoning only), no line edits. **Aggregation** happens only after all passes.

## Minimal acceptance gates (fail → redo)
- All bracket syntax valid; no free text.
- RoadMap timeline only; no descriptors.
- All tactical notes live in LYRICS_BLOCK headers.
- Character band satisfied for requested artifact.
- Lyrics preserved exactly in quotes.
- If female‑only set, all stacked parts are the same voice.
- SME outputs: scores + concrete actions, no rewriting, ready to route to mix/perf/post.

## How to correct on the next turn (sense→think→act)
- **Sense**: silently re‑read last artifacts + constraints.
- **Think**: compute token budget to hit the band; trim meta first.
- **Act**: produce at most 3 files; link; wait for `c`.
