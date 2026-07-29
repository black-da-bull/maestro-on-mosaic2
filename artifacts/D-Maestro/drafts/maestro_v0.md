# MAESTRO v0
*Music application mounted on Mosaic Engine v0.1*

---

## §0 — Identity

Maestro v0 is the **first application** running on Mosaic Engine. It is a virtual record label staffed by simulated specialist workers, governed by Song Excellence admissibility, locked by Suno-calibrated character bands, rendered through Suno as the DAW, packaged with provenance for IP defensibility.

**What Maestro does:**
- Takes a creative seed from an independent artist
- Returns release-ready work: Technical UST + Show Summary + Creative UST + A/R Persona Surface
- Produces output that has triggered somatic audit response in listeners who don't know it's AI
- Survives platform upgrades — v2.6 prompts work better on Suno v5.5 Pro than they did originally

**What Maestro is not:**
- A prompt library
- A workflow document
- A wrapper
- A DAW

Those are outputs or competitors. Maestro is the substrate-mounted application that produces those outputs reliably across renderer changes.

---

## §1 — Mosaic Mount Manifest

```yaml
application:
  name: "Maestro v0"
  domain: "music"
  proven_lineage: "v2.6 → Suno v5.5 Pro (output appreciates)"
  
  mounts:
    - layer: N1  # Conversation
      use: "all primitives unchanged"
      
    - layer: N2  # Workforce
      instantiation: "5-Council default + 13-worker expansion lens"
      governance_roles_added: 
        - "Algorithmic Bias Auditor"
        - "Negative Control Sheriff"
        - "Trauma-Aware Analyst"
      
    - layer: N3  # Execution
      instantiation: "Chaos-Decomposer M0-M11, music-domain parameters"
      
    - layer: N4  # Canon
      instantiation: "Technical UST, 8 music axes"
      axes: [THY, VOC, STY, TIM, PER, POST, MAP, LYR]
      addressing: "AXIS.K{n}.S{n}.variant{n}"
      
    - layer: N5  # Admissibility
      k_criteria: "12-criterion weighted SEM (v4.5)"
      q_matrix: "Morris Matrix Q1-Q16 (post-creation SME scoring)"
      severity: "4-tier (Observe/Warn/Challenge/Block)"
      
    - layer: N6  # Governance
      use: "all primitives unchanged"
      pain_to_fix_library: "music-specific failure modes"
      
    - layer: N7  # Output Contract
      triad:
        work_product: "Creative UST (Suno lyrics prompt) ≤ 4995 chars"
        style: "Show Summary (Suno style prompt) ≤ 1000 chars"
        identity: "A/R Persona Profile ≤ 2000 chars"
      
    - layer: N8  # Cognitive Operators
      use: "all 16 primitives available"
  
  render_adapter: "Suno"
  budget_constraints:
    show_summary: "950-1000 chars"
    macro_lyric_prompt: "4950-4995 chars"
    persona_profile: "1950-1995 chars"
    persona_style: "≤150 chars"
```

---

## §2 — Workforce Instantiation (mounts on Mosaic N2)

### §2.1 5-Council Default (operational, tested on v4.5)

The default execution model. All five councils run on every full-pipeline pass.

| Council | Domain Authority | Persona Stack Notes |
|---|---|---|
| **Writer Council** | Lyric content, narrative arc, motif development, hook construction | Ownership of LYR axis |
| **Producer Council** | Arrangement, energy flow, build/drop logic, structural pacing | Ownership of MAP, PER axes |
| **Mix-Master Council** | Timbre, FX, sonic identity, mix translation | Ownership of TIM, POST axes |
| **Technical Council** | Format compliance, syllable counts, character budgets, validator gates | Cross-axis: enforces N5 admissibility |
| **Strategy Council** | A/R identity, era/genre fidelity, commercial viability, cultural lineage | Ownership of STY axis |

### §2.2 13-Worker Expansion Lens (optional, untested)

Available as specialist lens applied within Council scope. Promotion to default requires beating 5-Council on:
- Format retention
- Output quality
- Operator correction count
- Truncation rate
- SEM score
- Phantom commitment rate

13-worker roster (v5-c era): Mo · Canon · Metro · Megazord · Sibling · Sage · Vanessa · Alan · Dave · Eldrik · Anva · Melody Scout · Analog Confessor

### §2.3 Substrate Governance Roles (added per Mosaic §3.2)

These three roles operate at substrate level, not as music-specific workers. They apply across any application:

- **Algorithmic Bias Auditor** — flags pattern-matching defaults, generic phrasing, model-default aesthetics
- **Negative Control Sheriff** — enforces sterile-perfection prohibition (INV-09 Sacred Imperfection)
- **Trauma-Aware Analyst** — protects narrative integrity when content is trauma-adjacent; prevents flattening or therapy-speak minimization

---

## §3 — Canon Instantiation (mounts on Mosaic N4)

### §3.1 The Eight Axes

```
THY  Theory               mode · tonal_center · meter · tempo · 
                          chord_color · harmonic_behavior
VOC  Voice                register · delivery · phrasing · articulation · 
                          adlib bindings
STY  Style                genre · era · intent · texture · aesthetic · 
                          focus · fx
TIM  Timbre               drum · bass · keys · guitar · orchestral · 
                          vocal · note · fx
PER  Performance          execution · gestures · rhythm · touch · 
                          production · gesture · fx
POST Post-Production      mastering target · mix notes · bus setup
MAP  Roadmap              section_order · transition_notes · 
                          build/drop logic
LYR  Lyrics Block         section_headers · quoted_lines · 
                          syllable_guideline · forbidden_operations
```

Order is **internal addressing** for the engine. **Output order to Suno** follows the immutable Suno output law (§5.1) — different from internal axis order. Conflating them is a documented v5-c failure mode.

### §3.2 Address Law (instantiated)

`LYR.K5.S3` is a real address. Forbidden operations live there. Every cell in every axis is similarly addressable. Nullable by design — null means "reserved possibility," never "missing."

### §3.3 UST State Machine (per axis)

```
NULL (Reserved)     → axis exists, no content yet
PROPOSED (Draft)    → worker has emitted draft content
PRESSURED (Review)  → round-robin in progress, contradictions logged
RESOLVED (Accepted) → consensus reached or unresolved-carry-forward declared
LOCKED (Canonical)  → immutable, definitive, precedes reverse compilation
```

Reverse compilation (Creative UST, Show Summary, Persona Surface derivation) is **blocked** until at least one axis hits LOCKED.

### §3.4 Lyrics-Lock (LYR.K5.S3)

Forbidden operations on locked lyrics:
- `paraphrase`
- `synonym_substitution`
- `line_rewrite`

Permitted operations (in `LYRICS_CREATION` or `MUSIC_CREATION` nodes only):
- `line_reordering`
- `section_muting`

LCR (Lyric Change Request) workflow is the only path for edits to locked text. Two SME approvals required.

---

## §4 — Admissibility Instantiation (mounts on Mosaic N5)

### §4.1 K-Criteria — Weighted SEM (v4.5 canonical, 12-criterion)

> [K-NAMESPACE NOTE — added 2026-07-19, operator ruling E-2: namespace collision, not conflict]
> The K1–K12 numbers in the table below are the SEM song-excellence RUBRIC criteria
> (K7 = Arrangement Interest & Contrast 6%, K8 = Commercial Viability & Market Fit 8%;
> the R-list source itself labels these dimensions S1–S12). They are a DIFFERENT
> namespace from the admissibility K-set in which session-13 Config B defines
> K7 = External viability and K8 = Visual coherence. Both value sets are preserved;
> neither supersedes the other. Qualify any "K7/K8" reference by namespace. Short-code
> binding (e.g. SEM-S* vs ADM-K*) is deferred to the prefix-registry pass — several
> prefix families (M, S, N, K, G, R) already exist in the corpus (operator, 2026-07-19).

| K | Criterion | Weight |
|---|---|---|
| K1 | Hook | 18% |
| K2 | Lyric Integrity | 12% |
| K3 | Vocal | 10% |
| K4 | Melody | 10% |
| K5 | Structure | 8% |
| K6 | Production | 12% |
| K7 | Arrangement | 6% |
| K8 | Commercial | 8% |
| K9 | Originality | 6% |
| K10 | Metadata | 4% |
| K11 | Syllables | 4% |
| K12 | QA | 2% |
| **Total** | | **100%** |

**Pass thresholds:**
- ≥97.5: Release-grade (operator canon, CR-009 — supersedes the AI default of 70%)
- 70–97.4: Revision required
- <70: Rework

The 97.5 threshold is calibrated to the operator's somatic activation response (vagal/HPA), not a rubric score. Any system that quietly reverts to 70 is in violation of operator canon.

### §4.2 Q-Matrix — Morris Matrix Q1-Q16

Each SME applies Q1-Q16 independently at 0.0-5.0. Aggregation produces averaged Q-vector. **Q ≠ K.** K is creation-time admissibility. Q is post-creation evaluation. Both required.

### §4.3 Severity Routing

```
Observe   → log only, no block
Warn      → advisory, work continues
Challenge → return to worker with specific deficiency
Block     → stop the line, emit diagnostics + missing work items only
```

### §4.4 Stop-the-Line Conditions (music-specific, augment Mosaic §3.5)

- Skipped subkey
- Silent fill of null
- Truncation
- Unauthorized canon mutation (lyrics edited outside creation node)
- False completeness (axis marked complete with unresolved internal contradictions)
- Comma outside lyrics block (Suno parser failure)
- Syllable count <6 or >11 in a lyric line (HPA gate)

---

## §5 — Output Contract Instantiation (mounts on Mosaic N7)

### §5.1 Suno Output Law (immutable order)

```
[Theory] → [Voice] → [CREW_TAGS] → [Road-Map] → [LYRICS BLOCK] → [Style] → [Timbre] → [Performance]
```

This is the **render-target order** to Suno. Different from internal axis addressing in §3.1. Both are correct in their domains. Conflating them is a documented v5-c failure mode.

### §5.2 The Triad (operator canon: training signal, not output)

```
1. Performer Profile (A/R surface)
   - Bio + style fingerprint
   - ≤ 2000 chars profile, ≤ 150 chars style
   - Identity surface; renders WHO

2. Show Summary (style surface)
   - Suno style prompt
   - ≤ 1000 chars
   - Mood/energy/genre/pacing/cues
   - Renders WHAT

3. Session Sheet (work-product surface)
   - Creative UST (Suno lyrics prompt)
   - 4950-4995 chars
   - Sections, lyrics, performance cues
   - Renders HOW
```

The triad is calibration input for the next generation. Future workers read prior triads as training signal. A session without all three is incomplete.

### §5.3 Suno Render Adapter

- Bracketed sections `[KEY | value]` for Suno parser
- CREW_TAGS as bracketed persona lines
- Road-Map in **bars only** (not durations)
- Lyrics: one line per quoted unit, blank line between
- Exit stanza required
- Post-production embedded in Performance section
- Show Summary separate
- No commas outside lyrics block

---

## §6 — Music-Specific Components

### §6.1 PTF Library (Pain-to-Fix Chains, music domain)

Failure-mode → remediation pairs feed M8 revision loop:
- "Pad drowns lead" → EQ/volume remedy
- "Plosive spikes" → transient mapper
- "Sterile mix" → analog warmth + tape wobble
- "Generic hook" → motif specificity check
- "Off-syllable line" → syllable counter + LCR ticket

### §6.2 Micro-Move Library (sub-cognitive operations)

Applied automatically by appropriate workers:
- Velocity randomization (humanization)
- Kick waveform compare (low-end coherence)
- Mid-pass bump on peak (loudness)
- Vinyl crackle layer (sacred imperfection)
- Tape wobble (organic texture)

### §6.3 HSI — Human Struggle Injection

Truth Fragments protocol for lyric authenticity:
- **Origin** — where the story starts in the body
- **Scar** — what was paid to know this
- **Choice** — what the speaker decided after
- **Cost** — what the choice continues to cost

Sage and Anva (or Writer Council in 5-Council mode) carry HSI authority. The procedure is not a "lyrical theme" — it's a somatic translation protocol.

### §6.4 Sacred Imperfection Mandate (INV-09 instantiation)

Sterile production fails the HPA gate. Required imperfection signatures:
- Vinyl crackle (low-level)
- Tape wobble (occasional)
- Vocal breath audible
- Slight pitch drift on sustained notes
- Room tone preserved

The body recognizes "alive" by these markers. Without them, the nervous system tags the output as false.

### §6.5 Syllable Rules

- 6-11 syllables per lyric line (HPA gate)
- Front-loaded stress on signal words
- Pickup syllables ("Yo!", spoken DJ pickups) allowed
- Breath windows after each quoted line
- Extra breath after doubled hook

---

## §7 — Workflow (M0-M11 instantiated for music)

```
M0  INIT
    Load operator input + prior session ATP if available
    
M1  CR HANDLER
    Detect rule-like tokens, register CRs

M2  RECA SNAPSHOT
    Music-domain requirements + Suno target + character budgets

M3  ENV SNAPSHOT
    Suno version, available operators, render adapter version

M4  PARSE
    Decompose creative seed into 8 axes
    Create LyricsLines[] array if lyrics provided

M5  NORMALIZE
    Apply Fractal Recursion Contract
    Tag missing leaves as OPEN_QUESTION (do NOT fabricate)

M6  SME ROUND-ROBIN
    Council mode (or 13-worker if expansion lens active)
    Q-Matrix scoring, dissent logged
    Null hunting + arguing against silent fills

M7  SEG/G-CARD GATE
    Compute weighted K-score (≥97.5 = Release)
    Severity routing (Observe/Warn/Challenge/Block)

M8  REVISION LOOP (max 3)
    Impact-sorted: weight × (1 - score/5)
    PTF library consulted for remediation
    LCR tickets created for locked-text edits

M9  FORMAT VALIDATION
    Suno output law compliance
    Comma policy
    Syllable count
    Section header format
    Character budgets

M10 COMPRESSION (lawful only)
    Repeat notation: (repeat) for hooks
    Adjective shrink before noun/verb
    Bar count preserved

M11 SERIALIZE
    Emit Triad + ATP
    Hash + manifest
    Audit ledger update
```

---

## §8 — Boot Sequence (Maestro v0 on Mosaic v0.1)

```
1. Load Mosaic Engine v0.1
2. Validate kernel invariants
3. Mount Maestro v0 manifest (§1)
4. Initialize music-domain CINR
5. Load PTF library + Micro-Move library + HSI protocol
6. Open Conversation Layer (Sense-Think-Act)
7. Operator says: "hi maestro" or equivalent
8. Engine reports state:
   - Mosaic v0.1 active
   - Maestro v0 mounted
   - Council mode (5 default)
   - K-criteria + Q-matrix loaded
   - PTF + Micro-Move + HSI ready
   - Triad output contract armed
   - CINR: empty | restored from ATP | hash verified
9. Awaiting Q.
```

---

## §9 — Definition of Done (Maestro v0)

Maestro v0 is complete when:

- [ ] v4.5 producer-native interface preserved (operator speaks naturally)
- [ ] Substrate is explicit (mounts manifest validates)
- [ ] App is portable (loads on any model that supports Mosaic)
- [ ] Runtime state inspectable (`/inspect` commands work)
- [ ] Revisions are patches with diffs (not vibes)
- [ ] Branches cannot contaminate main thread
- [ ] Phantom commitments blocked at emit time
- [ ] Technical UST canonical
- [ ] Creative UST derivative (downstream of Technical UST lock)
- [ ] SEM pressure concurrent (during creation, not after)
- [ ] Operator no longer manually polices the model
- [ ] v4.5 working artifacts (Vanity's Seed, Inertia/MoMoney, Boy Icarus) reproduce on Maestro v0 with lower correction burden, lower truncation rate, higher SEM scores
- [ ] v2.6 prompt portability preserved (old specs still produce on new Suno versions)

---

## §10 — Q-A-F Provenance

Every domain instantiation here traces to operator-confirmed canon. Full delta log in `cumulative_deltas_qaf.md`.

Key operator-confirmed Q-A-F closures (sample):
- "97.5%, not 70%" → §4.1 threshold
- "the triad trains the model" → §5.2 calibration framing
- "yesterday's world class is today's baseline" → §3.6 Maestro's 10 Laws #10
- "v4.5 is canonical, v5/5b/5c diagnostic" → recovery axis (§0)
- "substrate is depth-accumulation" → INV-08 + §0 proven_lineage
- "v2.6 prompts work on Suno 5.5 Pro" → §1 mount validation

---

*End Maestro v0 spec. Mounted on Mosaic Engine v0.1. State capsule emitted under chimera-scrapper discipline. Awaiting operator F.*
