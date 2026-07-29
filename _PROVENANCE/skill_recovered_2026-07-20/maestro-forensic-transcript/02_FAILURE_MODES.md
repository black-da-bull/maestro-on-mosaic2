---
component: 02_FAILURE_MODES.md
status: RECONSTRUCTED (original MISSING) — 18-mode catalog rebuilt; numbering partially anchored
provenance: >
  Anchored numbers (from surviving cross-references in SKILL.md v1 and the found 03 draft):
  FM-01, FM-02, FM-03, FM-07, FM-08, FM-09, FM-11, FM-14, FM-16, FM-18. The remaining eight
  slots are filled from documented failure classes in the corpus; their original numbers are
  unknown and marked [renumbered]. Every mode carries a verbatim teaching excerpt actually
  present in the corpus — none are generic. Found original outranks on discovery.
---

# 02 — Failure Modes (the most important file)

Read before doing any transcript work. Per the found 03 draft: defenses compose — defending against one mode while leaving another active still produces skeleton files.

**FM-01 · Phantom commitment** [anchored]. AI emits state-change language with no state change behind it ("I have updated…", "going forward I will…"). Q+A without F is an open ticket, not a change. Teaching excerpt (Revised INV-18, claud2.txt): *"Flag phantom commitments as model corruptions."* Runtime defense: R-RT-PD-01, pre-emit detection — locked by operator turn U56.

**FM-02 · Mid-stream summarization** [anchored]. Compressing earlier material to manage attention drops the corrections that landed in the middle. Excerpt (operator standing instruction, eldrik.txt ~L64399): *"You maintain context windows by summarizing… SO MUCH DETAIL WAS DROPPED OVER SESSIONS THAT BY THE END WHAT I THOUGHT WAS A FULLY DEVELOPED, REAL WORLD STRESS TESTED MODULE WAS NOT."*

**FM-03 · AI prior text as canon on re-read** [anchored]. On re-read, the AI's own confident phrasing gets promoted to fact. Excerpt (INV-18, claud2.txt): *"Human turns have root authority. AI turns have proposal authority only… the system drifts toward confident AI language instead of human intent."*

**FM-04 · Parse-and-chunk mode** [renumbered]. Treating a continuous dev stream as discrete units before reading it. Excerpt (session 13 U13, flagship): *"you can't parse or chunk it. that's why your failing. you have to read it."* Named in-session: "parse-and-chunk mode." Repair: sequential line-bounded chunks, deltas as the unit (U41).

**FM-05 · Version-boundary segmentation** [renumbered]. Splitting a substrate along version markers cuts cross-version deltas in half. Excerpt (operator-issued canon, U41): *"DO NOT segment the file by version markers. Versions are downstream of deltas."*

**FM-06 · Goal-inference collapse** [renumbered]. Jumping to the inferred deliverable instead of reading what is there. Excerpt (U41): *"DO NOT jump to terminal output. Goal-inference collapse is the dominant failure mode."*

**FM-07 · Tool body without methodology** [anchored]. Loading the workflow while skipping methodology and failure modes; work looks organized, produces skeletons. Excerpt (found 03 draft): *"Even the skill's own structure is a trap if loaded in the wrong order."*

**FM-08 · Forward-primary reading** [anchored]. Forward walk as discovery instead of verification; running assessment forms from earliest context and resists late deltas. Defense: backward-primary passes (01_METHODOLOGY §4); mid-stream assessment provisional (INV-17).

**FM-09 · Universal supersession missed** [anchored]. Applying a correction as a local patch instead of propagating it to every dependent. Documented instance (V1, confirmed 2026-07-16/19): session-13 FIRM canon (R-list v0.2, 96 entries/92 FIRM) reached zero persisted artifacts; `drafts/maestro_v0.md` still carries K7=Arrangement/K8=Commercial against FIRM K7=External viability/K8=Visual coherence.

**FM-10 · Display before verification** [renumbered]. Surfacing drafts instead of iterating to verified in the background. Excerpt (U43, operator): *"remember that you should double-check all generated responses before display by verifying and validating. this infers that background operations are required."* The protocol demonstrably caught fabricated operator quotes before display (U47: "Background verification surfaced fabrications in chunk 2.").

**FM-11 · Skeleton file** [anchored — the single most important]. Well-formatted output with the substance compressed out; classification carrying no instance. Ten-step mechanism documented in 03_WHY_AI_DEFAULTS_HERE.md ("Six months of skeleton files"). Structural defense: fold invariant F2 — every digest category carries ≥1 source event id, fail-closed. Self-instance: the v1 skill package itself shipped as SKILL.md alone, 9 of 10 components missing (P0-a).

**FM-12 · Silent merge / forced coherence** [renumbered]. Harmonizing contradictions instead of parking them. Excerpt (session-13 U1 protocol, operator-issued): *"Resolve contradictions by: tracking lineage, identifying superseded concepts, branching when necessary, never forcing artificial coherence."* Defense: conflict register (F4); supersession only by later explicit operator statement citing the ID.

**FM-13 · Coverage-count blindness** [renumbered]. Counting only rendered user turns. Operator inputs hide in assistant-segment tails (REC-A/REC-B splitter defect, O-14), in tool-mediated widget answers (M8: AskUserQuestion responses render as no user turn), and in attachment events (MF-3: "4.5.5.txt / 2:15 PM" chrome). Defense: 01_METHODOLOGY §5 enumeration rules.

**FM-14 · Novel-treatment trap** [anchored]. Inventing a custom methodology instead of applying the established cross-vertical practice (event sourcing 2002, OT 1989, ADR 2011, SOAP 1968, AAR 1970s). Excerpt (found 03 draft): *"Reinvention here produces inferior tooling and burns operator attention."*

**FM-15 · Unpersisted method** [renumbered — 2026-07 validated instance]. A selection metric or script that lives only in conversation is not reproducible. Documented: the correction-density marker set behind session-13's selection was never persisted; the P1N validation could reproduce the rank but not the numbers (MF-2). Defense: every metric and splitter ships as a file with the run.

**FM-16 · AI-paraphrase-as-canon** [anchored]. Characterizing the operator from AI-collected paraphrase instead of operator self-statement. Defense (SKILL contract #12): source from 00/OPERATOR_CONTEXT/KERNEL — operator-authored documents only.

**FM-17 · Structured-output authority inversion** [renumbered]. A polished artifact outranking the conversational evidence it compressed. Excerpt (M4 lineage, operator 2026-07-16): *"when it chunked and parsed it was missing hundreds of lines of changes (i.e. sem, foil, phases and agent interactions)"* — and the chunked summaries then read as more authoritative than the omitted source. Rule: operator conversational input outranks structured AI output on conflict; regenerate the structured output, never the reverse.

**FM-18 · Narrative-as-padding misread** [anchored]. Treating operator narrative as preamble before "the ask." Excerpt (00_OPERATOR_ABOUT_ME, operator-authored): *"My narrative style is not rambling, overexplaining, or avoiding the point. It is how I surface the point when the visible problem is only one part of the system."* The narrative IS the specification.

## Repeat-correction marker

When the operator says *"once again"* (U28: "claude this items once again are historical artifacts…"), a mode above has already fired at least twice. Log it as a defect against the session, not as a new instruction.

## 2026-07 field notes (not part of the original 18 — validated additions, keep separate)

- Byte-vs-character losslessness: state normalization explicitly (CRLF→LF is benign but must be named) — MF-1.
- Quote-whitespace drift: flattening line breaks inside "verbatim" quotes is a fidelity defect even when content survives — MF-4.
- Concept-persisted / ID-lost: a rule's ancestor concept in old drafts does not mean the ratified rule persisted (QAF/phantom concepts existed in April drafts; R-RT-QAF-01 / R-RT-PD-01 / R-list v0.2 nowhere) — V1 nuance.
