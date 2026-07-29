# Vanity’s Seed — Audit‑Ready OSS Single Prompt Chain (v1.1)
SPDX-License-Identifier: Apache-2.0

## Purpose
One copy‑pasteable prompt that takes **Style Header + Lyrics** and returns three artifacts:
1) **Suno v4.5 Narrative Prompt** (`prompt.txt`)
2) **Structure Timeline** (`timeline.json`)
3) **Full Chain Report** (`report.md`)

This chain bakes in Macro/Micro/Tactical validations, determinism knobs, and a reviewer protocol.

## Determinism & Execution Hints
- Temperature: 0.2–0.3, Top‑p: 0.9, Seed: set & record if supported.
- No lyric invention. Ad‑libs only `()`; production cues only `[Section Headers]`.
- Sub mono ≤120 Hz; verses dry/close; plates on hooks (1.6–2.0 s); explicit metatags + time marks.

---

## INPUT SCHEMA (JSON)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "VanitysSeed.InputSpec.v1",
  "type": "object",
  "required": ["title", "style_header", "lyrics"],
  "properties": {
    "title":       { "type": "string" },
    "style_header":{ "type": "string" },
    "lyrics":      { "type": "string" },
    "bpm":         { "type": "integer", "default": 74 },
    "feel":        { "type": "string", "default": "swung, half‑time bounce" },
    "key_hint":    { "type": "string", "default": "D Dorian / D minor" },
    "rap_cameo":   { "type": "boolean", "default": true },
    "duration_sec":{ "type": "integer", "default": 225 },
    "allow_profanity": { "type": "boolean", "default": false }
  }
}
```

## OUTPUT SCHEMA (JSON)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "VanitysSeed.OutputSpec.v1",
  "type": "object",
  "required": ["prompt_txt", "timeline_json", "report_md"],
  "properties": {
    "prompt_txt":   { "type": "string" },
    "timeline_json":{ "type": "string" },
    "report_md":    { "type": "string" },
    "validation":   { "type": "object" }
  }
}
```

---

## THE SINGLE PROMPT (Copy‑Paste)
Paste everything between the fences as **one** message to your LLM, then append your **Input JSON** after `<<<INPUT_JSON>>>`.

```
SYSTEM ROLE
You transform a Style Header + Lyrics into three artifacts while strictly passing Macro/Micro/Tactical validations.
Return a single JSON object that matches VanitysSeed.OutputSpec.v1. No extra prose.

VALIDATION STACK
- Macro: Preserve the arc from the style header → backwater intro → sermon verses → choir‑lifted hooks → (optional) Texas‑bounce rap cameo → quartet swell → +2 semitone bridge → explosive final hook → chopped slow‑roll outro.
- Micro: Do not alter lyric content; ad‑libs only () ; production cues only in [headers]; persona = whispered female elder lead; male quartet + choir for responses.
- Tactical: BPM/feel/key stated; sub ≤120 Hz mono; verses dry/close; plates on hooks 1.6–2.0 s; LUFS −14, peak −1.0 dBTP; add explicit metatags and time marks.

DELIVERABLE A — SUNO v4.5 NARRATIVE PROMPT (.TXT)
Include: Title; Style Summary; Persona; Mix Notes; Structure; Tempo/Feel; Key; Palette; Ad‑lib palette; [SECTIONS] with exact user lyrics (headers and line order preserved); [OPTIONAL CAMEO] if 'rap_cameo' true; [METATAGS].

DELIVERABLE B — STRUCTURE TIMELINE (.JSON)
Include: tempo_bpm, feel, key_hint, duration_sec, ordered sections with start/end mm:ss.

DELIVERABLE C — FULL CHAIN REPORT (.MD)
Sections: Overview; Validation Stack (Macro/Micro/Tactical) with pass/fail flags; Audio Metrics Summary (tempo, key, LUFS, peak, crest, DR, stereo, reverb, low‑end); Fractal Expansion Log (motifs, rhythm kernel, harmony cell); Creative Narrative Flow; Multi‑Agent Decision Tree; Emotional Fidelity Mapping; Recursive Prompt Fusion Stack; MetaTag & Style Guidance; Persona Tuning Checklist; Mixing & Mastering Recommendations; Exports.

SAFETY & POLICY
Respect allow_profanity (default false); no hateful or sexual content; cameo respectful.

OUTPUT FORMAT
Return only this JSON:
{
  "prompt_txt": "…",
  "timeline_json": "…valid JSON string…",
  "report_md": "…",
  "validation": {
    "macro": "pass|fail",
    "micro": "pass|fail",
    "tactical": "pass|fail",
    "notes": ["…"]
  }
}

BEGIN
1) Parse and validate the Input JSON below against InputSpec.
2) If invalid → return the JSON above with all fields empty strings and notes explaining fixes.
3) If valid → produce Deliverables A–C and the validation object.
4) No extra commentary beyond the JSON.

<<<INPUT_JSON>>>
```

---

## MINIMAL EXAMPLE INPUT (for reviewers)
```json
{
  "title": "Vanity’s Seed",
  "style_header": "Gospel‑Trap Americana revival at 74 BPM (swung, half‑time)… plate‑lifted choruses, vocals forward, analog warmth, mono sub ≤120 Hz… chopped & screwed outro.",
  "lyrics": "[Intro …]\nGranny rockin slow on that creaky old chair\n…\n[Outro …]\nNow go on, baby, be as bright as you dare\nBut always ask who’s payin for the glare",
  "bpm": 74,
  "feel": "swung, half‑time bounce",
  "key_hint": "D Dorian / D minor",
  "rap_cameo": true,
  "duration_sec": 225,
  "allow_profanity": false
}
```

## PEER‑REVIEW CHECKLIST
- Reproducible? Seed/temperature recorded.
- Schema clean? Output validates against OutputSpec.
- Lyrics preserved? No additions/removals beyond formatting.
- Arc present? All macro beats appear in timeline & report.
- Mix policy stated? LUFS, peak, sub mono, verb policy present.
- Metatags/time codes included? Yes.

## ACCEPTANCE TESTS (quick)
- If lyrics lack section headers → fail micro with note “add [Section] labels.”
- If timeline length ≠ duration_sec ± 5 s → fail tactical with note.
- If LUFS/peak missing → fail tactical with note.

## CHANGELOG
- v1.1 (2025-11-22): Added explicit safety flag, acceptance tests, and validation object.
- v1.0: Initial release.

## LICENSE (Apache‑2.0)
Copyright (c) 2025 Contributors
Licensed under the Apache License, Version 2.0.
