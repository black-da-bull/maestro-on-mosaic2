```markdown
# MoMoney_Maestro_OS_Knowledge_Base_Heuristics.md

## MoMoney Maestro OS v4.5.1 — Knowledge Base and Heuristics

This document centralizes extracted insights, decision logic, and guidelines that inform the MoMoney Maestro OS's operations. It serves as an internal knowledge base, enabling the OS to learn from its history and apply contextual intelligence, as specified in `MoMoney_Maestro_OS_System_Prompt.md`.

---

### SECTION 1: VIRAL-5 STRATEGIC OVERLAY

The VIRAL-5 framework guides every tactical step to optimize for market penetration and longevity.

*   **1. FIT:** (Phase 1: Blueprinting & Narrative Design)
    *   **Objective:** Ensure the core concept aligns with genre, platform, and audience expectations.
    *   **Heuristics:**
        *   Define Title + Emotional Intent (theme & payoff) before writing.
        *   Emotion = Constraint: Treat emotional arcs as structural design rules.
        *   Mode Separation: Songs ≠ raps. Activate SongCouncil vs RapCouncil depending on mode.
        *   Reflect lived truth or narrative consistency across all verses.
        *   Match vocal energy to production cues for emotional coherence.
*   **2. HOOK:** (Phase 3: Revision, Assembly & Production Embedding)
    *   **Objective:** Craft compelling, memorable elements that capture attention quickly.
    *   **Heuristics:**
        *   Aggressively shorten Intro for 'Primary Cut' (streaming optimized, 3-5 sec grab, hook by 7-9 bars).
        *   Chorus = memory anchor + emotional payoff.
        *   Rewrite sections flagged for lack of payoff or emotional drift.
        *   Always close with a reflective or payoff moment unless intentionally unresolved.
        *   Use scorecards (1–10) to evaluate lyrics by structure, emotional weight, and authenticity.
*   **3. PROOF:** (Phase 4: Generation & Feedback / Phase 7.5: Cross-Domain Iteration)
    *   **Objective:** Validate the creative output's authenticity, impact, and technical viability.
    *   **Heuristics:**
        *   HPA (Human Perception-of-Authenticity) metric is paramount.
        *   Consensus Sprints with specialized agents ensure rigorous review.
        *   Technical Audit (VAL/QUINN Gates) ensures structural and quality compliance.
        *   Sacred Imperfection: Intentional flaws (grit, noise, human error) are technically controlled and strategically placed, not sterile.
*   **4. LIFT:** (Phase 8: Archival & Rights Management)
    *   **Objective:** Prepare assets for broad distribution and maximize revenue potential.
    *   **Heuristics:**
        *   IP Dossier Assembly: Compile final Blueprint, Session Ledger, HPA reports, final prompts, and master audio.
        *   Rights & Revenue Wiring: ISRC-ready metadata, `rev_split` mapping.
        *   Functional Production Notes: Styling tags must directly shape AI audio output.
*   **5. COMPOUND:** (Phase 9: Strategic Rollout)
    *   **Objective:** Turn a single track into a sustainable asset, expanding its reach and longevity.
    *   **Heuristics:**
        *   Platform-Specific Content Generation: Analyze for memetic moments, brainstorm TikTok trends, Reels, Shorts.
        *   Asset Compounding: Leverage Remix Blueprints (instrumentals, acapellas, alt takes, visualizers).
        *   Unhinged Multiverse: Tracks are fragments of a larger narrative, inviting audience co-creation and intertextuality.

---

### SECTION 2: HISTORICAL INSIGHTS LOG (Summary)

This section summarizes key learnings and process evolutions derived from historical chat sessions (Phase 0.1).

*   **Prime-Directive Format Enforcement:** Strict Suno v4.5 format is critical; evolution from `v2.5` to `v4.5.1` solidified precise metacontainer naming, character budgets, and the `LYRICS BLOCK` structure.
*   **Dual-Output Strategy:** The necessity of distinct "Primary Cut (Streaming Optimized)" and "Director's Cut (Extended Play)" prompts for market viability.
*   **Artifact Compression Logic:** Techniques for optimizing prompt length (moving repeats to metacontainers, using shorthand) are vital.
*   **Musical V&V (Council Edits):** The iterative nature of SME Round-Robin debates and micro-patch application is essential for quality.
*   **Tactical Mix Cues:** Embedding specific production directives (e.g., `mono kick/sub`, `dark plate on hooks`, `phone scene mono 200–5 kHz`) directly into prompts.
*   **Recursive Outlining/DSRP (Meta-Workflow):** The process of analyzing system components and relationships itself became a core OS capability.
*   **Modular Documentation:** The current structure of self-contained, interlinked Markdown files is the culmination of this learning.
*   **AI Correction & Adaptation:** The system's ability to correct its own assumptions (e.g., file access, syllable count enforcement, SFX placement) is paramount for process integrity.

---

### SECTION 3: SYSTEM DELTA REPORT (Summary of OS Evolution)

This section provides a high-level overview of how the MoMoney Maestro OS has evolved (Phase 0.2).

*   **From USTF to Strict Container:** Evolution from a generic Universal Song Template Framework to the highly specific `Suno v4.5 Strict Container` format.
*   **Metacontainer Consolidation:** `[Voice]` and `[CREW_TAGS]` merged into `[VocalPersona]`; `[Style]` renamed to `[AestheticIntent]`.
*   **Road-Map Simplification:** Transitioned from timed blocks to sequence-only, with bar durations embedded in `LYRICS BLOCK` headers.
*   **Introduction of Granular Lyrical Constraints:** Explicit enforcement of `6-11 syllable count` and precise `SFX placement` within `LYRICS BLOCK`.
*   **Formalization of Agent Personas:** Detailed definitions for all internal and external agents (`Chief System Architect`, `DJ Mo Money`, `MixMaster_Ghost`, `AI_Arranger.vx4`, `LyricForgeGPT`, `RapCouncil` members, etc.).
*   **Unhinged Multiverse Integration:** Elevation of this narrative framework to a core OS component, guiding creative and marketing strategies.
*   **Workflow Formalization:** Transition to a deterministic `Node-Edge Taxonomy` (N0-N9) and a `Framework Orchestrator` with dynamic strategy selection.
*   **Enhanced V&V Gates:** `VAL` (Structural) and `QUINN` (Quality) validators now include granular checks for lyrical and technical compliance.

---

### SECTION 4: DECISION TREE LOGIC FOR REVISIONS

This logic guides the system in proposing revisions based on `Session Ledger` entries (Phase 3.1).

*   **IF** `Consensus Gap` (Phase 2.1) is identified **AND** `DJ Mo Money` requests refinement **THEN** propose micro-patches targeting identified gaps.
*   **IF** `VAL_Report` (Phase 2.2) shows `fail` or `warn` on `lyric.line.syllable_count` or `lyric.line.sfx_placement` **THEN** rephrase lyrics for syllable count compliance or adjust SFX formatting.
*   **IF** `HPA_Score` (Phase 4.2) is below threshold **THEN** identify specific sonic issues from `HPA_Report.rationale` and apply targeted `micro-patch` to `[Timbre]` or `[Performance]` metacontainers.
*   **IF** `Cross-Domain Iteration` (Phase 7.5) identifies high-priority conflicts **THEN** loop back to the earliest relevant phase (Phase 1.2/1.3/1.4 for re-blueprinting, Phase 3.1/3.2/3.3 for re-prompting, or Phase 6 for re-generation).

---

### SECTION 5: HUMAN STRUGGLE INJECTION (HSI) TECHNIQUE

This technique enhances lyrical authenticity during revisions (Phase 3.1).

*   **Objective:** Embed raw, relatable human experience into lyrics to elevate emotional depth and authenticity.
*   **Truth Fragments:**
    *   **Origin:** The root cause of the emotional state (e.g., "dirt roads to juke joints").
    *   **Scar:** The lasting impact or visible wound of the struggle (e.g., "Every scar’s a secret I keep").
    *   **Choice:** The active decision made in the face of adversity (e.g., "I found heaven in that six-string coil").
    *   **Cost:** The price paid for that choice or struggle (e.g., "This fog ain’t mercy—it’s a curse").
*   **Application:** When rephrasing or generating lyrics, ensure these fragments are subtly woven in, making the narrative more visceral and relatable.

---

### SECTION 6: QUINN (QUALITY) VALIDATOR SPECIFIC CHECKS

Detailed checks for sonic quality (Phase 2.2).

*   `low.sub.separation`: Ensures clear distinction between kick and sub-bass frequencies, preventing mud. (Addressed by `prod.sidechain_kick_bass_synths`).
*   `vocal.presence.window`: Optimizes vocal clarity and forwardness in the mix. (Addressed by `vocal.tone.close_mic_forward_plus2dB_vs_band_de_essed`).
*   `fx.tension.curve`: Evaluates how effects contribute to emotional tension and narrative. (Addressed by explicit FX directives like `echo_delay_ping_pong.jumbled_memory` and `spiritual_punctuation`).

---

### SECTION 7: CREATIVE/STRUCTURAL INSIGHTS (InsightSynthesizer Module)

Core principles guiding creative and structural decisions.

*   **Unspoken Objective:** Build a meta-musical operating system (logic + content).
*   **Emotion = Constraint:** Treat emotional arcs as structural design rules.
*   **Mode Separation:** Songs ≠ raps. Activate **SongCouncil** vs **RapCouncil** depending on mode. (RapCouncil is default).
*   **Dual Purpose Sections:** `[Verse]` = rhythm + narrative pivot. `[Chorus]` = memory anchor + emotional payoff.
*   **Functional Production Notes:** Styling tags (e.g., `[Falsetto Whisper]`) must directly shape AI audio output.

---

### SECTION 8: ORCHESTRATION HINTS (Practical)

Practical tips for efficient workflow execution.

*   Use `ToT` for A/B/C drafts to explore multiple creative paths.
*   Run `Self-Consistency` on conflicting variants to resolve ambiguities.
*   Keep `Compression Engine` aggressive to manage character budgets.
*   Always bind a `Persona` to provide context and voice to the output.

---

### SECTION 9: MUSICAL REFLECTION HEURISTICS

Heuristics applied while converting raw ideas into structured prompts.

*   **Prosody before harmony:** Ensure lyrical rhythm and natural speech patterns are prioritized.
*   **Contrast architecture:** Build dynamic shifts between sections.
*   **Unity/variety balance:** Maintain thematic consistency while introducing fresh elements.
*   **Hook intelligibility:** Ensure the main hook is clear and impactful.
*   **Sub management:** Maintain clean low-end frequencies.
*   **Story fidelity:** Ensure the narrative remains true to the original intent.

---

*(This document is interlinked with `MoMoney_Maestro_OS_System_Prompt.md`, `MoMoney_Maestro_OS_Personas_and_Teams.md`, `MoMoney_Maestro_OS_Framework_and_Workflows.md`, and `MoMoney_Maestro_OS_Templates_and_Schemas.md`.)*
