# MAESTRO v5 — Research Dossier v0.2: Reverse Audio Compilation to Technical UST

**Reverse Compilation of Audio to Structured Timing Maps for Deterministic Video Generation in MAESTRO**

**Version:** 0.2 (Draft for Mo's review — extends v0.1, does not replace it)
**Date:** 2026-04-20
**Author:** Claude (pre-acceptance draft)
**Status:** DRAFT. Same evidence discipline as v0.1: `[VERIFIED]`, `[INFERRED]`, `[PROVISIONAL]`, `[REJECTED]`.
**Pairs with:** v0.1 `MAESTRO_v5_VIG_SEL_Research_Dossier.md` — v0.1 establishes the VIG/SEL split; v0.2 specifies how to drive VIG deterministically from audio alone when upstream control signals are missing or external.

---

## 0. Executive Synthesis

**The question:** When MAESTRO's upstream phases have produced audio — either natively from a Suno generation or from an external generator whose control signals MAESTRO never saw — how do we recover enough structure from the WAV alone to drive a **deterministic, reproducible video pipeline**?

**The answer, compressed:**

1. **Low- and mid-level musical structure is reliably recoverable from WAV.** Beat grid, downbeat grid, tempo map, section boundaries, functional labels (verse/chorus/bridge), key, chord progression, energy envelope, and spectral features can all be extracted with established open-source tools at production quality. Tolerances are well-characterized (±30ms on beats with madmom; boundaries within 0.5–3s of human annotation with All-In-One / SongFormer).

2. **TRIAD-level recovery (density, emotional intensity, sonic texture) is partially lossy but operationally sufficient.** Density and energy intensity derive cleanly from signal analysis. Sonic texture (grit vs clean, analog vs digital) recovers a *plausible reading*, not the original author's intent. This gap is acceptable provided the recovered TRIAD is marked as **inferred** rather than canonical.

3. **Technical UST can be generated purely from audio** for structural/energetic fields. Fields that require semantic content (lyric pivot moments, narrative beats) need transcription — either from original lyrics if available, or from an ASR pass on vocal stems.

4. **Path A (reverse-compile → generate) is the MAESTRO default.** It produces a canonical, versioned UST artifact that can drive any video model deterministically. Path B (direct audio-conditioned generation via Seedance 2.0 / LTX-2) is fast and promising but currently opaque — no auditable intermediate artifact, limited reproducibility. **Recommendation: A as canon, B as optional "express mode" running in parallel for comparison.**

5. **Frame-level sync is achievable but not always desirable.** The perceptual tolerance research is clear: viewers register "musical fit" at section-level alignment (within a bar or two), not frame-level. Beat-accurate cuts should be reserved for deliberate aesthetic moments, not applied as a default.

**Deliverables in this dossier:**
- Schema for Technical UST derived from audio
- Concrete audio feature extraction pipeline (tool selection + call graph)
- Mapping rules from audio features to visual directives (references v0.1 §5)
- API/tool support evaluation for both paths
- Path A vs Path B comparison + recommendation
- Reference Python pipeline sketch
- Integration points in MAESTRO v5 phase structure
- Failure modes specific to reverse compilation

---

## 1. Key Insight — Closing the Loop

Your framing is correct and it's worth naming explicitly as a MAESTRO architectural principle:

> **Closed-Loop Audiovisual Compilation:** Even when the audio generator is external to MAESTRO — Suno, Udio, live recording, or any opaque source — MAESTRO can reconstruct sufficient control from the output audio alone to drive deterministic video production downstream. The loop closes via reverse compilation: WAV → feature extraction → Technical UST → VIG.

Consequences:

- **Generator independence.** VIG is not coupled to any particular audio model. Whether the song was generated in Suno v5.5, Udio v1.5, or recorded live, the same reverse-compilation pipeline applies.
- **Retroactive MAESTRO-ification.** Old tracks without MAESTRO provenance can be brought into canon via reverse compilation. This operationalizes Mo's erasure resistance: prior work is not lost because upstream control was unavailable.
- **Deterministic regeneration.** Technical UST is versioned, hashable, and deterministic given the same WAV. Two VIG runs against the same UST produce comparable videos modulo model noise, not divergent creative interpretations.
- **Audit trail survives external generation.** Even if Suno's internal controls are invisible, the UST provides an auditable record of "what the video was told the song was doing." This is the receipt MAESTRO needs.

This is the same logic as a disassembler: the binary runs; the source is lost; you recover enough structure to modify and recompile. MAESTRO's reverse compiler is built for audio → video, but the discipline is identical.

---

## 2. Audio → Structure Reconstruction (Sub-Q1)

### 2.1 What can be extracted from WAV with high confidence

| Feature | Tool (Primary) | Typical Accuracy | Evidence |
|---|---|---|---|
| **Beat grid** (onset times of each beat) | madmom `RNNBeatProcessor` + `DBNBeatTrackingProcessor` | ~30ms MAE on 4/4 pop; F-measure 0.85+ across genres | [VERIFIED: Frontiers 2025 benchmark vs GTZAN] |
| **Downbeat grid** (bar-level onsets) | madmom `RNNDownBeatProcessor` + `DBNDownBeatTrackingProcessor` | F-measure 0.75+; strongest tool for offline work | [VERIFIED: madmom ISMIR 2016, Böck et al.] |
| **Tempo (BPM)** | madmom `TempoEstimationProcessor`, or derived from beat grid | ±2 BPM typical | [VERIFIED: same source] |
| **Tempo changes / variable tempo** | BeatNet (particle filtering) or madmom with variable-tempo config | Works for gradual tempo drift; struggles with abrupt changes | [VERIFIED: BeatNet ISMIR 2021] |
| **Section boundaries** (where verse→chorus happens) | All-In-One (ISMIR 2023) or SongFormer (Oct 2025) | HR.5F (strict 0.5s) ~0.55; HR3F (relaxed 3s) ~0.75 on SALAMI | [VERIFIED: All-In-One arxiv 2307.16425, SongFormer arxiv 2510.02797] |
| **Functional labels** (intro/verse/chorus/bridge/outro) | All-In-One or SongFormer output labels | Frame-level accuracy ~0.65–0.75 | [VERIFIED: same sources] |
| **Key** | Essentia `KeyExtractor` or librosa chroma + Krumhansl-Schmuckler | ~0.70 correct on pop | [VERIFIED: Essentia docs] |
| **Chord progression** | madmom `CNNChordFeatureProcessor` + `CRFChordRecognitionProcessor` | Major/minor recognition ~0.80 | [VERIFIED: Korzeniowski/Widmer 2016] |
| **Onset density** | librosa `onset_strength` integrated over windows | Signal-level measurement | [VERIFIED: librosa docs] |
| **RMS / loudness envelope** | librosa `rms`, or EBU R128 LUFS via pyloudnorm | Signal-level measurement | [VERIFIED: standard audio engineering] |
| **Spectral centroid / brightness** | librosa `spectral_centroid` | Signal-level measurement | [VERIFIED: librosa] |
| **Spectral flux** | librosa or essentia | Signal-level measurement | [VERIFIED: librosa] |
| **Harmonic/percussive separation** | librosa `hpss` (median-filtering) | Fast approximation | [VERIFIED: librosa] |
| **Source separation** (vocals/drums/bass/other stems) | Demucs (htdemucs / v4) or Spleeter (older, faster) | Demucs is current SOTA for quality | [VERIFIED: Demucs is widely benchmarked SOTA] |
| **Vocal presence / activity** | VAD on separated vocal stem | High accuracy on separated stems | [INFERRED from standard VAD] |

### 2.2 What struggles or fails

- **Highly polyrhythmic or non-4/4 material:** Downbeat trackers assume Western metrical conventions; 5/4, 7/8, or African polyrhythms confuse them.
- **Ambient / drone / beat-less music:** Beat trackers fabricate beats that aren't perceptually real. For these genres, skip beat extraction and rely on energy envelope + spectral change.
- **Abrupt tempo changes:** Standard DBN decoding is HMM-based and assumes smooth tempo — sudden tempo shifts (common in progressive/experimental work) get smoothed over.
- **Dense electronic music with ambiguous downbeats:** Techno at 128 BPM where kick is on every beat often has no strong 1 — trackers guess.
- **Heavily time-stretched or glitch-processed material:** Generated audio with artifacts (common in earlier Suno generations) can break onset detection.

**Mitigation:** For MAESTRO-grade deterministic output, the Technical UST must carry **confidence scores** per extracted field. Low-confidence fields trigger either a human review gate or a fallback to simpler signal-level features.

### 2.3 Foundation audio encoders — the new substrate

For cases where conventional DSP-based MIR fails, **foundation audio encoders** (self-supervised models trained on huge music corpora) provide a drop-in feature source:

- **MusicFM** (masked language modeling on music audio) — strongest for segmentation tasks at time of writing [VERIFIED: emergentmind MSA topic, Dec 2025]
- **MERT** (music encoder, contrastive + predictive pretraining) — broadly competitive
- Both integrate into All-In-One and SongFormer as frozen backbones for downstream tasks

For MAESTRO, practical recommendation: **start with the classical stack (madmom + librosa + Essentia + Demucs + All-In-One)** for reliability and interpretability. Consider MusicFM/MERT-based encoders for fields where the classical stack fails (abrupt transitions, non-Western meters, beat-less material).

---

## 3. Audio → TRIAD Recovery (Sub-Q2)

TRIAD-level fields (density, emotional intensity, sonic texture) are **higher-level abstractions** than structural features. They require derivation from lower-level features, and the mapping is lossy.

### 3.1 Density (Arrangement Thickness)

**Directly measurable:**
- Number of active frequency bands (spectral density)
- Number of simultaneously active sources (via source separation: count stems with energy > threshold)
- Polyphony estimate (via chroma energy distribution)
- Spectral flatness (noisier = denser in texture)

**Derivation:**
```
density(t) = f(
  number_of_active_stems(t),
  spectral_spread(t),
  onset_density(t),
  dynamic_range(t)
)
```
Concrete formula: normalize and weighted-sum active stems (Demucs: drums/bass/vocals/other → 0..4), spectral spread (normalized), and onset density per window. Tune weights empirically per genre.

**Confidence:** High. Density is close to a signal-level measurement; recovery from WAV is near-lossless.

### 3.2 Emotional Intensity Curve (Valence-Arousal)

**Directly measurable features correlated with arousal:**
- RMS energy / loudness
- Spectral centroid (brighter → higher arousal)
- Onset density
- Tempo

**Features correlated with valence (harder):**
- Mode (major/minor) — rough proxy
- Lyric sentiment analysis — requires transcription
- Harmonic dissonance

**Derivation:**
- For arousal: linear combination of normalized RMS, centroid, onset density, tempo → 0..1 scalar per time window.
- For valence: needs either lyrics (VAD sentiment analysis) or a trained MER (Music Emotion Recognition) model like those from the DEAM dataset research.

**Practical tool:** The V2M survey cited in v0.1 (Sulun et al.) describes Gaussian-mixture modeling over emotion classifier output to produce valence-arousal curves [VERIFIED: arxiv.org/pdf/2502.12489]. This is reusable for forward audio → visual mapping.

**Confidence:** Medium for arousal, lower for valence. Mark TRIAD "emotional intensity" as inferred, not canonical.

### 3.3 Sonic Texture (Grit vs Clean, Analog vs Digital)

**This is where TRIAD recovery is weakest.** Texture descriptors are subjective and culturally loaded. "Grit" might mean tape saturation, bit-crushing, vocal rasp, fuzz guitar, or distorted 808s — all acoustically different signals.

**Approach 1: Signal-level proxies**
- Total harmonic distortion estimate (via clean reference, which you don't have → limited value)
- High-frequency noise content (HF spectral flux)
- Crest factor (peaks vs RMS; lower crest factor = more compressed/clipped)
- Spectral flatness (more noisy = higher flatness)

**Approach 2: Audio embedding similarity**
- Embed audio with CLAP or MuQ-MuLan (see v0.1 §2.6)
- Compute similarity to labeled reference texts: "gritty", "clean", "analog warmth", "digital sheen"
- This gives a soft label per descriptor with similarity scores

**Approach 3: Audio tagging models**
- PANN (Pretrained Audio Neural Networks) or YAMNet produce general-purpose audio tags
- Trained taggers can label production characteristics if fine-tuned

**Confidence:** Low-to-medium. Sonic texture recovery produces a *plausible reading* — it may or may not match the original generative intent. Flag as `[inferred_texture]` in UST, not canonical.

### 3.4 Design Rule

The Technical UST schema should separate **measured** fields (high confidence, signal-derived) from **inferred** fields (lower confidence, model-derived):

```
technical_ust:
  measured:          # canonical once extracted
    beat_grid: [...]
    downbeat_grid: [...]
    sections: [...]
    energy_envelope: [...]
    ...
  inferred:          # marked with confidence and model provenance
    triad:
      density: {value: 0.7, confidence: 0.9}
      arousal: {value: 0.6, confidence: 0.75}
      valence: {value: 0.4, confidence: 0.5, needs_lyrics: true}
      texture_gritty: {value: 0.3, confidence: 0.4, model: "CLAP_similarity"}
      texture_analog: {value: 0.65, confidence: 0.4, model: "CLAP_similarity"}
```

This matches MAESTRO's canon/draft discipline: measured fields can become canon immediately; inferred fields require explicit acceptance before they join canon.

---

## 4. WAV → Technical UST Schema (Sub-Q3)

### 4.1 Full proposed schema

```yaml
technical_ust:
  version: "1.0"
  source_audio:
    path: "<path/url>"
    sample_rate: 44100
    duration_seconds: 187.5
    hash: "<sha256>"
  
  global:
    tempo_bpm: 96
    tempo_confidence: 0.92
    time_signature: "4/4"
    key: "A minor"
    key_confidence: 0.78
    
  beat_grid:              # measured
    - {t: 0.625, beat: 1, bar: 1}
    - {t: 1.250, beat: 2, bar: 1}
    - {t: 1.875, beat: 3, bar: 1}
    - {t: 2.500, beat: 4, bar: 1}
    - {t: 3.125, beat: 1, bar: 2}
    # ...
  
  sections:               # measured
    - t_start: 0.0
      t_end: 15.0
      label: "intro"
      label_confidence: 0.85
      energy_relative: 0.3
    - t_start: 15.0
      t_end: 45.0
      label: "verse_1"
      label_confidence: 0.92
      energy_relative: 0.5
    - t_start: 45.0
      t_end: 75.0
      label: "chorus_1"
      label_confidence: 0.88
      energy_relative: 0.9
    # ...
  
  envelopes:              # measured, sampled at fixed rate (e.g., 10 Hz)
    sample_rate_hz: 10
    rms: [0.02, 0.03, 0.04, ...]
    spectral_centroid: [850, 920, 1100, ...]
    onset_strength: [0.1, 0.2, 0.15, ...]
    low_end_energy: [0.3, 0.35, 0.4, ...]  # energy below 200 Hz
  
  stems:                  # measured via source separation
    vocals_presence: [0.0, 0.0, ..., 0.9, 0.95, ...]  # per window
    drums_presence: [0.0, 0.3, ..., 1.0, 1.0, ...]
    bass_presence: [0.2, 0.2, ..., 0.8, 0.9, ...]
    other_presence: [0.5, 0.5, ..., 0.7, 0.8, ...]
  
  chord_progression:      # measured
    - {t_start: 0.0, t_end: 7.5, chord: "Am"}
    - {t_start: 7.5, t_end: 15.0, chord: "F"}
    # ...
  
  triad_inferred:         # lower confidence, derived
    density_curve: {...}
    arousal_curve: {...}
    valence_curve: {...}
    texture: {gritty: 0.3, clean: 0.6, analog: 0.4, digital: 0.5}
  
  visual_directives:      # derived per v0.1 §5 mapping — the handoff to VIG
    - t_start: 0.0
      t_end: 15.0
      section_ref: "intro"
      cut_density: "minimal"           # 0–2 cuts in this section
      motion_intensity: "low"
      camera_density: "minimal"
      subject_focus: "environment"
      palette_cue: "cool"              # derived from key=A minor + low energy
      composition_stability: "stable"
      lyric_overlay: false             # intro = instrumental
    - t_start: 45.0
      t_end: 75.0
      section_ref: "chorus_1"
      cut_density: "fast"              # 4–8 cuts per section
      motion_intensity: "high"
      camera_density: "kinetic"
      subject_focus: "performer"
      palette_cue: "saturated"
      composition_stability: "escalating"
      lyric_overlay: true              # chorus = lyrics-forward
      beat_accented_cuts: [46.25, 48.75, 51.25]  # specific beats flagged for hard cuts
    # ...
  
  provenance:
    generated_at: "2026-04-20T14:30:00Z"
    pipeline_version: "maestro_ust_compiler_v1.0"
    tools_used:
      - {name: "madmom", version: "0.16.1", purpose: "beat_downbeat"}
      - {name: "all_in_one", version: "...", purpose: "sections"}
      - {name: "demucs", version: "4.0.1", purpose: "source_separation"}
      - {name: "librosa", version: "0.10.2", purpose: "envelopes"}
      - {name: "essentia", version: "2.1_beta6", purpose: "key_chords"}
    lyrics_source: "maestro_canon" | "asr_whisper" | "none"
    human_review_passed: false
```

### 4.2 Can this be generated purely from audio?

**Structural and envelope fields (measured block):** Yes, 100% from audio.

**Triad_inferred block:** Partially — arousal and density work from audio alone; valence and texture benefit from lyrics or external reference.

**Visual_directives block:** Derived from the two blocks above using v0.1 §5 mapping rules. Does **not** require additional external input — just the rulebook.

**What does require lyrics:**
- Lyric overlay timing (word-level or line-level)
- Lyric-driven scene pivots
- Sentiment-based valence refinement
- Narrative arc analysis (call-and-response, vocatives, apostrophe)

**Lyric acquisition path when MAESTRO doesn't have canonical lyrics:**
1. Prefer MAESTRO canon (lyrics from P2 are already available)
2. Fallback: ASR on vocal stem via Whisper-Large-v3 or newer. Accuracy on separated vocal stems is ~90%+ for clearly-sung English pop; degrades on rap with dense syllables, on heavily processed vocals, on non-English material. [INFERRED from general Whisper performance]
3. Mark ASR-derived lyrics as `inferred`, not `canonical`.

---

## 5. Beat-Accurate Video Guidance (Sub-Q4)

### 5.1 What precision is technically achievable

| Granularity | Achievable | Mechanism | Use Case |
|---|---|---|---|
| **Sample-level** (~0.02ms) | Overkill; never needed | — | — |
| **Frame-level** (~41.67ms at 24fps) | Yes | madmom beat grid has ~30ms MAE; sub-frame accuracy available | Hard aesthetic cuts on kick, snare, hit |
| **Beat-level** | Yes, reliably | Beat grid → cut timestamps | Rhythmic editing |
| **Bar-level** | Yes, reliably | Downbeat grid → section-internal pacing | Musical phrase alignment |
| **Section-level** (~1–5s) | Yes, reliably | Section boundaries → major visual transitions | Structural storytelling |

### 5.2 What precision perceptually matters

Research on audiovisual perception (AV-Align metric, ImageBind cross-modal scoring, the 2025 Frontiers synchronization study) converges on:

- **Above ~100ms misalignment**, viewers notice audio-visual desync and the video feels "off."
- **Between 50–100ms**, viewers register coherence or incoherence but not as a hard sync error.
- **Below ~50ms**, most viewers cannot distinguish tight sync from loose sync.

Practical implications:

1. **Beat-accurate cuts work when used sparingly**, at moments where the viewer is primed for the hit (chorus drops, verse-end resolutions, specific lyric pivots). Indiscriminate beat-cutting every 500ms is both over-engineered and visually fatiguing (v0.1 §5.3 Anti-pattern 1).

2. **Section-level alignment is the load-bearing synchronization.** If the chorus visual change happens within 1–2 bars of the audio chorus onset, the video feels "tight." Pushing this to within 100ms doesn't improve perception.

3. **Motion envelope alignment matters more than cut-level sync.** Visual motion intensity tracking audio RMS over 1–4 second windows produces the strongest "musical fit" signal. [INFERRED from perceptual research + observed commercial tool behavior]

### 5.3 Design recommendation

Technical UST should **separate mandatory sync points from optional beat accents**:

- **Mandatory sync:** section boundaries (must-transition visually within 1 bar)
- **Strong sync:** downbeat at section start (visual anchor element on first beat of section)
- **Optional accents:** selected beats within a section flagged for hard cuts or motion bursts

This gives VIG explicit guidance about where to spend its sync budget, rather than making every beat equally important.

---

## 6. API / System Support (Sub-Q5)

Your instinct — "can we build or leverage APIs that accept WAV as primary input" — is answerable. Two categories to distinguish.

### 6.1 Audio → Features APIs (for Path A)

These are reliable, production-grade, open-source. No API gatekeeper.

| Tool | Call Shape | Notes |
|---|---|---|
| **madmom** | Python library; `DBNBeatTrackingProcessor()(audio)` returns beat times | De facto SOTA offline; install: `pip install madmom` |
| **librosa** | Python library; broad toolkit | `pip install librosa`; widely maintained |
| **Essentia** | Python bindings for C++ library; comprehensive | `pip install essentia-tensorflow` (pre-built wheels) |
| **Demucs** | PyTorch library; source separation | `pip install demucs`; GPU recommended |
| **All-In-One** | GitHub; reference implementation | Research-grade but functional |
| **SongFormer** | GitHub (arxiv 2510.02797); newer SOTA | Requires MusicFM or MERT backbone checkpoints |
| **Whisper** (for lyric ASR) | OpenAI API or local via `whisper` pip package | Large-v3 recommended for music |

**Cost:** ~zero at runtime (local compute). Primary cost is GPU time for Demucs and foundation encoders.

**Latency:** A full feature extraction pass on a 3-minute song takes ~30–60 seconds on a modern GPU, ~2–5 minutes on CPU. Not real-time but fast enough for MAESTRO's batch workflow.

### 6.2 Audio → Video APIs (for Path B)

These are proprietary or emerging. Audio-as-input conditioning is real but varies by vendor.

| System | Audio Input Mode | Status | Notes |
|---|---|---|---|
| **Seedance 2.0** (ByteDance) | Accepts audio alongside text + image + video as direct conditioning input [VERIFIED: Medium deep-dive Feb 2026] | Commercial API | "Director-level control"; 2K resolution; 15s clips. Music-specific conditioning fidelity **unverified empirically** — worth hands-on testing. |
| **LTX-2** | Audio is generated alongside video, not conditioned on input audio. Multi-keyframe mode does accept image keyframes. | Open / local | Strong for on-device generation; not directly audio-conditioned in the sense we need. |
| **Veo 3.1** (Google) | Text + image input; generates audio output. Does NOT accept audio as input conditioning in documented API. | Commercial API | Not a direct Path B candidate; use as Path A backend. |
| **Sora 2** (OpenAI) | Text input; generates synchronized audio output. Audio-input conditioning not documented. | Commercial API | Same as Veo. |
| **Research models** (MM-Diffusion, TATS, TempoTokens, AV-Link) | Yes — audio as direct conditioning | Academic; no production APIs | Require self-hosting and custom integration |

**Key insight:** True Path B (send WAV, receive video conditioned on music features) is currently achievable **only via Seedance 2.0** at production grade. Everything else is either Path A in disguise (it extracts features internally) or research-level.

**Indirect Path B via chained commercial tools:** Revid.ai, Neural Frames, Freebeat accept WAV/Suno link as input and produce video. Under the hood they run a Path A pipeline — but from the user's perspective it looks like Path B. This is a **hosted Path A**. Useful for MVP but opaque: MAESTRO never sees the intermediate UST, which defeats the closed-loop principle.

### 6.3 Recommendation on API usage

- **For Path A substrate:** Build in-house from open-source MIR tools. You get the canonical UST, full auditability, and no API dependencies. Cost near zero, latency acceptable.
- **For Path B experimentation:** Use Seedance 2.0 in parallel. Treat it as a black-box "express mode." Compare output to Path A outputs to validate or correct your UST-driven pipeline.
- **Avoid:** Using Revid / Neural Frames / Freebeat as primary VIG because they hide the UST. If used, use only as sanity-check references or for teaser-level output where auditability matters less.

---

## 7. Forward Pipeline: Path A vs Path B

### 7.1 Path A — Reverse Compile → Then Generate

```
WAV
 │
 ├─→ [2.1–3.4: Feature extraction stack]
 │     └─→ beat grid, downbeats, sections, energy, stems, key, chords
 │     └─→ inferred TRIAD (density, arousal, valence, texture)
 │
 ├─→ [4.1: Technical UST assembly with provenance]
 │     └─→ versioned, hashed artifact: song_abc_ust_v1.json
 │
 ├─→ [v0.1 §5: Visual directives derivation]
 │     └─→ per-section: cut_density, motion, palette, subject, overlay rules
 │
 ├─→ [v0.1 §4: VIG Architecture C]
 │     └─→ Visual Brief (LLM + stylebook + UST) → Shot Grammar → Keyframes → I2V → Timeline
 │
 ├─→ [v0.1 §8: P4B Conformance Gate]
 │     └─→ pass / revise / reject
 │
 └─→ [v0.1 §7: SEL Export]
       └─→ 9:16 variant, archive master, teaser variants, manifest
```

### 7.2 Path B — Direct Audio-Conditioned Generation

```
WAV + optional text prompt + optional reference image
 │
 └─→ [Seedance 2.0 API call with audio as conditioning]
       └─→ short video clip (~15s), audio-beat-conditioned
       │
       └─→ [chain multiple calls per section for full-length]
             └─→ assemble
             │
             └─→ [SEL Export]
```

### 7.3 Comparison

| Dimension | Path A (Reverse Compile) | Path B (Direct) |
|---|---|---|
| **Control surface** | Full — every parameter inspectable/tunable | Limited — black-box; prompt + audio only |
| **Consistency across runs** | Deterministic (same UST → same directives) | Model-noise dependent; non-deterministic |
| **Identity stability** | Strong — UST drives identity-locked generation | Weak — no identity lock unless prompt carries it |
| **Reproducibility** | Full — UST is versioned, hashable | Partial — seeds help but model updates break |
| **Auditability** | Full — every decision has provenance | Minimal — API returns video, no intermediate artifact |
| **Speed** | Medium (feature extraction + multi-stage generation) | Fast (single API call per section) |
| **Cost** | Mixed (local extraction = cheap; generation varies) | API credits per generation |
| **Failure modes** | Distributed across stages (debuggable) | Concentrated in one opaque step (harder to debug) |
| **Extensibility** | High — swap any stage without replacing whole pipeline | Vendor-dependent |
| **Fit for MAESTRO canon** | **Native fit** (matches canon/draft discipline) | Tangential (opaque to canon) |
| **Duration ceiling** | Full song (chained + assembled) | Short clips (15–25s per call) |
| **Quality per clip** | Depends on downstream model chosen | Single SOTA model |
| **Cross-release continuity** | Strong (stylebook + UST retrievable) | None (no artifact to reference) |
| **Research risk** | Low — every tool production-grade | Medium — Seedance audio-conditioning for music is unverified at scale |

### 7.4 Recommendation

**Adopt Path A as the MAESTRO canonical pipeline. Keep Path B as an optional parallel path ("express mode") for:**

- Quick teasers where auditability is less critical
- Validation — compare Path B output to Path A output to sanity-check the UST-driven directives
- A/B visual variants for TikTok/Reels where fast iteration matters

**Do not replace Path A with Path B** until one of these conditions is met:
1. Seedance 2.0 (or successor) documents audio-conditioning mechanism in enough detail to audit
2. Direct audio-conditioned models support output clips long enough for full songs (currently 15–25s)
3. A mechanism emerges to extract an intermediate UST-equivalent artifact from direct generation calls

Neither condition is imminent. Path A is the architecturally honest choice for MAESTRO's decade-scale discipline.

### 7.5 Hybrid: Path A+B Parallel

The most interesting configuration is **running both in parallel** per song:

```
WAV
 ├─→ Path A → Technical UST → VIG → Canonical Video Artifact
 └─→ Path B → Direct Seedance output
              │
              └─→ [Diff analysis: Path A output vs Path B output]
                    └─→ signal for UST improvement (where did Seedance disagree?)
                    └─→ signal for Seedance trust (how often does it concur?)
```

Over time, the diff log becomes training data: where Path A and Path B disagree systematically, you've found a place where your UST rules are missing something. This is the long-game move — use Path B as a *teacher* for Path A's rulebook.

---

## 8. Reference Python Pipeline Sketch

Not production-ready. Illustrates the call graph and dependencies.

```python
import madmom
import librosa
import numpy as np
import json
import hashlib
from pathlib import Path
from demucs.pretrained import get_model as demucs_model
from demucs.apply import apply_model

def compile_audio_to_ust(wav_path: str, lyrics: str | None = None) -> dict:
    """Reverse-compile a WAV file into a Technical UST artifact."""
    
    # --- 0. Load and hash
    audio, sr = librosa.load(wav_path, sr=44100, mono=True)
    duration = len(audio) / sr
    audio_hash = hashlib.sha256(Path(wav_path).read_bytes()).hexdigest()
    
    # --- 1. Beat + downbeat grid (madmom)
    beat_proc = madmom.features.beats.RNNBeatProcessor()
    beat_tracker = madmom.features.beats.DBNBeatTrackingProcessor(fps=100)
    beat_times = beat_tracker(beat_proc(wav_path))
    
    downbeat_proc = madmom.features.downbeats.RNNDownBeatProcessor()
    downbeat_tracker = madmom.features.downbeats.DBNDownBeatTrackingProcessor(
        beats_per_bar=[3, 4], fps=100
    )
    downbeats_with_positions = downbeat_tracker(downbeat_proc(wav_path))
    # returns [[time, beat_in_bar], ...]
    
    # --- 2. Tempo
    tempo = librosa.feature.rhythm.tempo(y=audio, sr=sr)[0]
    
    # --- 3. Key
    # via essentia or librosa chroma + Krumhansl-Schmuckler
    # (left as exercise — essentia KeyExtractor is cleanest)
    
    # --- 4. Sections (All-In-One or SongFormer)
    # sections = all_in_one.segment(wav_path)
    # returns [{t_start, t_end, label, confidence}, ...]
    
    # --- 5. Source separation (Demucs)
    model = demucs_model('htdemucs')
    sources = apply_model(model, audio[None, None], device='cuda')
    # sources: [drums, bass, other, vocals], each same length as input
    stems = {name: s.squeeze().cpu().numpy() 
             for name, s in zip(['drums', 'bass', 'other', 'vocals'], sources[0])}
    
    # --- 6. Envelopes
    hop = sr // 10  # 10 Hz sampling
    rms = librosa.feature.rms(y=audio, hop_length=hop)[0]
    centroid = librosa.feature.spectral_centroid(y=audio, sr=sr, hop_length=hop)[0]
    onset_strength = librosa.onset.onset_strength(y=audio, sr=sr, hop_length=hop)
    
    low_end = librosa.stft(audio, hop_length=hop)
    freqs = librosa.fft_frequencies(sr=sr)
    low_mask = freqs < 200
    low_end_energy = np.abs(low_end[low_mask]).mean(axis=0)
    
    # --- 7. Stem presence
    def stem_presence(stem_audio, hop):
        rms_stem = librosa.feature.rms(y=stem_audio, hop_length=hop)[0]
        return (rms_stem / rms_stem.max()).tolist() if rms_stem.max() > 0 else [0.0] * len(rms_stem)
    
    stems_presence = {
        name: stem_presence(s, hop) for name, s in stems.items()
    }
    
    # --- 8. TRIAD inferred
    density = compute_density(stems_presence, onset_strength, rms)
    arousal = compute_arousal(rms, centroid, onset_strength, tempo)
    valence = compute_valence(audio, lyrics)  # needs lyrics for better result
    texture = compute_texture_via_clap(audio)  # CLAP similarity to descriptor list
    
    # --- 9. Assemble UST
    ust = {
        "version": "1.0",
        "source_audio": {
            "path": wav_path,
            "sample_rate": sr,
            "duration_seconds": duration,
            "hash": audio_hash,
        },
        "global": {
            "tempo_bpm": float(tempo),
            "tempo_confidence": 0.9,  # from madmom if exposed
            "time_signature": "4/4",  # or derived from downbeat tracker
            "key": "A minor",  # from essentia
            "key_confidence": 0.78,
        },
        "beat_grid": [
            {"t": float(t), "beat": int(p), "bar": int(i // 4) + 1}
            for i, (t, p) in enumerate(downbeats_with_positions)
        ],
        "sections": [],  # from All-In-One / SongFormer
        "envelopes": {
            "sample_rate_hz": 10,
            "rms": rms.tolist(),
            "spectral_centroid": centroid.tolist(),
            "onset_strength": onset_strength.tolist(),
            "low_end_energy": low_end_energy.tolist(),
        },
        "stems": stems_presence,
        "chord_progression": [],  # from madmom chord recognizer
        "triad_inferred": {
            "density_curve": density,
            "arousal_curve": arousal,
            "valence_curve": valence,
            "texture": texture,
        },
        "visual_directives": derive_visual_directives(sections, envelopes, triad),
        "provenance": {
            "generated_at": "2026-04-20T...",
            "pipeline_version": "maestro_ust_compiler_v1.0",
            "tools_used": [...],
            "lyrics_source": "maestro_canon" if lyrics else "none",
            "human_review_passed": False,
        },
    }
    
    return ust


def derive_visual_directives(sections, envelopes, triad):
    """Apply v0.1 §5 mapping rules to produce per-section visual directives."""
    directives = []
    for section in sections:
        d = {
            "t_start": section["t_start"],
            "t_end": section["t_end"],
            "section_ref": section["label"],
            "cut_density": map_energy_to_cut_density(section, envelopes),
            "motion_intensity": map_arousal_to_motion(triad, section),
            "camera_density": map_density_to_camera(triad, section),
            # ... etc
        }
        directives.append(d)
    return directives
```

Three practical notes:

1. `madmom` requires numpy < 2.0 at time of writing; pin carefully. It also compiles C extensions on install — expect 2–5 minutes first time.
2. Demucs v4 `htdemucs` is the default; `htdemucs_ft` (fine-tuned) is slightly better for vocals.
3. All-In-One / SongFormer integration is still somewhat rough — both ship as research code. Budget for adapter work.

---

## 9. MAESTRO v5 Integration — Where This Lives

Relating v0.2 to v0.1's phase structure:

```
P2 — Draft Assembly
  └ Song draft, lyrics, arrangement cues

P3 — Performance and Identity Fit
  └ Master audio + artist identity bundle

  ┌─ NEW: P3.5 — UST Compilation  ──────────────────────┐
  │  Input: Master audio (P3) + lyrics (P2) + stylebook │
  │  Process: Reverse compilation per §2–4              │
  │  Output: Technical UST artifact (versioned, hashed) │
  │  Consumer: P4A VIG                                  │
  └─────────────────────────────────────────────────────┘

P4A — VIG: Visual Identity Generation
  └ Input now includes UST (was already implicit; now canonical)
  └ Visual directives from UST drive shot grammar + pacing directly

P4B — Visual Conformance Gate
  └ Additional check: does rendered video honor UST directives?
  └ E.g., if UST calls for high cut_density in chorus, does video deliver?

P5 — SEL: Surface Export Layer
  └ Unchanged, but SEL manifest now includes UST hash for provenance
```

**Key integration points:**

- **UST is a canonical artifact** between P3 and P4A. Versioned, hashed, provenanced.
- **UST is generator-agnostic.** If MAESTRO knows P3's generation controls (Suno prompt tags, voice selection, etc.), those are recorded separately; but UST is derived from audio and remains valid even when upstream controls are unknown.
- **UST is stylebook-independent.** Two artists can share a UST schema with different stylebooks producing different videos from identical UST — separation of concerns is clean.
- **UST hash enables regeneration.** If a VIG render fails or a model updates, the same UST can be re-fed into a new VIG run and the result is comparable.

---

## 10. Failure Modes Specific to Reverse Compilation

| Failure | Symptom | Root Cause | Mitigation |
|---|---|---|---|
| **Silent beat misalignment** | Downbeat grid is off by half a bar; all downstream visual cuts shifted | Beat tracker ambiguity (4/4 vs cut-time) | Confidence scores on downbeats; human review for low-confidence cases; reference against drums stem for kick alignment |
| **Ghost sections** | Section boundaries detected where humans don't hear them | Model over-segments on production changes (instrumentation shifts) mistaken for section changes | Confidence threshold; merge adjacent same-label sections; cross-check against energy envelope |
| **Lost sections** | Real bridge or middle-8 not detected | Model under-segments when energy is smooth | Manual override allowed; UST supports `manual_sections` field that overrides model output |
| **TRIAD inference diverges from intent** | Recovered texture doesn't match what the song "is" | High-level features are lossy | Mark all TRIAD fields as `inferred` with model provenance; require explicit canonicalization step |
| **Tempo ambiguity** | Half-time / double-time confusion (trap at 70 vs 140 BPM) | Beat trackers default to higher BPM when both are defensible | Detect with tempo doubling/halving heuristic; expose as tempo_candidates list, pick via kick density |
| **Non-4/4 mishandled** | 7/8 or 5/4 song gets fit to 4/4 grid | Downbeat tracker trained on mostly 4/4 | Support 3/4 and 6/8 via madmom config; flag anything that doesn't fit for human review |
| **Silent passages confuse envelope** | Gaps treated as "low energy" when they're structural silences | Normalization against non-silent portions | Detect silence explicitly; treat as separate structural element |
| **UST drift across versions** | v1.0 and v1.1 UST from same WAV differ | Tool or model updates | UST_compiler_version in provenance; old UST remains canonical for old videos; new compilations get new UST |
| **Lyric ASR errors propagate** | Mis-transcribed lyrics drive wrong lyric-overlay timing | Whisper accuracy varies | Prefer canonical lyrics from P2; only ASR when unavoidable; mark inferred lyrics explicitly |
| **Source separation bleed** | Vocals detected during instrumental sections (bleed from Demucs) | Imperfect separation | Threshold vocal_presence; require sustained detection, not single-frame |

---

## 11. Open Research Questions

1. **[PROVISIONAL]** Does Seedance 2.0's audio conditioning actually respect musical beat structure, or does it respond primarily to general audio energy? Requires empirical test: same song, same prompt, different audio variants (original, pitched, time-stretched, silence) — does the video change in musically-coherent ways?

2. **[UNRESOLVED]** Should TRIAD texture descriptors be a fixed vocabulary (grit/clean/analog/digital/etc.) or open-ended embeddings? Fixed gives auditability; open gives nuance.

3. **[UNKNOWN]** What's the right confidence threshold for promoting an `inferred` UST field to `canonical`? Likely song-specific and genre-specific. Initial default: ≥0.85 inference confidence + human acceptance.

4. **[UNRESOLVED]** Is there a way to reverse-compile Suno-specific generation parameters (style tags, voice selection, persona) from the WAV? Almost certainly not perfectly — generation is lossy — but signature patterns might be detectable. Low priority.

5. **[PROVISIONAL]** Should UST store raw audio features or just the derived visual directives? Trade-off: storing raw makes re-derivation cheap when rules change; storing only derivatives is more compact. Initial recommendation: store both, compress raw.

6. **[UNKNOWN]** Can a single foundation audio encoder (MusicFM, MERT) replace the madmom + librosa + Essentia stack? Would simplify the pipeline considerably. Not yet, but trend is moving that direction.

7. **[UNRESOLVED]** What's the policy for UST when the same song is re-generated in Suno (v5.5 vs v6)? Each generation produces slightly different audio → slightly different UST. Do we keep both? Version-link?

---

## Appendix — Evidence Provenance Index (v0.2-specific additions)

### MIR tools

- **madmom (beat/downbeat/tempo/chord/onset)** [VERIFIED]: `github.com/CPJKU/madmom`, ISMIR 2016 paper Böck et al.
- **Frontiers 2025 benchmark (madmom beat tracking F-measure SOTA)** [VERIFIED]: `frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1595939/full`
- **BeatNet (realtime joint beat/downbeat/tempo/meter)** [VERIFIED]: `github.com/mjhydri/BeatNet`, ISMIR 2021
- **All-In-One music structure analysis** [VERIFIED]: `arxiv.org/pdf/2307.16425` (ISMIR 2023)
- **SongFormer** [VERIFIED]: `arxiv.org/html/2510.02797` (Oct 2025)
- **MusicFM / MERT foundation audio encoders (current SOTA for MSA)** [VERIFIED]: `emergentmind.com/topics/music-structure-analysis-msa` (Dec 2025 summary)
- **librosa** [VERIFIED]: standard reference, McFee et al. SCIPY 2015
- **Essentia** [VERIFIED]: Bogdanov et al. ISMIR 2013
- **Demucs htdemucs v4** [VERIFIED]: widely benchmarked SOTA for source separation

### Audio-conditioned generation

- **Seedance 2.0 audio-as-input** [VERIFIED]: `medium.com/codetodeploy` deep dive Feb 2026
- **LTX-2 inline audio generation** [VERIFIED]: `blogs.nvidia.com` CES 2026 coverage
- **Veo 3.1 / Sora 2 audio-output (not audio-input)** [VERIFIED]: `datacamp.com/blog/top-video-generation-models`
- **AV-Link bidirectional A↔V** [VERIFIED]: `openaccess.thecvf.com` ICCV 2025

### Perceptual synchronization research

- **Synchronization tolerance thresholds** [INFERRED from]: Frontiers 2025 Human-Media Interaction study + classical V2M audio-visual alignment literature
- **AV-Align and ImageBind cross-modal scoring** [VERIFIED]: referenced in V2A survey `emergentmind.com/topics/video-to-audio-generation-model`

### Other

- **Whisper for vocal ASR accuracy** [INFERRED from]: general Whisper-Large-v3 reported benchmarks; specific music-vocal accuracy requires testing
- **V2M survey (valence-arousal modeling pattern)** [VERIFIED]: `arxiv.org/pdf/2502.12489`
- **CLAP / MuQ-MuLan for texture similarity** [VERIFIED]: `emergentmind.com/topics/pretrained-text-audio-embeddings-clap-and-muq-mulan`

---

**End of Research Dossier v0.2**

*Pairs with v0.1. Accepted sections become MAESTRO canon. Nothing finalizes until Mo confirms.*
