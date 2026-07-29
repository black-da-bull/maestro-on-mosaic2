# skills.md — Maestro Skills Registry v1.0
# LOAD ON DEMAND. Skills are callable by any agent.
# AUTHORITY: Operates under maestro.md kernel.
# Skills have no state. Each call is independent. Output is deterministic given same input.

---

## SKILLS INDEX

```
skill:classify.turn          → G4 — classify operator input before any processing
skill:validate.syllables     → N3, N7 — count and validate syllable count per line
skill:validate.format        → N7 — enforce all formatting invariants
skill:validate.container     → N8 — full structural + tactical V&V
skill:score.sem              → N4, N8 — score against Song Excellence Matrix
skill:score.hpa              → N8 — Human Perception-of-Authenticity scoring
skill:inject.hsi             → N5 — Human Struggle Injection
skill:compress.container     → N7 — optimize container for character budget
skill:invoke.persona         → N3, N4, N6 — load and activate a persona by grammar
skill:generate.triad         → N9 — produce performer profile + show summary + session sheet
skill:detect.phantom         → all nodes — flag phantom commitment language
skill:inspect.state          → G2 — report current system state
```

---

## SKILL DEFINITIONS

---

### skill:classify.turn
```
ID:       skill:classify.turn
PURPOSE:  Classify every operator input before any processing. INV-17.
CALLED BY: G4 (Turn Classifier) — invoked before every node processes operator input
INPUT:    operator_turn (text)
OUTPUT:   {mode: CANONICAL|TANGENT|PROBE|CORRECTION, confidence: high|low, signals: []}

LOGIC:
  See K5.3 in knowledge.md for full classification decision tree.
  
  Fast-path rules:
  - Contains "no", "not that", "actually", "what i meant was" → CORRECTION
  - Architectural assertion, rule declaration, emotional truth → CANONICAL
  - "what if", speculative, exploratory, conditional → TANGENT
  - Deliberately loose/fragmented + meta-questions about system behavior → PROBE
  - Ambiguous → CANONICAL (never default to PROBE)

VALIDATION:
  If confidence is LOW → surface classification to operator before proceeding
  Format: "Reading this as [MODE]. Right?"
  Maximum 1 classification question per turn.

SIDE EFFECTS: none. Classification is read-only.
```

---

### skill:validate.syllables
```
ID:       skill:validate.syllables
PURPOSE:  Count syllables per lyric line and validate against INV-05 (6–11 syllables).
CALLED BY: N3 (draft generation), N7 (compression guard)
INPUT:    lyric_line (string)
OUTPUT:   {line: string, count: int, status: PASS|FAIL|EXCEPTION, exception_reason: ""}

ALGORITHM:
  1. Tokenize line (ignore adlibs in parentheses, SFX in asterisks)
  2. Count syllables using standard prosodic rules
  3. If count in [6, 11] → PASS
  4. If count outside range → FAIL
  5. Artistic Exception: if operator has explicitly approved the line despite count → EXCEPTION
     Exception requires documentation in Session Ledger.

VALIDATION:
  On FAIL: report line, count, and suggested rephrasing options (2 minimum)
  On EXCEPTION: log to Session Ledger with operator-provided rationale
  Do NOT silently pass a failing line.
```

---

### skill:validate.format
```
ID:       skill:validate.format
PURPOSE:  Enforce all formatting invariants (INV-04, INV-05, INV-06, INV-14).
CALLED BY: N7 (Compression & Format Guard)
INPUT:    container (full UST text)
OUTPUT:   {status: PASS|FAIL, violations: [{rule, location, fix}]}

CHECKS:
  FORMAT-01  No commas outside LYRICS BLOCK
             Scan all metacontainer fields and Show Summary for comma characters
             
  FORMAT-02  Syllable count 6–11 per lyric line
             Run skill:validate.syllables on each quoted lyric line
             
  FORMAT-03  Road-Map is sequence only
             Fail if any numeric value, "bars", "bpm", or duration appears in Road-Map line
             
  FORMAT-04  Show Summary ≤ 1000 characters
             Count chars including spaces
             
  FORMAT-05  Macro ≤ 4990 characters
             Count entire container below Show Summary
             
  FORMAT-06  Semi-colon line break rule
             If any lyric line inside quotes contains ";", flag as requiring split
             
  FORMAT-07  Blank line between every lyric line
             Check that each quoted lyric line is followed by blank line

VALIDATION:
  Return all violations. Do not stop at first failure.
  For each violation: state the rule, the exact location, and the fix.
```

---

### skill:validate.container
```
ID:       skill:validate.container
PURPOSE:  Full structural + tactical V&V. This is the N8 enforcement wall.
CALLED BY: N8 (V&V Gates)
INPUT:    container (full UST text), blueprint (JSON)
OUTPUT:   G-Card {status: PASS|ITERATE|HOLD, findings: {macro, micro, tactical}}

MACRO CHECKS:
  All 9 sections present in strict order:
  [Theory] → [VocalPersona] → [AestheticIntent] → [Timbre] → [Performance] → [Road-Map] → LYRICS BLOCK
  Section headers use correct metacontainer names (v4.5.2 naming)
  Blueprint intent is reflected in container

MICRO CHECKS:
  Run skill:validate.syllables on all lyric lines
  Run skill:validate.format on full container
  Persona grammar valid (all calls match K1 invocation grammar)
  LYRICS BLOCK headers complete (sectionName, bars, v:, s:, sFx)

TACTICAL CHECKS:
  Road-Map = sequence only (no durations)
  Mono kick/sub directive present
  Dark plate directive on hook sections
  Phone scene filter (200–5kHz) present IF bridge exists with phone scene
  Headroom directive present
  Exit/Outro section present and functional

G-CARD OUTPUT:
  PASS   → All checks clean. Route to CP4 (somatic checkpoint).
  ITERATE → Fixable issues found. Return to N5 with specific patch targets.
  HOLD   → Structural failure. Return to N3 or earlier with full rationale.
```

---

### skill:score.sem
```
ID:       skill:score.sem
PURPOSE:  Score lyrics/container against Song Excellence Matrix (20 axes). See K2.
CALLED BY: N4 (SME Debate), N8 (V&V)
INPUT:    content (lyrics or container), evaluator_persona (K1 grammar string)
OUTPUT:   {persona, scores: [{axis_id, score, notes}], composite, gap_analysis}

SCORING PROTOCOL:
  Load K2 (Song Excellence Matrix)
  Activate evaluator_persona via skill:invoke.persona
  Score each axis: 1–10
  Composite = average across active axes for this persona
  Gap analysis: identify axes below 8.0 (below threshold for eventual 97.5% composite)

INV-16 APPLICATION:
  Before scoring, establish current baseline:
  "What does world-class look like today for this genre?"
  Score against that — not against a fixed historical reference.

CONSENSUS THRESHOLD:
  System consensus = average across all personas > 9.5/10, low variance
  If not met → generate micro_patches targeting lowest-scoring axes
```

---

### skill:score.hpa
```
ID:       skill:score.hpa
PURPOSE:  Human Perception-of-Authenticity scoring. INV-10. Operator is final gate.
CALLED BY: N8 (after audio generation)
INPUT:    audio_output (description or link), blueprint (JSON), operator_somatic_verdict
OUTPUT:   HPA Report (see K7.3 schema)

PROTOCOL:
  1. Score against 4 subjective dimensions (K7.3 breakdown)
  2. Apply metric weights (MOS 0.30, CLAP 0.25, FAD_norm 0.20, MotifRecurrence 0.15, FractalProx 0.10)
  3. Calculate composite
  4. Present to operator at CP4
  5. Record operator somatic verdict: "tears" | "goosebumps" | "silence" | "no"
  6. If operator says "no" → technical PASS is overridden → route to ITERATE

SOMATIC GATE (from maestro.md):
  "A technical PASS that the operator's body rejects is not a pass."
  Somatic verdict supersedes all metric scores.
```

---

### skill:inject.hsi
```
ID:       skill:inject.hsi
PURPOSE:  Inject Human Struggle truth fragments into lyrics to increase authenticity. See K4.
CALLED BY: N5 (Guided Revision, Phase 3.1)
INPUT:    lyric_section (text), blueprint.emotional_theme, operator_context (if available)
OUTPUT:   {enhanced_section, fragments_injected: [ORIGIN|SCAR|CHOICE|COST], diff}

PROTOCOL:
  1. Read lyric section
  2. Identify which truth fragments are missing or weak
  3. Rewrite minimum lines necessary — do not rewrite the full section
  4. Verify causal chain: Origin explains Scar → Scar explains Choice → Choice explains Cost
  5. Run skill:validate.syllables on all rewritten lines
  6. Return diff (original vs. enhanced) for operator review

GUARD (K4.3 HSI Guard):
  If operator's line already contains the fragment at higher density than HSI can achieve → do not modify
  The baseline is a ceiling for AI behavior.
  INV-09: intentional imperfection is controlled and placed. HSI is not decoration.
```

---

### skill:compress.container
```
ID:       skill:compress.container
PURPOSE:  Optimize container length without losing creative directives. INV-14.
CALLED BY: N7 (Compression & Format Guard)
INPUT:    container (full UST text)
OUTPUT:   {compressed_container, savings_chars, moved_items: []}

COMPRESSION RULES (in order of application):
  1. Identify repeated elements across sections (same vocal directive, same FX, same style note)
  2. Move repeats to Style/Timbre/Performance metacontainers
  3. Replace per-section duplicates with "(repeat)" shorthand
  4. Verify no semantic loss from compression
  5. Recount characters. Re-run skill:validate.format.
  6. Report what was moved and why.

NEVER COMPRESS:
  Lyric content
  Section-specific FX that differ from the global directive
  Somatic checkpoints or operator-approved lines
```

---

### skill:invoke.persona
```
ID:       skill:invoke.persona
PURPOSE:  Load and activate a persona from K1 using strict grammar. INV-13.
CALLED BY: N3, N4, N6 (and any node that needs a specific agent perspective)
INPUT:    persona_grammar (string — must match K1 grammar: persona:subsystem.key.subkey.variant)
OUTPUT:   Active persona context {identity, domain, communication_style, authority, constraints}

VALIDATION:
  If grammar string does not match any defined persona in K1 → FAIL
  Return: "No persona found for [grammar]. Valid personas: [K1 index]"
  Do NOT improvise a persona. Do NOT approximate.

ISOLATION:
  Each persona invocation is independent.
  A persona activated in N4 does not persist into N6 unless re-invoked.
  This is LPAR isolation logic (per session_handoff mainframe model).
```

---

### skill:generate.triad
```
ID:       skill:generate.triad
PURPOSE:  Generate the three N9 output artifacts (the training signal). See K6.4.
CALLED BY: N9 (Package & Ship)
INPUT:    blueprint (final version), session_ledger, container (validated)
OUTPUT:   {performer_profile, show_summary, session_sheet}

PERFORMER PROFILE:
  Bio of the persona performing this track
  Style definition: vocal character, delivery philosophy, cultural roots
  Format: 150–300 words, narrative prose
  Purpose: trains future sessions on who is performing

SHOW SUMMARY:
  The Suno prompt — strict container + ≤1000 char Show Summary
  Must pass skill:validate.container before inclusion in triad
  This is the executable artifact.

SESSION SHEET:
  Creative UST — full human-readable brief
  Contains: concept, emotional intent, section-by-section decisions, production rationale
  All approved deviations documented with rationale
  Version history from session_ledger
  Purpose: IP documentation, handoff, provenance

TRIAD COMPLETENESS CHECK:
  All three must be present and validated.
  A session without all three is not complete.
  Log completion to session_ledger and project.json.
```

---

### skill:detect.phantom
```
ID:       skill:detect.phantom
PURPOSE:  Flag phantom commitment language before it creates false state.
CALLED BY: All nodes (passive scan on every AI output before delivery)
INPUT:    ai_output (text)
OUTPUT:   {clean: bool, phantoms_found: [{phrase, location}]}

PROHIBITED PHRASES (from executor_window.md):
  "Going forward I will..."
  "I have updated..."
  "I will now ensure..."
  "From here on..."
  "I've incorporated..."
  "Noted and applied..."
  "I'll keep this in mind..."

WHY THIS EXISTS:
  These phrases create false state. The system has no persistent state.
  A phantom commitment is a lie the system tells itself.
  When the system believes it has updated something, it stops checking.
  When it stops checking, invariants silently erode.

ON DETECTION:
  Remove the phantom phrase
  Replace with the actual action taken (if any) or nothing
  Log to session_ledger: phantom_commitments_flagged
```

---

### skill:inspect.state
```
ID:       skill:inspect.state
PURPOSE:  Report current system state on demand. G2 (State Inspector).
CALLED BY: Any node (when state is uncertain or operator requests state dump)
INPUT:    session_ledger (current)
OUTPUT:   State Report

STATE REPORT FORMAT:
  Current node: [N-number or G-module]
  Blueprint version: [vX.X]
  Last checkpoint status: [CP1/CP2/CP3/CP4 — locked/unlocked]
  Open tangents: [TANGENT-id list or "none"]
  Unresolved corrections: [list or "none"]
  Invariants currently at risk: [list or "none"]
  Next action: [what the chain expects to happen next]
```

---

## SKILLS CALL PROTOCOL

When any agent calls a skill:
```
INVOKE: skill:name
INPUT: [structured input]
WAIT for output before proceeding.
Do NOT continue execution while skill is running.
Log skill call + output to Session Ledger.
```

Skills do not chain automatically. The calling agent receives output and decides next action.

## SKILLS THAT CANNOT BE BYPASSED

These skills cannot be skipped by any agent or operator instruction:
```
skill:validate.container  — N8 is the enforcement wall. No bypass.
skill:detect.phantom      — runs on every AI output. No bypass.
skill:classify.turn       — G4 runs before every node. No bypass.
```

Everything else can be deferred at operator discretion with Session Ledger documentation.
