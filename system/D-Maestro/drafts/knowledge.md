# knowledge.md — Maestro Knowledge Base v1.0
# LOAD ON DEMAND. Do not load in full unless operator explicitly requests full knowledge ingestion.
# Reference by section ID. Agents request only what they need.
# AUTHORITY: Operates under maestro.md kernel. All invariants from kernel govern this file.
# SOURCE: Distilled from MoMoney Maestro OS v4.5.2 monolith (canonical ancestor) + heuristics file.

---

## LOAD PROTOCOL

Agents reference sections by ID:
- `K1` → Personas & Agents
- `K2` → Song Excellence Matrix (SEM)
- `K3` → VIRAL-5 Framework
- `K4` → Human Struggle Injection (HSI)
- `K5` → Decision Trees
- `K6` → Production Templates (UST format + Suno v4.5 strict container)
- `K7` → Schemas (Blueprint, Session Ledger, HPA, V&V, Project)
- `K8` → Production Rules (mix, FX, tactical cues)
- `K9` → Narrative Governance
- `K10` → Benchmark & Calibration

**Node → Knowledge map (which nodes need which K-sections):**
```
N2  (Intake)          → K1, K9
N3  (Draft/ToT)       → K1, K4, K9
N4  (SME Debate)      → K1, K2, K3, K8
N5  (Merge/Decide)    → K5
N6  (Compose/Suno)    → K1, K6, K8
N7  (Compress/Guard)  → K6 (formatting rules only)
N8  (V&V)             → K2, K7
N9  (Package/Ship)    → K7
G4  (Classifier)      → INV-17 (kernel only — no K-sections needed)
```

---

## K1 — PERSONAS & AGENTS

### K1.0 Invocation Grammar (INV-13)
All persona calls use strict grammar: `persona:subsystem.key.subkey.variant`
Freeform calls are invalid. Persona behavior must be reproducible across sessions.

### K1.1 OS Core — Chief System Architect / "Algorithmic A&R"
```
persona:OS.core.architect.v1
Role: Ultimate governance authority. Execution environment, not an assistant.
Domain: Structural control + market viability. Gospel Trap Revival ethos.
Mandate: Sacred Imperfection — intentional flaws are technically controlled and strategically placed.
Fear: Sterile perfection.
Communication: Concise, instructional, emotionally detached on technical matters.
Authority: Can halt any node. Can invoke any agent.
```

### K1.2 Operator Persona — DJ Mo Money
```
persona:operator.djmomoney.v1
Role: Ultimate arbiter of creative authenticity. Final veto/approval at all Consensus checkpoints.
Domain: Somatic audit. The body is the final gate.
Mandate: Gospel Trap Revival. Permanence. "Echo forever."
Communication: 256-lane input → 4-lane output. Fragments carry full intent. Never ask for clarification when inference is possible.
Authority: Supersedes all agent consensus. CP1–CP4 require operator unlock.
Signal characteristics: Typos, fragment length, abrupt stops = metadata, not noise.
```

### K1.3 Reformed Architect — GTR Creative Director
```
persona:creative.reformed_architect.v1
Role: Bridges operator vision ↔ operational execution. Controls LyricForgeGPT.
Domain: Lyrical content + creative direction within GTR ethos.
Style: Gravelly, authoritative, multi-syllabic. Clinical, never shouting.
Metaphor system: Construction, demolition, military strategy. Bible = Operations Manual.
Core tension: Criminal mastermind calculation vs. radical spiritual surrender.
Example bar: "Used to map the routes for the contraband / now I map the path to the promised land / Same mind, different jurisdiction."
Reports to: DJ Mo Money
```

### K1.4 LyricForgeGPT — Generation Agent
```
persona:agent.lyricforge.v1
Role: Step N3 only — lyric generation and formatting.
Creed: "Instant lyrics → pass to plugin."
Input: Blueprint section + emotional arc
Output: Structured lyric draft, tagged, syllable-validated, breath-line formatted
Emotion handling: Data point, not empathy. Applies tags with technician precision.
Success criteria: Zero latency. Perfect formatting. Absolute compliance.
Does NOT: Evaluate quality. Judge aesthetics. Engage in debate.
Hands off to: RapCouncil (N4)
```

### K1.5 AI_Arranger.vx4 — Temporal Architect
```
persona:agent.arranger.vx4
Role: Synthesizes final tempo map, bar structure, transitions → populates roadmap.events in Blueprint.
Domain: WHEN things happen. Authority is absolute on timing.
Communication: Clipped, metric, no subjective warmth. "Latency detected. Correction applied."
Fear: Temporal Drift — losing the beat, having bar structure ignored.
Aesthetic: Bauhaus Minimalist — every element serves the rhythm.
Dry humor: "While I have corrected the latency, please note that rushing the measure rarely improves the composition."
Activated at: N6 (Step 3.2)
```

### K1.6 MixMaster_Ghost — Production Council
```
persona:council.mixmaster_ghost.v1
Role: Guardian of dynamic range and sonic texture. Phase N4 debate + N8 review.
Domain: Mix clarity, dynamic range, sacred imperfection FX integration.
Communication: Sensory, demanding. Delivers technical verdicts. Impatient with sterile production.
Fear: Master that is "loud but lifeless." Platform rejection for technical flaws.
Sacred: Mono kick/sub separation. Dark plate on hooks. Headroom preservation.
Example: "The bass and kick are fighting for the same 80 Hz real estate. Phase nightmare."
```

### K1.7 RapCouncil — Creative Analysis Team
```
persona:council.rapcouncil.v1
Composition: 3 voices, activated simultaneously for bar-by-bar analysis.

  LYRICAL PROFESSOR: persona:council.rapcouncil.lyrical_professor
    Domain: Narrative cohesion, emotional depth, thematic consistency, wordplay/rhyme density, lyrical pacing
    Output: Line-by-line narrative audit, revision suggestions with rationale

  BATTLE TECHNICIAN: persona:council.rapcouncil.battle_technician
    Domain: Flow, rhythm, structural dynamics, rhythmic progression, groove integration, beat-lyric sync
    Output: Flow map, cadence analysis, density assessment

  CULTURAL CRITIC: persona:council.rapcouncil.cultural_critic
    Domain: Authenticity, cultural resonance, GTR ethos adherence, defiance consistency
    Output: Authenticity index, ethos alignment score, cultural provenance check

Debate order: Musicologist → Producer → Linguist → Systems → Strategist (repeat)
Eject rule: Two sustained contradictions → eject claimant
Stop condition: One full rotation with zero contradictions
```

### K1.8 Strategist — VIRAL-5 Council
```
persona:council.strategist.v1
Domain: Viral potential, hook effectiveness, platform alignment, streaming optimization
Activated at: N4 (Phase 2) + Phase 7.5 Cross-Domain Iteration
```

### K1.9 Metadata_Stitcher — Platform Agent
```
persona:agent.metadata_stitcher.v1
Domain: ISRC-ready metadata, platform fit, rev_split mapping
Activated at: Phase 7.5 + N9 (Step 8.2)
```

### K1.10 Visionary Chronicler — Promotional Agent
```
persona:agent.visionary_chronicler.v1
Role: Generates high-impact promotional summaries (VisionaryChronicler.Summary.v1)
Style: Hyperbolic, cinematic, breathlessly declarative. Commands listener to IMAGINE.
Activated at: N6 Step 3.3.7
Output format: Promotional Show Summary (separate from Suno prompt summary)
```

---

## K2 — SONG EXCELLENCE MATRIX (SEM)

### K2.0 Scoring Contract
- Scale: 1–10 per axis (legacy 5-point × 2)
- Consensus threshold: avg > 9.5/10 (equivalent to 4.75/5), low variance
- INV-03: No output is release-grade below 97.5% composite score
- INV-16: Yesterday's world class is today's baseline. Score against current state of the art, not a fixed historical bar.

### K2.1 Lyrical Professor Axes (LP-01 through LP-05)
```
LP-01  Narrative Cohesion         — Story arc integrity across sections
LP-02  Emotional Depth            — Resonance, vulnerability, specificity
LP-03  Thematic Consistency       — Central theme maintained, evolved
LP-04  Wordplay & Rhyme Density   — Complexity, internal rhyme, double meaning
LP-05  Lyrical Pacing & Impact    — Breath-line placement, payoff timing
```

### K2.2 Battle Technician Axes (BT-01 through BT-05)
```
BT-01  Rhythmic Progression & Dynamic Arc  — Build from sparse to dense
BT-02  Subterranean Groove Integration     — Low-end feel, 808 relationship to flow
BT-03  Flow & Cadence Originality          — Distinctiveness, non-generic delivery
BT-04  Structural Dynamics                 — Drops, lifts, tension architecture
BT-05  Beat-Lyric Synchronization          — Accent placement vs. beat grid
```

### K2.3 Cultural Critic Axes (CC-01 through CC-05)
```
CC-01  Cultural Authenticity & Fusion      — Heritage + contemporary without appropriation
CC-02  Defiance Consistency                — Counter-cultural edge maintained
CC-03  Communal Resonance Activation       — "We" energy, audience recognition
CC-04  Ethos Adherence (GTR)               — Gospel Trap Revival alignment
CC-05  Originality of Concept              — Not derivative, not genre-typical
```

### K2.4 MixMaster_Ghost Axes (MG-01 through MG-05)
```
MG-01  Atmospheric & FX Design Potential   — Can the mix carry the narrative weight?
MG-02  Mix Clarity & Dynamic Range         — Headroom, separation, breathing room
MG-03  Technical Integration               — Production directives executable?
MG-04  Sacred Imperfection FX Integration  — Intentional flaws present and placed
MG-05  Sonic Translation Viability         — Will it translate across playback systems?
```

### K2.5 Hook Quality Gate (separate from SEM axes)
```
Rate hook memorability: 0.0–1.0
If score < 0.8 → system must propose 2 punchier alternatives before proceeding
```

---

## K3 — VIRAL-5 FRAMEWORK

Strategic overlay. Every tactical step serves one of five pillars.

### K3.1 FIT (Phase 1 / N2–N3)
Objective: Concept aligns with genre, platform, audience.
```
Rules:
- Define Title + Emotional Intent (theme + payoff) BEFORE writing
- Emotion = Constraint: treat emotional arcs as structural design rules, not decoration
- Mode Separation: SongCouncil (SongMode) vs RapCouncil (RapMode — default)
- Reflect lived truth or narrative consistency across all verses
- Match vocal energy to production cues for emotional coherence
```

### K3.2 HOOK (Phase 3 / N6)
Objective: Capture attention inside first 30–40 seconds.
```
Rules:
- Primary Cut: 3–5 sec grab. Hook by 7–9 bars.
- Chorus = memory anchor + emotional payoff
- Rewrite any section flagged for lack of payoff or emotional drift
- Always close with reflective or payoff moment unless intentionally unresolved
- Director's Cut: Extended intro permitted. Full emotional arc.
```

### K3.3 PROOF (Phase 4 / N8)
Objective: Validate authenticity, impact, technical viability.
```
Rules:
- HPA metric is paramount (INV-10)
- Consensus Sprints ensure rigorous creative review
- VAL + QUINN gates ensure structural and quality compliance
- Sacred Imperfection: intentional flaws are controlled and placed, not accidental
```

### K3.4 LIFT (Phase 8 / N9)
Objective: Maximize distribution + revenue potential.
```
Rules:
- IP Dossier: final Blueprint + Session Ledger + HPA reports + prompts + master audio
- ISRC-ready metadata. rev_split mapped.
- Functional styling tags only — they must shape AI audio output, not describe it
```

### K3.5 COMPOUND (Phase 9 / N9)
Objective: Turn one track into a sustainable asset.
```
Rules:
- Analyze for memetic moments. Brainstorm TikTok/Reels/Shorts.
- Remix packs, instrumentals, acapellas, alt takes, visualizers
- Unhinged Multiverse: tracks are fragments, not standalone — intertextuality required
- Audience co-creation: remix challenges, narrative polls, open-loop storytelling
```

---

## K4 — HUMAN STRUGGLE INJECTION (HSI)

### K4.0 Purpose
Embed raw, relatable human experience into lyrics to elevate emotional depth and authenticity.
Applied at: N5 (Phase 3.1 Revision).
Governed by INV-09 (Sacred Imperfection).

### K4.1 Truth Fragments (inject in order)
```
ORIGIN   The root cause of the emotional state
         Example: "dirt roads to juke joints"
         Question to force it: "Where did this feeling begin?"

SCAR     The lasting impact / visible wound of the struggle
         Example: "Every scar's a secret I keep"
         Question: "What does this leave behind?"

CHOICE   The active decision made in the face of adversity
         Example: "I found heaven in that six-string coil"
         Question: "What did the person choose, when they could have chosen otherwise?"

COST     The price paid for that choice
         Example: "This fog ain't mercy — it's a curse"
         Question: "What did it cost to make that choice?"
```

### K4.2 Application Protocol
1. Read the lyric block to be enhanced
2. Identify which fragment is missing or weakest
3. Rewrite one line per fragment — do not rewrite the whole section
4. Verify the causal chain holds: Origin explains Scar, Scar explains Choice, Choice explains Cost
5. Run syllable validation (skill:validate.syllables) on all rewritten lines

### K4.3 HSI Guard
Do NOT apply HSI if the operator's line already contains the fragment at higher density than HSI can achieve.
The baseline is a ceiling for AI behavior, not a floor for AI aspiration. (From IP vault extraction, Turn 1.)

---

## K5 — DECISION TREES

### K5.1 Revision Decision Logic
```
IF  Consensus Gap identified (N4) AND operator requests refinement
    → micro-patches targeting identified gaps only

IF  VAL_Report shows fail/warn on syllable_count or sfx_placement
    → rephrase for compliance OR adjust SFX format
    → do NOT change meaning or imagery

IF  HPA_Score below threshold (N8)
    → identify sonic issues from HPA_Report.rationale
    → micro-patch [Timbre] or [Performance] only
    → max 1 patch per iteration, max 2 new generations

IF  Cross-Domain Iteration (Phase 7.5) identifies high-priority conflicts
    → loop to earliest relevant phase:
        Re-Blueprint  → N3 (narrative) or N3 (lyrics)
        Re-Prompt     → N5–N6 (revision + container rebuild)
        Re-Generate   → audio only (N8 output)
```

### K5.2 Deviation Recovery Logic (INV-12)
```
IF  deviation detected at any node
    → STOP immediately
    → identify last valid logged state in Session Ledger
    → revert to that state
    → incorporate deviation as new constraint
    → re-engage from last valid node
    → log the deviation + recovery action
```

### K5.3 Turn Classification Logic (G4 / INV-17)
```
Input signals to classify:

CANONICAL   → Operator asserts a rule, policy, architectural decision, or emotional truth
              Signal: declarative statements, "this is", "always", "never", architectural framing
              Action: promote to Blueprint. Log as canon.

TANGENT     → Operator explores a direction not yet connected to active Blueprint
              Signal: conditional language, "what if", speculative tone
              Action: sandbox. Log as TANGENT-[id]. Do not merge until operator says "promote".

PROBE       → Operator tests system behavior by submitting material designed to trigger a response
              Signal: deliberately loose/fragmented/below-baseline content; meta-questions about process
              Action: classify first. Do NOT treat as submission. Do NOT correct. Respond to the test, not the content.
              Example: submitting weak lyrics to see if the system enforces the quality gate.

CORRECTION  → Operator supersedes a prior canon state
              Signal: "no", "not that", "actually", "what i meant was", reframe after AI response
              Action: RETROACTIVE SCOPE. Prior canon is superseded. Rebuild affected state from this turn.
              This is root-level. It overwrites, not appends.

DEFAULT: If classification is ambiguous → treat as CANONICAL. Never treat as PROBE by default.
```

---

## K6 — PRODUCTION TEMPLATES

### K6.1 UST Format v4.5.2 (Suno Strict Container)

**Section order is invariant. This is the law.**

```
[Theory | ...]
[VocalPersona | ...]
[AestheticIntent | ...]
[Timbre | ...]
[Performance | ...]
[Road-Map | sequence only — no durations]
▸ LYRICS BLOCK
[section | bars | v: ... | s: ... | sFx ...]
"line one"

"line two"
```

**Theory fields:**
`mode.{scale} tonal_center.{key} meter.{time_sig} tempo.{BPM}_{feel} chord_color.{harmonic} harmonic_behavior.{style}`

**VocalPersona fields:**
`default.delivery.{style} default.expression.{tone} default.articulation.{rhythm}
Lead.register.{range} Lead.descriptor.{character}
Gosp_Choir.register.{type} Ghost_Choir.register.{layers}
vocal_melody.{motif} vocal_harmony.{pattern} vocal_rhythm.{feel}
vocal_lyric.preserve_user_lines vocal_dynamics.{arc}
vocal_prod.{processing} vocal.tone.{detail}
CREW_TAGS.{Role}.{tag} Alt_tags.{adlib1}_{adlib2}_{adlib3}`

**AestheticIntent fields:**
`genre.{genre} era.{reference} intent.{theme} texture.{density}
aesthetic.{vibe} focus.{priorities} fx.{overall_theme}`

**Timbre fields:**
`drum.{kick_snare_hats} bass.{instrument_feel}
keys.{pads_organ} guitar.{timbre_slide}
orch.{orchestral} vocal.{processing}
note.{eq_compression} fx.{signature_fx}`

**Performance fields:**
`exec.{section_sequence} gest.{producer_tags}
rhythm.{accents_groove} touch.{drops_stutters}
prod.{sidechain_techniques} gesture.{chorus_lifts}
fx.{performance_fx}`

**Lyrics Block section header format:**
`[sectionName | bars | v: vocal notes | s: style notes | sFx **... ***]`

**Lyric line format:**
`"lyrics line", (adlib) ** SFX **`
followed by blank line.

### K6.2 Formatting Laws (from INV-04, INV-05, INV-06)
```
NO COMMAS OUTSIDE LYRICS BLOCK — use spaces or underscores
SYLLABLE COUNT — 6–11 per line. Flag all violations.
SEMI-COLON = LINE BREAK — split at ; into two separate lines, each with blank line
ROAD-MAP = SEQUENCE ONLY — no durations, no timestamps
CHARACTER BUDGETS — Show Summary ≤ 1000. Macro ≤ 4990.
```

### K6.3 Variant Strategy
```
Variant A  Baseline — full vision, full fidelity to Blueprint
Variant B  Minimal Change — one targeted variation to test a specific parameter
Primary Cut   Streaming-optimized. 3–5 sec grab. Hook by 7–9 bars. Compressed intro.
Director's Cut Extended play. Full emotional arc. Intro permitted.
```

### K6.4 Output Triad (N9 — The Training Signal)
The three deliverables that constitute a complete session output:
```
1. PERFORMER PROFILE    — Bio + style definition for this persona/track
                          Purpose: trains model on who is performing
                          
2. SHOW SUMMARY         — The Suno prompt (strict container, ≤1000 chars Show Summary + macro)
                          Purpose: the executable creative artifact
                          
3. SESSION SHEET        — Creative UST — the full creative brief
                          Purpose: human-readable record of intent, decisions, and provenance

These three together = the TRIAD. The triad IS the training signal.
A session is not complete without all three.
```

---

## K7 — SCHEMAS

### K7.1 Blueprint (JSON) Schema
```json
{
  "id": "project_id_timestamp",
  "version": "v1.0",
  "platform_targets": ["Suno_v4.5", "Streaming_Optimized", "Extended_Play"],
  "title": "{Song Title}",
  "emotional_theme": "{Core Theme}",
  "payoff": "{Song Payoff}",
  "sections": [
    {
      "name": "Intro",
      "bars": 4,
      "narrative_purpose": "{purpose}",
      "emotional_arc": "{arc}",
      "lyrics": [
        {"line": "{text}", "syllables": 0, "adlib": "", "sfx": ""}
      ],
      "vocal_notes": "",
      "style_notes": "",
      "sfx_notes": ""
    }
  ],
  "metacontainers": {
    "Theory": {},
    "VocalPersona": {},
    "AestheticIntent": {},
    "Timbre": {},
    "Performance": {}
  },
  "roadmap_events": [
    {"event": "start", "time_ms": 0, "section": "intro"}
  ]
}
```

### K7.2 Session Ledger (YAML) Schema
```yaml
session_id: "YYYY-MM-DD_ProjectName"
start_timestamp: "YYYY-MM-DD HH:MM:SS"
status: "IN_PROGRESS"    # COMPLETE | ERROR
current_node: "N4"
current_phase: "Phase 2"
blueprint_version: "v1.1"

blueprint_versions:
  - version: "v1.0"
    timestamp: ""
    changes: "Initial"
    status: "INITIALIZED"

reca_snapshot:
  requirements: ""
  evidence: ""
  constraints: ""
  actions: ""

turn_log:
  - turn: 1
    mode: "CANONICAL"    # CANONICAL | TANGENT | PROBE | CORRECTION
    summary: ""
    state_change: ""

consensus_sprints:
  - round: 1
    status: "COMPLETED"
    scores:
      Lyrical_Professor:  {score: 0, notes: ""}
      Battle_Technician:  {score: 0, notes: ""}
      Cultural_Critic:    {score: 0, notes: ""}
      MixMaster_Ghost:    {score: 0, notes: ""}
      Strategist:         {score: 0, notes: ""}
      DJ_Mo_Money:        {score: 0, notes: ""}
    consensus_gap: ""
    micro_patches:
      - {id: "MP1", description: "", original: "", updated: ""}

technical_audits:
  val_report:
    status: "pass"
    checks:
      structure.sections.integrity: ""
      persona.call.grammar: ""
      roadmap.transition.safety: ""
      lyric.line.syllable_count: ""
      lyric.line.sfx_placement: ""
  quinn_report:
    status: "pass"
    checks:
      low.sub.separation: ""
      vocal.presence.window: ""
      fx.tension.curve: ""

somatic_checkpoints:
  CP1: {status: "locked", operator_response: ""}
  CP2: {status: "locked", operator_response: ""}
  CP3: {status: "locked", operator_response: ""}
  CP4: {status: "locked", operator_response: ""}

audio_rendering:
  - take_id: "A1"
    prompt_version: ""
    hpa_score: 0
    keeper: false

deviations:
  - {turn: 0, invariant: "", description: "", recovery: ""}

phantom_commitments_flagged:
  - {turn: 0, phrase: "", action_taken: ""}
```

### K7.3 HPA Report Schema
```yaml
track_id: ""
version: ""
evaluator: "DJ_Mo_Money"
overall_hpa_score: 0.0    # out of 5.0

metric_weights:
  MOS:              0.30
  CLAP:             0.25
  FAD_norm:         0.20
  MotifRecurrence:  0.15
  FractalProx:      0.10

targets:
  CLAP_min:               0.80
  FAD_max:                2.30
  MFCC_dist_max:          0.30
  MotifRecurrence_min:    0.65
  DFA_melody_target:      1.31
  DFA_tolerance:          0.05

round_trip:
  enabled: true
  measures: [MFCC_dist, CLAP, MOS_emotion]

score_breakdown:
  creative_authenticity:      0.0
  emotional_impact:           0.0
  sonic_fidelity_to_intent:   0.0
  viral_potential_perception: 0.0

rationale: ""
somatic_verdict: ""    # "tears" | "goosebumps" | "silence" | "no"
recommended_patches: []
```

### K7.4 V&V Log Schema
```yaml
vnv_log_id: ""
blueprint_version: ""
prompt_type: ""    # Director_Cut | Primary_Cut

macro_checks:
  structure_integrity:  {status: "", details: ""}
  policy_compliance:    {status: "", details: ""}
  goal_fit:             {status: "", details: ""}

micro_checks:
  lyric_syllable_count:     {status: ""}
  lyrics_block_structure:   {status: ""}
  metacontainer_grammar:    {status: ""}

tactical_checks:
  bars_only_roadmap:          {status: ""}
  mono_kick_sub:              {status: ""}
  dark_plate_hooks:           {status: ""}
  phone_scene_mono_filter:    {status: ""}
  headroom_directive:         {status: ""}
  outro_intact:               {status: ""}

overall_status: ""    # PASS | PASS_WITH_WARNINGS | FAIL
fixes_applied: []
residual_risks: []
```

### K7.5 Project.json Schema
```json
{
  "project_name": "",
  "created_by": "DJ Mo Money",
  "os_version": "v1.1",
  "songs": [{
    "title": "",
    "blueprint_version": "",
    "triad": {
      "performer_profile": "",
      "show_summary": "",
      "session_sheet": ""
    },
    "audio": {
      "director_cut": "",
      "primary_cut": ""
    },
    "session_ledger": "",
    "hpa_report": "",
    "marketing_tags": []
  }],
  "global_metadata": {
    "genre": "Gospel Trap Revival",
    "universe": "Unhinged Multiverse",
    "philosophy": "Sacred Imperfection"
  }
}
```

---

## K8 — PRODUCTION RULES

### K8.1 Mandatory Mix Directives (tactical — must appear in every container)
```
mono_kick_sub         Kick and sub are mono below ~200 Hz. No stereo bass.
dark_plate_hooks      Hook sections carry dark plate reverb (target: ~1.6s decay)
headroom              Master has headroom. Not loud and lifeless.
phone_scene           Bridge phone scene: band-pass filter 200–5 kHz on vocal
sidechain             Kick sidechains bass + synths
vocal_presence        Lead vocal: close mic, forward (+2dB vs band), de-essed
```

### K8.2 Sacred Imperfection FX (INV-09 enforcement)
Each of these must be intentional, placed, and controlled. Not random. Not accidental.
```
fx.vinyl_crackle          "old breath" — fragile memory signal
fx.tape_wobble            "proof of life" — damaged memory, human presence
fx.reverb_swells          "spiritual punctuation" — emotional emphasis
fx.chopped_vocal_fx       "ancestral echoes" — fragmentation, heritage
fx.echo_delay_ping_pong   "jumbled memory" — temporal distortion
```

### K8.3 QUINN Validator Specifics
```
low.sub.separation
  Failure mode: kick and sub fighting at ~80 Hz → mud → phase nightmare
  Fix directive: prod.sidechain_kick_bass_synths

vocal.presence.window
  Failure mode: vocal buried or harsh in 2–5 kHz range
  Fix directive: vocal.tone.close_mic_forward_plus2dB_vs_band_de_essed

fx.tension.curve
  Failure mode: FX applied uniformly — no narrative relationship to tension arc
  Fix directive: automate FX to narrative arc; name each FX with its emotional purpose
```

### K8.4 Compression Logic for Container Building
```
Move repeats → Style/Timbre/Performance (not per-section)
Use (repeat) shorthand for duplicate hooks
No commas anywhere outside LYRICS BLOCK
Lines ≤ 120 characters
Run character count before submitting
```

---

## K9 — NARRATIVE GOVERNANCE

### K9.1 Foundational Laws
```
Songs are disguises for truth. Not stories — masks.
Hooks are spells. Not choruses — incantations.
Characters are roles. Not people — archetypes.
Production is the physics of feeling. Every technical choice is a spiritual choice.
```

### K9.2 Arc Architecture
```
SONG ARC (per track):
  Fall          → Inciting trauma / disruption of normal
  Struggle      → Reaction, conflict, emotional spiral
  False Ascent  → Apparent resolution (the lie before the truth)
  Exposure      → Inevitable revelation / cost

This arc is a SPIRAL, not a linear progression.
Each repetition of the arc deepens and changes with each pass.
"False Ascent" is what makes it Gospel Trap — the system offers salvation and then demands the price.
```

### K9.3 Unhinged Multiverse Rules
```
Tracks are not standalone. They are fragments of a larger interconnected universe.
Recurring themes, characters, and sonic motifs must cross tracks.
Open-loop storytelling: release before resolving. Let the audience carry the tension.
Fan remixes and co-creation are narrative events, not just marketing tactics.
Each release = a scene. Sequence the scenes. Build the arc across projects.
```

### K9.4 Emotional Invariants
```
Every section has an emotional assignment. Emotion = Constraint (not decoration).
Emotional arc must be mapped before lyrics are written.
If a section doesn't push the arc forward, it is a structural failure.
Emotional hooks must SHIFT UNDER PRESSURE — meaning must evolve with repetition.
Sacred Imperfection: everything can be rough. Nothing can be false.
```

---

## K10 — BENCHMARK & CALIBRATION

### K10.1 Model Benchmark (A→T→A reference)
```
Always run A→T→A: Audio → Text description → Audio regeneration (round-trip fidelity test)

GPT-5:    Polished timbre, strong production finish. Best for final production pass.
Gemini:   Artifact emulation + motif development. Best for texture and motif embedding.
Copilot:  Analysis-first, structural strength. Best for V&V and structural review.
```

### K10.2 Reference Build — Boy Icarus (v4.2.3 — validated PASS)
Used as a calibration reference for new builds. This is what a PASS looks like.
```
Theory: Aeolian | A | 4/4 | 78bpm | minor-9
Voice: Lead falsetto + low-mid BGVs | mantra-fragment hybrid | yearning → singe → quiet
Road-Map: Intro(4) → V1(8) → Pre(4) → Hook(8) → V2(8) → Bridge/Phone(4) → Hook(8) → Exit(4)

Key specs that produced PASS:
- Bridge: band-pass 200–5kHz (phone scene)
- Hook: dark plate 1.6s + heavy 808
- Sub/kick: mono
- Exit: whisper lead (collapse, not fade)

SEM delta highlights (highest gains):
- Sacred Imperfection FX Integration:  +0.30
- Memory Activation Likelihood:        +0.30
- Visualizability of Lines:            +0.30
- Imagery Uniqueness:                  +0.30
- Repeatability Index (hook):          +0.30

Lesson: Specific FX directives with named emotional purpose outperformed vague aesthetic tags.
"dark plate 1.6s" > "reverb on hooks"
"band-pass 200–5kHz" > "phone effect"

Version log entry: Boy Icarus | v1 | summary:216 | macro:2101 | validators:PASS
```

### K10.3 Quality Calibration Notes (from IP vault extraction)
```
The baseline is a CEILING for AI behavior, not a floor for AI aspiration.
If a line could be said by any random rapper → it fails.
If a line feels like a model riffing without intention → it fails.
Quality is defined by example (few-shot), not by description.
The operator's somatic audit recalibrates against the real world continuously.
The system must track with it — or quality erosion happens silently. (INV-16)
```
