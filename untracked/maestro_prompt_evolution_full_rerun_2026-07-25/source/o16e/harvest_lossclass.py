#!/usr/bin/env python3
"""O16E mechanical loss-class harvester. Tools-first per skill 01_METHODOLOGY.
Scans every thread source for the four DEC-28 loss-classes and measures DETAIL DENSITY,
not just presence. Output: per-file class metrics + block offsets for verbatim pull."""
import re, os, json, hashlib

# Loss-class detectors — structural, not just keyword. Each returns (hits, sample_offsets)
CLASS = {
 'SEM': {
   'schema': re.compile(r'(S(?:EM)?[-_ ]?\d{1,2}\b|criteri|weight(?:ed|ing)?|\b\d{1,2}\.\d\s*/\s*10|97\.5|composite\s+score|scoring\s+(?:band|rubric|matrix)|excellence\s+matrix)', re.I),
   'strong': re.compile(r'(SEM[-_ ]?\d{1,2}|weight\s*[:=]\s*\d|criteria\s*\d{1,2}|12\s+criteria|97\.5)', re.I),
 },
 'FOIL': {
   'schema': re.compile(r'(FOIL|macro\.?\s*micro|tier\s*[0-9IVX]|face\s+[AB]\b|stanza[./]section[./]line[./]word|factor(?:ing|ed)|first[- ]outer[- ]inner[- ]last|tiered\s+(?:system|language))', re.I),
   'strong': re.compile(r'(FOIL|macro[.\s]*micro[.\s]*tactical|stanza[.\s/]+section[.\s/]+line[.\s/]+word|Face\s+[AB]\b|tier\s*[1-4])', re.I),
 },
 'AGENTS': {
   'schema': re.compile(r'(act\s+as|\bpersona\b|\bcouncil\b|round[- ]robin|\bSME\b|\broster\b|\bseat\b|owner\s*/\s*reviewer|tie[- ]break|subagent|storyline|facilitator|orchestrat)', re.I),
   'strong': re.compile(r'(act\s+as\s+["a-z]|persona\s*[:=]|council\s+(?:member|matrix|of)|round[- ]robin|owner/reviewer|storyline\s*[:=])', re.I),
 },
 'EXCELLENCE': {
   'schema': re.compile(r'(excellence|quality\s+gate|G-?Card|SE20|HPA|VIRAL|sacred\s+imperfection|release[- ]grade|admissib|gold\s+standard|governance)', re.I),
   'strong': re.compile(r'(song\s+excellence|G-?Card|SE20|HPA|sacred\s+imperfection|excellence\s+(?:statement|criteria|matrix|governance))', re.I),
 },
 'UST': {
   'schema': re.compile(r'(\bUST\b|truth\s+object|technical\s+ust|creative\s+ust|axis(?:es)?\b|THY|VOC|STY|TIM|\bPER\b|POST|LYR|blueprint\.json|K[1-8]\b)', re.I),
   'strong': re.compile(r'(Technical\s+UST|Creative\s+UST|truth\s+object|axis\s+(?:identity|names?|set)|THY\.|VOC\.|K[1-8]\s*[:=])', re.I),
 },
}

def scan(path):
    try: t=open(path,encoding='utf-8',errors='replace').read().replace('\r\n','\n')
    except: return None
    n=len(t)
    res={'bytes':n}
    for cls,pats in CLASS.items():
        weak=pats['schema'].findall(t)
        strong=[(m.start()) for m in pats['strong'].finditer(t)]
        # density = strong hits per 10k chars
        res[cls]={'weak':len(weak),'strong':len(strong),
                  'density':round(len(strong)/(n/10000),2) if n else 0,
                  'first_off':strong[0] if strong else None}
    return res

# Thread source registry (dedup: eldrik family -> one primary; skip context.md monster)
SOURCES = {
 # S0 prehistory (samples from extracted)
 'S0/council_2025-05-20':'work/O16E/threads/TH-00_prehistory/2025-05-20_-_Council-Driven_AI_Workflow.md',
 'S0/fractal_2025-05-29':'work/O16E/threads/TH-00_prehistory/2025-05-29_-_Fractal_Music_GPT_Prototype.md',
 'S0/odie_2025-03-30':'work/O16E/threads/TH-00_prehistory/2025-03-30_-_ODIE_Modular_Design_Review.md',
 'S0/lyrical_warfare_2025-03-31':'work/O16E/threads/TH-00_prehistory/2025-03-31_-_Lyrical_Warfare_Superteam.md',
 'S0/gold_standard_2025-05-02':'work/O16E/threads/TH-00_prehistory/2025-05-02_-_Gold_Standard_Prompt_Breakdown.md',
 'S0/defsol_2023-11-10':'work/O16E/threads/TH-00_prehistory/2023-11-10_-_Extracted_Definitive_Solution_Text.md',
 # S1 v1-v3
 'S1/begin_gpt':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/Begin GPT 1.txt',
 'S1/momoney_dev':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/MoMoeny Dev.md',
 'S1/dumbass_blueprint':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/dumbass session.md',
 'S1/gemini_gem_v4x':'corpus/sessions/D-Maestro/maestro-ai-music-system-main/legacy/maestro-os-v4.x-baseline-001/oldMaestroGeminiGemIterativeDesignViaConversationalDialogueDevelopmentSessionExport.txt',
 'S1/universalmaestro_v3g':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/UniversalMaestro.v3.0g.CustomGPT.Instructions.md',
 # S2-S3 baseline + quality architecture
 'S2/1213_v4x':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/maestro-os-v4.x-baseline-001/1213.txt',
 'S2/song_review_T01':'corpus/sessions/D-Maestro/maestro-ai-music-system/source/distributed/suno_v45_config_bundle_v3/conversation_-2--song-review_2025-05-07-0505.agi.md',
 'S3/taxonomy_v45':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/2025-05-16 - Suno v4.5 Taxonomy Research.md',
 'S3/houseinorder':'corpus/artifacts/D-Maestro/Maestro/houseinorder.txt',
 'S3/inmyroom':'corpus/artifacts/D-Maestro/Maestro/inmyroom.tx.txt',
 'S3/SEM_matrix_design':'corpus/artifacts/D-Maestro/Maestro/song.excellence.matrix.iterative.design.session.txt',
 'S3/SEM_reformatted_ARTIFACT':'corpus/artifacts/D-Maestro/SONG EXCELLENCE MATRIX!!!/song_excellence_reformatted.md',
 'S3/os_dev_T02':'corpus/sessions/E-scatter/maestro/conversation_os-dev_2025-09-22-1602.agi.md',
 'S3/chop_screw':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/chop and screw module dev chat.txt',
 'S3/extrct_engine':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/extrct-engine-dev-chat.txt',
 'S3/session_ust_T05':'corpus/sessions/OneDrive-v45/session-ust.txt',
 'S3/devsession_iter':'corpus/sessions/D-Maestro/Maestro/maestro.devsession.iterative.txt',
 # S4 v4.5.x PROVEN
 'S4/v455_evidence':'corpus/artifacts/D-Maestro/sources/v2-6-4-5-5__maestro_evolution_execution-evidence.txt',
 'S4/v452_monolith':'corpus/artifacts/D-Maestro/canon/MoMoney Maestro OS v4.5.2 — MONOLITHIC PROMPT.md',
 'S4/chimera_devsession_T04':'corpus/sessions/OneDrive-v45/maestro_devsession.ai_optimized.md',
 # S5 v5/v5b/v5c
 'S5/eldrik_PRIMARY':'corpus/artifacts/D-Maestro/sources/eldrik.txt.txt',
 'S5/clarity':'corpus/sessions/D-Maestro/maestro-ai-music-system/dev-chats/conversation_maestro-chat---clarity_2026-04-03-1250.agi.md',
 'S5/foil_tiered':'corpus/sessions/D-Maestro/sources/conversation_foil-based-tiered-system_2026-04-03-1252.agi.md',
 'S5/v5_ust_sem':'corpus/sessions/D-Maestro/maestro-ai-music-system-main/legacy/maestrov5-dev-ust and sem-sessions.txt',
 'S5/day3_v5b_v5c':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/Day 3 Dev Chat.md',
 'S5/staging_spine_v5b':'corpus/artifacts/D-Maestro/Maestro/v5-b/staging.spine.merged.ai_optimized.md',
 'S5/houseinorder_v5b_aiopt':'corpus/artifacts/D-Maestro/Maestro/v5-b/houseinorder.ai_optimized.md',
 'S5/technical_ust_v5b_aiopt':'corpus/artifacts/D-Maestro/Maestro/v5-b/technical_ust_template.ai_optimized.md',
 'S5/chimera_quality':'corpus/artifacts/D-Maestro/pws - maestro v5/chimera-quality-dev-chat (1).txt',
 'S5/lyric_baseline':'corpus/artifacts/D-Maestro/pws - maestro v5/Lyric quality baseline (1).txt',
 'S5/branch_lyric':'corpus/artifacts/D-Maestro/pws - maestro v5/Branch · Branch · Lyric quality baseline (1).txt',
 'S5/v5c_workspace_identity':'corpus/artifacts/D-Maestro/sources/workspace_identity-maestro_v5-c.txt',
 'S5/maestro_architecture_session':'corpus/untracked/maestro architecture session.md',
 'S5/fabric_rebirth':'corpus/untracked/Maestro - Fabric - Rebirth.md',
 'S5/technical_ust_template':'corpus/artifacts/D-Maestro/Maestro/technical.ust.template.txt',
 # v5b coldstart pack (the located S5b)
 'S5b/coldstart_TECH_UST_CANON':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/maestro_v5b_coldstart/docs/TECHNICAL_UST_CANON.md',
 'S5b/coldstart_GOV_ADDENDUM':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/maestro_v5b_coldstart/docs/TECHNICAL_UST_GOVERNANCE_ADDENDUM.md',
 'S5b/coldstart_COUNCIL_MATRIX':'corpus/code/D-Maestro/maestro-ai-music-system-main/legacy/maestro_v5b_coldstart/docs/COUNCIL_MATRIX.md',
 # S6 session-13
 'S6/session13_window2':'corpus/artifacts/D-Maestro/sources/claude-session13-window2.txt',
 'S6/claud2':'corpus/artifacts/D-Maestro/sources/claud2.txt',
 'S6/051526_SEM':'corpus/artifacts/D-Maestro/sources/claude-session051526.md',
 'S6/maestro5_report':'corpus/artifacts/D-Maestro/sources/maestro5 report.txt',
 # S5c canon register (v5c)
 'S5c/v5c_canonical_spine':'corpus/artifacts/D-Maestro/canon/Maestro_v5c_Canonical_Spine.md',
 'S5c/v5c_canonical_root':'corpus/artifacts/D-Maestro/canon/Maestro_v5c_Canonical_Root.md',
 # S9 maestro-current (the TARGET being verified)
 'S9/current_01_TECH_UST':'corpus/maestro-current/01_TECHNICAL_UST_CANON.md',
 'S9/current_02_CREATIVE_UST':'corpus/maestro-current/02_CREATIVE_UST_TEMPLATE.md',
 'S9/current_04_COUNCIL':'corpus/maestro-current/04_COUNCIL_TOPOLOGY.md',
 'S9/current_05_GOVERNANCE_SEG':'corpus/maestro-current/05_GOVERNANCE_SEG.md',
 'S9/current_TOPOLOGY_MATERIALIZED':'corpus/maestro-current/compiled/TECHNICAL_UST_TOPOLOGY_MATERIALIZED.md',
}
out={}
for k,p in SOURCES.items():
    if not os.path.exists(p):
        out[k]={'MISSING':p}; continue
    out[k]=scan(p); out[k]['path']=p
json.dump(out, open('work/O16E/lossclass_metrics.json','w'), indent=1)

# Print matrix
print(f"{'stratum/thread':40s} {'bytes':>8} | {'SEM':>10} {'FOIL':>10} {'AGENT':>10} {'EXCEL':>10} {'UST':>10}")
print(f"{'':40s} {'':>8} | {'strong/dens':>10}"*5)
for k,v in out.items():
    if 'MISSING' in v: print(f"{k:40s}  MISSING"); continue
    def cell(c): return f"{v[c]['strong']}/{v[c]['density']}"
    print(f"{k:40s} {v['bytes']:>8} | {cell('SEM'):>10} {cell('FOIL'):>10} {cell('AGENTS'):>10} {cell('EXCELLENCE'):>10} {cell('UST'):>10}")
