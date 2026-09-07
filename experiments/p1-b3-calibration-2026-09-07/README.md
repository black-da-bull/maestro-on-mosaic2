# P1 B3 Empirical Calibration — 2026-09-07

Doctrine: **Your Vision. Our Mission.**

Status: **EXPERIMENT CANDIDATE — NOT CANON — NOT A RELEASE THRESHOLD.**

## Purpose
Resolve the first P1 item from `_PROVENANCE/STATE.md`: **empirical B3 baselines**. This run does not treat archival prompt evidence as equivalent to a fresh renderer test. It creates a new Suno-facing triad from the historical D-dorian / 78 BPM Southern Soul × Delta Blues × Gospel Roots Rock fixture and evaluates the raw Suno generations for whether the Hammond B3 / Leslie behavior survives reverse compilation and rendering.

## Authority and preservation
- Lyrics are carried forward verbatim from the historical end-to-end fixture. No lyric rewrite is authorized by this experiment.
- The current output contract is the triad: `show_summary.txt` + `ar_profile.txt` + `creative_ust.txt`.
- Packaging is downstream and may not mutate the frozen triad surfaces.
- This experiment is evidence generation only. A successful render does not promote new runtime law without operator acceptance.

## Controlled variable
The experiment measures **B3/Leslie interpretation**. Hold the following constant across all raw renders:
- model: Suno v5.5
- mode: Custom
- key/mode: D dorian
- tempo/feel: 78 BPM half-time sway
- lyrics: exact triad lyrics
- structure: Intro → Build → Verse → Pre-Chorus → Chorus → Bridge → Outro
- vocal identity: no Voice / Persona / Inspo / Custom Model for the first calibration set
- personalization: disable My Taste / style augmentation for the first calibration set
- advanced controls: identical across renders
- no Studio edits / remastering before scoring

The only intended test target is whether the triad's repeated B3/Leslie control survives into the generated audio.

## Render procedure
1. Open Suno Create in Custom mode and select v5.5.
2. Paste `suno_style_prompt.txt` into Style of Music.
3. Paste `suno_lyrics_prompt.txt` into Lyrics exactly.
4. Use title `P1 B3 Calibration 01`.
5. Generate the normal pair of raw outputs.
6. Use Reuse Prompt with no text or setting changes and generate one additional pair.
7. Preserve all four raw generations before any edits.
8. Record each Suno song URL / ID and score it with `evaluation_rubric.md`.

## What counts as evidence
Evidence is the audible renderer behavior in the four raw generations. Prompt compliance claims must point to the audio. Textual intent alone is not a PASS.

## Promotion rule
Do not promote a B3 baseline automatically. After scoring, compare the four outputs and identify the smallest prompt delta needed. Operator acceptance is required before any experiment result becomes a persisted Maestro baseline.

## Provenance
Historical calibration seed: `artifacts/D-Maestro/sources/eldrik.txt.txt` end-to-end test fixture containing Hammond B3 warm Leslie / B3 Leslie capture / B3 swell behavior.
Current derivative grammar: `maestro-current/02_CREATIVE_UST_TEMPLATE.md`.
Current queue: `_PROVENANCE/STATE.md` P1.
