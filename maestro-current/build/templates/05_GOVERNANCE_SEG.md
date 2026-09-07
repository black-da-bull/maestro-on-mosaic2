# SEG — Song Excellence Governance, Current Model v0.2 (P-3 ruling applied)
**SEG is the governance UMBRELLA (current name — DEC-14; era aliases: "Feasibility gate" (v2.1),
"Structural Excellence Gate" (MONO OS)). SEM ⊂ SEG.**

## Inside the umbrella
- **SEM** — the weighted scoring system: 12 criteria, 0–5 × weights (Hook 18/Lyric Integrity 12/
  Vocal 10/Melody 10/Structure 8/Production 12/Arrangement 6/Commercial 8/Originality 6/
  Metadata 4/Syllable 4/QA 2), composite = Σ((score/5)×weight). Evaluation capability and
  arithmetic are architectural; numeric pass targets require explicit applicable context
  (DEC-PROMO-01/02/03). There is no universal numeric default.
  Namespace: SEM rubric numbering ≠ admissibility K-set (DEC on E-2); qualify every K-reference;
  short-code binding deferred to O-15 (DEC-12).
- **Hard sub-gates**: metadata · lyric-syllable (style-conditioned per DEC-25) · hook ≥4 · production ·
  **Lyric Change Compliance** (unauthorized edits auto-fail regardless of composite).
- **G-Card** — decision ARTIFACT summarizing SEG result, top deficiencies, required actions
  (not an independent scalar; corpus-division v0_3 resolution).
- **SE20** — cultural lineage & authenticity gate (the soul, measured); composition within the
  ordered sequence still OQ (held).
- **HPA** — human perception of authenticity; paramount inside PROOF; can keep/revise/reject
  regardless of technical compliance. Sacred Imperfection doctrine: emotional truth exceeding
  sterile compliance — logged exceptions, never accidental failures.
- **Admissibility K-set (era: session-13 Config B)** — distinct namespace; current audio scope
  uses the audio subset; visual members ride the VIS module. Definitions carried, not remixed
  with SEM criteria.
## Execution model (DEC-24: interwoven, not terminal-only)
Song Excellence runs CONCURRENT with Technical UST construction: SEM criteria serve as live
criteria for subagent fills and for team round-robins/management reviews; every step emits UST
delta + SEM delta together (preload ratchet). The terminal surface evaluates the composite
against the explicitly applicable run/policy/version/context threshold, alongside independent
hard gates, evidence and lawful exceptions, then emits the G-Card decision artifact. It CLOSES
the interwoven evaluation; it is not a standalone end-gate chain. If threshold applicability or
source authority is unresolved, record that unresolved numeric verdict; never invent a default
or claim numeric PASS. Critique, feasibility and remediation remain available.
Historical G-Card ≥7.0 scalar = era history (its stratum), not a current second threshold.
Syllable sub-gate: style-conditioned per DEC-25 (see 02).

Stop-the-line: skipped subkey · silent fill · truncation · unauthorized lyric change · false
completeness. Every step emits UST delta + SEM delta together. Q1–Q16 = PHANTOM (never fabricate).

## ERA ADDRESS SPACE — v5-b governance monolith (registered layer, O16D fold)
Source (hash-verified): `legacy/maestro_v5b_coldstart/docs/TECHNICAL_UST_GOVERNANCE_ADDENDUM.md`
(sha256 `29b0c9ff38a0cf4ecdfe1f1325a16837f6e75da4574814b19fa01cc1c97099fb`) + TECHNICAL_UST_CANON.md
§9 (sha256 `bfe0b238a08edcd317b80ac0bf9be3a124029995770d91d83f8358ec5a441b5b`), package
`v5-b.coldstart.1`, 2026-01-23. The v5b stratum gives the gates FIRST-CLASS ADDRESS SPACE —
"structurally equal to the core UST … share the same address space":

- **SEG.K1–K5** (25 subkeys): formal feasibility · temporal integrity (bar counts, pickups,
  halftime safety) · spectral feasibility (masking, occupancy) · human execution limits (range,
  breath, articulation speed, fatigue) · policy enforcement (SEG.K5.S1 lyrics_lock_compliance …
  SEG.K5.S5 pass_fail_verdict).
- **G.K1–K6** (30): coherence · sonic architecture · performance authenticity · cultural/genre
  integrity · strategic value · scoring mechanics — G.K6.S2 evidence binding to exact UST
  addresses; G.K6.S4 pass_threshold ≥7.0 (the era gate DEC-24 already classifies as history).
- **SE20.K1–K7** (35): theory/form · lyrical craft (incl. bar_math_accuracy) · vocal design ·
  arrangement/dynamics · timbre/mix intent · performance truth · originality/identity.
- **Cross-axis bindings (non-optional):** SEG findings bind to THY.*/structure-era.*/LYR.*;
  G-Card evidence cites exact AXIS.K#.S#; SE20 failures trigger Phase-2 re-meetings and block
  Phase-3 promotion.
- **Phase guarantee:** P1 nulls logged · P2 SEG+SE20 enforced per axis meeting · P3 G-Card +
  promotion · P4 reverse compilation only on all-PASS · P5 Suno output only from Creative UST +
  Show Summary.

Disposition (DEC-22/DEC-24): this layer is the v5b-era EXECUTABLE FORM of the interwoven model —
registered as the address-level detail stratum for SEG/G-Card/SE20. It does NOT reinstate ≥7.0 as
a current threshold; G≥7 and the song-local SEM target are separate historical mechanisms,
not successive universal constants (DEC-PROMO-02). Its 7×5 SE20 item set is an era instance of the
SE20 checklist (composition OQ stays held). Era-alias register: the v5b expansion of SEG —
"Structural & Engineering Gate" — joins DEC-14's alias list ("Feasibility gate" v2.1, "Structural
Excellence Gate" MONO OS); current name remains Song Excellence Governance.

## Scoped SEM configuration — DEC-PROMO-01/02/03
The originating interaction is `song_test_2025-12-07_001` / `decomposer_v1.6_run_001`:
composite 76.8, then Morris: “who said 70% pass? we are 97.5% pass”. Source:
`artifacts/D-Maestro/Maestro/song.excellence.matrix.iterative.design.session.txt`, lines
3547–3612 (operator statement at 3599). The 97.5 value is RUN_LOCAL_VALID there. CR-009-derived
universal-floor interpretations are superseded; historical texts remain intact.
Session PASS_THRESHOLD input is demonstrated in `code/D-Maestro/maestro-ai-music-system-main/Activity.txt`
M7.3 (line 401). Its later proposed default is not imported. Minimal current contract:

```yaml
sem_configuration:
  score_max: 5
  weights:
    hook: 18
    lyric_integrity: 12
    vocal: 10
    melody: 10
    structure: 8
    production: 12
    arrangement: 6
    commercial: 8
    originality: 6
    metadata: 4
    syllable: 4
    qa: 2
  threshold_selection: explicit_applicable_context
  default_threshold: null
  allowed_scopes: [run, policy, version, context]
  required_policy_fields: [threshold, scope, context_ref, authority_ref]
```

An applied evaluation supplies its threshold (on the 0–100 SEM scale), scope, context_ref and
source-authority reference in the run's existing evidence/ledger surfaces. No numeric fallback
is authorized. A policy or version label alone does not establish authority or applicability.
The build validator checks configuration and explicit-policy arithmetic; this is not deployed
song-runtime enforcement. Independent lyric lock, feasibility, evidence binding, authenticity
judgment and logged Sacred Imperfection remain intact; a numeric comparison alone is never
an overall SEG release verdict. D4 remains an executable-runtime obligation.
