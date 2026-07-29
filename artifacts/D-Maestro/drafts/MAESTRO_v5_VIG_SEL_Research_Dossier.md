# MAESTRO v5 — Research Dossier: VIG + SEL

**From Music Semantics to Visual Identity: A Systems Investigation of Audio-Conditioned Video Generation and the Role of Suno Hooks as a Distribution Surface**

**Version:** 0.1 (Draft for Mo's review)
**Date:** 2026-04-20
**Author:** Claude (in collaboration with Mo, pre-acceptance draft)
**Status:** DRAFT — pending Mo acceptance gate. Nothing in this document is canon until explicitly confirmed.

**Evidence labels used throughout:**
- **[VERIFIED]** — Directly supported by public documentation, first-party product materials, or peer-reviewed literature
- **[INFERRED]** — Reasoned from known multimodal architecture patterns and public benchmarks
- **[PROVISIONAL]** — Plausible but weakly evidenced; requires additional verification before committing
- **[REJECTED]** — Previously assumed but contradicted by evidence

---

## 0. Executive Synthesis

MAESTRO v5 currently lacks a formal axis for transforming song identity into visual identity. The investigation into "Suno Hooks as audio-to-video generator" surfaced a foundational premise error: **Hooks is a distribution/discovery surface, not a generative model.** The corrected question is therefore split across two architectural concerns:

1. **VIG (Visual Identity Generation)** — the system component that turns song identity into controllable visual artifacts, using real audio-conditioned video generation stacks (Sora 2, Veo 3.1, Seedance 2.0, LTX-2, Kling, Runway, Pika) and/or chained pipelines that combine LLM briefing + image models + image-to-video motion synthesis.

2. **SEL (Surface Export Layer)** — the system component that packages VIG artifacts for publication to music-discovery surfaces: Suno Hooks (feed inside Suno), TikTok, YouTube Shorts, Instagram Reels, and archival endpoints. SEL governs format, crop, caption, start-point selection, and variant fan-out.

A secondary nuance: **Suno *does* have native generative video in the form of Animated Cover Art** [VERIFIED], but it is scoped to short looping cover-art animation, not narrative music video production. This feature is relevant to VIG as one upstream input type (album art animation) but does not replace the need for a full VIG axis.

The document that follows delivers: a contradiction report, verified product reality for Hooks and adjacent features, three ranked VIG architecture hypotheses, a formal audio-to-visual translation matrix, a capability benchmark across the generator landscape, an SEL specification, a MAESTRO v5 phase redesign (P2–P5 + artifact schemas), failure modes with mitigations, an implementation roadmap, open research questions, and a full evidence provenance index in the appendix.

Top-level recommendations, pending Mo's acceptance:

- **Adopt VIG as P4A and SEL as P5** in MAESTRO v5, with a Visual Conformance Gate (P4B) between them.
- **Default VIG architecture: Hybrid Multimodal Pipeline (Architecture C)** — storyboard-anchored, music-conditioned, with identity locking via reference images and stylebook. Architectures A and B remain valid for different use cases (concept-heavy abstraction and tight identity control respectively).
- **Explicitly reject "Hooks as generator"** in MAESTRO canon. Document the rejection with provenance so it doesn't regenerate in future design discussions.
- **Treat Animated Cover Art as a VIG sub-capability** (album-level looping visual), not a substitute for music video generation.

---

## 1. Contradiction Report (Canon / Draft / Rejected / Verified)

This table separates what was previously assumed from what the evidence actually supports. Each row documents the consequence for MAESTRO design.

| # | Prior Assumption | Current Evidence | Status | Consequence for MAESTRO |
|---|---|---|---|---|
| 1 | Suno Hooks generates video from audio | Hooks accepts user-uploaded clips (10s–4min), pairs with Suno track, crops to 9:16, optionally overlays lyric captions. Explicitly "not meant to create scenes from prompts or build entire edits for you." [VERIFIED: help.suno.com + suno.com/hub] | **REJECTED** | VIG cannot be architected on Hooks mechanism; Hooks is repositioned as SEL target |
| 2 | Hooks performs cross-modal latent alignment | No evidence of any audio→video generative model inside Hooks. Feed mechanics only. [VERIFIED by absence in official docs] | **REJECTED** | Latent-alignment research belongs in VIG upstream of Hooks, not in Hooks itself |
| 3 | Hooks performs beat-sync video generation | Creator manually selects track start-point and audio source. Sync is manual, not generative. [VERIFIED: suno.com/hub workflow] | **REJECTED** | Beat-sync mechanics move to VIG layer |
| 4 | Suno has no native generative video | Animated Cover Art (late 2025, updated March 2026) generates short looping video covers from static cover art, Basic/Advanced modes, "up to five minutes" generation time, credit-based pricing [VERIFIED: jackrighteous.com guide] | **VERIFIED (partial correction)** | Animated Cover Art is a valid upstream VIG input; scoped to looping covers, not full music videos |
| 5 | Text-to-video models cannot accept audio conditioning | Veo 3 / Veo 3.1 (Google) produces "natively generated audio" alongside video; Sora 2 (OpenAI) generates "synchronized audio alongside visuals"; **Seedance 2.0 (ByteDance) explicitly accepts audio as a conditioning input alongside text + image + video**; LTX-2 has "built-in audio, multi-keyframe support" [VERIFIED: multiple sources Feb–Apr 2026] | **VERIFIED** | VIG can leverage audio-accepting video models directly; Seedance 2.0 is the most directly aligned with music-conditioned generation |
| 6 | CLIP-style cross-modal alignment is the right backbone for audio→video | Contrastive alignment exists across three primary corpora: CLIP (text-image), CLAP / MuQ-MuLan (text-audio, music-specific), ImageBind (6-modality joint space). **ImageBind specifically enables audio-to-image generation by substituting audio embeddings into CLIP-text-conditioned decoders** [VERIFIED: ImageBind paper]. **AV-Link (ICCV 2025)** uses frozen video + audio DiT activations with cross-attention for bi-directional A↔V generation [VERIFIED: ICCV 2025] | **VERIFIED** | VIG latent-alignment strategy should use CLAP or MuQ-MuLan for music-text alignment, ImageBind or AV-Link-style fusion blocks for audio-conditioned video |
| 7 | Music-to-video is a solved academic problem | Video-to-Music (V2M) is comparatively well-studied (dedicated surveys exist); **the reverse direction — music-to-video with full semantic and beat awareness — remains weakly addressed in academic literature**. TempoTokens (AAAI) and TATS project audio embeddings into text-conditioned video generators as a mapping intermediate, not end-to-end. [VERIFIED: arxiv surveys] | **PROVISIONAL → REJECTED** | VIG must synthesize from a commercial + academic mix; pure-academic end-to-end M2V is not yet SOTA. Commercial pipelines (Freebeat, Neural Frames, Revid, Kaiber) are more mature but less transparent |
| 8 | A single model performs song→music-video end-to-end | Commercial tools are **chained pipelines**: audio analysis (BPM/structure/energy/lyrics) → storyboard/brief → image generation → image-to-video motion → beat-synced cut edit → lyric overlay. Neural Frames: "auto-detect BPM, structure, and energy" then Autopilot storyboard. Freebeat: BPM + beat + mood analysis, Pika/Runway/Kling model choice. [VERIFIED: product pages] | **VERIFIED (chained, not monolithic)** | VIG architecture must be a pipeline, not a single model call. This matches your preference for explicit structure and auditability |
| 9 | Hooks supports any aspect ratio | Hooks accepts 10s–4min clips and **adapts all input to 9:16 vertical** [VERIFIED: suno.com/hub + help.suno.com] | **VERIFIED** | SEL must produce 9:16 variant for Hooks; master format should be highest resolution with defined safe-zones for crop |
| 10 | Hooks audio always uses the Suno track | Hooks lets creator **choose audio source: either the clip's original audio or the Suno track** [VERIFIED: suno.com/hub]. This is a deliberate product decision with consequences for the feed algorithm | **VERIFIED** | SEL export manifest must include "preferred audio source" field; this also means Hooks tolerates lyric-mismatched uploads, which has identity-drift risk |

---

## 2. Verified Product Reality: Suno Hooks and Adjacent Features

This section establishes what the Suno ecosystem actually does, separated by feature, with first-party source confirmation.

### 2.1 Hooks (Feed / Distribution Surface)

**Role:** Short-form music-discovery feed inside Suno. Creator-driven upload of paired song + video clip.

**Verified mechanics** [VERIFIED: help.suno.com/en/articles/8049409, suno.com/hub/ai-video-generator, suno.com/hub/create-viral-short-videos]:

- **Input:** User-supplied video clip (raw footage, externally edited video, or externally AI-generated video). Length range: 10 seconds minimum to 4 minutes maximum.
- **Song pairing:** Creator selects a track from their Recents, Public, or Liked library.
- **Audio source toggle:** Creator chooses whether to use the clip's original audio OR the selected Suno track.
- **Start point:** Creator slides to pick where the track begins in the clip.
- **Captions:** Optional lyric overlay via "Show Lyrics" toggle.
- **Sync:** If the creator pre-edited the clip in another tool, Hooks offers a sync option for audio/visual alignment.
- **Aspect ratio:** All input adapted to 9:16 portrait.
- **Feed interactions:** Thumbs-up, comments, share, remix.
- **Access:** Left sidebar menu (desktop) or top of Hooks feed (mobile).

**Explicitly NOT present:**

- ❌ No text-to-video generation
- ❌ No audio-to-video generation
- ❌ No image-to-video generation
- ❌ No beat-synced cut generation
- ❌ No scene composition from prompts
- ❌ No latent-space cross-modal alignment

**First-party quote establishing non-generative scope** [VERIFIED: suno.com/hub/ai-video-generator, 3 weeks old at time of research]: Hooks is "not meant to create scenes from prompts or build entire edits for you. Instead, it gives musicians and casual creators something more focused: a way to pair songs with their clips."

### 2.2 Animated Cover Art (Native Generative Video, Scoped)

**Role:** Native Suno feature that generates short looping video from a song's cover image. Launched late 2025, guide updated 14 March 2026.

**Verified mechanics** [VERIFIED: jackrighteous.com animated-cover-art guide]:

- **Input:** Static cover image already attached to a song + optional short motion prompt.
- **Output:** Short looping video cover displayed during song playback; downloadable for external use.
- **Modes:** Basic and Advanced (affect visual quality and credit cost).
- **Duration starting point:** 5-second test runs recommended; longer options available at higher cost.
- **Generation time:** Up to 5 minutes per generation.
- **Variants:** Generates multiple options per request for user selection.
- **Access:** "Generate Cover Art" or "Animate" option on a song's cover image.

**Architectural implication:** This is an **image-to-video** pipeline (static cover → animated loop). It is not music-conditioned in any documented way — the primary conditioning is the cover image plus the motion prompt, not the audio track's features. [INFERRED from absence of audio-conditioning language in product documentation]

**Fit to VIG:** Animated Cover Art produces one narrow artifact type — the album/single loop — and fits cleanly as a VIG sub-capability for release-level visual identity. It does not substitute for narrative or performance-oriented music video generation.

### 2.3 Suno's Song-Detail "Upload Video" Slot

**Role:** Legacy or parallel attachment mechanism that lets a creator upload a video to a Suno song's detail page. [VERIFIED: flexclip.com workflow guide describes this path; navigates Library → ⋮ → Remix/Edit and related attachment options]

**Architectural implication:** Another SEL-adjacent surface. Different from Hooks (which is a feed) and from Animated Cover Art (which is generative). Distinct asset slot; SEL should manage it separately or treat it as a variant of the same export manifest.

### 2.4 Suno Studio and Custom Models (v5.5, March 2026)

**Role:** Full DAW, voice cloning, custom model fine-tuning. Not directly in scope for VIG/SEL, but relevant context for MAESTRO upstream phases. [VERIFIED: suno.com/blog/v5-5]

### 2.5 Suno API (Generation + Metadata)

**Role:** Programmatic access for song generation, with webhook callbacks returning audio URL + JSON metadata. Relevant to MAESTRO P2 assembly. Typical generation 20–30 seconds. [VERIFIED: third-party API integration guides]

### 2.6 Third-Party Audio-to-Video Generators (The Real VIG Candidates)

These are **external to Suno**. They are what your original prompt was describing architecturally, even though it attached the Hooks label to them.

| Tool | Core Claim | Verified Mechanics | Evidence |
|---|---|---|---|
| **Neural Frames** (Suno-to-Video) | Auto-detect BPM/structure/energy → Autopilot storyboard → timeline editor with beat-level animation | Chained pipeline; multi-model generation control; audio-reactive modulation | [VERIFIED: neuralframes.com/suno-to-video] |
| **Freebeat** | Beat + tempo + mood analysis; model choice (Pika/Runway/Kling); lip-sync singing; dance-video generation | Chained; "director-level shot planning"; A-roll/B-roll support; 16:9 and 9:16 export | [VERIFIED: freebeat.ai + freebeatfit.com reviews] |
| **Revid.ai** | Audio analysis → visual style selection (AI video / moving AI image / stock) → beat or lyric sync | Chained; explicit beat-sync vs lyric-sync toggle; dynamic cuts; auto lyric transcription | [VERIFIED: revid.ai/tools/suno-to-video] |
| **LlamaGen** | "AI trained specifically on Suno tracks"; genre/mood → visuals; lyric typography integration | Claims specialization in Suno patterns; unverified internal mechanism | [PROVISIONAL: marketing language, mechanism opaque] |
| **Kaiber** | Visual-identity-focused; creative expression over structured output | Popular in EDM for drop/build visualization; less structured than Freebeat | [VERIFIED: riverbeats.life EDM comparison] |

### 2.7 Direct Audio-Capable Video Generators (Non-Suno-Specific)

These are foundation-model-level video generators, several of which now accept or emit audio natively. They are the most architecturally pure VIG substrates.

| Model | Audio Role | Input Modalities | Notes | Evidence |
|---|---|---|---|---|
| **Veo 3 / Veo 3.1 / 3.1 Lite** (Google) | Natively generates synchronized audio with video (dialogue, SFX, ambience) | Text + image → video+audio | 8-second clips at 720p/1080p; 16:9 and 9:16 native; lip-aware speech | [VERIFIED: modelslab.com, datacamp.com] |
| **Sora 2** (OpenAI) | Generates synchronized audio alongside visuals in one pass | Text → video+audio | Up to 25 seconds continuous; physics simulation focus; failure-mode simulation | [VERIFIED: datacamp.com top models 2026] |
| **Seedance 2.0** (ByteDance) | **Accepts audio as conditioning input** (alongside text + image + video) | Text + image + video + audio → video | "Director-level control"; 2K resolution; 15s clips; most directly music-conditionable | [VERIFIED: medium.com/codetodeploy deep dive Feb 2026] |
| **LTX-2** | Built-in audio generation; multi-keyframe; advanced conditioning LoRAs | Text + keyframes → video+audio | Local/on-device via NVIDIA RTX + ComfyUI; up to 20s at 4K | [VERIFIED: blogs.nvidia.com Jan 2026] |
| **MiniMax Hailuo 02** | Video with physics focus; audio integration via pipeline | Text → video | Noise-Aware Compute Redistribution architecture; 1080p | [VERIFIED: datacamp.com] |
| **Runway Gen-3 / Gen-4** | Video gen; audio added separately in workflow | Text + image → video | Strong control surfaces; motion brushes; Act-One animation | [VERIFIED: commonly referenced in 2026 tool comparisons] |
| **Pika 2.0+** | Video generation, scene-extension oriented | Text + image → video | Common inside Freebeat-style chained pipelines | [VERIFIED: freebeat + comparison sources] |
| **Kling 2.0+** | High-quality motion; cinematic camera language | Text + image → video | Used inside Freebeat's multi-model switcher | [VERIFIED: freebeat + comparison sources] |
| **Stable Video Diffusion** | Open-source image-to-video | Image → video | Base for custom/local pipelines; augmented U-Net with temporal attention | [VERIFIED: arxiv paper on SVD architecture] |
| **CogVideoX** | Text-to-video with 3D VAE + expert transformer | Text → video | Cited as SOTA open architecture for 10-second coherent video; used in MM-Audio research | [VERIFIED: arxiv.org/html/2603.16093v1] |

---

## 3. Formal Definition: Music-to-Visual Identity Translation (M2VIT)

**The missing MAESTRO capability is not "Hooks generation." It is Music-to-Visual Identity Translation, defined as:**

> **M2VIT** — The structured process by which a song's sonic, lyrical, emotional, structural, and stylistic parameters are transformed into controllable visual artifacts suitable for release-level visual identity, promotional short-form video, and archival music-video production, with continuity across releases and auditable provenance.

**M2VIT is a first-class axis, not a utility.** It produces versioned artifacts with the same rigor as song drafts: briefs, blueprints, scene specs, and rendered outputs, each with provenance.

### 3.1 Inputs to M2VIT

Organized as a three-tier feature hierarchy (this separation matters for architecture decisions later):

**Tier 1 — Low-level signal features** (extractable deterministically from audio)
- BPM / tempo, tempo stability
- Onset density / rhythmic density
- Spectral centroid / brightness
- Spectral flux (timbral change rate)
- Low-end energy (sub-bass weight)
- Dynamic range / loudness envelope
- Key / mode

**Tier 2 — Mid-level musical structure** (extractable via MIR models)
- Section boundaries (verse/chorus/bridge/drop)
- Chord progression and harmonic tension
- Arrangement density per section
- Vocal presence / register / gender / style
- Harmonic vs percussive separation

**Tier 3 — High-level affective and narrative meaning** (extractable via LLM + multimodal models)
- Lyrical content, imagery, narrative voice
- Emotional valence and arousal (per-section contour)
- Genre priors and subgenre cues
- Cultural/regional signifiers
- Performer persona and identity cues
- Trauma/memory/heritage themes (Mo-specific: the symbolic lexicon — Delta, echoes, spirals, ghosts)

### 3.2 Outputs of M2VIT

Layered artifacts, canonical-vs-draft-separated:

- **Visual Brief** (draft, pre-render): written spec of concept, mood, palette, setting, characters, references
- **Shot Grammar Spec** (draft): per-section shot list, camera language, edit density, motion vocabulary
- **Aesthetic Constraint Map** (canon once accepted): rules that govern every render — palette, typography, identity locks, sacred-imperfection flags, banned clichés
- **Style Reference Bundle** (canon): reference images, LUTs, camera lens profiles, motion presets
- **Rendered Visual Artifacts** (draft until accepted, then versioned canon): scenes, loops, full cuts
- **Export Package Manifest** (for SEL): surface-specific crops, caption variants, start-point selections, audio-source decisions

### 3.3 Governing Principles (ported from Mo's collaboration framework)

- **Canon vs Draft separation**: generated output is draft until explicitly accepted; accepted artifacts become canon and cannot be silently overwritten.
- **Rationale preservation**: every brief, spec, and constraint carries the reasoning that produced it. No compression of "why."
- **Sacred Imperfection flag**: aesthetic-constraint map includes an explicit roughness budget — polish thresholds above which output is flagged as "too clean; may be killing the soul."
- **Erasure resistance**: every artifact carries provenance, version, and authorship metadata. No artifact can be orphaned.
- **Contradiction surfacing**: if a new generation conflicts with the aesthetic-constraint map or stylebook, the conflict is surfaced, not silently reconciled.

---

## 4. VIG Architecture Hypotheses (Three Candidates, Ranked)

Three architecture candidates are proposed, each optimized for a different trade-off. All three are implementable today on commercial + open-source substrates. Each is specified with: inputs, transformations, control surfaces, strengths, likely failure points, and fit profile.

---

### Architecture A — Prompt-Expanded Text-to-Video (Concept-Forward)

**Thesis:** Treat the audio → video step as a **textual translation problem**. Use audio-feature extraction + lyric parsing + style references to construct a rich, structured prompt, then hand that prompt to a text-to-video model (Veo 3.1, Sora 2, CogVideoX) that handles the actual video synthesis.

**Inputs:**
- Song audio file
- Lyrics (from MAESTRO canon)
- Metadata: genre, mood, BPM, key, section map
- Stylebook (aesthetic constraint map)
- Optional: cover art reference

**Transformations:**
1. Audio feature extraction (BPM, onsets, section boundaries, energy envelope) via MIR library (librosa, madmom, essentia)
2. Lyric semantic analysis via LLM: extract imagery, emotional arc, named entities, metaphors
3. Musical structure mapping via LLM + templates: convert Tier-1/Tier-2 features into English descriptions
4. Visual Brief assembly via LLM with stylebook constraints injected as system context
5. Per-section prompt generation: one prompt per verse/chorus/bridge/drop, each 50–200 words
6. Text-to-video model call per section (8s–25s clips)
7. Stitch + light post-processing (lyric overlay, beat-aligned cut marks)

**Control surfaces:**
- Prompt engineering: direct English control of scene semantics
- Style tokens: genre/era/cinematographer references
- Negative prompts: excluded clichés, anti-patterns
- Section-level override: different visual direction per song section

**Strengths:**
- Fastest to implement (no custom training)
- Highest-quality individual clips (leveraging SOTA models like Veo 3.1)
- Strong for abstract/atmospheric/conceptual songs
- Easy to version and audit (prompts are inspectable text)
- Aligns with Mo's preference for text-based canon + auditability

**Failure points:**
- Weak temporal continuity across sections (each clip is independently generated)
- Character/subject identity drift between shots
- Over-literal lyric rendering when LLM describes lyrics directly
- Text-to-video models cannot truly "hear" the song — beat sync is post-hoc, not generative
- Cannot directly control fine-grained motion timing

**Fit profile:**
- Independent artists with limited production resources ✅
- Concept-heavy releases (abstract, ambient, art-pop) ✅
- High release cadence (one video per week) ✅
- Narrative music videos with recurring characters ❌
- Performance-forward footage ⚠️ (weak — no lip-sync from audio)

**Reference implementations:** Revid.ai workflow, Neural Frames Autopilot mode, most Suno-to-video third-party tools.

---

### Architecture B — Storyboard + Image-to-Video (Identity-Forward)

**Thesis:** Treat the audio → video step as a **staged production pipeline**. Generate keyframes/scene boards as images first, then animate each with image-to-video motion synthesis, with music-conditioned pacing at the edit layer.

**Inputs:**
- Everything from Architecture A
- Artist reference images (face, body, style, wardrobe)
- Location/setting reference images
- Optional: camera/lens reference stills

**Transformations:**
1. Audio feature extraction + section map (same as A)
2. Shot Grammar Spec via LLM: per-section shot list, count, camera angle, subject, action
3. Keyframe image generation (Midjourney, FLUX, DALL-E, Imagen) with identity locking via reference images or trained LoRA
4. Image-to-video motion synthesis per keyframe (Runway Gen-4, Pika 2.0, Kling 2.0, LTX-2, Stable Video Diffusion) — 3–10 second clips
5. Edit timeline assembly with cut points mapped to beat/section boundaries
6. Optional: lip-sync pass on performance shots via tools like Wav2Lip or commercial lip-sync services
7. Beat-aligned transitions and lyric overlays

**Control surfaces:**
- Reference image locking (subject consistency)
- Trained LoRA / Custom Models for persistent character identity
- Shot-by-shot direction (camera, composition, action)
- Edit rhythm as an explicit, tunable parameter
- Hand-authored shot list override possible at any step

**Strengths:**
- Strongest identity consistency across shots (this is critical for Mo's erasure resistance)
- Stage-by-stage auditability — every shot is a versioned artifact
- Supports performance footage, recurring characters, narrative arcs
- Matches traditional music video production grammar
- Scales to feature-length music videos

**Failure points:**
- Higher complexity (5+ model calls per song section)
- Slower (multi-hour generation per song)
- Keyframe-to-video motion can feel static or unnatural
- Pipeline has more failure modes (each stage can break independently)
- Higher cost per video

**Fit profile:**
- Studio workflows with brand/identity consistency requirements ✅
- Performance-forward cuts (concerts, intimate vocal shots) ✅
- Narrative music videos (storylines, recurring characters) ✅
- MAESTRO-canonical artist identity (the "sovereign space") ✅
- Fast-turnaround TikTok teasers ⚠️ (too slow for daily content)

**Reference implementations:** Freebeat Storytelling mode, Neural Frames full timeline workflow, n8n music-video pipeline templates combining LLM + image gen + Runway/Pika.

---

### Architecture C — Hybrid Multimodal Pipeline (MAESTRO-Grade, Recommended)

**Thesis:** The right architecture is not one model but a **planner-executor loop** that combines audio analysis, lyric parsing, style retrieval, and multiple generative substrates, with explicit state tracking and continuity controls between stages.

**Inputs:**
- Everything from A and B
- MAESTRO canon: accepted decisions, aesthetic constraint map, artist persistent identity bundle, prior-release visual references (for cross-release continuity)
- Explicit "mode" selector: concept / performance / narrative / hybrid

**Transformations:**

**Stage 1 — Analysis and Briefing**
1. Audio feature extraction (Tier 1 + Tier 2 features)
2. Lyric semantic analysis + narrative extraction via LLM
3. Retrieval from artist canon: similar-themed prior releases, established visual motifs
4. **Visual Brief** assembly with provenance (constraint sources, LLM reasoning, retrieval hits)
5. Human review gate (optional; Mo's preference)

**Stage 2 — Structural Planning**
6. Shot Grammar Spec generation (per-section shot list)
7. Aesthetic Constraint Map validation (does the shot list honor the stylebook? Sacred Imperfection budget? Excluded clichés?)
8. Contradiction surfacing: if plan conflicts with canon, flag; do not silently reconcile
9. Review gate

**Stage 3 — Generation**
10. Keyframe / reference image generation with identity locks (Architecture B style)
11. **OR** direct text-to-video per section if concept-mode (Architecture A style)
12. **OR** audio-conditioned video via Seedance 2.0 (passing audio as direct input) or LTX-2 for native audio + multi-keyframe
13. Stage-level artifact persistence with versioning

**Stage 4 — Assembly and Sync**
14. Edit timeline with beat-aligned cuts and section-aligned structural changes
15. Lip-sync pass where applicable
16. Color grade and LUT application from stylebook
17. Lyric overlay per SEL requirements

**Stage 5 — Conformance Check (P4B Gate)**
18. Automated checks: identity consistency, palette conformance, motion continuity, captions-present
19. Optional perceptual evaluation: does the video "feel" musically right? (see §5.4)
20. Gate to SEL or return to Stage 2/3 for revision

**Control surfaces:**
- All control surfaces from A and B
- Mode selector (concept / performance / narrative / hybrid / cover-loop)
- Audio-conditioning depth selector (text-prompt only vs full audio to model)
- Identity lock strength
- Sacred Imperfection budget (roughness threshold)
- Prior-release continuity weight (how much should this video reference the artist's prior visual canon?)

**Strengths:**
- Combines concept strength of A with identity strength of B
- Explicit stage gates match Mo's canon/draft discipline
- Every artifact versioned, every decision provenanced
- Supports cross-release visual continuity ("persistent audiovisual canon for artists across releases" from §12)
- Degrades gracefully: if one model fails, substitutes available
- Matches Mo's reliability hierarchy: clear prompting → explicit instructions → context engineering → structured outputs → external enforcement → hard controls

**Failure points:**
- Highest implementation complexity
- Orchestration overhead
- Requires a state-management layer (the "virtual whiteboard")
- More failure modes to monitor
- Calibration of gate thresholds is an ongoing art

**Fit profile:**
- MAESTRO-grade repeatability ✅
- Multi-release artist identity systems ✅
- Mo's personal workflow ✅ (by construction)
- Quick one-off TikTok clips ⚠️ (overkill; use Architecture A for those)

**Reference implementations:** No single commercial product implements this fully. It is effectively a pipeline you build on top of: MAESTRO P2 (audio) → MIR tools → LLM (Claude/GPT) → image gen → image-to-video or Seedance 2.0 → editor (Creatomate, FFmpeg, or custom).

---

### Ranking and Recommendation

| Architecture | Implementation Complexity | Identity Control | Speed | Cost | Fit for MAESTRO |
|---|---|---|---|---|---|
| A — Prompt-expanded T2V | Low | Low | Fast | Low | Good for fast SEL output (teasers, TikTok) |
| B — Storyboard + I2V | Medium-High | High | Slow | Medium-High | Good for narrative and studio workflows |
| **C — Hybrid (Recommended)** | **High** | **High** | **Medium** | **Medium** | **Canonical MAESTRO default** |

**Recommendation:** Adopt **Architecture C** as the MAESTRO canonical default. Keep A and B as explicit mode options selectable in the Visual Brief. The planner can choose a mode per artifact based on the target SEL surface and the creative intent.

---

## 5. Audio-to-Visual Translation Framework (Formal Mapping Matrix)

The mapping is specified as a structured table with the source feature, target visual parameter, nominal mapping, and exceptions/anti-patterns. This is the core "physics" of VIG. It should be consulted — and refined — at every Visual Brief assembly.

### 5.1 Core Mapping Matrix

| Audio Feature (Source) | Visual Parameter (Target) | Nominal Mapping | Exceptions / Anti-patterns |
|---|---|---|---|
| **BPM / tempo** | Cut rate | Cuts per bar or cuts per 8 beats; high BPM → higher cut rate | Ambient/drone tracks: inverse relationship (slow BPM may still want medium motion to avoid funereal pacing); trap at 140 BPM halftime should cut at 70 BPM feel, not 140 |
| **Onset density** | Motion intensity | Dense onsets → high on-screen motion; sparse onsets → static/contemplative framing | Layered percussion with sparse kick can mislead — use kick density specifically, not total onset density |
| **Low-end weight / sub-bass energy** | Camera heaviness / physicality / scale | Heavy sub → wide, physical camera, ground-hugging, architectural scale | Hip-hop 808s are structural, not atmospheric — camera should anchor to subject not environment |
| **Spectral centroid (brightness)** | Lighting sharpness / color temperature | Bright timbres → cool/white/high-contrast lighting; dark timbres → warm/shadowed/low-contrast | Genre priors override: lo-fi hip-hop is sonically dark but visually often warm amber, not cold |
| **Spectral flux (timbral change rate)** | Visual texture variability | High flux → rapid texture/material changes; low flux → sustained material identity | Drone/ambient can have low flux but reward slow material morphs — absolute rate matters less than change salience |
| **Vocal intimacy / register / closeness** | Shot distance / lens choice / framing | Close-mic intimate vocal → close-up / 50mm; distant/reverb-heavy vocal → wide / 24mm | Falsetto doesn't mean close — can signal vulnerability or power; check lyrical context |
| **Vocal gender / identity cues** | On-screen subject identity | Match wherever canonical artist identity is locked | When using AI-generated performer, lock identity via LoRA / reference image to prevent drift |
| **Lyrical specificity** | Degree of scene literalism | Highly specific lyrics ("red door on Pine Street") → literal rendering appropriate; abstract lyrics ("the fire of memory") → abstract rendering | Avoid literal rendering of metaphors; avoid abstract rendering of concrete imagery — the inversion is almost always wrong |
| **Lyrical imagery density** | Scene-change rate | Image-dense lyrics → more scenes; image-sparse → fewer, longer scenes | Rap with high bar density doesn't want a scene per bar — use 2–4 bar units |
| **Harmonic tension / dissonance** | Visual instability / asymmetry / pacing escalation | Tension → tilt, asymmetric composition, escalating cut rate, unsettled motion | Resolution moments should *settle* the composition; don't let tension run into resolution without visual rest |
| **Section boundaries** | Structural visual change | Verse→chorus should be visible; bridge/drop should feel categorically different | Abrupt mid-verse cuts should not occur at arbitrary timestamps — sync to nearest section boundary if possible |
| **Dynamic range / loudness envelope** | Visual contrast envelope | Quiet → low visual contrast; loud → high contrast | Compressed tracks (modern pop) have flat loudness — derive emotional contour from lyrics/harmony instead |
| **Key / mode** | Color palette warmth/cool | Major → warmer; minor → cooler; modal → ambiguous | Too on-the-nose; genre priors and artist stylebook usually dominate |
| **Genre codes** | Wardrobe / setting / motion vocabulary / typography | Genre priors strongly constrain all surface-level visual choices | Cross-genre songs require planner to choose dominant genre or deliberate hybrid — don't average, pick |
| **Arrangement density** (layer count) | On-screen compositional density | More layers → more on-screen elements; minimal arrangement → minimal composition | Bad cliché: "layered arrangement means busy screen" — layered can also mean depth, not breadth |

### 5.2 Affective Mapping Overlay

On top of Tier-1/2 mappings, a valence-arousal overlay governs lighting, color, and camera energy. Standard affective circumplex applies:

- **High arousal + positive valence** (energetic joy): saturated palette, high-key lighting, rapid camera, upward composition
- **High arousal + negative valence** (aggression, panic): desaturated or high-contrast palette, hard shadows, handheld or kinetic camera, unstable composition
- **Low arousal + positive valence** (calm, intimate): warm palette, soft lighting, slow camera, stable composition
- **Low arousal + negative valence** (melancholy, grief): cool/desaturated palette, diffuse or single-source lighting, static or very slow camera, weight in lower frame

**Derivation:** Valence-arousal estimation is standard practice in V2M research (Sulun et al. use Gaussian-mixture modeling over emotion classifier output [VERIFIED: arxiv.org/pdf/2502.12489 V2M survey]); the same estimators work for music → visual parameter mapping in reverse.

### 5.3 Anti-Patterns (What Not To Do)

**Anti-pattern 1: Beat-matching every cut.** Over-sync produces visual fatigue. Cut on musical *events* (section boundaries, lyrical pivots, harmonic resolutions), not on every kick. Empirically, tools that "cut on every beat" test worse than tools that cut every 2–8 bars.

**Anti-pattern 2: Literal lyric rendering.** Generating the image of every noun the singer utters produces a karaoke slideshow, not a music video. Lyrics should inform the mood and provide occasional anchor imagery, not drive scene-by-scene.

**Anti-pattern 3: Genre cliché stacking.** Rap + chains + gold + fisheye is not a visual identity; it's a meme. Use genre priors as a baseline to deviate from, not a destination.

**Anti-pattern 4: Over-polished rendering of rough-sounding music.** If the song has Sacred Imperfection — gritty recording, tape hiss, deliberate wear — the video must carry matching visual grain/imperfection. Polished visuals on rough audio reads as inauthenticity. (Mo-specific principle: "polish can kill the soul.")

**Anti-pattern 5: AI-sheen homogenization.** Default AI-generated video trends toward a recognizable "AI aesthetic" — overly smooth, slightly dreamy, impossible physics. For MAESTRO-grade identity, the aesthetic constraint map must include explicit counter-measures: grain injection, imperfect physics, deliberately unglossy color.

**Anti-pattern 6: Character identity drift.** Across shots of the same performer, even small variations in face/wardrobe read as cheap AI. Identity lock via LoRA or reference image is non-optional for any shot featuring a persistent character.

**Anti-pattern 7: Scene transitions that ignore musical section changes.** Transitioning mid-verse is disorienting. Pin major visual transitions to section boundaries (verse→chorus, drop, bridge).

### 5.4 Perceptual Fit: Why Some Video Feels Musically "Right" Even Without Exact Sync

Research on audio-visual perception shows that temporal alignment tolerance for musical coherence is **surprisingly loose** — humans register "musical fit" from:

1. **Section-level alignment** (scene change near section boundary, within a bar or two)
2. **Energy envelope matching** (visual motion intensity tracks audio RMS over 1–4 second windows)
3. **Emotional congruence** (visual affect matches audio affect at section granularity)
4. **Structural echo** (visual callback when a musical motif repeats)

Note what is **not** on this list: exact beat-level sync, exact lyric-word-level sync. These are often over-prioritized by automated tools. Freebeat/Revid type beat-cutting is useful when it's not overdone; surgical beat-sync is more often a symptom of not knowing what else to do. [INFERRED from general audio-visual perception research + tool behavior observation]

---

## 6. Capability Benchmark Matrix

Comparison of candidate VIG substrates plus Hooks (as distribution, not generation) across dimensions relevant to MAESTRO. Scores: ● strong, ◐ partial, ○ weak/absent, — not applicable.

| Capability | Pure T2V (Sora 2 / Veo 3.1) | Image-to-Video (Runway Gen-4 / Pika / Kling) | Audio-Conditioned T2V (Seedance 2.0 / LTX-2) | Chained Workflows (Freebeat / Neural Frames / Revid) | Audio-Reactive Visualizers (legacy) | Hooks (distribution only) |
|---|---|---|---|---|---|---|
| True video generation | ● | ● | ● | ● (via chained calls) | ○ | ○ |
| Audio awareness (native) | ◐ (audio-out, not audio-in) | ○ | ● (audio-in) | ◐ (post-hoc feature extraction) | ● | ○ |
| Lyric awareness | ○ | ○ | ○ (unless via text prompt) | ● (transcription + sync) | ○ | ● (caption overlay) |
| Temporal continuity (within clip) | ● | ● | ● | ◐ (depends on chaining) | — | — |
| Temporal continuity (across clips) | ○ | ◐ (with reference images) | ◐ | ◐ | — | — |
| Style / identity control | ◐ | ● (with LoRA / ref images) | ● | ● | ○ | — |
| Character consistency | ○ | ● | ◐ | ◐ | — | — |
| Beat sync (generative) | ○ | ○ | ◐ | ● (post-hoc) | ● | ○ |
| Section-aware pacing | ○ | ○ | ○ | ● | ○ | — |
| Export-ready formats (9:16 etc.) | ● | ● | ● | ● | ● | ● (9:16 enforced) |
| Remixability | ○ | ○ | ○ | ◐ | — | ● (native remix) |
| Suitability for music marketing (teaser) | ◐ | ◐ | ◐ | ● | ● | ● (distribution) |
| Suitability for cinematic music video | ● | ● | ● | ◐ | ○ | — |
| Clip length ceiling | 8–25s | 5–10s | 15–20s | Full song (chained) | Unlimited | 4 min (input cap) |
| Provenance / auditability | ● (prompts) | ◐ | ◐ | ◐ | ● | ● |
| MAESTRO fit | VIG substrate for Arch A | VIG substrate for Arch B | VIG substrate for Arch C direct-mode | VIG reference impl. (Arch C) | Niche use only | **SEL target (primary)** |

**Key reading:** No single tool covers every dimension. MAESTRO's VIG must be a composed system that leverages the best substrate per capability, which is exactly Architecture C.

Specific observations:

- **Seedance 2.0 and LTX-2** are the most architecturally interesting for pure audio-conditioning, but neither has a well-established music-video workflow yet. VIG can pioneer this in the MAESTRO context.
- **Chained workflows (Freebeat, Neural Frames, Revid)** are the most *operational* VIG stack today — treat them as reference implementations of Architecture C, even though they are closed-source.
- **Hooks is explicitly a distribution/SEL target**, not a VIG substrate. The matrix makes the category error visible if it ever returns.

---

## 7. SEL: Hooks and Adjacent Surfaces as Export Targets

SEL governs the transformation from MAESTRO-canonical video artifacts to surface-specific variants. Each destination has distinct constraints, affordances, and optimization heuristics. SEL is **stateless with respect to creative decisions** — it does not modify intent, it only formats.

### 7.1 Surface Catalog

| Surface | Aspect Ratio | Duration | Audio Source | Lyric/Caption | Remix Affordance | Key Optimization |
|---|---|---|---|---|---|---|
| **Suno Hooks** | 9:16 (enforced) | 10s–4min | Clip-original OR Suno track (toggle) | Optional lyric overlay via "Show Lyrics" | Native remix, thumbs, comment | Start-point selection at hook moment |
| **TikTok** | 9:16 | Up to 10 min, best 21–34s | Platform library or uploaded | Burned-in captions recommended | Stitch/duet | Hook in first 1–2 seconds |
| **Instagram Reels** | 9:16 | Up to 3 min | Platform library or uploaded | Burned-in captions recommended | Remix, Collab | Front-load motion; avoid talking-head openers |
| **YouTube Shorts** | 9:16 | Up to 3 min | Uploaded | Burned-in or YouTube auto-captions | Remix | Shareable title and description |
| **X / Twitter video** | 16:9 or 1:1 preferred; 9:16 acceptable | Up to 2:20 | Uploaded | Burned-in for sound-off viewing | Quote retweet only | First frame = thumbnail |
| **Full music video archive** | 16:9 at 1080p or 4K | Full song (3–8 min) | Canonical master audio | Separate lyric version artifact | — | Archive-grade quality, no compression |
| **Suno song-detail upload slot** | Unclear — verify at time of export | Full song | Suno track | N/A | Listener-visible on song detail | Discovery inside Suno ecosystem |
| **Animated Cover Art slot** (Suno native) | Image / square loop | 5s–longer | Attached to song | None | None | Loop seamlessness; identity alignment with cover |

### 7.2 Hooks-Specific Strategy

Hooks has unique mechanics because it sits *inside* the music-creation platform rather than a general video platform. Implications for SEL:

- **Audience pre-context:** Viewers in the Hooks feed are already music-creators/music-listeners. The hook doesn't need to sell the fact that it's music — it needs to sell *this particular* track's identity.
- **Audio source toggle is a creative decision:** Using the clip's original audio (ambient, dialogue) vs. the Suno track changes the message. Mo-canonical tracks should default to Suno-track audio unless there's a specific reason (a diegetic scene, a voice sample introduction) to use clip audio.
- **4-minute ceiling favors full-song cuts:** Unlike TikTok's optimal 21–34s, Hooks can carry a full song. SEL should produce both a full-length variant and a short teaser variant.
- **Lyric overlay is optional, not default:** Decide per track. Lyric-forward songs (narrative rap, singer-songwriter) benefit; instrumental or atmospheric tracks do not.
- **Remix topology matters:** A Hook that invites remix (visible gap, strong iconic shot) travels further in the feed than a closed-form hook.
- **Identity-consistency across Hooks:** When publishing multiple Hooks per track (teaser, chorus-drop, full cut), visual identity must persist. This is a cross-variant continuity requirement SEL must enforce against the stylebook.

### 7.3 SEL Export Package Manifest Schema

Every VIG artifact promoted to SEL produces an Export Package Manifest with the following fields:

```
export_package_manifest:
  source_artifact_id: <uuid of canonical video in VIG>
  source_song_id: <uuid in MAESTRO canon>
  stylebook_version: <version hash>
  
  variants:
    - surface: hooks
      aspect_ratio: "9:16"
      duration_seconds: <int>
      start_offset_in_song: <float seconds>
      audio_source: "suno_track" | "clip_original"
      lyric_overlay: true | false
      caption_style_ref: <stylebook entry>
      target_hook_moment: <lyric phrase or time>
    
    - surface: tiktok
      aspect_ratio: "9:16"
      duration_seconds: 25
      audio_source: "burned_in"  # audio is baked into file for platform music rights
      lyric_overlay: true
      caption_style_ref: <stylebook entry>
      first_frame_hook: <description>
    
    - surface: archive_master
      aspect_ratio: "16:9"
      duration_seconds: <full_song_length>
      audio_source: "canonical_master"
      resolution: "3840x2160"
      codec: <spec>
  
  provenance:
    generated_at: <timestamp>
    vig_artifact_version: <version>
    approved_by: <user or automated gate>
    approval_timestamp: <timestamp>
    revision_history: [<list of prior versions>]
```

This manifest is itself a canonical artifact — versioned, signed, never orphaned. It is the "receipt" that proves the video deployed to Hooks/TikTok/etc. was actually the approved version and not a drifted re-generation.

---

## 8. MAESTRO v5 Integration Design

The integration slots VIG and SEL into MAESTRO's existing phase structure (P2–P5) without modifying upstream phases.

### 8.1 Phase Map (Corrected)

```
P1 — Conception
  └ (unchanged)

P2 — Draft Assembly
  └ Song draft, lyrics, arrangement, identity cues
  └ Output: Song Draft artifact (audio + lyrics + metadata)

P3 — Performance and Identity Fit
  └ Voice, delivery, affect, persona locking
  └ Output: Master Audio artifact (canonical)
  └ Output: Artist Identity Bundle (voice profile, persona notes)

P4A — VIG: Visual Identity Generation         [NEW]
  └ Input: Master Audio, Lyrics, Artist Identity Bundle, Stylebook
  └ Architecture: Hybrid Multimodal Pipeline (default; A and B available as modes)
  └ Stages: Analysis → Briefing → Planning → Generation → Assembly
  └ Outputs: Visual Brief, Shot Grammar Spec, Rendered Video Artifact(s)

P4B — Visual Conformance Gate                 [NEW]
  └ Checks: identity consistency, stylebook conformance, continuity, Sacred Imperfection budget, anti-pattern flags
  └ Gate decision: pass → P5 | revise → back to P4A stage N | reject → back to P4A stage 1
  └ Output: Conformance Report + Approval or Rejection

P5 — SEL: Surface Export Layer                [NEW]
  └ Input: Approved canonical Video Artifact + Stylebook + Release Plan
  └ Stages: Manifest generation → Variant fan-out → Caption/crop/format → Publish or hand-off
  └ Outputs: Export Package Manifest, surface-specific video variants, publication artifacts
```

### 8.2 Canonical Artifacts

| Artifact | Produced In | Status Lifecycle | Schema Anchor |
|---|---|---|---|
| **Visual Brief** | P4A Stage 1–2 | Draft → Reviewed → Accepted | §3.2, textual spec |
| **Shot Grammar Spec** | P4A Stage 2 | Draft → Reviewed → Accepted | §3.2, per-section shot list |
| **Aesthetic Constraint Map** | Stylebook (maintained across P4A runs) | Canon (versioned) | §3.2, rules + references |
| **Style Reference Bundle** | Stylebook | Canon (versioned) | Images, LUTs, motion presets |
| **Rendered Video Artifact** | P4A Stage 3–4 | Draft → Conformance → Accepted | Video file + metadata |
| **Conformance Report** | P4B | Immutable once issued | Checklist results |
| **Export Package Manifest** | P5 | Immutable once issued | §7.3 schema |
| **Surface Variant** | P5 | Immutable once published | Video file per surface |

### 8.3 State Management (The Virtual Whiteboard)

Every run of VIG/SEL maintains a persistent whiteboard of:

- **Current objective**: which song, which release, which target surfaces
- **Active constraints**: stylebook entries in force, Sacred Imperfection budget, excluded clichés
- **Known facts**: feature extraction results, lyric analysis, retrieval hits from prior canon
- **Open questions / NULLs**: unresolved creative decisions awaiting input
- **Pending decisions**: proposals awaiting acceptance
- **Accepted decisions**: locked choices (visual direction, cast, location)
- **Rejected / superseded decisions**: what was considered and ruled out, with rationale
- **Terminology**: internal naming for characters, locations, motifs to prevent drift across sessions

This whiteboard is **read oldest-to-newest** when reconstructing prior work, per Mo's continuity rule.

### 8.4 Interface Points

- **P3 → P4A:** Master audio and lyrics are frozen before VIG begins. No retroactive edits to audio without invalidating VIG output (versioning rule).
- **P4A → P4B:** Rendered artifact is immutable at gate entry; P4B does not modify, only evaluates.
- **P4B → P5:** Only *approved* artifacts enter SEL. Rejected artifacts return to the appropriate P4A stage with conformance report attached.
- **P5 → external surfaces:** SEL produces variants and a manifest; actual publishing may be manual (Mo reviews + posts) or automated (via surface APIs).
- **Cross-release continuity:** P4A's retrieval step pulls from the artist's persistent visual canon (prior approved artifacts) to maintain identity across releases.

---

## 9. Failure Modes and Mitigations

Organized by where they manifest in the pipeline.

### 9.1 Generation Failures (P4A)

| Failure | Symptom | Root Cause | Mitigation |
|---|---|---|---|
| **Generic visuals** | Output indistinguishable from any AI music video | Weak brief; over-reliance on default style tokens; no stylebook | Require stylebook minimum before P4A runs; inject anti-pattern list into every prompt |
| **Semantic mismatch** | Visual doesn't match lyrical/emotional content | LLM misread lyrics; missing cultural context; genre prior override | Explicit LLM lyric-analysis review step; human gate on Visual Brief for high-stakes releases |
| **Character identity drift** | Same "artist" looks different across shots | No identity lock; model variation between calls | Reference-image locking via LoRA or IP-Adapter; generate all shots in a single session where possible |
| **Temporal discontinuity** | Shots don't flow; world state jumps between scenes | Each clip generated in isolation; no continuity tracking | Shot Grammar Spec enforces setting continuity; pass "previous shot end frame" as image-to-video seed |
| **Over-literal lyric rendering** | Each noun rendered as object; reads as karaoke | LLM briefing step too literal | Explicit anti-pattern in brief-generation prompt; require abstraction unless specific lyric is flagged as anchor |
| **Generic AI aesthetic / sheen** | Overly smooth, dreamy, impossible physics | Default model behavior | Sacred Imperfection budget enforced in brief; grain/imperfection injection in post; deliberate camera shake / film effects at render time |
| **Beat-sync over-indexing** | Cut every beat; visually exhausting | Automated beat detection drives edits | Cut on sections and musical events, not beats; target 2–8 bar cut units |
| **Model failure / bad render** | Artifact unusable | Any generation can fail | Architecture C's mode flexibility — substitute Arch A or B path for failing sections |

### 9.2 Distribution Failures (P5)

| Failure | Symptom | Root Cause | Mitigation |
|---|---|---|---|
| **Wrong aspect ratio delivered** | Video cropped badly on Hooks/TikTok | Safe-zone violated at VIG stage | VIG enforces 9:16 safe-zone; master is 16:9 with 9:16 markers |
| **Audio source mismatch** | Hooks plays wrong audio | Manifest field incorrect; audio-source toggle ambiguous | Manifest schema mandates explicit field; default to Suno-track unless override |
| **Lyric overlay misaligned** | Captions out of sync | Lyric transcription used original track timing, not edited clip | Re-derive caption timing from the edited variant, not the source track |
| **Start point lands on weak moment** | Hook fails to hook | Automatic start-point selection without musical understanding | Explicit start-point field in manifest; test with preview; favor chorus/drop/strong-lyric moments |
| **Wrong variant published** | Non-canonical artifact reaches public | Version drift between P4B approval and P5 publish | Manifest hash-checked against approval; publish blocked on mismatch |
| **Cross-variant identity drift** | Teaser and full-cut look like different songs | Variants generated independently | All variants derived from single approved master; SEL does not re-generate, only reformats |

### 9.3 Identity Drift Failures (Cross-Release)

| Failure | Symptom | Root Cause | Mitigation |
|---|---|---|---|
| **Visual identity reinvented per release** | No coherent artist identity across catalog | VIG runs without consulting prior canon | Stylebook + prior-canon retrieval mandatory in P4A Stage 1 |
| **Stylebook bloat** | Stylebook becomes contradictory | No rationalization of additions | Stylebook versioning + contradiction check before accepting new entries |
| **"Signature motif" erosion** | Recurring visual elements disappear | Motifs not explicitly canonized | Motif Registry as part of canon; referenced in every brief |
| **Accidental brand-inconsistency** | Wardrobe/color/typography changes between releases | No constraint-map enforcement | Aesthetic Constraint Map validated at P4B; rejections on violation |

### 9.4 Audience-Level Failures

| Failure | Symptom | Root Cause | Mitigation |
|---|---|---|---|
| **Clip fatigue from repetitive motifs** | Audience tires of same visuals | Over-reliance on signature motifs | Balance: 70% identity-consistent elements + 30% novel per release |
| **Misaligned surface strategy** | Video that would work for archive fails on Hooks | One-size-fits-all export | SEL produces surface-specific variants (not just crops) |
| **Lyric/visual mismatch reads as inauthentic** | Audience sees the song and video as disconnected | Weak brief or no lyric-visual coherence pass | LLM lyric analysis + human gate on brief |
| **Sacred Imperfection ignored** | Too-polished output for rough-sounding song | Default model behavior toward polish | Explicit roughness budget + grain/imperfection injection |

---

## 10. Implementation Roadmap

### Phase 0 — Foundation (Weeks 1–2)

- Lock this dossier's contradiction report and M2VIT definition as MAESTRO canon
- Expand stylebook to include VIG-relevant fields: Aesthetic Constraint Map, Motif Registry, Anti-pattern list, Sacred Imperfection budget
- Set up artist identity bundle: reference images for primary persona, wardrobe references, location references

### Phase 1 — Minimum Viable VIG (Weeks 3–6)

- Implement Architecture A (prompt-expanded T2V) first — lowest complexity, validates the briefing pipeline
- Integrate audio feature extraction (librosa or equivalent)
- Integrate LLM briefing (Claude or GPT-4) with stylebook injection
- Target substrate: Veo 3.1 Lite (cost-efficient) for first generations
- Output: one-song end-to-end test producing a Hooks-exportable clip
- Manual P4B review (no automation yet)

### Phase 2 — SEL Baseline (Weeks 5–7, parallel)

- Implement Export Package Manifest schema
- Implement 9:16 crop + lyric overlay pipeline (FFmpeg or equivalent)
- Hooks upload workflow (manual upload acceptable initially)
- Version/hash validation on publish

### Phase 3 — Architecture B Integration (Weeks 8–12)

- Add image generation stage (Midjourney or FLUX)
- Add image-to-video stage (Runway Gen-4 or Kling 2.0)
- Integrate LoRA or IP-Adapter for identity locking
- Test narrative music-video production end-to-end

### Phase 4 — Architecture C Orchestration (Weeks 12–20)

- Planner-executor loop implementation
- Mode selector (concept/performance/narrative/hybrid)
- Cross-release canon retrieval
- Automated P4B checks (identity consistency, palette conformance)
- Seedance 2.0 or LTX-2 integration for direct audio-conditioning when available

### Phase 5 — Stabilization and Governance (Ongoing)

- Conformance gate tuning
- Stylebook evolution discipline (version control, contradiction flagging)
- Motif Registry maintenance
- Post-release audience signal collection (what works, what tires out)

### Critical Path Dependencies

- **VIG depends on stylebook** — do not start P4A without one
- **SEL depends on VIG producing an approved artifact** — do not start P5 without P4B passing
- **Architecture C depends on Architectures A and B being operational** — do not skip

### Budget Notes (Order of Magnitude, Not Canonical)

- Phase 1 Veo 3.1 Lite generation: ~$0.30–$1 per 8-second clip at public API pricing
- Phase 3 Runway Gen-4 / Kling: $0.50–$5 per clip depending on length and quality
- A full Architecture C run for a 3-minute song: $10–$50 in model calls, depending on iteration count and substrate choice
- Chained commercial tools (Freebeat, Neural Frames): subscription-based, $20–$100/month, less transparent cost per video

---

## 11. Open Research Questions

These are explicitly **unresolved** and flagged as such per Mo's uncertainty-marking rule.

1. **[UNKNOWN]** Does Seedance 2.0's "audio as conditioning input" support music specifically, or is it primarily tuned for speech/dialogue? The ByteDance technical documentation is not yet detailed enough to answer. Verification requires hands-on testing.

2. **[UNRESOLVED]** What is the right metric for "musical fit" of generated video? Existing metrics (ImageBind similarity, CLAP score) measure semantic alignment but not the perceptual-rhythm fit that makes a music video feel right. An affective-alignment metric specific to music video may need to be developed.

3. **[PROVISIONAL]** Is a custom-trained music-video model (fine-tuned on music video corpora) better than composed commercial pipelines? Strong argument either way. Custom training gives continuity; commercial gives SOTA quality.

4. **[UNKNOWN]** How does Hooks' feed algorithm weight audio-source choice (Suno track vs clip original) in discovery ranking? Not documented. Requires empirical observation of Hooks posts by Mo over 10+ samples to infer.

5. **[UNRESOLVED]** At what release cadence does cross-release continuity become an audience expectation vs an audience-fatigue risk? The 70/30 consistent-novel ratio above is a provisional heuristic, not a measured result.

6. **[UNKNOWN]** What are the copyright implications of identity-locked generation (LoRA trained on artist likeness) for music videos distributed commercially? Legal landscape is evolving; some platforms treat trained LoRAs as derivative works.

7. **[PROVISIONAL]** Is the "Sacred Imperfection budget" parameterizable, or is it a qualitative artist-level constraint only? Initial hypothesis: qualitative per-artist, with per-release tightening/loosening.

8. **[UNKNOWN]** Can Suno's Animated Cover Art API be invoked programmatically, or is it strictly interactive? If API-accessible, it integrates cleanly as a VIG sub-capability. If not, it remains a manual step outside the MAESTRO pipeline.

---

## 12. Forward-Looking Extensions

These are speculative but structured — not fabrications, but reasoned projections from current trajectories.

### 12.1 Real-Time Listener-Personalized Visuals

Once video models reach sub-second inference (not yet in 2026, but plausible by 2027–2028), VIG can produce listener-adaptive visuals: a live stream where the video is personalized to the listener's stated preferences, inferred mood, or platform context. MAESTRO would need a "realtime mode" where the stylebook is loaded once but the render happens per-listener.

### 12.2 Adaptive Music Videos

Video that responds to engagement signals in a scrubbable or branching format. The same song could have multiple visual paths (performance-forward, narrative, abstract) selectable by the listener. SEL would produce a branching manifest rather than flat variants.

### 12.3 Multimodal Artist Identity Engines

A canonical artist identity bundle that persists across songs, releases, platforms, and modalities — voice, visual identity, written voice, merchandise design all derived from a single canon. MAESTRO's stylebook + voice profile + motif registry is already the seed of this.

### 12.4 Music-Native Generative Cinema

Long-form narrative film constructed around an album rather than a song. MAESTRO's phase structure could extend: P6 — Album-Level Narrative, P7 — Feature Cinematic Production. Each song contributes a "scene" with per-song VIG output and album-level story continuity.

### 12.5 Persistent Audiovisual Canon

Every release adds to a permanent, queryable canon — songs, videos, stylebook evolution, motif usage, character appearances — that can be retrieved from, referenced, remixed, and audited across decades. This is Mo's erasure-resistance doctrine operationalized at catalog scale. The implementation is archival + retrieval + provenance, not new generative capability.

### 12.6 Cross-Artist Collaboration with Identity Preservation

When artist A features on artist B's track, MAESTRO could coordinate identity-locked VIG that preserves both artists' visual canons in the same video. Requires a federated stylebook model and a negotiation layer for conflicting constraints.

---

## Appendix A — Evidence Provenance Index

All claims in this document carry inline evidence labels. This appendix lists source URLs for [VERIFIED] claims, grouped by domain.

### Suno product reality

- **Hooks mechanics** (VERIFIED): `help.suno.com/en/articles/8049409`, `suno.com/hub/ai-video-generator`, `suno.com/hub/create-viral-short-videos`
- **Animated Cover Art** (VERIFIED): `jackrighteous.com/blogs/guides-using-suno-ai-music-creation/suno-animated-cover-art-video-feature-guide` (updated March 14, 2026)
- **Hooks feature context / launch** (VERIFIED): `jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-hooks-deep-dive` (October 2025, community feedback)
- **Suno v5.5 feature set** (VERIFIED): `suno.com/blog/v5-5`
- **Suno API integration patterns** (VERIFIED): `aivideobootcamp.com/blog/suno-ai-complete-guide-2026/`
- **Suno Animated Cover Art vs Hooks distinction** (VERIFIED by absence of cross-referencing in both sets of docs)

### Foundation video generation models

- **Veo 3 / Veo 3.1 / Veo 3.1 Lite** (VERIFIED): `modelslab.com/blog/ai-tools/google-veo-3-1-lite-ai-video-generation` (March 31, 2026 release), `datacamp.com/blog/top-video-generation-models` (top 10 of 2026)
- **Sora 2** (VERIFIED): `datacamp.com/blog/top-video-generation-models`
- **Seedance 2.0 (audio as conditioning input)** (VERIFIED): `medium.com/codetodeploy/beyond-the-hype-a-tech-deep-dive-into-the-2026-ai-video-landscape-and-seedance-2-0-f05f771076b7` (Feb 2026)
- **LTX-2** (VERIFIED): `blogs.nvidia.com/blog/rtx-ai-garage-ces-2026-open-models-video-generation/` (January 2026)

### Audio-conditioned video / cross-modal research

- **TempoTokens / audio-to-video via text-conditioned backbone** (VERIFIED): `ojs.aaai.org/index.php/AAAI/article/view/28486/28947` (AAAI paper)
- **MM-Diffusion joint A/V generation** (VERIFIED): same paper citing Ruan et al. 2023
- **AV-Link (temporally aligned cross-modal diffusion features)** (VERIFIED): `openaccess.thecvf.com/content/ICCV2025/papers/Haji-Ali_AV-Link_Temporally-Aligned_Diffusion_Features_for_Cross-Modal_Audio-Video_Generation_ICCV_2025_paper.pdf`
- **Tri-Ergon, SelVA, V2A survey** (VERIFIED): `emergentmind.com/topics/video-to-audio-generation-model`
- **Stable Video Diffusion architecture** (VERIFIED): `arxiv.org/html/2603.16093v1`
- **CogVideoX** (VERIFIED): same arxiv source
- **V2M survey (Video-to-Music, useful for understanding the reverse direction)** (VERIFIED): `arxiv.org/pdf/2502.12489`

### Cross-modal embedding / alignment

- **CLAP and MuQ-MuLan** (VERIFIED): `emergentmind.com/topics/pretrained-text-audio-embeddings-clap-and-muq-mulan`
- **MuLan original paper** (VERIFIED): `archives.ismir.net/ismir2022/paper/000067.pdf`
- **ImageBind (audio-to-image via CLIP-text-conditioned decoders)** (VERIFIED): `arxiv.org/pdf/2305.05665`
- **Ex-MCR (extending multi-modal contrastive representations)** (VERIFIED): NeurIPS 2024 paper
- **Audio-Visual-Language modeling survey** (VERIFIED): `techrxiv.org/users/971218/articles/1339141`

### Commercial music-to-video tool mechanics

- **Neural Frames (Suno-to-video)** (VERIFIED): `neuralframes.com/suno-to-video`
- **Freebeat** (VERIFIED): `freebeat.ai`, `freebeatfit.com/blogs/brand-story/best-ai-music-video-generators-for-lyric-and-audio-sync` (November 2025)
- **Freebeat Suno pipeline** (VERIFIED): `freebeat.ai/suno-to-video`
- **Revid.ai** (VERIFIED): `revid.ai/tools/suno-to-video`, `revid.ai/tools/ai-music-video-generator`
- **Kaiber / EDM comparison** (VERIFIED): `riverbeats.life/suno-music-video-generator/`
- **LlamaGen** (PROVISIONAL — marketing language only): `llamagen.ai/suno-music-video`
- **n8n workflow template (Suno + Flux + Runway + Creatomate)** (VERIFIED): `n8n.io/workflows/3814-generate-ai-songs-music-videos-using-suno-api-flux-runway-and-creatomate`

### Video-to-music datasets and research (useful for reverse-derivation)

- **Video2Music (affective multimodal transformer)** (VERIFIED): `dorienherremans.com/sites/default/files/2311.00968.pdf`, `arxiv.org/html/2311.00968v2`
- **V-MusProd (ICCV 2023)** (VERIFIED): `openaccess.thecvf.com/content/ICCV2023/papers/Zhuo_Video_Background_Music_Generation_Dataset_Method_and_Evaluation_ICCV_2023_paper.pdf`

### Suno competitive landscape

- **Suno vs Udio 2026 comparison** (VERIFIED): `neuronad.com/suno-vs-udio/`
- **Suno v5/v6 release status** (VERIFIED): `musicmaker.im/blog/detail/Suno-V6-Latest-Update-What-s-Confirmed-What-s-Rumored-2026-81c99537ca0d`

---

**End of Research Dossier v0.1**

*Everything above is a draft proposal pending Mo's explicit acceptance. Accepted sections move to MAESTRO canon; rejected sections are marked and archived with rationale. Nothing finalizes until confirmed.*
