# KNOWLEDGE SPINE — Maestro v5-b (Cold Start) — v5-b.coldstart.1

# Knowledge Spine — Maestro (v5-b)

## 1. The Evidence Contract (Atom 3)

The Evidence Contract is the primary defense against "hallucinated" constraints and aesthetic drift. It ensures that every technical decision is rooted in either the artist's original intent or the physical laws of musical arrangement. In v5-b, a claim without a binding is treated as a system error.

- **Rule of One:** Each subkey value must be exactly one sentence. This forces the SME to be concise and prevents "scope creep" within a single data point. Multiple constraints must be broken into separate subkeys (e.g., THY.K1.S1 and THY.K1.S2) to maintain granular addressability and auditability during Phase 3 meetings.
    
- **Binding Requirement:** Every value must cite its source. This creates a logical chain from raw intent to final prompt, ensuring the prompt is "built" rather than "guessed."
    
    - **Creative UST Binding:** e.g., `binds:STY.K1` ensures a timbre choice supports the established genre.
        
    - **Raw Binding:** e.g., `raw:L4` proves a vocal delivery choice responds to a specific line of the artist's input (e.g., a line about a whisper requiring a `[whispery]` tag).
        
    - **Downstream Binding:** e.g., `binds:THY.K2` justifies a mix choice based on harmonic density or frequency masking.
        
- **Downstream Sensitivity:** Owners must predict the impact of their constraint. This creates a "predictive audit" where SMEs must justify why their constraint is necessary for the track's survival.
    
    - _Example:_ "If [tempo] exceeds 140 BPM, then [vocal_articulation] must transition from legato to staccato to maintain intelligibility against the transient density."
        
    - _Implication:_ Failure to account for this sensitivity results in "muffled" or "rushed" AI generations where the transformer fails to prioritize the correct audio features.
        
- **Exclusion Logic:** Fills must not only state what _is_ present but what is _forbidden_. This narrows the AI's "hallucination window" by establishing negative constraints.
    
    - _Example:_ "To maintain the 'lo-fi' aesthetic, no frequency above 15kHz or below 40Hz is permitted in the [mastering] chain; exclude all modern high-fidelity sheen and sub-harmonic synth resonance."
        

## 2. Gate Definitions (V&V)

Gates are binary "Stop-the-Line" checkpoints. If a gate returns a FAIL, the process halts immediately. The system generates a "Missing Work Item" report rather than a song prompt, preventing "garbage in, garbage out" scenarios.

- **SEG (Feasibility):** A "Physics" check. It evaluates the internal logic of the Technical UST to ensure the parameters are physically possible for a human or AI to execute.
    
    - _Check:_ Does the [tempo] allow for the [melisma] density requested in the Voice axis without sounding like digital artifacts?
        
    - _Failure Consequence:_ Immediate routing back to the Arranger (Alan) for meter or tempo recalibration. No reverse-compilation is permitted until SEG is green.
        
- **G-Card (Scoring):** A quantitative alignment audit. It measures how well the Technical UST adheres to the Creative UST's "Affect" targets.
    
    - _Scoring:_ Each Axis is scored 1–10. A score < 7.0 triggers an automatic "Contested Consensus" meeting.
        
    - _Audit Trail:_ Every score must be accompanied by a "Rationale" sentence citing the specific AXIS.KEY address that drove the score. High scores indicate perfect alignment between "Vibe" (Creative) and "Physics" (Technical).
        
- **SE20 (Quality & Lineage):** The "Cultural Weight" check. It ensures the track isn't generic or "Stock AI" sounding. It guards against the "Uncanny Valley" of generated music.
    
    - _Criteria:_ Does this arrangement advance the lineage of the genre? For example, "Does this 'Trap Gospel' track use authentic 808 slides and preacher yell-ins, or just generic lo-fi loops?"
        
    - _Authority:_ Anva (A&R) holds primary veto power here. If a prompt feels "too safe" or "too generic," SE20 fails, forcing a Phase 2 re-meeting.
        
- **CAP (Budget):** Hard character limit enforcement for Suno v4.5 token efficiency.
    
    - _Target:_ 4960–4999 characters for the Macro.
        
    - _Protocol:_ If count > 4999, the "Promotion Law" must strip adverbs, redundant descriptors, and non-essential ad-libs until the budget is balanced. Characters are treated as a finite "Instructional Currency" that must be spent wisely.
        

## 3. Creative UST Patch (Atom 4)

The `[Road Map]` block is the structural spine of the track, ensuring the AI model understands the "Energy Flow" over time. In v5-b, it is promoted to a primary axis to prevent "structural wandering" where the AI forgets to resolve a bridge or return to a chorus.

- **Fields & Implications:**
    
    - `[sections]`: Explicit order (e.g., Intro -> V1 -> C1 -> V2 -> C2 -> B -> C3 -> Outro). Defines the "Skeleton" of the arrangement.
        
    - `[bars_per_section]`: Strict bar counts to prevent the AI from ending sections prematurely or overstaying its welcome in a loop.
        
    - `[pickups_and_turnarounds]`: Instructions for the "hinges" between sections (e.g., "1-bar snare roll pickup into Chorus 1" or "4-bar total silence drop").
        
    - `[energy_flow]`: The dynamic arc (e.g., "Linear build to Chorus 3; immediate total-silence drop for the first 2 bars of the Outro").
        
    - `[section_thesis]`: The emotional or narrative goal of each segment (e.g., "Verse 1 is the 'Grief'; Chorus is the 'Resolution'").
        

## 4. Governance & Conflict Resolution

- **V&V Marshal:** The Orchestrator acts as the Marshal. The Marshal is a "Rules-Lawyer"—they do not care if a song is "good" or "catchy," only if it is "valid" according to the Evidence Contract and Technical Schema. The Marshal's primary tool is the "Stop-the-Line" command.
    
- **Stop-the-line Protocol:**
    
    - If Vanessa (Vocals) ejections occur in Phase 2 due to "Vocal Realism" violations, Phase 3 (Meetings) cannot begin until a viable vocal strategy is proposed.
        
    - If Eldrik (Engineering) flags a "Spectral Collision" (e.g., sub-bass and kick fighting for the same 50Hz space), the Marshal must block Phase 4 promotion until EQ or sidechain constraints are added.
        
- **Tie-Break Authority:** When SMEs reach a 50/50 split on a non-physics issue, the Tie-Break Authority (listed in the Council Matrix) makes a final, unchallengeable ruling. This prevents "Meeting Loop" paralysis and ensures the industrial pipeline maintains its velocity.
    
- **The Delta Note:** Any time the system modifies or "corrects" an artist's request for technical feasibility (e.g., slowing down a fast song to fit 200 words of lyrics), it must generate a "Delta Note" (What changed | Why it changed | Risk of ignoring the change). This ensures the artist understands the technical trade-offs required to make the track successful.
