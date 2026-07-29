# Creative UST — Current Template v0.2 (O-16 derivation)
**Derived meso surface — a producer's session sheet executing inside Suno's macro lyrics box.
Compiled from a LOCKED Technical UST via FOIL reverse-pass, concurrently with Show Summary and
Bio/A&R (never sequential patches). Carries full lyric preservation + local performance control;
does NOT carry the system's global explanatory burden.**

## Budgets (DISC-04: 5000 = rounded era statement of ≤~4990)
Creative UST ≤5000 chars (CAP band 4960–4999) · Show Summary ≤1000 · A&R Style ≤150, Profile ≤2000.
Character savings are fuel for nuance, not the goal. No genericization for convenience.

## Structure (END-era shell; Y-3 freeze + M13)
Consolidated metacontainers first — Theory · VocalPersona · AestheticIntent · Timbre · Performance —
then the Lyrics block. NO Road-Map block (forbidden legacy construct): section order lives in
`Performance.execution` and in the lyric section headers. `[End]` is the terminal MARKER (not an
axis). Intro and Outro are named sections; fade-in/fade-out behavior belongs in their section-level
performance instructions (M13).

## Container rules (grounded in the v4.5.5 staging floor)
No commas outside quoted lyric blocks · variable format Single / A;B / A OR B ·
lyric header `[section | bars | v: vocal notes | s: style notes | sFx ...]` ·
line order "quoted lyric" → (adlib) → **SFX** · standalone adlibs/SFX consolidate onto the
preceding lyric line · semicolons inside quoted lyrics force line splits ·
syllable rule per DEC-25 (below).

## Syllable / format rule (DEC-25 — style-conditioned, supersedes the fixed-band OQ)
The syllable rule is a BREATH-PATTERN rule, jointly a format rule and a bar-count-accuracy rule.
It varies by style and delivery: a cipher artist (Eminem/Twista class) and a gospel funeral dirge
carry DIFFERENT lyric-block format displays. The 6–10 (rubric) and 6–11 (v4.5.x) bands are era
instances of this rule, not the rule. Each project's style profile sets its breath-pattern band and
display format; deviations log as Sacred Imperfection with breath/stress/performance justification.

## Performance-spacing transformation (DEC-26)
Input lyrics normally arrive in literature/poetry form. Creative UST derivation MUST transform the
display to VOCAL PERFORMANCE SPACING (breath points, bar alignment, delivery grouping) without
altering the locked words — lyric lock binds words; spacing/display is the transformable layer.

## MATERIALIZED TEMPLATE (O16C — imported, not summarized)
Sources (hash-verified): canonical shell `artifacts/HYDRA/creative_ust_canonical_shell.md`
(md5 `2adf028eb4632ed6b78ec639dee43a6f` — mandatory containers/field-set/syntax/handling/character-efficiency rules,
END-era: no Road-Map block, crew tags removed, execution order in [Performance]) + working
scaffold `artifacts/D-Maestro/Maestro/creative.ust.template.txt` (md5 `7b03d390da3012c0a1c856064ac589c6`).
Migration applied: [Voice]→[Voices] + `performers` field (shell canon); [Post Production]→
[Post-Production]; Style gains `era`/`focus`; Performance gains `touch`/`phrasing ops`;
scaffold's "6–10 SYLLABLE" cue = era instance of DEC-25 (style-conditioned). Full scaffold:

### Canonical field set (shell, mandatory)
[Theory]: mode · tonal center · meter · tempo · chord color
[Voices]: performers · register · delivery · expression · layering · articulation
[Style]: genre · era · intent · texture · aesthetic · focus
[Timbre]: drum tone · bass tone · keyboard tone · guitar tone · fx palette · vocal tone
[Performance]: execution · gesture · rhythm handling · touch · phrasing ops
[Post-Production]: mastering · mix notes · automation priorities · cleanup rules
Syntax: `[field | content]` · section header `[Title | (n) bars | performance notes | production cues]`
· line `"lyric", (adlib) ** sfx: cue **` · terminal `[End]`.
Handling: notation ≠ promotion; repeat notation only for exact repeated blocks after upstream
classification; local unique detail stays local; recurring performer identity → [Voices];
character reduction alone is not success.

### Working scaffold (full, migrated from the proven template)
```text
[Theory]
[mode | INSERT MODE]
[tonal_center | INSERT ROOT NOTE]
[meter | INSERT METER WITH groove modifiers]
[tempo | INSERT TEMPO WITH transitions if applicable]
[chord_color | DESCRIBE chord usage, e.g., gospel sus9 AND add11 WITH modal tension]

[Voices]
[register | DESCRIBE LEAD VOICE AND RANGE WITH supporting textures]
[delivery | INSERT cadence type, e.g., Southern sermon cadence WITH blues phrasing]
[expression | WHISPER-TO-BELT arcs OR falsetto confession arcs]
[layering | CHOIR STACKS, chipmunk FX, stereo breath echoes, etc.]
[articulation | INSERT features like AAVE vowel slides OR gospel melisma]

[Style]
[genre | Country Trap Gospel Revival OR Southern Gothic Soul × Americana]
[intent | WHAT STORY THIS TRACK TELLS — grief, survival, baptism, etc.]
[texture | lap steel swells, lo-fi vinyl hiss, ambient gospel pads, etc.]
[aesthetic | cinematic OR torchlight revival vibe OR radio prayer booth style]

[Timbre]
[drum tone | DESCRIBE – e.g., lo-fi stomp loops WITH trap swing]
[bass tone | INSERT – Moog subbass OR upright bowed bass]
[keyboard tone | muted Rhodes OR gospel Hammond pad swirl]
[guitar tone | slide OR lap steel WITH delay OR reverb tail]
[fx palette | tape hiss; thunder crack; preacher echoes; crowd murmur; reverse decays]
[vocal tone | smoky baritone; layered falsetto; whispery lead WITH choir wash]

[Performance]
[execution | LIST STRUCTURE, e.g., Verse 1 → Chorus → Verse 2 → Bridge → Final Chorus → Outro]
[gesture | stomp-claps; breath gaps; preacher yell-ins; choir bounce]
[rhythm_handling | triplet drag groove WITH half-time chorus shift OR pocket-tight push flow]
[adlibs | “Lawd,” “mmm-hmm,” “say that,” “revived,” etc.]

[Post-Production]
[mix | mono verse; stereo choir; analog plate OR cassette compression]
[mastering | glue comp; reverb swells; airband tilt EQ; gospel wideners]
[transition | vinyl hiss tails; tape stops; crowd bleed; risers]

▸ LYRICS BLOCK

[Intro | X bars | lead type; vocal FX | instrumentation | FX notes]
“INSERT LINES”
(adlib | INSERT IF NEEDED)
(fx | INSERT FX CUES IF NEEDED)

[Verse 1 | X bars | tone description | instrumentation | swing/feel]
"INSERT LINE (breath-pattern band per style profile — DEC-25)"
"INSERT NEXT LINE"
(fx | OPTIONAL)
(adlib | OPTIONAL)

[Chorus | X bars | harmonized OR solo OR chipmunk lead]
"INSERT HOOK LINE"
"REPEAT WITH VARIATION"
(choir | CALL-AND-RESPONSE)
(fx | REVERB SWELL OR SUB DROP)

[Bridge | X bars | tone shift | dynamic arc]
"INSERT REFLECTIVE OR PEAK LINE"
"INSERT RESPONSE"
(fx | THUNDER OR REVERSE ECHO)

[Verse 2 | X bars | continuation OR new character POV]
"INSERT STORY EXPANSION LINE"
"INSERT VISUAL PHRASE OR METAPHOR"

[Final Chorus | X bars | FULL LIFT]
"REPRISE HOOK"
"CALLBACK TO EARLY LINE"
"INSERT CLOSURE LINE"
(choir | “Hallelujah” or gospel belt)

[Outro | X bars | fade FX; spoken word; vinyl drag]
"INSERT FADEOUT LINE OR ADLIB"


[End]
```

## Lyric lock
Quoted lyrics are immutable after blow-up intake. Unauthorized lyric change = stop-the-line +
auto-fail of the production gate regardless of composite (Lyric Change Compliance).

## Era layer — v5-b coldstart template (registered beside M13, not harmonized; O16D fold)
**PATCH.CREATIVE.UST.MAP.V1** (package `v5-b.coldstart.1`, 2026-01-23; CHANGELOG + MIGRATION_LOG +
`templates/CREATIVE_UST_TEMPLATE.txt` sha256 `e192d29da2a1b63173e7897355bf8ffcad001963fdf049ab4eb7854ca77701d3`):
the v5b era INSERTED a [Road Map] block between [Performance] and [Post Production] — the
"Creative MAP parity patch" — holding sections / bars_per_section / pickups_and_turnarounds /
energy_flow / section_thesis. M13 (later stratum, operator-ruled) REMOVES the block and re-homes
its functions: timing → LYR section headers; structure-reservation → Performance.execution. Both
records preserved; chronology governs — the CURRENT template has NO Road-Map block. The v5b
template corroborates current rules elsewhere: its [Formatting Rules] head-block (speaker tags
outside lyric quotes · sFX wrapped `** sFX: … **` · no commas outside quotes · no singer names
inside lyric quotes) and its "6–10 SYLLABLE" cue (era instance of DEC-25). Precise era cap bands
(SYSTEM_PROMPT.md + recovered runtime/context.md): Creative 4960–4999 · Show Summary 960–999 ·
A&R style ≤150 + bio 1960–1999 — sharpening the rounded ≤1000/≤2000 statements above, same
rounding pattern DISC-04 established for 5000≈4960–4999.
