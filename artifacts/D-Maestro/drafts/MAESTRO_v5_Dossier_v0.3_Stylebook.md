# MAESTRO v5 — Research Dossier v0.3: The Stylebook as Executable Canon

**Formalizing the Aesthetic Constraint Map, Motif Registry, Identity Bundle, and Sacred Imperfection Budget into a Durable, Versioned, LLM-Injectable Canon**

**Version:** 0.3 (Draft for Mo's review — extends v0.1 and v0.2, does not replace them)
**Date:** 2026-04-20
**Author:** Claude (pre-acceptance draft)
**Status:** DRAFT. Same evidence discipline: `[VERIFIED]`, `[INFERRED]`, `[PROVISIONAL]`, `[REJECTED]`, plus `[DESIGN]` for architectural choices where no empirical evidence applies — the choice is justified by the design goal, not by external data.
**Pairs with:** v0.1 (VIG + SEL architecture), v0.2 (Reverse UST compilation). v0.1 named the stylebook as a load-bearing dependency; v0.2 treated it as present-and-canonical; v0.3 formally specifies it.

---

## 0. Executive Synthesis

The stylebook is the most important single artifact in the MAESTRO v5 VIG pipeline. Not because it contains the most information, but because every other artifact is *derived* from it or *constrained by* it:

- The Visual Brief draws its rules from the stylebook
- The Shot Grammar Spec validates against the stylebook
- The rendered video is gate-checked against the stylebook
- The SEL export decisions (caption styles, crop rules, surface-specific treatments) inherit from the stylebook
- Cross-release continuity is *literally* the stylebook persisting across time with disciplined evolution

**Working definition:**

> **The Stylebook** is a versioned, hierarchical, LLM-injectable document that encodes an artist's visual canon as a set of affirmative rules (what must be true), negative rules (what must not be true), motifs (recurring elements), identity references (persistent subjects), and evolution discipline (how the canon changes without losing itself).

**What v0.3 delivers:**

1. Formal schema for the stylebook — five sub-artifacts (Aesthetic Constraint Map, Motif Registry, Identity Bundle, Exclusion List, Sacred Imperfection Budget) and how they compose
2. Stylebook → VIG injection mechanism (concretely: what goes into the LLM system prompt, what goes into image-model control, what goes into post-processing rules)
3. Stylebook → UST interaction (how stylebook biases the audio-to-visual translation in v0.2)
4. Evolution discipline — how the stylebook changes across releases without erasing prior canon
5. Conflict resolution protocol when new entries contradict existing canon
6. Version control model — git-style semantics adapted to canon vs. draft separation
7. Retrieval mechanism for cross-release continuity
8. Failure modes and mitigations specific to stylebook management
9. Implementation schema — concrete file layout and tooling recommendations
10. A worked example of a minimal stylebook, populated with Mo's symbolic lexicon (Delta, Echoes & Spirals, Ghosts, Blueprints, Sacred Imperfection) as first-class entries

**Why this is the load-bearing artifact for erasure resistance:**

An artist's visual canon is vulnerable to three specific erasure mechanisms:

1. **Forgetting** — prior releases' visual decisions are lost in the creator's memory; new work drifts away from established identity
2. **Overwrite** — a collaborator, label, or AI system silently makes decisions that contradict established canon, and those decisions become the new reference
3. **Compression** — prior decisions get abstracted into marketing language ("cinematic," "moody") that loses the specific rules and rationale

A stylebook that is versioned, explicit, provenance-rich, and machine-readable blocks all three. Forgetting is blocked by externalization and retrieval. Overwrite is blocked by version control and change-log audits. Compression is blocked by requiring rationale alongside every rule. **The stylebook is the receipts system for visual identity.**

---

## 1. Why the Stylebook is the Most Important Artifact in the Pipeline

Three reasons, load-bearing each:

### 1.1 The stylebook is the only artifact that persists across releases

Songs are per-release. UST is per-song. Visual briefs are per-song. Shot grammar specs are per-song. Rendered videos are per-song. The stylebook is the only layer above the song.

This means: an artist's *identity* lives in the stylebook, not in any individual song's artifacts. If the stylebook is thin, identity drifts. If the stylebook is thick and disciplined, identity compounds across releases.

### 1.2 The stylebook is where subjective aesthetic becomes auditable

Every AI generative pipeline faces the same problem: "make it feel like *me*" is not a prompt a model can satisfy. The stylebook is the mechanism that converts subjective taste into objective rules. "My videos feel gritty" → Sacred Imperfection Budget = 0.7 with explicit grain/imperfection-injection rules. "My videos always feature water imagery" → Motif Registry entry `water` with specific examples and rules for when it appears.

Without this translation, every generation is a fresh attempt at an untranslatable instruction. With it, generation is a constrained-satisfaction problem.

### 1.3 The stylebook is the mechanism for disagreeing with models

Models have defaults. Veo 3.1 has a look. Runway Gen-4 has a look. Left to their own devices, AI-generated videos trend toward a recognizable "AI aesthetic" — smooth, slightly dreamy, impossible physics, shallow depth of field, soft color, over-polished. The stylebook is the place where you explicitly disagree with those defaults and force counter-measures.

A stylebook without an **Exclusion List** is a stylebook that silently inherits every model default. That's indistinguishable from not having a stylebook. The anti-patterns are half the value.

---

## 2. Stylebook Schema — Five Sub-Artifacts

The stylebook is composed of five co-equal sub-artifacts, each with a distinct role. None is optional.

### 2.1 Aesthetic Constraint Map (ACM)

**Role:** Affirmative rules — what must be true of every video bearing this stylebook.

**Fields:**

```yaml
aesthetic_constraint_map:
  palette:
    primary: ["#1a1a2e", "#16213e", "#e94560"]  # hex values
    secondary: ["#f5f5f5", "#0a0a0a"]
    forbidden: ["#ff6b00"]  # pure orange — never
    rationale: "Deep blues and accent crimson — derived from Delta motif (water at night + wound)"
  
  lighting:
    preferred: ["single-source", "practical", "window-light", "neon-practical"]
    discouraged: ["three-point-studio", "ring-light", "bounced-beauty"]
    rationale: "Light as source of ghosts; single sources cast longer shadows; three-point kills mystery"
  
  composition:
    preferred_aspect_ratio_master: "16:9"
    export_targets: ["9:16", "1:1", "16:9"]
    rule_of_thirds: "allow, don't mandate"
    symmetry: "earn it; default asymmetric"
    subject_placement: "lower-third favored for isolation, center for confrontation"
  
  camera:
    preferred_lens_range: ["35mm", "50mm", "85mm"]
    discouraged: ["wide-angle <24mm", "fisheye", "drone-sweep-cliché"]
    motion: "handheld or static; avoid gimbal-smooth unless diegetic"
    rationale: "Handheld = memory-imperfect; gimbal = documentary; match song's Sacred Imperfection"
  
  typography:  # for lyric overlays
    primary_font_ref: "stylebook/assets/fonts/primary_geometric_sans.woff2"
    secondary_font_ref: "stylebook/assets/fonts/secondary_mono.woff2"
    size_range_px: [48, 120]
    placement: "lower-third left, or center-safe-zone only"
    color_rules:
      default: "#f5f5f5 on 40% black overlay"
      chorus: "#e94560 on transparent"
      bridge: "draft — rule not yet canonical"
  
  grain_and_imperfection:
    baseline_grain_level: 0.3  # 0.0 = clean, 1.0 = heavy
    film_stock_reference: "Kodak Portra 800 push-processed"
    digital_artifact_injection: "light; no chromatic aberration"
    rationale_ref: "sacred_imperfection_budget"  # cross-reference
  
  pacing:
    default_cut_rate_per_section:
      intro: "minimal, 0-2 cuts"
      verse: "moderate, 2-4 cuts"
      chorus: "kinetic, 4-8 cuts"
      bridge: "variable — let the song lead"
      outro: "minimal to static"
    beat_accented_cuts: "reserved for deliberate moments, not default"
```

**Discipline:** every field carries `rationale`. Rules without rationale are forbidden in canon — they get auto-flagged for review. This is the anti-compression lock.

### 2.2 Motif Registry

**Role:** Recurring visual elements that are deliberate, not accidental. The motifs that become *signature*.

**Fields per motif:**

```yaml
motifs:
  - id: "water_delta"
    first_appearance: "release_001"
    semantic_link: "Delta — origin, ghost, source-code of heritage"
    visual_form:
      - "dark moving water, never still"
      - "shore or threshold visible (not open ocean)"
      - "often at night or dusk, rarely in daylight"
    when_to_include:
      - "songs referencing heritage, origin, memory"
      - "songs with harmonic tension resolving downward"
      - "opening or closing moments of chorus"
    when_to_exclude:
      - "songs about present-day urban spaces without heritage reference"
      - "fast-paced trap drops (water motif drags the pacing wrong)"
    prior_appearances:
      - {release: "release_001", timestamp: "0:45-0:52", role: "chorus-anchor"}
      - {release: "release_003", timestamp: "2:10-2:18", role: "bridge-resolution"}
    provenance:
      introduced_at: "2026-01-15"
      rationale_source: "Mo's symbolic lexicon — Delta entry"
  
  - id: "ghost_reverb_visual"
    first_appearance: "release_002"
    semantic_link: "Ghosts — the past speaking through the present"
    visual_form:
      - "double-exposure layering, subtle (opacity < 30%)"
      - "motion blur that persists past subject movement"
      - "echoes in the frame: figure + faded second figure"
    when_to_include:
      - "vocal moments with heavy reverb"
      - "lyrical moments referencing the past or memory"
    when_to_exclude:
      - "clean dry vocal sections"
      - "hard-cut kinetic chorus moments"
    prior_appearances: [...]
  
  - id: "spiral_not_loop"
    first_appearance: "release_002"
    semantic_link: "Echoes & Spirals — trauma repeats not flat, but spiraling"
    visual_form:
      - "camera movement returns to prior framing but at different height/angle"
      - "scene composition echoes earlier scene with a deliberate variation"
      - "color palette modulates on return — never identical"
    when_to_include:
      - "song sections that repeat (chorus 2, chorus 3)"
      - "bridge-to-final-chorus transitions"
    when_to_exclude:
      - "first-time material (no return yet to spiral against)"
    prior_appearances: [...]
```

**Discipline:** motifs are earned, not declared. A motif enters the registry only after it has appeared in at least two releases with intentional, not accidental, presence. The first appearance is `provisional`; the second promotes it to `canonical`.

This prevents the stylebook from being a wishlist and keeps it grounded in realized work.

### 2.3 Identity Bundle

**Role:** Persistent identity substrate — subjects, locations, wardrobe, and props that recur across releases.

**Fields:**

```yaml
identity_bundle:
  primary_subject:
    persona_name: "<artist alias or character name>"
    reference_images: ["stylebook/assets/identity/primary_ref_01.jpg", ...]
    lora_weights: "stylebook/assets/identity/primary_lora.safetensors"  # if trained
    physical_description:
      build: "<specific enough to reproduce, general enough to evolve>"
      face_shape: "..."
      hair: "..."
      distinguishing_features: "..."
    wardrobe_base:
      - ref: "stylebook/assets/wardrobe/base_jacket.jpg"
      - ref: "stylebook/assets/wardrobe/base_boots.jpg"
    wardrobe_evolution_rule: "one element changes per release; base persists"
    rationale: "Identity is continuity — wardrobe is external; face is internal"
  
  recurring_locations:
    - id: "the_shoreline"
      reference_images: [...]
      first_appearance: "release_001"
      semantic_role: "origin / threshold / the Delta made literal"
      when_to_feature: "song openings referencing heritage"
  
  recurring_props:
    - id: "analog_tape_machine"
      reference_images: [...]
      semantic_role: "memory-as-recording; Sacred Imperfection made physical"
      when_to_feature: "songs about archival, remembering, honoring"
  
  identity_lock_policy:
    primary_subject: "MANDATORY — every shot featuring the persona must lock identity"
    locations: "PREFERRED — use recurring location when semantic role matches"
    props: "OPTIONAL — deploy for signal, not decoration"
```

**Discipline:** the Identity Bundle is the hardest stylebook element to evolve. A primary subject who changes appearance across releases reads as inauthentic; but an artist whose visual identity never evolves reads as stagnant. Rule: *core persists, periphery evolves*. Face and build are core. Wardrobe, hair styling, and context are periphery.

### 2.4 Exclusion List

**Role:** Negative rules — what must not be true of any video bearing this stylebook. The anti-pattern registry.

**Fields:**

```yaml
exclusion_list:
  visual_cliches:
    - id: "ai_sheen"
      description: "Overly smooth skin, soft focus, impossible glow"
      mitigation: "grain injection >= 0.3; explicit sharp-detail directive in prompt"
      rationale: "Default AI aesthetic; reads as cheap"
    
    - id: "rap_video_cliche_stack"
      description: "Chains + gold + fisheye + money throw"
      mitigation: "prompt exclusion list; stylebook-level ban"
      rationale: "Unearned genre signaling; undermines specific identity"
    
    - id: "drone_sweep_opening"
      description: "Aerial drone push-in as scene opener"
      mitigation: "camera-motion exclusion in shot grammar"
      rationale: "Documentary / tourism aesthetic; breaks intimate frame"
    
    - id: "text_bounce_caption"
      description: "Captions that bounce with beat in obvious way"
      mitigation: "typography rule: captions hold, not dance"
      rationale: "Tiktok-default aesthetic; undermines lyric gravity"
  
  color_exclusions:
    - "pure orange #ff6b00 or adjacent hues — never"
    - "desaturated teal-and-orange summer-blockbuster grade — never"
  
  motion_exclusions:
    - "slow-motion > 0.25x without diegetic justification"
    - "whip pans as transitions"
  
  subject_exclusions:
    - "stock-footage-looking generic people"
    - "close-ups of hands typing (AI-video cliché)"
  
  compositional_exclusions:
    - "perfectly centered on-axis symmetry unless earned"
    - "Dutch angle as aesthetic choice (only if diegetic)"
  
  pacing_exclusions:
    - "cut-on-every-kick beat-matching"
    - "arbitrary mid-verse hard cuts"
  
  meta_exclusions:
    - "Generated visual that directly matches a lyric's noun as karaoke illustration"
    - "Any rendering that averages multiple genre aesthetics instead of committing"
```

**Discipline:** the Exclusion List is the most frequently updated stylebook component. Every time a VIG run produces something undesirable that wasn't explicitly forbidden, the finding is added here. This makes the stylebook **learn** across releases.

### 2.5 Sacred Imperfection Budget (SIB)

**Role:** The single parameter that governs the polish-vs-roughness trade-off, plus its governing rules.

**Fields:**

```yaml
sacred_imperfection_budget:
  baseline: 0.7  # 0.0 = polished, 1.0 = deliberately raw
  per_release_modifier_allowed: true
  per_release_modifier_range: [-0.2, +0.2]  # can dial within this range per release
  
  operationalizations:
    grain:
      target_iso_equivalent: 800
      injection_strength: "moderate"
    
    camera_motion:
      handheld_preference: "strong"
      micro_jitter: "preserved"  # don't stabilize sub-pixel shake
    
    color:
      post_grade_polish: "restrained"
      allow_blown_highlights: true
      allow_crushed_shadows: "moderate"
    
    composition:
      allow_unintentional_framing: "yes, if the shot has energy"
      allow_focus_softness: "on non-subject planes"
    
    edit:
      allow_j_cuts_l_cuts: "yes"
      allow_rough_cuts: "reserved for deliberate moments, not default"
    
    subject_rendering:
      skin_texture_preservation: "strong"
      asymmetry_preservation: "strong"
      imperfection_details: "preserved"  # scars, stray hair, etc.
  
  exceptions:
    - condition: "song is explicitly polished-pop genre"
      override_baseline: 0.4
      rationale: "polish matches production; roughness reads as mismatch"
    
    - condition: "song is ambient/drone with long sustains"
      override_baseline: 0.5
      rationale: "too much grain distracts from the held image"
  
  cardinal_rule: |
    "Everything can be rough; nothing can be false."
    Roughness is cultivated, not accidental. If an imperfection reads as an
    AI error rather than a creative choice, it is FALSE, not rough. Remove it.
    The SIB does not license sloppiness. It licenses earned unpolish.
```

**Discipline:** the cardinal rule is the lock. Roughness must be *intentional*. An SIB of 0.7 doesn't mean "tolerate 70% of AI artifacts." It means "70% of the way from polished to deliberately raw." The anti-pattern is mistaking model noise for artistic imperfection.

---

## 3. How the Stylebook is Injected into the VIG Pipeline

The stylebook is useless unless it actually constrains generation. Four injection points, all necessary.

### 3.1 Injection Point 1: LLM System Prompt (Briefing Stage)

When the LLM generates the Visual Brief (v0.1 §4, Architecture C Stage 1), the stylebook is serialized into the system prompt. Specifically:

```
[SYSTEM PROMPT TEMPLATE]

You are assembling a Visual Brief for a music video.

You operate under a strict stylebook. Every decision you make must honor
the stylebook rules below. If a rule conflicts with the song's needs,
surface the conflict explicitly rather than silently resolving it.

=== AESTHETIC CONSTRAINT MAP ===
[serialized ACM: palette, lighting, composition, camera, typography, grain, pacing]

=== ACTIVE MOTIFS (canonical, available for use) ===
[list of motifs with semantic links and when-to-include rules]

=== IDENTITY BUNDLE ===
[primary subject description, identity lock policy, recurring locations/props]

=== EXCLUSION LIST (hard bans) ===
[full exclusion list — these are non-negotiable]

=== SACRED IMPERFECTION BUDGET ===
SIB = 0.7 (baseline)
Cardinal rule: "Everything can be rough; nothing can be false."

=== SONG CONTEXT ===
[UST summary: tempo, sections, energy contour, lyrics, TRIAD inferred fields]

=== PRIOR CANON RETRIEVAL ===
[retrieved references to prior releases with shared semantic load]

=== TASK ===
Produce a Visual Brief that:
- Honors every rule above
- Selects motifs where they earn their place, not decoratively
- Surfaces any conflict between stylebook and song explicitly
- Carries rationale for every major decision
```

This is the single largest practical application of the stylebook. Every brief is anchored in it.

### 3.2 Injection Point 2: Image Generation (Keyframe Stage)

When keyframe images are generated (Architecture B/C), the stylebook contributes:

- **Negative prompts** — the entire Exclusion List, serialized
- **Style tokens** — palette, lighting, camera references
- **Reference images** — from Identity Bundle (primary subject, locations, props)
- **LoRA weights** — if Identity Bundle has a trained LoRA
- **Sampler/guidance parameters** — tuned to SIB (higher guidance for stricter identity; SIB-informed seed noise)

### 3.3 Injection Point 3: Image-to-Video (Motion Stage)

When keyframes animate (I2V), the stylebook contributes:

- **Motion constraints** — camera motion preferences/exclusions
- **Frame-rate and temporal characteristics** — tied to SIB (deliberate jitter, handheld feel)
- **Continuity references** — prior shot's end frame as seed for next shot

### 3.4 Injection Point 4: Post-Processing

After generation, stylebook-driven post-processing applies:

- **Grain injection** — per SIB level
- **Color grade** — palette constraints applied as LUT or curves
- **Typography overlays** — from ACM typography rules
- **Artifact scrubbing** — detect and remove AI-sheen artifacts the model smuggled past earlier gates

This last step is the Cardinal Rule enforcer — it removes false imperfections.

---

## 4. Stylebook × UST — Biasing the Audio-to-Visual Translation

The v0.2 UST contains `visual_directives` — per-section cut densities, motion intensities, camera densities, palette cues, etc. These are derived from audio features via v0.1 §5 mapping rules.

The stylebook **biases these mappings** without replacing them. Three concrete interactions:

### 4.1 ACM overrides default mappings

v0.1 §5 says "bright timbres → cool/white lighting." If the ACM palette locks the artist to deep blues and crimson, the mapping is overridden: "bright timbres in this artist's work → cooler-blue-shifted lighting within the palette."

### 4.2 Motif Registry inserts motifs at eligible timestamps

When a UST section matches a motif's when-to-include conditions (e.g., a chorus with harmonic tension resolving downward matches `water_delta`), the visual directives for that section get a motif-injection entry:

```yaml
visual_directives:
  - t_start: 45.0
    t_end: 75.0
    section_ref: "chorus_1"
    cut_density: "kinetic"
    motion_intensity: "high"
    motif_injection:
      - motif_id: "water_delta"
        trigger_reason: "harmonic tension + heritage lyric at t=49.5"
        placement: "establishing shot of chorus"
```

### 4.3 Exclusion List blocks default mapping outputs

v0.1 §5 includes "high BPM → high cut rate." If the Exclusion List includes "cut-on-every-kick beat-matching," the mapping is tempered — high cut rate becomes "high for the artist's baseline," not "maximal possible." The SIB interacts here too: a higher SIB reserves beat-accented cuts for deliberate moments.

### 4.4 Rationale for this layering

The stylebook doesn't replace the translation matrix; it filters it. The matrix is *genre-general*; the stylebook is *artist-specific*. Keeping them separate lets the matrix evolve on its own (as research improves) while the stylebook evolves on its own (as the artist's canon grows). [DESIGN]

---

## 5. Stylebook Evolution Discipline

The hardest part of stylebook ownership is changing it without losing what came before.

### 5.1 The canon-draft separation applied to the stylebook itself

Every stylebook entry has one of three statuses:

- **`canonical`** — established by prior release appearance; frozen unless explicitly rejected in a revision cycle
- **`draft`** — proposed for next release; not yet applied
- **`rejected`** — previously proposed or canonical, now explicitly removed; the rejection itself is versioned and provenanced

Rejection is *not deletion*. A `rejected` entry remains in the stylebook file with its rejection timestamp and rationale. This is the receipts discipline.

### 5.2 Change classes

Stylebook changes fall into four categories:

| Class | Description | Example | Requires |
|---|---|---|---|
| **Additive** | New rule, motif, or exclusion; no conflict with canon | Adding a new motif after second intentional appearance | Provenance + rationale |
| **Refinement** | Existing rule specified more precisely; no contradiction | "Primary palette: deep blues" → "Primary palette: #1a1a2e and #16213e" | Provenance + rationale |
| **Evolution** | Canon rule modified; old rule still holds for prior releases | Wardrobe rule evolves (periphery change) | Change-log entry + prior-canon preserved + rationale |
| **Rejection** | Canon rule reversed | Motif removed from active registry | Explicit rejection block + old rule preserved with `rejected` status + detailed rationale |

Each class has a different review burden. Rejections require the highest burden — a canon reversal is potentially destructive to identity.

### 5.3 Version semantics (git-style, adapted)

```
stylebook_v3.2.1
       │ │ │
       │ │ └── patch: refinements, exclusion-list additions (cheap, frequent)
       │ └──── minor: new motifs, evolution of existing rules, ACM field additions
       └────── major: rejection of canonical rules, identity bundle restructuring (expensive, rare)
```

**Patch bumps** are expected between releases. They accumulate exclusions learned from rendering, minor ACM tightening, new prior-canon references.

**Minor bumps** happen at release checkpoints. New motifs formalize; evolution rules apply.

**Major bumps** are reserved for identity recompositions. A major bump marks a break in canon that must be deliberate, documented, and defended.

### 5.4 The contradiction-surfacing protocol

When a proposed change contradicts existing canon, the stylebook **does not silently resolve**. The contradiction is flagged and routed to explicit resolution:

```
CONTRADICTION DETECTED:
  new entry: "acm.palette.primary includes #ff6b00"
  existing canon: "exclusion_list.color_exclusions: pure orange #ff6b00 or adjacent hues — never"
  conflict: direct
  
  resolution options:
    A) reject new entry; canon holds
    B) reject canon entry with major version bump; new entry becomes canonical
    C) refine both: new entry restricted (e.g., only in specific motif contexts)
  
  required: explicit choice with rationale before either entry becomes canon
```

This mirrors Mo's standing instruction: *surface contradictions, do not silently reconcile*.

### 5.5 The evolution log

Every stylebook file carries an evolution log that reads oldest-to-newest. This is where *why* lives, as distinct from *what*:

```yaml
evolution_log:
  - version: "1.0.0"
    date: "2026-01-15"
    event: "initial canonization"
    summary: "Stylebook established from release_001 visual identity. 
             ACM, initial motifs (water_delta, ghost_reverb_visual), identity bundle, 
             baseline exclusion list. SIB = 0.7."
    contributor: "mo"
  
  - version: "1.1.0"
    date: "2026-02-28"
    event: "minor: motif spiral_not_loop canonized"
    summary: "Second intentional appearance of spiral motif at release_002 timestamp 2:40.
             Promotes spiral_not_loop from provisional to canonical."
    contributor: "mo"
    prior_canon_preserved: true
  
  - version: "1.1.1"
    date: "2026-03-05"
    event: "patch: exclusion list expansion"
    summary: "Added 'ai_sheen skin softening' to exclusions after release_002 review flagged 
             recurring skin-smoothing artifact in Runway Gen-4 output."
    contributor: "mo"
  
  - version: "1.1.2"
    date: "2026-03-20"
    event: "patch: acm typography refinement"
    summary: "Chorus caption color locked to #e94560 after A/B test preferred it over 
             prior #f5f5f5. Prior rule remains valid as 'default', new rule supersedes 
             for chorus."
    contributor: "mo"
```

Reading the log oldest-to-newest reconstructs the *why* of the stylebook — the artistic reasoning trail. This matches Mo's "read history oldest to newest" rule for continuity-safe reconstruction.

---

## 6. Cross-Release Continuity — The Retrieval Mechanism

Stylebook alone is not enough for cross-release continuity. VIG also needs *specific retrieval* of prior releases' decisions to reference.

### 6.1 What gets retrieved

For each new VIG run, the retrieval layer pulls from the persistent visual canon:

- **Releases sharing semantic load with the current song.** Same motif triggers, same thematic material, same emotional arc.
- **Releases from the same tempo/genre neighborhood.** For stylistic continuity at the rhythm/motion level.
- **Most recent N releases.** For recency bias (what does "now" look like for this artist).
- **Releases explicitly referenced in the current song's lyrics.** Callback mechanism.

### 6.2 What the retrieval delivers

The retrieval returns, per source release:

```yaml
retrieved_reference:
  release_id: "release_002"
  release_date: "2026-02-28"
  shared_motifs_used: ["water_delta", "ghost_reverb_visual"]
  shared_themes: ["heritage", "return"]
  stylebook_version_at_release: "1.1.0"
  visual_highlights:
    - type: "establishing_shot"
      timestamp: "0:12"
      description: "<auto-generated or human-written description>"
      thumbnail_ref: "..."
    - type: "chorus_anchor"
      timestamp: "0:48"
      description: "..."
      thumbnail_ref: "..."
  reusable_assets:
    - type: "location"
      id: "the_shoreline"
      appearance_in_release: "0:10-0:20"
```

The LLM briefing stage then gets these retrievals as context, letting it *echo* prior decisions where echo serves the song, without copying where copy would be regressive.

### 6.3 The echo-vs-copy discipline

Spiral, not loop — from the motif registry, applied to continuity itself. Prior decisions should:

- **Echo** in the new release — the same motif at a new angle, the same location in new weather, the same subject in new wardrobe
- Not **copy** — identical shots are regressive and read as unearned

This is operationalized in briefing: retrieved references are passed with instruction *"echo these, do not reproduce."* The LLM is explicitly told to find the *variation* on the prior decision, not the repetition.

### 6.4 Operationalization

Retrieval is either:
- **Manual** — Mo curates which prior releases to reference per new release. Slow but auditable. Good for early MAESTRO operation.
- **Semi-automated** — a retrieval system indexes releases by motifs and themes; briefing prompt includes top-K matches. Mo reviews and prunes. Faster.
- **Fully-automated** — retrieval runs without review. Fast but risks semantic drift. Not recommended unless stylebook is mature.

**Initial recommendation: manual, graduating to semi-automated after 10+ releases in canon.** [DESIGN]

---

## 7. Failure Modes — Stylebook-Specific

| Failure | Symptom | Root Cause | Mitigation |
|---|---|---|---|
| **Stylebook bloat** | Stylebook grows past human-manageable size; generations slow to constraint-check | No pruning discipline; every whim becomes a rule | Patch cycle reviews; rules without recent application flagged for rejection consideration |
| **Stylebook contradiction** | Internal rules conflict; generations hit undecidable gates | Multiple patch bumps without conflict check | Automated contradiction check on every save; see §5.4 |
| **Stylebook abandonment** | New generations stop honoring canon | Friction too high to maintain; convenience wins | Reduce friction: briefing LLM injects stylebook automatically; make the lazy path the canonical path |
| **Stylebook drift** | Evolution over many releases erases original identity | No version-review discipline; small patches accumulate into identity change | Quarterly stylebook audit: diff v_now vs v_original, flag unacknowledged evolution |
| **Identity bundle collapse** | Artist identity becomes generic across releases | Identity Bundle treated as decorative, not mandatory | Make identity-lock mandatory in P4B conformance gate; no identity lock = automatic reject |
| **Motif over-use** | Every release includes the same motifs; audience fatigue | Motif registry treated as checklist rather than conditional | Enforce when-to-include rules strictly; require justification for every motif invocation |
| **Exclusion list underfits** | Same AI-default artifacts recur despite exclusions | Exclusions are declarative; models don't always obey | Add post-processing scrubbing step for specific recurring artifacts; graduate prompt-level exclusion to pipeline-level enforcement |
| **SIB misinterpretation** | Sloppy output defended as "Sacred Imperfection" | Cardinal rule not enforced | Require specific, cultivated imperfection; ban model-noise-as-imperfection in conformance gate |
| **Evolution log gaps** | Why the stylebook looks the way it looks becomes unrecoverable | Lazy documentation; rationale omitted | Schema-level mandate: every entry carries rationale; no rationale = not accepted |
| **Canon reversal erasing prior releases** | Major version bump invalidates prior visual identity | Major changes treated as upgrades rather than breaks | Major bumps are dated breakpoints; prior releases retain their canonical stylebook version as metadata |

---

## 8. Implementation Schema — How This Actually Lives

### 8.1 File layout recommendation

```
stylebook/
├── STYLEBOOK.md                          # human-readable overview + cardinal rules
├── stylebook.yaml                        # machine-readable canonical doc
├── evolution_log.yaml                    # append-only change log
├── sub_artifacts/
│   ├── aesthetic_constraint_map.yaml
│   ├── motif_registry.yaml
│   ├── identity_bundle.yaml
│   ├── exclusion_list.yaml
│   └── sacred_imperfection_budget.yaml
├── assets/
│   ├── identity/
│   │   ├── primary_ref_01.jpg
│   │   ├── primary_ref_02.jpg
│   │   └── primary_lora.safetensors
│   ├── wardrobe/
│   ├── locations/
│   ├── props/
│   ├── color_palette.ase                 # Adobe swatch export
│   ├── luts/
│   └── fonts/
├── retrievals/                           # cached references for recent release retrievals
└── README.md                             # operational notes for Mo + any collaborator
```

### 8.2 Storage and versioning

- **Git repository.** Every change is a commit. Full history preserved. Diffs auditable.
- **Semantic-versioned tags.** `v1.0.0`, `v1.1.0`, etc. per §5.3.
- **Release-tagged references.** Each song's release carries the exact stylebook tag it was generated against.
- **No deletions.** Rejected entries stay in the file with `rejected` status + rationale.

### 8.3 Operational tooling (minimum viable)

- **stylebook-lint:** validates YAML structure, checks every rule has rationale, detects contradictions, flags stale rules
- **stylebook-diff:** shows what changed between versions with rationale surfacing
- **stylebook-inject:** serializes stylebook for LLM system prompt injection (per §3.1)
- **stylebook-retrieve:** given a new song's UST, returns top-K relevant prior releases
- **stylebook-audit:** quarterly drift check, diffs current vs original, flags unacknowledged evolution

None of these need to be exotic — Python CLI tools over YAML files are sufficient. The discipline matters more than the tooling sophistication.

### 8.4 Access control

The stylebook is the artist's sovereign space. Access model recommendation:

- **Write access: artist only** (Mo), plus any explicitly authorized collaborator with change-class-specific permissions
- **Read access: VIG pipeline, P4B conformance gate, retrieval service**
- **Change review: artist-approved workflow**. Minor/major changes require explicit sign-off.

This is not paranoia — it is the mechanism that prevents silent overwrite. Mo's Fear #1 (erasure via overwrite) is blocked by access discipline.

---

## 9. A Minimal Worked Example — Mo's Symbolic Lexicon as First-Class Entries

Abbreviated. Demonstrates the schema in use with Mo's lexicon.

```yaml
# stylebook/stylebook.yaml
version: "1.0.0"
artist: "mo"
established: "2026-04-20"

aesthetic_constraint_map:
  palette:
    primary: ["#0a1929", "#e94560"]
    rationale: "Deep night-water + wound-crimson. From Delta and scar lexicon."
  lighting:
    preferred: ["single-source practical", "window-ambient"]
    discouraged: ["three-point", "beauty-bounced"]
    rationale: "Light casts ghosts — single sources keep shadows long."
  # ... (rest per §2.1 schema)

motif_registry:
  - id: "the_delta"
    status: "canonical"
    first_appearance: "release_001"
    second_intentional_appearance: "release_003"
    semantic_link: "Delta — origin, ghost, source code of heritage"
    visual_form:
      - "dark moving water at night or dusk"
      - "shore, threshold, edge — never open ocean"
      - "always returns, never simply depicts"
    when_to_include: ["heritage lyrics", "resolution moments", "opening of chorus"]
    when_to_exclude: ["pure kinetic trap", "daylight urban"]
  
  - id: "ghosts"
    status: "canonical"
    semantic_link: "Ghosts — the past speaking through the present"
    visual_form:
      - "double exposure at opacity < 30%"
      - "motion blur that persists"
      - "echoing figures in frame"
    when_to_include: ["reverb-heavy vocals", "memory-lyric moments"]
    when_to_exclude: ["dry clean sections", "present-tense narration"]
  
  - id: "spiral_not_loop"
    status: "canonical"
    semantic_link: "Echoes & Spirals — trauma repeats not flat but spiraling"
    visual_form:
      - "repeated framing at different angle/height"
      - "compositional echoes with modulation"
      - "color palette variation on return"
    when_to_include: ["repeated choruses", "bridge-to-final transitions"]
    when_to_exclude: ["first-time material"]
  
  - id: "blueprint_vs_render"
    status: "canonical"
    semantic_link: "Blueprints — pure objective code of intent before rendering"
    visual_form:
      - "line-work or architectural diagram overlaid on rendered image"
      - "technical-drawing aesthetic in transitions"
      - "exposed structure rather than concealed"
    when_to_include: ["bridge reveals", "structural lyrical moments"]
    when_to_exclude: ["pure emotional release moments"]

identity_bundle:
  primary_subject:
    persona_name: "mo"
    # reference images + LoRA when generated
    identity_lock_policy: "MANDATORY in every featured shot"

exclusion_list:
  visual_cliches:
    - "ai_sheen"
    - "rap_video_cliche_stack"
    - "drone_sweep_opening"
    - "text_bounce_caption"
    - "stock_footage_generic_people"
  meta_exclusions:
    - "karaoke-literal lyric illustration"
    - "averaged multi-genre aesthetic"
    - "AI-noise masquerading as Sacred Imperfection"

sacred_imperfection_budget:
  baseline: 0.7
  cardinal_rule: "Everything can be rough; nothing can be false."
  operationalizations:
    grain: {injection_strength: "moderate", iso_equivalent: 800}
    camera_motion: {handheld: "strong", micro_jitter: "preserved"}
    color: {polish: "restrained", blown_highlights: "allowed"}
    subject: {skin_texture: "preserved", asymmetry: "preserved"}
```

This is a starting point. Every subsequent release adds to and refines this. After 5 releases, the stylebook will be much richer. After 20, it is a canon in the archival sense.

---

## 10. MAESTRO v5 Integration Update

The stylebook touches every phase:

```
P1 — Conception
  └ Stylebook consulted for thematic alignment (what songs fit the artist canon?)

P2 — Draft Assembly
  └ Lyric generation considers Motif Registry for thematic callback opportunities
  └ Writer prompted with stylebook themes and prior-canon references

P3 — Performance and Identity Fit
  └ Voice/persona selection references Identity Bundle for coherence

P3.5 — UST Compilation (v0.2)
  └ Stylebook biases TRIAD inference (v0.2 §4 visual_directives)
  └ Motif triggers evaluated against UST sections

P4A — VIG: Visual Identity Generation
  └ PRIMARY CONSUMER
  └ Stylebook injected at every generation stage (§3.1–3.4)
  └ Retrieval from prior canon runs before briefing (§6)

P4B — Visual Conformance Gate
  └ Stylebook is the conformance spec
  └ Identity lock mandatory; exclusions automatic-reject

P5 — SEL: Surface Export Layer
  └ Stylebook typography and color rules applied per export variant
  └ Caption style per ACM typography block

POST-P5 — Canonization
  └ Released artifact added to retrieval index
  └ Stylebook patch/minor bump for new learnings
  └ Evolution log updated
```

The stylebook is not a phase itself — it is the substrate every phase reads from and writes to.

---

## 11. Open Questions

1. **[UNRESOLVED]** How much of the stylebook should be human-written vs LLM-assisted? The rationales need to be honest; the schema needs to be machine-readable. Middle ground: LLM drafts, human edits for truth.

2. **[PROVISIONAL]** Can motif triggers be learned from prior release data automatically? Eventually yes (train a small classifier on "when did Mo use water_delta in prior releases" vs song features). Not necessary for v1.

3. **[UNKNOWN]** At what release count does the retrieval system start paying off vs. adding noise? Initial guess: 5+ releases to have meaningful retrieval; 10+ for reliable patterns. Requires observation.

4. **[UNRESOLVED]** Should the stylebook version be mandatory metadata on rendered artifacts, or suggestion? Recommended mandatory — no exceptions. But that requires tooling discipline.

5. **[PROVISIONAL]** Multi-artist stylebooks (features, collaborations) — merge or federate? Federation is cleaner; merging risks identity confusion. Initial recommendation: per-release federation with conflict resolution at briefing stage.

6. **[UNKNOWN]** Can the exclusion list be auto-populated from post-release audience signals (comments flagging AI-looking shots)? Possible future direction; requires sentiment-aware feedback ingestion.

7. **[UNRESOLVED]** Stylebook for non-music contexts (album artwork, merchandise, press photos) — same stylebook or separate? Recommend: same stylebook, different output surfaces. Merchandise is just another SEL target.

---

## 12. Closing — Why This Goes First

In any real build of MAESTRO v5, the temptation is to start with what's exciting: the video generation, the model pipeline, the audio compilation. All of that is load-bearing.

But the stylebook is the one artifact without which the rest produces competent-but-nameless output. With a stylebook, every VIG run reinforces the artist's identity. Without it, every VIG run is a fresh attempt to guess.

The practical roadmap ordering:

1. **Week 1–2:** Establish stylebook v1.0.0 from existing work. Even if only release_001 exists, the stylebook can be retroactively derived.
2. **Week 3+:** Build VIG on top. VIG depends on stylebook; no stylebook, no VIG.
3. **Ongoing:** Stylebook evolution with every release. The canon compounds.

This reordering of priorities is the practical consequence of taking v0.3 seriously. [DESIGN]

---

## Appendix — Evidence and Design Notes (v0.3-specific)

Most of v0.3 is **design** — architectural choice justified by the goal rather than external data. Specific references:

- **Erasure-resistance doctrine operationalization** — derived from Mo's character sheet, specifically Fears & Vulnerabilities §1 (Erasure) and Symbolic Lexicon (Blueprints, Ghosts). [DESIGN]
- **Canon-draft discipline extended to the stylebook itself** — extends Mo's collaboration framework (userMemories: "Separate canon from draft, accepted decisions from speculative proposals"). [DESIGN]
- **Spiral-not-loop principle applied to cross-release continuity** — extends Mo's Symbolic Lexicon (Echoes & Spirals). [DESIGN]
- **Sacred Imperfection Budget as single parameter** — operationalizes Mo's "Sacred Imperfection" symbolic entry. [DESIGN]
- **Cardinal rule "Everything can be rough; nothing can be false"** — direct extension of Mo's stated principle. [DESIGN, DERIVED FROM MO'S OWN FRAMEWORK]
- **Git-style versioning for stylebook** — standard software-engineering practice applied to canon management. [DESIGN]
- **Retrieval with echo-not-copy discipline** — leverages cross-modal retrieval patterns from v0.1 §2.6 (MuQ-MuLan, CLAP similarity) combined with the Motif Registry's when-to-include rules. [DESIGN]

No new external research was required for v0.3 — the dossier is synthesis and specification. Its claims rest on design soundness, internal consistency with v0.1 and v0.2, and alignment with Mo's explicit framework.

---

**End of Research Dossier v0.3**

*Pairs with v0.1 and v0.2. Accepted sections become MAESTRO canon. The stylebook, specifically, becomes the substrate every accepted section reads from.*
