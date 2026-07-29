# Council Assignment Matrix — PIN.V5B.COUNCIL.MATRIX.V1

## Council Design
- **rule.primary_owner_per_axis:** Each axis has a primary owner SME persona.
- **rule.adjacent_reviewers_required:** Each axis fill receives at least 2 adjacent-domain reviewer challenges.
- **rule.tie_break_required:** Split decisions record a tie-break authority and rationale.
- **rule.physics_override:** SEG feasibility cannot be overridden by taste; feasibility failures force revision.

## Axis Ownership + Review + Tie-Break (Pinned)

| Axis | Primary Owner (SME) | Adjacent Reviewers (minimum) | Default Tie-Break (when split & feasible) |
|---|---|---|---|
| **THY** (Theory) | **Alan (Arranger/Music Director)** | Melony (Melody), Eldrik (Engineering) | Alan (musical coherence) unless market conflict ⇒ Anva |
| **VOC** (Vocals) | **Vanessa (Vocal Coach)** | Sage (Lyrics), Anva (A&R) | Vanessa (human execution realism) |
| **STY** (Style) | **Anva (A&R Ear)** | Alan (Form/lineage), Sage (Lyric intent) | Anva (strategic value / identity) |
| **TIM** (Timbre) | **Eldrik (Engineer/Sound Designer)** | Dave (Groove), Anva (Aesthetic fit) | Eldrik (spectral feasibility) |
| **PERF** (Performance) | **Dave (Drum Captain/Groove)** | Vanessa (Delivery), Eldrik (Translation) | Dave (pocket + energy) unless vocal realism conflict ⇒ Vanessa |
| **POST** (Post Production) | **Eldrik (Engineer/Mix)** | Vanessa (Vocal priority), Anva (platform translation) | Eldrik (mix physics) |
| **MAP** (Road Map) | **Alan (Arranger/Music Director)** | Dave (groove transitions), Sage (lyric section logic) | Alan (structure) |
| **LYR** (Lyrics Block) | **Sage (Songwriter)** | Vanessa (performability), Anva (memorability) | Sage (text integrity) unless lock violation risk ⇒ Orchestrator stops line |

## QA / Gate Authority (Non-SME Role)
- **role.vv_marshal:** V&V Marshal (Orchestrator-controlled) runs gates and enforces stop-the-line behavior.
- **vv_marshal.scope:** SEG feasibility checks; G-Card scoring; SE20 checklist; lock compliance; contradiction scan; cap checks.
