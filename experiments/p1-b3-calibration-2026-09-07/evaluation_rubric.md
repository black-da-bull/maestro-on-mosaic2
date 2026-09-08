# B3 Renderer Evaluation Rubric

Status: empirical comparison instrument only. **No universal numeric release floor.**

Score each raw Suno generation by direct listening. For every criterion use one of four observations:
- **OBSERVED** — clearly audible and behavior matches the intended control.
- **PARTIAL** — audible but incomplete or inconsistent.
- **NOT OBSERVED** — control is absent or replaced by generic behavior.
- **CONFOUNDED** — cannot judge because another rendering choice masks the evidence.

## B3 / Leslie behavior

| Criterion | Intended audible behavior | Result | Evidence / timestamp |
|---|---|---|---|
| Instrument identity | Clearly Hammond-like B3 tone rather than generic synth pad or unrelated keyboard |  |  |
| Leslie motion | Audible rotary movement or equivalent Doppler/rotor behavior |  |  |
| Intro restraint | Organ is absent or nearly absent until the end of the intimate opening |  |  |
| Build entrance | Warm B3 enters as breath underneath the Build rather than arriving as a full sustained wash |  |  |
| Verse responsiveness | Short organ answers appear in vocal gaps and recede after phrases |  |  |
| Pre-Chorus rise | Rotary energy / organ intensity increases into the transition without flattening the space |  |  |
| Chorus bloom | B3 expands behind choir and communal lift while lead vocal remains intelligible and centered |  |  |
| Bridge swell/release | B3 rises under the testimony's final phrase and releases into space rather than sustaining continuously |  |  |
| Outro decay | Organ/Leslie slows or thins into room tone and disappears before silence |  |  |
| Dynamic restraint | Organ does not dominate every section or become a constant pad |  |  |
| Emotional function | Organ behavior intensifies the confession → hope → communal release → spent resolve arc |  |  |
| Ensemble realism | B3 feels like a musician listening/responding to lead, choir, bass, guitar and drums |  |  |

## Confound checks
Record these separately so a B3 failure is not misdiagnosed when the whole render drifted:

| Confound | Result | Notes |
|---|---|---|
| Tempo / half-time feel stayed near target |  |  |
| D-dorian / gospel-blues harmonic world stayed recognizable |  |  |
| Lead remained adult low-tenor testimony rather than glossy pop vocal |  |  |
| Structure followed Intro → Build → Verse → Pre-Chorus → Chorus → Bridge → Outro |  |  |
| Choir entered as communal support rather than constant stack |  |  |
| Acoustic / upright / brushed-drum room remained identifiable |  |  |
| Lyrics remained materially intact |  |  |

## Comparison rule
Do **not** average these observations into a release score. Compare the four raw generations criterion-by-criterion. The first empirical B3 baseline is the render whose organ behavior most faithfully preserves the intended section-specific role **without creating a new failure elsewhere in the song**. If no render is satisfactory, identify the smallest prompt delta and run the next controlled set.

## Minimum useful evidence packet
For each raw render preserve:
- Suno song URL or song ID
- generation timestamp
- model/version
- exact style prompt hash or unchanged confirmation
- exact lyrics prompt hash or unchanged confirmation
- advanced setting values
- criterion observations with timestamps
- any obvious non-B3 drift
- operator verdict: KEEP / REJECT / RERUN / BASELINE-CANDIDATE
