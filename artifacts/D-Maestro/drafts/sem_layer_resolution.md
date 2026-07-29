# SEM_LAYER_RESOLUTION.md

**Artifact ID:** SLR.v0.2026-04-28
**Inputs:** SDG.v0.1.2026-04-28 (working dependency graph) · SEC.v4.5.2026-04-28 (corrective evidence) · RTFA.v0.2026-04-28 (prior candidate audit) · `song.excellence.matrix.iterative.design.session.txt` · `song.excellence.yaml` · v4.5 monolith §2.2 / §7.4 / §7.6 · MOSAIC v2.1/v2.2/v2.3 diagrams · CR-009 evidence · SE20 evidence · HPA evidence
**Status:** CANDIDATE — proposal authority only. Operator confirmation required for promotion to substrate canon.
**Resolves:** Layer 5 internal architecture for SDG.v0.1.

---

## 1. Executive Finding

SEM is **not a single rubric**. SEM is a **layered admissibility system** with three concurrent subsystems plus a final perception check. The v4.5 corpus operationally ran: (a) **weighted quality scoring** — 12-criterion matrix producing a composite percentage with a release threshold; (b) **admissibility gates** — binary pass/fail checks (Metadata, Lyric Syllable, Hook, Production) embedded in a Decision Tree; (c) **stop-the-line conditions** — immediate-halt validators (skipped subkey, silent fill, truncation, unauthorized lyric, false completeness) running on every UST delta; (d) **post-render HPA score** — Human Perception of Authenticity validation after audio rendering. The v5-c MOSAIC progression (v2.1 → v2.2 → v2.3) **compressed and reorganized the admissibility layer** into K-axis criteria (K1–K6 in v2.2; K7–K8 added in v2.3 as External viability and Visual coherence) while **preserving** the weighted scoring, stop-the-line, and HPA layers as concurrent subsystems. CR-009's 70% → 97.5% correction applies only to the **release threshold of the composite weighted quality score** — it does not apply to binary admissibility gates or stop-the-line blockers, which are pass/fail and halt-on-violation respectively. **Mosaic Layer 5 must implement the dual-layer pattern (Option E): weighted quality scoring + concurrent admissibility gates + stop-the-line blockers + post-render HPA**, using v5-c K-axis naming for the admissibility layer while retaining v4.5 weighted scoring as a separate parallel layer.

---

## 2. Source Inventory

| Source | Classification | Evidence Function |
|---|---|---|
| `song.excellence.matrix.iterative.design.session.txt` (8000+ lines, S0023, S1208–S1786, S1842) | **decides** | Original 12-criterion weighted matrix; M6–M8 SME round-robin → SEG/G-Card → revision loop; live PASS evidence at composite_pct = 99.1% above 97.5% threshold |
| `song.excellence.yaml` | **informs** | Rubric stub structure |
| v4.5 monolith §2.2 (VAL_Report) | **decides** | Format validation gates concurrent with SEM scoring |
| v4.5 monolith §7.4 (Decision Tree Logic) | **decides** | Gate → corrective action mapping (Metadata/Syllable/Hook/Production); routing back to specific phases on fail |
| v4.5 monolith §7.6 (QUINN checks) | **informs** | Specific validators (commas outside lyrics, syllable count, road-map order-only) |
| v4.5 monolith §6.4 (HPA Report Schema) | **decides** | HPA score breakdown: creative_authenticity, emotional_impact, sonic_fidelity_to_intent, viral_potential_perception |
| MOSAIC v2.1 diagram (gates row: SEG/G-Card/SE20/CAP/LOCK) | **informs** | Five distinct named gates pre-K-axis compression |
| MOSAIC v2.2 diagram (Plane 3: K1–K6) | **informs** | First K-axis admissibility framing with 4-tier severity (Observe/Warn/Challenge/Block) |
| MOSAIC v2.3 / Maestro v0 candidate diagram (Plane 3: K1–K8) | **decides** | K7 External viability (NEW), K8 Visual coherence (NEW, tied to VIS axis) — corrects the "K8 = Compression Survivability" assumption |
| Day 3 documentation §8 (Song Excellence Mapping) | **informs** | Song Excellence is active pressure substrate, not terminal evaluation; informs judgment, does not replace domain ownership |
| CR-009 (migration log) | **decides** | Pass threshold: 70% rejected; canon expectation 97.5% release-grade |
| SE20 Sonic Excellence 20 Matrix (project knowledge: SE20.K1.S1–K4.S5) | **informs** | 20 evidence-bound items (4 keys × 5 subkeys), each with PASS/WARN/N/A status and UST address citation |
| SEG (Structural Excellence Gate) — 7 binary structural checks | **informs** | Bar count correctness, section symmetry, lyrics-structure agreement, vocals/FX feasibility, genre integrity, prompt contradictions |
| G-Card scoring artifact schema | **informs** | Output artifact: gcard_id, seg_composite_pct, final_decision (PASS/CONDITIONAL/HOLD), buy_in_pct, top_deficiencies, required_actions, iteration_cap, ledger_pointers |
| Self-Correction Protocol (v4.5 monolith) | **decides** | Stop-the-line: deviation detection → cease → revert to last validly logged state |
| Q1–Q16 Morris Matrix | **needs_source** | Mentioned only in Chaos-Decomposer §5.2 as something to scan for during ingestion (S1015); no instantiated Q1–Q16 schema, weights, or scoring rules found in primary corpus |
| `song_excellence_session.ai_optimized.md` (18,000+ lines per prior session handoff) | **contrasts** | Operator-flagged as containing AI-induced sediment; treated as supporting evidence only, not deciding evidence |

---

## 3. SEM Lineage

The SEM evolved through five distinct epochs. Each epoch added or restructured a layer without erasing prior layers — operator's non-destructive evolution discipline in action.

**Epoch 1 — Early v4.5 weighted matrix (S0022–S0036).** Twelve criteria with explicit weights summing to 100%: Hook Strength (18%), Lyric Integrity & Emotional Clarity (12%), Vocal Delivery & Character (10%), Melody & Topline Craft (10%), Structure & Pacing (8%), Production Quality (12%), Arrangement Interest & Contrast (6%), Commercial Viability & Market Fit (8%), Originality / Distinctive Element (6%), Metadata & Governance (4%), Lyric Syllable Integrity (4%), Pre-release QA Checks (2%). Scoring: 0–5 per criterion, composite = Σ(score × weight). **Original threshold: composite ≥ 70 → release candidate; 60–69 → targeted revision; <60 → major rework.** Decision Tree appended for binary gates: Metadata Gate, Lyric Syllable Gate, Hook Gate (≥4), Composite Score, Production Gate, Final QA. Quality scoring and binary gates are operationally distinct layers from this epoch onward.

**Epoch 2 — VAL_Report and HPA emerge as parallel layers (v4.5 monolith Phase 2.2 and §6.4).** VAL_Report runs in Phase 2.2 as format validation (no commas outside lyrics block, road-map order-only, container lint, lyric_lock policy, syllable rule). HPA Report runs in Phase 4.2 post-render with four perception axes scored 1–5: creative_authenticity, emotional_impact, sonic_fidelity_to_intent, viral_potential_perception. Aggregate HPA threshold not stated as fixed number in primary evidence; functions as a keeper-selection criterion (Phase 4.2: "HPA Scoring & Keeper Selection"). Self-Correction Protocol added as stop-the-line: deviation detection → cease → revert to last logged state. **By end of Epoch 2: weighted SEM scoring, binary gates, VAL_Report, HPA, and Self-Correction are all running concurrently as separate subsystems.**

**Epoch 3 — CR-009 threshold correction.** Migration log entry: *"CR-009 — Pass threshold correction. Change: Reject 70% pass guidance; canon expectation is ~97.5% pass for release-grade gating. Status: ACTIVE. Conflict: Earlier assistant guidance used ~70; marked superseded."* Confirmed in operational evidence (S1842): *"seg.composite_pct = 99.1%, above your PASS threshold (97.5%). All gates are true. The run therefore produced a PASS G-Card."* CR-009 raises the **composite weighted quality score** threshold from 70 to 97.5. CR-009 does not modify binary gates (which remain pass/fail), does not modify stop-the-line (which remains halt-on-violation), and does not modify HPA (which remains a separate keeper-selection layer).

**Epoch 4 — v5-c MOSAIC v2.1 gate consolidation.** Diagram shows five named gates as a row: **SEG (Feasibility gate), G-Card (Quality score ≥ 7.0), SE20 (Cultural lineage authenticity), CAP (Char budget 4960–4999), LOCK (Lyrics immutable)**. SEG = Structural Excellence Gate with 7 binary structural checks (bar count, section symmetry, lyrics-structure agreement, vocals/FX feasibility, genre integrity, prompt contradictions). G-Card = scoring artifact (separate object from G-Card structural checks; this is the *output* of the M7 evaluator with composite, decision, deficiencies, required actions). SE20 = Sonic Excellence 20 Matrix, 4 keys × 5 subkeys = 20 evidence-bound items with UST address citations. CAP = character budget validator. LOCK = lyric immutability enforcement. Notable: **G-Card threshold is ≥ 7.0 on a 1–10 scale** in this view, distinct from the 97.5% threshold on the 0–100 composite. These are different artifacts with different threshold scales.

**Epoch 5 — v5-c MOSAIC v2.2 K-axis admissibility runtime.** Plane 3 reorganizes the admissibility layer into six K-axes: **K1 Structural viability** (sections, bars, formal coherence), **K2 Cross-axis coherence** (no orphan claims or contradictions), **K3 Creative strength** (motif, emotion, non-genericity), **K4 Performance truth** (believability, pocket, phrase realism), **K5 Sonic identity** (timbral distinctiveness, genre truth), **K6 Compression survivability** (what survives lawful projection). Stop-the-line conditions explicitly enumerated: skipped subkey, silent fill, truncation, unauthorized lyric change, false completeness. SEM Gating Modes added: 4-tier severity (Observe/Warn/Challenge/Block). Output discipline: *"Every step emits UST delta + SEM delta together."* This is the K-axis compression of v2.1's named gates into a unified 6-criterion admissibility rubric.

**Epoch 6 — v5-c MOSAIC v2.3 / Maestro v0 candidate.** Plane 3 expands to **K1–K8**: K7 **External viability** (NEW) — likely encompasses Commercial Viability + Pre-release QA from v4.5; K8 **Visual coherence** (NEW) — tied to the new VIS (Visual Identity) axis added to Plane 2. K1–K6 retain their v2.2 definitions. **K8 in v2.3 is Visual coherence, not Compression survivability — Compression survivability is K6 in both v2.2 and v2.3.** This corrects a question framing in the input task.

**Mosaic Layer 5 target.** Layer 5 implements the dual-layer pattern observed in operational v4.5 with v5-c K-axis naming for the admissibility layer. Three concurrent subsystems plus post-render perception: weighted SEM scoring (continuous, 12 criteria, composite ≥ 97.5% release threshold), K-axis admissibility (binary or severity-tiered, K1–K6 minimum, K7–K8 if VIS axis is in scope), stop-the-line blockers (immediate halt on validator failure), and HPA perception score (post-render keeper selection).

---

## 4. Criterion Ledger

### 4.1 v4.5 Weighted SEM Criteria (Quality Scoring Layer)

| ID | Name | Source | Weight | Min Pass | Behavior | Type | Status |
|---|---|---|---|---|---|---|---|
| S1 | Hook Strength | v4.5 SEM session S0023 | 18% | ≥4 | Continuous score 0–5; feeds composite | Quality scoring | CANON |
| S2 | Lyric Integrity & Emotional Clarity | v4.5 SEM session S0023 | 12% | ≥3 | Continuous; lyric lock enforced separately | Quality scoring | CANON |
| S3 | Vocal Delivery & Character | v4.5 SEM session S0023 | 10% | ≥3 | Continuous | Quality scoring | CANON |
| S4 | Melody & Topline Craft | v4.5 SEM session S0023 | 10% | ≥3 | Continuous | Quality scoring | CANON |
| S5 | Structure & Pacing | v4.5 SEM session S0023 | 8% | ≥3 | Continuous | Quality scoring | CANON |
| S6 | Production Quality | v4.5 SEM session S0023 | 12% | ≥3 | Continuous; mix basics | Quality scoring | CANON |
| S7 | Arrangement Interest & Contrast | v4.5 SEM session S0023 | 6% | ≥2 | Continuous | Quality scoring | CANON |
| S8 | Commercial Viability & Market Fit | v4.5 SEM session S0023 | 8% | ≥3 | Continuous | Quality scoring | CANON |
| S9 | Originality / Distinctive Element | v4.5 SEM session S0023 | 6% | ≥2 | Continuous | Quality scoring | CANON |
| S10 | Metadata & Governance | v4.5 SEM session S0023 | 4% | ≥3 | Binary collapsed to 0/5 | Quality scoring (binary subset) | CANON |
| S11 | Lyric Syllable Integrity | v4.5 SEM session S0023 | 4% | ≥4 | Binary (6–10 per line) collapsed to 0/5 | Quality scoring (binary subset) | CANON |
| S12 | Pre-release QA Checks | v4.5 SEM session S0023 | 2% | ≥2 | Binary collapsed to 0/5 | Quality scoring (binary subset) | CANON |
| **S∑** | **Composite (weighted sum)** | v4.5 SEM session + CR-009 | 100% | **≥97.5%** | Release-grade gating threshold | Composite quality | CANON |

**Note:** S10, S11, S12 collapse to 0/5 binary in scoring but each also feeds the corresponding **admissibility gate** in the Decision Tree (Metadata Gate, Lyric Syllable Gate, Pre-release QA). Same data, two consumption paths.

### 4.2 v4.5 Admissibility Gates (Decision Tree Layer)

| ID | Name | Source | Behavior | Type | Status |
|---|---|---|---|---|---|
| G-MD | Metadata Gate | v4.5 SEM session S0031 | Binary; HOLD if missing | Admissibility (binary) | CANON |
| G-LS | Lyric Syllable Gate | v4.5 SEM session S0032 | Binary; ITERATE on fail (phrasing or overlay, no rewrite if locked) | Admissibility (binary) | CANON |
| G-HK | Hook Gate | v4.5 SEM session S0033 | Binary; Hook Strength ≥4 → pass | Admissibility (binary) | CANON |
| G-CS | Composite Score Gate | v4.5 SEM session + CR-009 | Continuous; ≥97.5 → release; 60–69 → targeted revision; <60 → major rework (per CR-009: 70 deprecated) | Quality threshold | CANON (with deprecated thresholds noted) |
| G-PR | Production Gate | v4.5 SEM session S0035 | Binary; LUFS, no clipping, low-end clarity | Admissibility (binary) | CANON |
| G-FQ | Final QA Gate | v4.5 SEM session S0036 | Binary; stems exported, ledger updated, release pack ready | Admissibility (binary) | CANON |
| G-RM | Road-Map Gate | v4.5 monolith §7.6 / VAL_Report | Binary; order-only enforced | Admissibility (binary) | CANON |

### 4.3 v4.5 VAL_Report Format Validators

| ID | Name | Source | Behavior | Type | Status |
|---|---|---|---|---|---|
| V-CMM | No commas outside lyrics block | v4.5 monolith VAL_Report | Binary; halt-on-violation | Stop-the-line | CANON |
| V-RMO | Road-Map order-only | v4.5 monolith VAL_Report | Binary; halt-on-violation | Stop-the-line | CANON |
| V-SFX | sFX syntax valid | v4.5 monolith VAL_Report | Binary | Stop-the-line | CANON |
| V-SS | Show summary within limit | v4.5 monolith VAL_Report | Binary (≤1000 chars) | Stop-the-line | CANON |
| V-FU | Final UST within limit | v4.5 monolith VAL_Report | Binary (≤4990 chars) | Stop-the-line | CANON |
| V-LL | Lyric lock policy | v4.5 monolith VAL_Report | Binary; LCR required outside creation nodes | Stop-the-line | CANON |
| V-CL | Container lint | v4.5 monolith QUINN (§7.6) | Binary; all vocal lines quoted, sFX marked | Stop-the-line | CANON |

### 4.4 v4.5 Self-Correction Protocol (Stop-the-Line Master)

| ID | Name | Source | Behavior | Type | Status |
|---|---|---|---|---|---|
| ST-DD | Deviation Detection | v4.5 monolith Self-Correction Protocol | Halt on detected deviation; revert to last validly logged state | Stop-the-line master | CANON |

### 4.5 v4.5 HPA Score (Post-Render Perception)

| ID | Name | Source | Behavior | Type | Status |
|---|---|---|---|---|---|
| H-CA | Creative Authenticity | v4.5 monolith §6.4 | Continuous 0–5 | Post-render perception | CANON |
| H-EI | Emotional Impact | v4.5 monolith §6.4 | Continuous 0–5 | Post-render perception | CANON |
| H-SF | Sonic Fidelity to Intent | v4.5 monolith §6.4 | Continuous 0–5 | Post-render perception | CANON |
| H-VP | Viral Potential Perception | v4.5 monolith §6.4 | Continuous 0–5 | Post-render perception | CANON |
| H-AGG | Overall HPA Score | v4.5 monolith §6.4 | Aggregate (computation rule not fixed in primary corpus); keeper-selection criterion | Post-render perception | CANON |

### 4.6 v5-c MOSAIC v2.1 Named Gates

| ID | Name | Source | Behavior | Type | Status |
|---|---|---|---|---|---|
| SEG | Structural Excellence Gate | MOSAIC v2.1 + project knowledge | 7 binary structural checks (bar count, section symmetry, lyrics-structure agreement, vocals/FX feasibility, genre integrity, prompt contradictions) | Admissibility (binary structural) | CANDIDATE — partially preserved in K1 |
| GC | G-Card scoring artifact | MOSAIC v2.1 + SEM session M7 | Output artifact: composite, decision, deficiencies, required actions, iteration_cap | Output artifact | CANON |
| GC-T | G-Card threshold ≥7.0 (scale 1–10) | MOSAIC v2.1 + project knowledge | Continuous; alternate scale to 97.5% / 100 | Quality threshold (alternate scale) | NEEDS SOURCE — relationship between 7.0/10 and 97.5%/100 not explicitly mapped |
| SE20 | Sonic Excellence 20 Matrix | MOSAIC v2.1 + project knowledge | 4 keys × 5 subkeys = 20 evidence-bound items, each with PASS/WARN/N/A and UST address citation | Admissibility (evidence-bound) | CANDIDATE — preserved in operational evidence; relationship to K-axes not fully mapped |
| CAP | Character budget validator | MOSAIC v2.1 | Binary (4960–4999 chars for final UST) | Stop-the-line (format) | CANON — preserved as stop-the-line |
| LOCK | Lyric immutability | MOSAIC v2.1 | Binary; lyric edits blocked outside creation nodes | Stop-the-line | CANON — preserved as stop-the-line |

### 4.7 v5-c MOSAIC v2.2 K-Axis Admissibility Runtime

| ID | Name | Source | Behavior | Type | Status |
|---|---|---|---|---|---|
| K1 | Structural viability | MOSAIC v2.2 | Sections, bars, formal coherence | Admissibility (severity-tiered) | CANON |
| K2 | Cross-axis coherence | MOSAIC v2.2 | No orphan claims or contradictions | Admissibility (severity-tiered) | CANON |
| K3 | Creative strength | MOSAIC v2.2 | Motif, emotion, non-genericity | Admissibility (severity-tiered) | CANON |
| K4 | Performance truth | MOSAIC v2.2 | Believability, pocket, phrase realism | Admissibility (severity-tiered) | CANON |
| K5 | Sonic identity | MOSAIC v2.2 | Timbral distinctiveness, genre truth | Admissibility (severity-tiered) | CANON |
| K6 | Compression survivability | MOSAIC v2.2 | What survives lawful projection | Admissibility (severity-tiered) | CANON |

### 4.8 v5-c MOSAIC v2.3 K-Axis Expansion (Maestro v0 Candidate)

| ID | Name | Source | Behavior | Type | Status |
|---|---|---|---|---|---|
| K7 | External viability | MOSAIC v2.3 | NEW — likely encompasses Commercial Viability + Pre-release QA | Admissibility (severity-tiered) | CANDIDATE — present in v0 candidate, scope mapping incomplete |
| K8 | Visual coherence | MOSAIC v2.3 | NEW — tied to VIS (Visual Identity) axis added to Plane 2 | Admissibility (severity-tiered) | CANDIDATE — depends on VIS axis being in scope |

### 4.9 SEM Gating Modes (Severity Tiers)

| ID | Name | Source | Behavior | Status |
|---|---|---|---|---|
| MODE-OBS | Observe | MOSAIC v2.2 | Log only, no block | CANON |
| MODE-WRN | Warn | MOSAIC v2.2 | Advisory; downstream proceeds with flag | CANON |
| MODE-CHL | Challenge | MOSAIC v2.2 | Return for argument; round-robin reopens | CANON |
| MODE-BLK | Block | MOSAIC v2.2 | Stop progression; cannot proceed | CANON |

### 4.10 Q1–Q16 Morris Matrix

| ID | Name | Source | Status |
|---|---|---|---|
| Q1–Q16 | Morris Matrix scoring system | Chaos-Decomposer §5.2 (S1015) — *"SME protocols, Agent Council roles, Q1–Q16 scoring systems"* | **NEEDS SOURCE** — referenced as something to scan for during ingestion; no instantiated Q1–Q16 schema, weights, criterion definitions, or scoring rules found in primary corpus. May not exist as a discrete system. May be a conflation with the 12-criterion weighted matrix or with SE20's 20 items. |

---

## 5. Mapping Table

| Old ID | Old Name | New ID | New Name | Relationship | Notes |
|---|---|---|---|---|---|
| S1 (Hook Strength) | v4.5 18% weighted | K3 (partial) | Creative strength | merged | Hook contributes to K3 motif/non-genericity; weight preserved in parallel scoring layer |
| S2 (Lyric Integrity) | v4.5 12% weighted | K2 + K3 | Cross-axis coherence + Creative strength | split | Coherence side → K2; emotional clarity → K3; weighted score retained separately |
| S3 (Vocal Delivery) | v4.5 10% weighted | K4 | Performance truth | merged | Performance truth absorbs vocal delivery + believability + phrase realism |
| S4 (Melody & Topline) | v4.5 10% weighted | K3 | Creative strength | merged | Topline craft folds into creative strength |
| S5 (Structure & Pacing) | v4.5 8% weighted | K1 | Structural viability | renamed | Direct rename with broader scope (sections/bars/formal coherence) |
| S6 (Production Quality) | v4.5 12% weighted | K5 | Sonic identity | merged | Sonic identity absorbs production quality + timbral distinctiveness |
| S7 (Arrangement Interest) | v4.5 6% weighted | K1 + K3 | Structural viability + Creative strength | split | Structure-side → K1; novelty-side → K3 |
| S8 (Commercial Viability) | v4.5 8% weighted | K7 (v2.3 only) | External viability | preserved | Promoted from low-weight criterion to dedicated K-axis in v2.3 |
| S9 (Originality) | v4.5 6% weighted | K3 | Creative strength | merged | Non-genericity component of K3 |
| S10 (Metadata & Governance) | v4.5 4% weighted | (preserved as binary admissibility gate) | Metadata Gate | preserved | Stays binary; not in K-axis taxonomy |
| S11 (Lyric Syllable Integrity) | v4.5 4% weighted | K6 + Lyric Syllable Gate | Compression survivability + binary gate | split | Format compliance → binary gate; survival of meaning under syllable constraint → K6 |
| S12 (Pre-release QA) | v4.5 2% weighted | K7 (v2.3 only) | External viability | preserved | Promoted to K-axis in v2.3 |
| G-MD (Metadata Gate) | v4.5 binary gate | (preserved) | Metadata Gate | preserved | Binary admissibility, separate from K-axes |
| G-LS (Lyric Syllable Gate) | v4.5 binary gate | (preserved) | Lyric Syllable Gate | preserved | Binary admissibility, separate from K-axes |
| G-HK (Hook Gate) | v4.5 binary gate | (preserved) | Hook Gate | preserved | Binary admissibility, separate from K-axes |
| G-CS (Composite Score Gate) | ≥70 (deprecated per CR-009) | G-CS (97.5) | Composite Score Gate | superseded | Threshold raised; mechanism preserved |
| G-PR (Production Gate) | v4.5 binary gate | (preserved) | Production Gate | preserved | Binary admissibility |
| G-RM (Road-Map Gate) | v4.5 binary gate | (preserved) | Road-Map Gate | preserved | Binary; order-only |
| V-CMM | No commas outside lyrics | (preserved) | Stop-the-line: comma | preserved | Renamed as stop-the-line condition |
| V-RMO | Road-map order-only | G-RM | (renamed admissibility) | renamed | Same function, different layer |
| V-SS | Show summary within limit | (preserved) | Stop-the-line: char budget | preserved | Becomes CAP in v2.1 |
| V-FU | Final UST within limit | CAP | Char budget | renamed | CAP = 4960–4999 |
| V-LL | Lyric lock policy | LOCK | Lyric immutability | renamed | Stop-the-line preserved |
| V-CL | Container lint | (preserved) | Stop-the-line: container | preserved | All vocal lines quoted, sFX marked |
| ST-DD | Deviation detection (Self-Correction) | (preserved) | Stop-the-line master | preserved | Halt + revert pattern preserved |
| H-CA, H-EI, H-SF, H-VP, H-AGG | HPA Score (post-render) | (preserved) | HPA Score | preserved | Operates as separate post-render layer; not in admissibility |
| SEG (v5-c v2.1) | Structural Excellence Gate | K1 (partial) | Structural viability | compressed | 7 binary structural checks compressed into K1 severity-tiered axis |
| GC (G-Card artifact) | Output object | (preserved) | G-Card | preserved | Output artifact retained; threshold question (7.0/10 vs 97.5/100) NEEDS SOURCE |
| SE20 (v5-c v2.1) | Sonic Excellence 20 Matrix | K-axis evidence binding | Per-axis evidence | compressed | 20 evidence-bound items map to K1–K6; SE20.K1 ≈ K1, SE20.K2 ≈ K2, etc. — full mapping NEEDS SOURCE |
| CAP (v5-c v2.1) | Character budget | (preserved) | Stop-the-line: CAP | preserved | Becomes a named stop-the-line condition |
| LOCK (v5-c v2.1) | Lyric immutability | (preserved) | Stop-the-line: LOCK | preserved | Becomes a named stop-the-line condition |
| K1–K6 (v5-c v2.2) | Admissibility runtime | K1–K6 | (canonical) | preserved | Direct preservation in v2.3 |
| (NEW in v2.3) | — | K7 | External viability | added | Encompasses S8 + S12; tied to commercial/release readiness |
| (NEW in v2.3) | — | K8 | Visual coherence | added | Tied to VIS axis in Plane 2 |
| Q1–Q16 (Morris Matrix) | Possibly hypothetical | (no successor) | — | needs_source | No instantiation found in primary corpus |

---

## 6. Runtime Architecture Recommendation

**Selected: Option E — Dual system: weighted quality scoring + concurrent admissibility gates + stop-the-line blockers + post-render perception.**

### 6.1 Why Option E and not the alternatives

**Why not Option A (Weighted SEM only):** The primary corpus does not show v4.5 operating with weighted SEM as the sole gating mechanism. Even at the earliest 12-criterion epoch, binary admissibility gates (Metadata, Lyric Syllable, Hook, Production) and the Self-Correction Protocol stop-the-line ran concurrently with composite scoring. Eliminating admissibility and stop-the-line would degrade the operational baseline.

**Why not Option B (K-gates only):** K1–K6/K8 are admissibility criteria, not quality scoring. They produce severity-tiered pass/fail decisions, not continuous composite scores. Eliminating weighted scoring would lose CR-009's 97.5% release threshold (which applies specifically to composite quality), the impact-sorted remediation formula `weight × (1 − score/5)` from M8 (which requires continuous scores and weights), and the fine-grained quality gradient that supports targeted revision vs major rework decisions.

**Why not Option C (Weighted SEM below K-gates):** This implies K-gates run first and weighted SEM is a sub-process. Primary evidence shows the opposite ordering: M6 SME round-robin produces weighted scores → M7 evaluator computes composite + binary gates → M8 revision loop applies impact-sorted remediation. Both layers are concurrent within M7's evaluation, not stacked.

**Why not Option D (K-gates below weighted SEM):** Same objection in reverse. Neither is a sub-process of the other. They are concurrent layers consuming different aspects of the same UST state.

**Why Option E is correct:** The v4.5 corpus operationally ran four concurrent layers, and v5-c MOSAIC v2.2/v2.3 preserves all four with renamed components. Operator-confirmed evidence (S1842): weighted composite_pct = 99.1% AND all binary gates true → PASS G-Card. Both conditions had to hold. This is structural proof of the dual-layer requirement. Stop-the-line evidence: the Self-Correction Protocol explicitly halts on validator failure independent of composite score. HPA evidence: post-render perception runs after audio generation, separate from pre-render scoring/gating. Mosaic Layer 5 must implement all four as concurrent subsystems with explicit interfaces between them.

### 6.2 Layer 5 Internal Structure

```
LAYER 5 — ADMISSIBILITY (concurrent with creation, not after)
├── Layer 5a — Weighted Quality Scoring
│   ├── 12-criterion v4.5 matrix (S1–S12 with weights summing to 100%)
│   ├── Continuous scoring 0–5 per criterion
│   ├── Composite = Σ(score × weight)
│   ├── CR-009 release threshold: composite ≥ 97.5%
│   ├── Impact-sorted remediation: weight × (1 − score/5)
│   └── Output: composite_pct, ranked_deficiencies, G-Card artifact
│
├── Layer 5b — K-Axis Admissibility (concurrent with 5a)
│   ├── K1 Structural viability (sections, bars, formal coherence)
│   ├── K2 Cross-axis coherence (no orphan claims or contradictions)
│   ├── K3 Creative strength (motif, emotion, non-genericity)
│   ├── K4 Performance truth (believability, pocket, phrase realism)
│   ├── K5 Sonic identity (timbral distinctiveness, genre truth)
│   ├── K6 Compression survivability (what survives lawful projection)
│   ├── K7 External viability (CANDIDATE — v2.3, commercial/release readiness)
│   ├── K8 Visual coherence (CANDIDATE — v2.3, requires VIS axis in scope)
│   ├── Severity tiers: Observe / Warn / Challenge / Block
│   └── Evidence binding: every K-axis verdict cites UST address(es)
│
├── Layer 5c — Stop-the-Line Conditions (concurrent with 5a and 5b)
│   ├── Skipped subkey
│   ├── Silent fill
│   ├── Truncation
│   ├── Unauthorized lyric change
│   ├── False completeness
│   ├── Comma outside lyrics block (V-CMM)
│   ├── Show summary > 1000 chars
│   ├── Final UST > 4990 chars (CAP)
│   ├── Container lint failure
│   ├── Road-map non-order-only
│   ├── Lyric lock violation outside creation node (LOCK)
│   ├── Missing definitive technical.ust LOCK before reverse compilation
│   └── Behavior: HALT immediately + revert to last validly logged state
│
└── Layer 5d — Post-Render HPA (after Suno audio rendering)
    ├── Creative authenticity (1–5)
    ├── Emotional impact (1–5)
    ├── Sonic fidelity to intent (1–5)
    ├── Viral potential perception (1–5)
    ├── Aggregate HPA score (computation NEEDS SOURCE)
    └── Used for keeper selection from multiple Suno renders
```

### 6.3 Layer Interactions

**Layer 5a ⟵⟶ Layer 5b:** S1–S12 weighted scores feed K-axis evaluation as evidence. K-axis severity tiers feed back into impact-sorted remediation. Both layers consume the same UST state but produce different verdicts — composite percentage (5a) vs per-axis admissibility (5b). Both must pass for G-Card PASS.

**Layer 5b ⟵⟶ Layer 5c:** K-axis Block severity = stop-the-line trigger. Conversely, stop-the-line conditions render K-axis evaluation invalid (cannot assess admissibility on a corrupted UST). When Layer 5c fires, both 5a scoring and 5b admissibility halt until reverted to last valid state.

**Layer 5d separation:** Post-render HPA does not gate pre-render emission. HPA is a keeper-selection criterion among multiple successful renders. Failed pre-render layers (5a, 5b, 5c) prevent reaching 5d entirely. HPA failure does not unwind upstream layers — it triggers re-render or re-prompt.

---

## 7. Threshold Resolution

### 7.1 Threshold Inventory by Layer

| Threshold | Layer | Scale | Value | Behavior | Source | Status |
|---|---|---|---|---|---|---|
| Composite release | 5a Weighted | 0–100% | **≥97.5%** | Release candidate | CR-009 | CANON |
| Composite revision | 5a Weighted | 0–100% | 60–69% (deprecated) | Targeted revision (under old 70% threshold) | v4.5 SEM session | DEPRECATED per CR-009 |
| Composite rework | 5a Weighted | 0–100% | <60% (deprecated) | Major rework (under old 70% threshold) | v4.5 SEM session | DEPRECATED per CR-009 |
| Per-criterion min pass | 5a Weighted | 0–5 | varies (S1=4, S2-S6=3, S7=2, S8=3, S9=2, S10=3, S11=4, S12=2) | Floor for valid score; below = remediation candidate | v4.5 SEM session S0023 | CANON |
| K-axis Observe | 5b K-axis | severity tier | — | Log only | MOSAIC v2.2 | CANON |
| K-axis Warn | 5b K-axis | severity tier | — | Advisory | MOSAIC v2.2 | CANON |
| K-axis Challenge | 5b K-axis | severity tier | — | Return for argument | MOSAIC v2.2 | CANON |
| K-axis Block | 5b K-axis | severity tier | — | Stop progression | MOSAIC v2.2 | CANON |
| G-Card numerical | (artifact) | 1–10 | ≥7.0 | Quality threshold (alternate scale) | MOSAIC v2.1 + project knowledge | NEEDS SOURCE — relationship to 97.5/100 not mapped |
| HPA aggregate | 5d HPA | 1–5 | NEEDS SOURCE | Keeper selection (computation rule absent in primary corpus) | v4.5 monolith §6.4 | NEEDS SOURCE |
| Stop-the-line | 5c | binary | violation = halt | Cannot proceed; revert | v4.5 Self-Correction Protocol | CANON |
| CAP | 5c | char count | 4960–4999 | Final UST char budget | MOSAIC v2.1 | CANON |
| Show summary | 5c | char count | ≤1000 | Show summary char budget | v4.5 monolith | CANON |
| Lyric syllable | 5b/5c | int range | 6–10 per line | Lyric line syllable count | v4.5 SEM session | CANON (note: `userMemories` flags as T4-A unresolved between 6–10 vs 6–11 — operator decision required) |

### 7.2 What Each Threshold Applies To

CR-009's 97.5% applies **only to the Layer 5a composite weighted quality score**. It does not apply to:

- **Per-criterion scores** — these have their own minimum-pass values (S0023) preserved unchanged
- **K-axis admissibility (5b)** — these use severity tiers, not percentages
- **Stop-the-line conditions (5c)** — these are binary violations, not thresholds
- **Per-render HPA (5d)** — operates on a different scale (1–5 aggregate) with its own (NEEDS SOURCE) rule
- **G-Card numerical threshold of 7.0/10** — this is on a different scale; relationship to 97.5/100 NEEDS SOURCE

### 7.3 Final Release Readiness

A track is **release-ready** only when **all four layers pass simultaneously**:

1. Layer 5a: composite ≥ 97.5% AND no per-criterion below its minimum pass
2. Layer 5b: all K-axes at Observe or Warn severity (no Challenge or Block)
3. Layer 5c: no stop-the-line violations
4. Layer 5d (post-render): HPA aggregate ≥ keeper threshold (NEEDS SOURCE)

Operator-confirmed PASS evidence (S1842): composite_pct 99.1%, all gates true, run produced PASS G-Card. This empirically confirms the multi-layer-must-all-pass requirement.

---

## 8. Stop-the-Line Integration

Stop-the-line conditions are a **separate concurrent layer** within Layer 5, not subordinate to admissibility scoring. They run on every UST delta emission and halt the pipeline immediately on violation. They are not normal SEM criteria — they cannot be remediated by improving a score; they require revert to last valid state.

### 8.1 Required Stop-the-Line Conditions (operator-listed)

| Condition | Source | Halt Trigger | Recovery | Status |
|---|---|---|---|---|
| **Skipped subkey** | MOSAIC v2.2 + Day 3 | Any required UST address transitioned past PROPOSED without lawful fill or justified-open | Revert; re-engage SME for skipped address | CANON |
| **Silent fill** | MOSAIC v2.2 + Day 3 | UST address filled without lawful SME labor or without argued rationale | Revert fill; re-route to lawful SME | CANON |
| **Truncation** | MOSAIC v2.2 | Output cut off mid-emission; partial state presented as complete | Revert; re-emit with full state | CANON |
| **Unauthorized lyric change** | MOSAIC v2.1/v2.2 + LOCK | Lyric edit outside LYRICS_CREATION/MUSIC_CREATION node without LCR | Revert; LCR procedure required | CANON |
| **False completeness** | MOSAIC v2.2 + Day 3 | Incomplete state declared complete; summary substituting for actual fill | Revert; re-state actual completion status | CANON |
| **Missing LOCK** | Day 3 + MOSAIC | Reverse compilation attempted before definitive technical.ust LOCK | Halt reverse compilation; require LOCK first | CANON |
| **Output order violation** | v4.5 §7.6 + MOSAIC v2.1 | Road-map contains durations or violates order-only | Revert; re-emit with order-only | CANON |
| **Character-limit breach** | v4.5 VAL_Report + MOSAIC v2.1 | Final UST > 4999 chars OR Show Summary > 1000 chars | Revert; compress via worker-owned reverse processing (FOIL discipline) | CANON |
| **Comma outside lyrics block** | v4.5 monolith CR-008 | Comma appears outside `"...", ("...")` pattern | Revert; re-emit with comma policy | CANON |
| **Container lint failure** | v4.5 §7.6 QUINN | Vocal line not quoted, sFX not marked, headers malformed | Revert; re-emit with valid container | CANON |
| **Speaker attribution violation** | v4.5 monolith CR-007 | `[Lead:]` colon labels used; multi-primary not declared | Revert; use `[Lead]` only | CANON |
| **Stage direction misuse** | v4.5 monolith CR-006 | `"*(...)*"` quoted stage directions instead of `[ ** sFX: ... ** ]` | Revert; re-emit with sFX block syntax | CANON |

### 8.2 Stop-the-Line Behavior

- **Halt is immediate** — no continued emission after detection
- **Revert is to last validly logged state** — not just last emission, last *logged* valid state from the session ledger
- **No score remediation path** — stop-the-line is not "low score → improve"; it is "invalid state → restore valid state"
- **Detection is concurrent with emission** — every UST delta is checked; not a post-completion validator
- **All stop-the-line conditions are equal severity** — there is no tier; halt applies uniformly

### 8.3 Why Stop-the-Line Cannot Be Folded Into K-Axes

The user's task explicitly required: *"Do not treat stop-the-line blockers as normal SEM criteria."* Primary corpus supports this:

- **Different scale:** K-axes use severity tiers (Observe/Warn/Challenge/Block); stop-the-line is binary violation/no-violation
- **Different remediation:** K-axes can be remediated by improving the underlying address; stop-the-line requires revert
- **Different ownership:** K-axes are SME-evaluated; stop-the-line is controller-detected (procedural validation, no semantic judgment)
- **Different timing:** K-axes evaluate after SME labor on an address; stop-the-line evaluates on every emission delta
- **Different scope:** K-axes apply to UST content semantics; stop-the-line applies to UST format and process integrity

Even though K-axis Block tier appears to overlap with stop-the-line, they are different mechanisms. K-axis Block: "the work on this axis cannot continue until challenged content is resolved." Stop-the-line: "the system has entered an invalid state and must revert before any work continues anywhere." These produce different system behaviors.

---

## 9. Impact on SDG.v0.1 Layer 5

SDG.v0.1 Layer 5 was specified as a single layer with two concurrent functions: SEM Gates running concurrently with Stop-the-Line Conditions, plus Pain-to-Fix → Atomic Remediation. This resolution shows Layer 5 needs to be **internally split into four sublayers** (5a, 5b, 5c, 5d) with explicit interfaces.

### 9.1 Required Changes to SDG.v0.1

**Change 1 — Layer 5 internal structure.** Replace SDG.v0.1's single-layer Layer 5 with the four-sublayer structure documented in §6.2 of this resolution. Sublayers 5a, 5b, 5c are concurrent during creation; 5d operates post-render.

**Change 2 — Edge E11 split.** SDG.v0.1 E11 ("SEM Gates run concurrently with Stop-the-Line Conditions") becomes three edges:

- **E11a:** Layer 5a Weighted Quality Scoring runs concurrently with Layer 5b K-Axis Admissibility (both pre-render, both gating)
- **E11b:** Layer 5c Stop-the-Line runs concurrently with both 5a and 5b (independent halt mechanism)
- **E11c:** Layer 5d HPA runs post-render, sequential to 5a/5b/5c success

**Change 3 — Edge E12 stays in Layer 5b.** Pain-to-Fix → Atomic Remediation operates within Layer 5b's K-axis remediation flow plus Layer 5a's per-criterion deficiency handling. Library structure per OD-5 unchanged.

**Change 4 — Add new edge E22.** *Composite quality threshold (CR-009) is 97.5% on the Layer 5a weighted scale only. Does not apply to 5b severity tiers, 5c binary violations, or 5d HPA aggregate.* CANON. Source: CR-009.

**Change 5 — Add new edge E23.** *G-Card is an output artifact aggregating Layer 5a composite + Layer 5b K-axis verdicts + Layer 5c clean status + ranked deficiencies + required actions.* CANON. Source: v4.5 SEM session M7 + MOSAIC v2.1.

**Change 6 — Mark VIS axis (Layer 4) and K8 (Layer 5b) as candidate scope expansions.** Per MOSAIC v2.3 / Maestro v0 candidate, both the VIS canonical axis and K8 admissibility criterion are candidates for Mosaic substrate. Operator decision required on whether VIS is in scope for Mosaic v0 or deferred to a later release.

**Change 7 — HPA layer addition.** SDG.v0.1 did not surface HPA as a substrate primitive. Layer 5d HPA is a CANON post-render perception layer. Add edge E24: *HPA score (4-axis perception 1–5 each) gates keeper selection from multiple Suno renders.* CANON. Source: v4.5 monolith §6.4. Implementation note: HPA aggregate computation rule is NEEDS SOURCE.

### 9.2 What Does Not Change in SDG.v0.1

- Layer 4 Canon Layer (Technical UST + UST State Machine + Address Law + Null Protocol) unchanged
- Layer 6 Definitive LOCK gate unchanged
- Layer 7 Output Contract (Triad + ATP) unchanged — Triad still depends on LOCK, ATP packages Triad
- Cross-Plane Feedback (Layer 8) unchanged in function; Layer 5 internal split adds new feedback paths within Layer 5
- All operator decisions OD-1 through OD-5 unchanged

---

## 10. Open Questions

Only canon-blocking items listed.

**OQ-1: G-Card numerical threshold (7.0/10) vs composite weighted threshold (97.5/100).**
MOSAIC v2.1 evidence states G-Card threshold "Quality score ≥ 7.0" on a 1–10 scale. v4.5 SEM session evidence states composite ≥ 97.5% on a 0–100 scale per CR-009. These are not the same scale and the relationship is not mapped in primary corpus. **Possible interpretations:** (a) two scales for the same value (97.5/100 = 9.75/10, which exceeds 7.0); (b) two different gates measuring different things (composite = aggregated quality, G-Card = something else); (c) MOSAIC v2.1's "≥7.0" is a separate G-Card-specific threshold for promotion vs the composite for release.
**Blocks:** Layer 5a final threshold canonization. Operator must decide which threshold authoritative or how they relate.

**OQ-2: HPA aggregate computation rule.**
v4.5 monolith §6.4 lists four HPA sub-scores (creative_authenticity, emotional_impact, sonic_fidelity_to_intent, viral_potential_perception) each on 1–5. Aggregate "overall_hpa_score" is shown but the computation rule (mean? weighted? min-of-four?) is not stated in primary corpus.
**Blocks:** Layer 5d implementation. Mosaic cannot compute HPA aggregate without operator-confirmed rule.

**OQ-3: SE20 → K-axis mapping completeness.**
Operational evidence shows SE20 with 4 keys × 5 subkeys = 20 evidence-bound items. SE20.K1 maps roughly to K1 (Structural viability), SE20.K2 to K2 (Cross-axis coherence), SE20.K3 to K4 (Performance truth), SE20.K4 to K1+K3 (build/drop/contrast/density/space). Full mapping is not explicitly stated; SE20 may carry detail that K-axes compress out.
**Blocks:** Whether SE20 is preserved as evidence-binding sub-rubric within K-axes, or whether K-axes fully replace SE20. Operator decision required.

**OQ-4: K7 External viability scope.**
K7 (NEW in v2.3) appears to encompass v4.5 S8 (Commercial Viability) + S12 (Pre-release QA). Whether K7 also absorbs aspects of release readiness (distribution metadata, ISRC, stems, rights) — partially in v4.5 Phase 8 IP Dossier — is not explicit.
**Blocks:** Layer 5b K7 implementation. Scope must be defined before Mosaic v0 ships.

**OQ-5: K8 Visual coherence dependency on VIS axis.**
K8 (NEW in v2.3) is tied to the VIS (Visual Identity) axis added to Plane 2 in v2.3. If VIS axis is not in Mosaic v0 scope, K8 cannot operate. If VIS is in scope, K8 admissibility criteria must be defined.
**Blocks:** Mosaic v0 substrate scope decision (8 axes vs 9 axes).

**OQ-6: Q1–Q16 Morris Matrix existence.**
Mentioned in Chaos-Decomposer §5.2 as something to look for during ingestion. No instantiated Q1–Q16 schema, weights, or scoring rules found in primary corpus. May be: (a) a reference to the 12-criterion weighted matrix conflated with another count; (b) a reference to SE20's 20 items conflated; (c) an actual separate system that exists outside the searched corpus; (d) a hypothetical placeholder never implemented.
**Blocks:** Confirmation that Layer 5 is complete. If Q1–Q16 is a real separate system, Layer 5 may need a fifth sublayer.

---

## 11. Next Artifact Recommendation

**PERSONA_SCHEMA_DECISION.md**

Rationale: With SEM Layer 5 architecture now resolved to four sublayers (5a/5b/5c/5d), the next blocker for SUBSTRATE_SPEC_v0.1 is the worker schema canonization. Per OD-1, the v4.5 9-element flat schema is canonical. This decision needs to be formalized into a substrate-grade specification document with:

1. **Authoritative 9-element schema definition** — exact field names, types, semantics, validation rules
2. **Day 3 extension fields** — null_resolution_lens, fill_argument_style, preserve_null_conditions, downstream_risk_checks, contradiction_trigger_patterns — formalized as required or optional additions
3. **4-layer Persona Stack mapping** — explicit presentation grouping rules per OD-1 ("presentation only, not operational")
4. **Worker validation contract** — what makes a worker registration valid, what fails registration, error messages
5. **Worker-to-K-axis ownership mapping** — which workers own which Technical UST addresses (already partially specified in `os.maestro.momoney.knowledgeSpine` SME ownership map: THY/VOC/STY/TIM/PER/POST/MAP/LYR each have SME owners)

Inputs: v4.5 monolith Section 2 (worker definitions); `os.maestro.momoney.customInstructions.v4.2.3.md`; Day 3 documentation worker contract; `os.maestro.momoney.knowledgeSpine` SME ownership map; SDG.v0.1 Layer 2 specifications; this resolution's K-axis ownership requirements.

Output: PERSONA_SCHEMA_DECISION.md with: authoritative schema, validation contract, presentation mapping, ownership map, runtime registration rules, blocked/needs-source items, runtime implications for Layer 2.

**After PERSONA_SCHEMA_DECISION:** CONVERSATION_LAYER_LINEAGE.md (resolves Chimera-Indigo lineage attribution per OD-4) → SUBSTRATE_SPEC_v0.1.md (compiles all decisions into substrate canon) → BLUEPRINT_v0.1.md.

**Not next:** SUBSTRATE_SPEC_v0.1, CONVERSATION_LAYER_LINEAGE, BLUEPRINT_v0.1. All blocked on PERSONA_SCHEMA_DECISION.

---

**End SLR.v0.2026-04-28**

*SEM Layer 5 resolved as four-sublayer dual system: weighted quality scoring (5a) + K-axis admissibility (5b) + stop-the-line blockers (5c) + post-render HPA (5d). CR-009's 97.5% threshold applies only to Layer 5a composite. K8 in v2.3 is Visual coherence (NEW), not Compression survivability (which is K6 in both v2.2 and v2.3). Q1–Q16 Morris Matrix marked NEEDS SOURCE — no instantiation found in primary corpus. Six open questions (OQ-1 through OQ-6) listed; OQ-1 (G-Card threshold scale) and OQ-2 (HPA aggregate rule) are most critical for Layer 5 implementation. Seven changes required to SDG.v0.1 Layer 5 (internal split + new edges E22/E23/E24). Next artifact: PERSONA_SCHEMA_DECISION.md.*

*All edges remain CANDIDATE pending operator confirmation. FOIL discipline honored.*
