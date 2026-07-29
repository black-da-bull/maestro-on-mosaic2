# Style Library Assessment v0.1 — PROPOSAL
**Status:** PROPOSAL (awaiting ROOT disposition)
**Evidence class:** Render-facing surfaces (Suno Saved Styles export) — runtime ground truth of what was actually submitted to the target engine. PRIMARY-adjacent under the evidence hierarchy.
**Source:** `D:\maestro-on-mosaic\style-library.md` (present at canonical root; corpus also mounted in-session by ROOT alongside ontology ratification block)
**Ontology check:** The mounted ontology block matches canon verbatim (fold/rebuild plan v0.2 + who_dat follow-up). Zero drift, zero contest. Ratified as restatement, not new material.

---

## Corpus character
Several hundred saved style-box surfaces spanning the Suno era of the lineage (post-migration; no aisonggenerator-era surfaces present — expected, these are Suno account artifacts). Entries are title+body concatenations, blank-line separated. All entries are Asset-A-adjacent: they are the *actual submitted* Show-Summary/style-box strings, not drafts.

## Findings

**F1 — Axis-container footprints confirm the 8-axis canon from runtime ground truth.**
Bracketed containers appearing in-surface: `[Theory] [Voice] [Style] [Timbre] [Performance] [Post-Production]` — exactly six of the eight canonical axes (THY VOC STY TIM PER POST). LYR absent from style box (correct: lyrics box carries it). END absent as a container but present as `[execution | Intro → Verse → …]` keys **inside Performance** — direct runtime confirmation of the AX-CONTRA-1 resolution (END canonical; sequence lives in PER's execution key).

**F2 — One MAP footprint (historical, no contest).**
A chop-plan entry carries `[Road Map] Intro → Verse 2 → Chorus …`. Era-native terminology footprint predating the END supersession. Discovery footprint per the parallel-windows ROOT finding — log, do not revert, no supersession action required.

**F3 — House Low-End Law (survived-challenge invariant; registry candidate).**
Near-verbatim recurrence across dozens of entries spanning multiple version eras:
- Three-tier low end: sub sine 27–45 Hz / punch 50–80 Hz / mid-bass 100–160 Hz (sweet spot 120–140)
- Kick 55–65 Hz sidechained to sub (med attack / fast release; ~3:1 where stated)
- Mono <120 Hz; verses narrow/mono-core, choruses wide (choir L/R, leads center-anchored)
- Vocal window: notch 250–350, presence +1–2 dB @ 3–5 kHz, de-ess 7–9 kHz
- Master: subsonic HPF 23–25 Hz, sub bus un-HPF'd
- Dual deliverables: SPL ≈ −9.5 LUFS / SQ ≈ −12 LUFS, TP ≤ −1.0 dBTP
Recurrence across eras = invariant class per the promotion registry rules. **Proposal:** codify as `lowend_registry_v0_1.py` (sibling to `axis_registry_v0_2.py`), fail-closed invariants binding the tier boundaries and deliverable targets.

**F4 — "Evolutionary layer, not replacement" directive family.**
Repeated layer-contract phrasing ("LAYER 1 of 2 / 1 of 3", "post-production evolutionary layer", "does not replace the original") — a proven construct family mapping to the Derivative Distribution Surface / remix lane. Second registry candidate.

**F5 — Triad-in-the-wild confirmation + one open item.**
Entries carrying `SHOW SUMMARY: … BIO: …` in one surface, plus standalone `A/R PERSONA PROFILE` entries, confirm the triad shipped as designed. **Open item (hold, spec-not-resolved):** several style-box entries carry full Creative-UST container grammar ([Theory]…[Post-Production] blocks) — determine whether the style box lawfully carried container grammar in certain eras or whether that is budget-overflow drift. Do not resolve silently.

**F6 — Delimiter grammar footprints.**
`[ ]`, `( )`, `" "`, `** **`, `|` all present in-surface, consistent with the constraint-born origin grammar.

**F7 — Era stratification keys present in-surface.**
Version strings appear inside surfaces: `v4.5, style B`, `v4.5+`, `v5 pro beta, style B`, `v5+`, `v5.5 pro`. Usable as stratification keys for the forensic pipeline without external metadata.

## Recommendation
Ingest `style-library.md` into the forensic pipeline as its own eventlog class (render-facing surfaces). Parser delivered at `code\style_library_parser_v0_1.py` — splits entries, hashes for provenance, tags era strings, axis containers, MAP footprints, house-law presence, layer directives, triad markers; emits `artifacts\style_library_index_v0_1.json`. Automates F1–F7 as repeatable classification rather than one-off reading.
