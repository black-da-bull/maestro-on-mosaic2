# Run It To Me — Maestro Triad Renderer Calibration

**Date:** 2026-09-08  
**Status:** calibration evidence; not canon; no promotion decision.  
**Doctrine:** Your Vision. Our Mission.

## Objective
Use the five preserved Suno stem exports as a controlled evidence family to test how effectively renderer-facing Maestro controls survive into audio. This calibration deliberately separates measurable prompt-to-audio adherence from unsupported semantic claims.

## Source family and provenance
The family is: cover → fresh A → Style B → Style C → Style D. Each ZIP was hashed before analysis. The stem MP3 metadata also preserves the Creative UST in `lyrics-eng`, allowing exact prompt recovery without re-downloading or reconstructing it from memory.

- Cover ZIP SHA-256: `505bf2f0bd115bf7aec4b10fa16ae48aa8eee051f341a3a7c5ec30b9a1a7ed4c`
- Fresh A ZIP SHA-256: `532e03856abdd39322ba1a0bd30fb43a3f916a79554931d31ab56e48d9509df1`
- Style B ZIP SHA-256: `6f6862bdc8c0e30ee6c5b9cdc2692e4f9888c85777d2904e90fb2b0f910e1e5d`
- Style C ZIP SHA-256: `924e7242d4b439081d3e8d48e2fc10819ea1bea91f176796a41a7873432bb7f5`
- Style D ZIP SHA-256: `f7ab2004a029726da08bbaf8ebedfd0c1d802244c160928da6571c83c0151a49`

## Prompt recovery finding
Cover and Fresh A have the same Creative UST byte-for-byte: SHA-256 `ad59202386c78ab6d3d42bc8b7ab71d0e8304b446b40114b86229797ba8084f2`. Style B/C/D share a second identical Creative UST: SHA-256 `8798eb896787fb50179195383290b2747072f16dd5caf1a6a27feddb9d11fde6`. The substantive directives are the same; the B/C/D form moves `[Style]`, `[Timbre]`, and `[Performance]` before `[LYRICS NARRATIVE]`, whereas Cover/Fresh A place those blocks after the narrative. The separate Suno Style-box / Show Summary text is not stored in these stem metadata and remains a separate provenance field.

## Analysis method
The calibration uses the supplied stems directly, so no source-separation model is needed. Audio was downmixed only for analysis buses at 16 kHz. Measurements include rhythm autocorrelation/tempo families, chroma/key profile estimation, independent MIDI pitch-class cross-checks, spectral-band energy, stem activity/onset rates, vocal pitch-range proxies, dynamic contrast, lead/BGV activity relationships, lead/accompaniment energy relationships, and novelty-based structural segmentation. Exact semantic timbre labels such as “dobro” or “gospel organ” are not promoted from signal features alone.

## Core results

| Render | Duration | Tempo evidence | Tonal estimate | D rank | Bass <100 Hz | Guitar activity | BGV activity | Lead↔band corr | Dynamics |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| cover | 336.9s | 156.2 / 78.1 / 38.3 (0.2% nearest error) | D# minor | 4 | 0.81 | 0.40 | 0.33 | -0.41 | 12.7 dB |
| fresh_A | 287.8s | 45.7 / 133.9 / 69.4 (11.0% nearest error) | D# major | 6 | 0.90 | 0.30 | 0.21 | -0.48 | 13.1 dB |
| style_B | 252.8s | 78.1 / 156.2 / 38.3 (0.2% nearest error) | G# major | 5 | 0.76 | 0.35 | 0.37 | -0.24 | 14.9 dB |
| style_C | 272.9s | 35.4 / 144.2 / 46.9 (7.5% nearest error) | A# major | 5 | 0.79 | 0.11 | 0.27 | -0.33 | 13.3 dB |
| style_D | 291.5s | 35.4 / 72.1 / 144.2 (7.5% nearest error) | D# major | 4 | 0.63 | 0.63 | 0.24 | -0.53 | 10.5 dB |

## Criterion-level calibration verdicts

### 1. Exact tonal-center control — NOT OBSERVED
The Creative UST specifies tonal center D. Audio chroma does not place D first in any render, and the independent MIDI note distributions agree that D is not the dominant pitch class. Estimated centers vary across D#/G#/A# regions. This is the clearest failure of exact Theory adherence in the five-output family.

### 2. Exact tempo control — PARTIAL; relative half/double-time behavior is stronger
Cover and Style B show dominant 78/156 BPM evidence. Style C and D cluster near 72/144, while Fresh A is slower near 69/134. The absolute 78 BPM target therefore drifts, but the approximate 1:2 half/double relationship survives more consistently than the exact number. This supports treating relational performance grammar and exact numeric tempo as separate controls.

### 3. 808 / blockbuster low-end intent — OBSERVED
The Bass stems devote roughly 63–90% of analyzed spectral power below 100 Hz across the family. The low-end directive is one of the strongest cross-render invariants.

### 4. Guitar presence versus guitar-role consistency — PRESENT BUT STYLE-SENSITIVE
A Guitar stem exists in every render, but activity varies sharply: about 0.11 in Style C versus 0.63 in Style D. The instrument survives, but its prominence is not stabilized by the repeated Creative UST alone.

### 5. Choir / call-and-response behavior — GENERALLY SUPPORTED
Every render contains a separate Backing Vocals stem. Lead/BGV energy correlations are low or negative, and each render contains non-trivial BGV-only activity. This is consistent with responsive/alternating support rather than simple constant doubling. Exact section placement still requires section-aligned lyric or listening evidence.

### 6. Band listening / responsive accompaniment — STRONG PROXY OBSERVATION
Lead-vocal versus guitar/keys/synth energy correlations are negative in every render (approximately -0.24 to -0.53). As a signal-level proxy, the accompaniment repeatedly makes room when the lead is active and rises into vocal space, matching the intended conversational/live-interplay behavior better than a constant pad model.

### 7. Dynamic lift — OBSERVED, VARIABLE
Whole-render p90–p10 RMS contrast ranges roughly 10.5–14.9 dB. Style B is the most dynamically contrasted in this set; Style D is the flattest. Dynamic behavior exists across all five, but magnitude is style/render-sensitive.

### 8. Named timbres, lyric-word preservation, exact section mapping, and vocal identity — OPEN
Signal descriptors can prove presence, spectral behavior, timing, and interaction, but they do not by themselves prove labels such as “overdriven slide dobro,” “gospel organ,” or “outlaw mystique.” Word-for-word lyric preservation requires ASR/listening evidence. Speaker identity requires a stronger speaker-embedding or direct-listening comparator. Novelty segmentation finds multi-section form, but section names should not be assigned without lyric/timestamp evidence.

## What B/C/D prove about the triad surfaces
Styles B/C/D carry the same Creative UST bytes yet differ materially in duration, tonal center, guitar prominence, backing-vocal overlap, dynamic contrast, and rhythm behavior. Because the operator changed the external Style prompt across these renders, the set is valid evidence that the Style surface materially participates in the rendered outcome. It does **not** by itself assign each difference to a specific Style phrase because the exact four external Style-box texts are not embedded in the exports and stochastic renderer variance is still present.

## Calibration conclusion
The triad is neither “working” nor “not working” as one binary. The evidence shows **layer-specific effectiveness**. Low-end intent, backing-vocal separation, responsive accompaniment, and half/double-time relational behavior survive well. Exact tonal-center control is weak in this family. Exact tempo is intermittent. Instrument prominence and dynamic magnitude remain highly render/style sensitive. This is enough evidence to replace prompt-only validation with a measured triad-adherence matrix.

## Next lawful experiment
Use Poster Two Deux as the independent replication corpus with the same metric definitions and thresholds. Do not change the harness after seeing Poster Two results unless the change is versioned and the Run It To Me calibration is preserved. After replication, promote only criteria that survive both work windows; preserve song-specific behavior as local evidence.