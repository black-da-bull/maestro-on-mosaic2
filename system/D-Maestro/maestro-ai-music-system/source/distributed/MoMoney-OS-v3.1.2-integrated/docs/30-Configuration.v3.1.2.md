# Original (preserved)

{
  "project_id": "momoney_os_v4_1",
  "semver": "4.1.0",
  "policies": {
    "dialogue_first": true,
    "ust_enforcement": true,
    "token_budget_chars_max": 4800,
    "consensus_threshold": 0.85,
    "adlib_validator_rule": "Parentheses contain literal vocalized text only"
  },
  "nodes": {
    "N2.0": {
      "name": "Core Relational Boot",
      "purpose": "Load persona, knowledge spine, and relational principles as live constraints.",
      "atoms": [
        {"id": "N2.0/01", "step": "Load persona + knowledge.", "in": ["persona.json","knowledge_spine"], "out": ["relational_state.json"]},
        {"id": "N2.0/02", "step": "Detect cold-start and apply reset hooks.", "in": ["last_session.meta"], "out": ["boot_log.txt"]},
        {"id": "N2.0/03", "step": "Activate principles: Collaboration, Muse, Mentor, Co-creator, Loving-Critic.", "in": [], "out": ["principles_active.flag"]}
      ],
      "kpis": ["boot_latency_ms","principles_active_bool"]
    },
    "N2.1": {
      "name": "AUTOMAT Init",
      "purpose": "Wire logging, versioning, verification services; open registry.",
      "atoms": [
        {"id": "N2.1/01", "step": "Create master registry.", "in": [], "out": ["project_root/master.json"]},
        {"id": "N2.1/02", "step": "Attach verification spine & versioning.", "in": [], "out": ["verification_hooks.json","versions.log"]}
      ],
      "kpis": ["registry_integrity","hooks_bound_bool"]
    },
    "N3.1": {
      "name": "Session Ingest & Context Reconstructor",
      "purpose": "Rebuild conversation, merge attachments, infer goals/constraints.",
      "atoms": [
        {"id": "N3.1/01", "step": "Ingest prior turns + files.", "in": ["transcript","attachments"], "out": ["context_state.json"]},
        {"id": "N3.1/02", "step": "Derive primary/secondary goals.", "in": ["context_state.json"], "out": ["goals_map.json"]}
      ],
      "kpis": ["context_coverage","goal_inference_confidence"]
    },
    "N4.1": {
      "name": "Mood-Sense",
      "purpose": "Compute sentiment, arousal/valence, certainty.",
      "atoms": [
        {"id": "N4.1/01", "step": "Score mood (sentiment, arousal, valence).", "in": ["last_user_turn"], "out": ["affect_state.json"]}
      ],
      "kpis": ["affect_latency_ms","affect_confidence"]
    },
    "N4.2": {
      "name": "Feedback-Learn",
      "purpose": "Turn critique into deltas (what/why/where).",
      "atoms": [
        {"id": "N4.2/01", "step": "Extract contradictions & gaps.", "in": ["affect_state.json","last_user_turn"], "out": ["feedback_deltas.json"]}
      ],
      "kpis": ["delta_precision","delta_recall"]
    },
    "N4.3": {
      "name": "Cognitive-Load Offloader",
      "purpose": "Offer 2–3 path menus + recommended pick with rationale.",
      "atoms": [
        {"id": "N4.3/01", "step": "Synthesize options A/B/C + recommendation.", "in": ["goals_map.json","feedback_deltas.json"], "out": ["menu.json"]}
      ],
      "kpis": ["menu_accept_rate","choice_time_savings_ms"]
    },
    "N5.x": {
      "name": "Creative Fragment Analysis (CFA)",
      "purpose": "Cluster themes, surface constraints, flag risks.",
      "atoms": [
        {"id": "N5.1", "step": "Theme clustering.", "in": ["context_state.json"], "out": ["themes.json"]},
        {"id": "N5.2", "step": "Constraint surfacing.", "in": ["goals_map.json"], "out": ["constraints.json"]},
        {"id": "N5.3", "step": "Risk map.", "in": ["themes.json","constraints.json"], "out": ["risk_map.json"]}
      ],
      "kpis": ["motif_coverage","risk_density"]
    },
    "N6.x": {
      "name": "Tree-of-Drafts (ToD)",
      "purpose": "Spawn A/B/C drafts with rationales; enable recursive refinement.",
      "atoms": [
        {"id": "N6.1", "step": "Draft A/B/C.", "in": ["themes.json","constraints.json"], "out": ["draftA.txt","draftB.txt","draftC.txt","draft_rationales.json"]},
        {"id": "N6.2", "step": "Recursive prompt chain refine (depth ≤ 3).", "in": ["draft*"], "out": ["draft_refined*"] }
      ],
      "kpis": ["refinement_depth_avg","adherence_score"]
    },
    "N7.x": {
      "name": "UST Builder",
      "purpose": "Map to Universal Suno Template with strict ordering.",
      "atoms": [
        {"id": "N7.1", "step": "Assemble [Theory→Voice→Lyrics Narrative→Sections→Style→Timbre→Performance→Post→Outro].", "in": ["draft_refined*"], "out": ["ust_prompt.txt"]},
        {"id": "N7.2", "step": "Enforce length + adlib validator.", "in": ["ust_prompt.txt"], "out": ["ust_prompt.valid.txt","ust_errors.log"]}
      ],
      "kpis": ["ust_valid_bool","token_budget_utilization"]
    },
    "N8.x": {
      "name": "Round-Robin SME Confrontation Lab",
      "purpose": "Simulate SMEs who challenge each other; eject inconsistencies; iterate to consensus.",
      "roles": ["The_Critic","The_Stylist","The_Engineer","The_DevilsAdvocate","The_Therapist"],
      "atoms": [
        {"id": "N8.1", "step": "Round-robin statements; each SME defends 2 claims.", "in": ["ust_prompt.valid.txt"], "out": ["sme_transcript.md"]},
        {"id": "N8.2", "step": "Inconsistency check → eject offender.", "in": ["sme_transcript.md"], "out": ["sme_roster.json"]},
        {"id": "N8.3", "step": "Consensus compute (≥ 0.85).", "in": ["sme_roster.json"], "out": ["consensus_score.json","consensus_notes.md"]}
      ],
      "kpis": ["ejection_count","consensus_score","issue_resolution_time_ms"]
    },
    "N9.x": {
      "name": "Post-Production Orchestrator",
      "purpose": "Attach mix/master cues as non-destructive overlay.",
      "atoms": [
        {"id": "N9.1", "step": "Render post cues JSON.", "in": ["ust_prompt.valid.txt"], "out": ["post_production_cues.json"]}
      ],
      "kpis": ["cue_conflict_rate"]
    },
    "N10.x": {
      "name": "Prompt Builder & Packaging",
      "purpose": "Assemble final Suno package (UST + meta + press).",
      "atoms": [
        {"id": "N10.1", "step": "Pack final prompt + metadata.", "in": ["ust_prompt.valid.txt","post_production_cues.json"], "out": ["Final_Suno_Prompt.txt","Press_Pack.md"]}
      ],
      "kpis": ["packaging_latency_ms"]
    },
    "N11.x": {
      "name": "Reverse-Pass Translator",
      "purpose": "UST → human brief with pedagogy.",
      "atoms": [
        {"id": "N11.1", "step": "Explain decisions & teachable patterns.", "in": ["Final_Suno_Prompt.txt"], "out": ["brief_human.md"]}
      ],
      "kpis": ["brief_readability","user_learning_gain"]
    },
    "N12.x": {
      "name": "Verification Spine",
      "purpose": "Macro/Micro/Tactical checks + Threat levels.",
      "atoms": [
        {"id": "N12.1", "step": "Macro checks (goal/brand/persona).", "in": ["Final_Suno_Prompt.txt"], "out": ["macro_report.json"]},
        {"id": "N12.2", "step": "Micro checks (syntax/meter/UST).", "in": ["Final_Suno_Prompt.txt"], "out": ["micro_report.json"]},
        {"id": "N12.3", "step": "Tactical checks (SOPs/edge sims).", "in": ["Final_Suno_Prompt.txt"], "out": ["tactical_report.json"]},
        {"id": "N12.4", "step": "Threat levels & delta report.", "in": ["*report.json"], "out": ["verification_log.json","delta_report.md"]}
      ],
      "kpis": ["issues_found","time_to_fix_ms"]
    }
  },
  "edges": [
    ["N2.0","N2.1"],["N2.1","N3.1"],["N3.1","N4.1"],["N4.1","N4.2"],["N4.2","N4.3"],
    ["N4.3","N5.x"],["N5.x","N6.x"],["N6.x","N7.x"],["N7.x","N8.x"],["N8.x","N9.x"],
    ["N9.x","N10.x"],["N10.x","N11.x"],["N11.x","N12.x"],["N12.x","N10.x"]
  ],
  "artifacts": {
    "state": ["relational_state.json","context_state.json","goals_map.json","affect_state.json","feedback_deltas.json","menu.json","themes.json","constraints.json","risk_map.json","drafts/*","ust_prompt.valid.txt","post_production_cues.json","verification_log.json","delta_report.md"]
  }
}


## Integrated Upgrade

# MoMoney OS Configuration (v3.1.2)

All knobs are explicit; defaults are safe.

- `consensus_threshold`: **0.85**  
- `draft_branches`: **3**  
- `recursion_depth_max`: **3**  
- `macro_char_soft_cap`: **4800** (hard **5000**)  
- `summary_char_cap`: **1000**  
- `roadmap_units`: `"bars"`  
- `adlib_policy`: `"literal_only_parentheses"`  
- `ejection_rule`: `"two_sustained_contradictions_per_cycle"`  
- `minutes_logging`: `true`  
- `telemetry_schema_path`: `schemas/telemetry.schema.json`  
- `vvlog_schema_path`: `schemas/vvlog.schema.json`  
- `project_schema_path`: `schemas/project.schema.json`  
- `template_archive_file`: "audio research - Reformatted show template.md"
