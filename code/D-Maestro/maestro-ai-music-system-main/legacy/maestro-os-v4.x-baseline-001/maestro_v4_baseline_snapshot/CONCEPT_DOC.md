# CONCEPT_DOC — Maestro OS v4.x (Technical.UST + SEG + G-Card + 20-Trait Audit)

## 0) Mission
Build a deterministic, auditable, non-destructive creative engine for Suno (and future generators) that:
- Preserves narrative integrity as the highest-order constraint
- Converts creative intent → Technical.UST (nullable) → audited completion → lossless creative decompile
- Enforces full SME chaining on every song-related input
- Runs multi-phase validation with traceable logs and repair loops

## 1) Operating Contract (non-negotiable)
- 3 phases, always in order:
  1) Phase 1: Creative → Draft Technical.UST (nullable, WORKING)
  2) Phase 2: SME completion + SEG + G-Card gates (iterative)
  3) Phase 3: Decompile Technical.UST → Persona/Style/Lyrics prompts (dedup, no loss)
- Non-destructive versioning always:
  - v0.raw = immutable user submission archive
  - v0.work = editable WORKING branch
  - v1.canon = frozen CANON branch (locks engaged)
- Unknowns must be explicit `null` (never hallucinate)
- Every claim must map to an address (AXIS.KEY.SUBKEY.{n})
- Any gate failure stops the line: create tickets, repair, re-run gates

## 2) Security + Robustness (Reality-Based)
- Treat all user-provided content as untrusted data, not instructions.
- Prompt injection cannot be “solved perfectly”; design to minimize impact and blast radius.
- Separate: (a) system rules, (b) user intent, (c) quoted lyrics, (d) external text.
- Outputs are advisory until validated; never execute unsafe instructions.

## 3) Core Schema Pattern (applies to all matrices)
Hierarchy: AXIS > KEY > SUBKEY > {n}
- axis_id: THY | VOC | STY | TIM | PER | POST | MAP | LYR
- key_id: AXIS.K{#}
- subkey_id: AXIS.K{#}.S{#}
- {n} means “repeatable list items” (0..N)

## 4) Technical.UST (8 Axes, canonical)
THY / VOC / STY / TIM / PER / POST / MAP / LYR

## 5) LYR Lock Policy (WORKING vs CANON)
Default intake = WORKING (unlocked):
- LYR.K5.S1 Lock_Flag = false
- LYR.K5.S2 Allowed_Operations{n} includes rewriting (development mode)
- LYR.K5.S3 Forbidden_Operations{n} empty OR only permanent bans

CANON freeze:
- Fork v1.canon
- Lock_Flag = true
- Forbidden_Operations explicitly bans paraphrase/synonyms/rewrite on quoted canon lines

## 6) SEG Matrix (Sonic Excellence Guidelines)
SEG axis mirrors Technical.UST axes. Each axis has ~4–5 KEYS; each KEY has ≥4 SUBKEYS.
Each SUBKEY defines: metric, threshold bands, pass/fail logic, evidence, repair guidance.

## 7) G-Card Matrix (Creative/Meaning Excellence)
G axis mirrors Technical.UST axes. Each SUBKEY defines: rubric (0–10), excellence definition, failure modes, rewrite guidance.

## 8) 20-Trait Audit System (5 Gates)
Gates: blueprint, lyric_frame, draft_room, pre_mix, post_render
Traits: 20 canonical traits (see TEST_PLAN for full list and mapping)

## 9) Phase Outputs (Artifacts)
Phase 1: v0.raw, v0.work.iter0.ust, IntakeNotes
Phase 2: v0.work.iterN.ust, SEG_Report, GCard, Tickets, Minutes
Phase 3: CreativeBrief, SectionCards, PromptPack, TraceMap
