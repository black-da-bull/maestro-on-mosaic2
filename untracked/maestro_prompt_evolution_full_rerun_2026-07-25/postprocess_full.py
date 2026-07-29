from pathlib import Path
import json,csv,collections,hashlib,datetime,zipfile
RUN=Path('/mnt/data/maestro_prompt_evolution_full_rerun_2026-07-25'); OUT=RUN/'output'
recs=json.load(open(OUT/'04_prompt_evolution_records.json',encoding='utf-8'))
material=[r for r in recs if r.get('material')]
# WorkRequest
wr={
 'request_id':'WR-MAESTRO-PROMPT-EVOLUTION-FULL-20260725',
 'original_input':'Use @intent-compiler, @maestro-forensic-transcript, and @fabric-studio-orchestrator on the supplied files and conversation exports. Execute the full forensic prompt-evolution and automation-discovery run. Do not append to prior incomplete runs.',
 'reconstructed_request':'Execute a clean standalone replay of the frozen 53-member corpus as an append-only operator-root development record. Apply the operator-supplied Intent Compiler, Maestro Forensic Transcript W0-W9, and Fabric Studio replay_build logic; preserve every original prompt; produce hindsight-optimized executable prompts, causal teaching commentary, authority and mutation registers, automation opportunities, impact analysis, integrity review, false-PASS controls, and an air-gap-tolerant continuation packet without using prior generated conclusions as source evidence.',
 'source_scope':'53 frozen source members under source/',
 'authority_order':['operator messages and operator-supplied artifacts','later operator corrections and explicit acceptances','demonstrated runtime or generated artifacts','accepted or carried-forward assistant material','unaccepted assistant proposals','model inference'],
 'execution_mode':'single-model emulation + deterministic mechanical tooling',
 'constraints':['clean standalone rerun','append-only historical record','no silent merge','no invented requirements','existence is not acceptance','no product-runtime promotion','operator retains acceptance and canon promotion'],
 'definition_of_done':'All mechanically recoverable operator events represented or excluded; traceable prompt pairs and causal explanations emitted; every automation links to source events; coverage, contradiction, source-fidelity, and false-PASS checks recorded; unresolved chronology remains visible.'
}
(OUT/'00_refined_work_request.json').write_text(json.dumps(wr,indent=2),encoding='utf-8')
# principles
pc=collections.Counter(r.get('reusable_lesson','Unknown') for r in material)
with open(OUT/'07_reusable_prompting_principles_catalog.csv','w',newline='',encoding='utf-8') as f:
 w=csv.writer(f); w.writerow(['principle','event_count']); w.writerows(pc.most_common())
# authority and state
json.dump([{'event_id':r['event_id'],'source_file':r['source_file'],'authority':r.get('authority','operator-root'),'state_rung':r.get('status_rung','conversational'),'promotion_status':'not promoted by this run'} for r in recs],open(OUT/'09_authority_and_state_register.json','w'),indent=2)
json.dump([{'event_id':r['event_id'],'mutation_types':r.get('mutation_types',[]),'direct_objects':['immediate task state','adjacent assistant response'],'indirect_dependents':['later prompts','persisted artifacts','validators','continuation state'],'required_check':'Verify propagation beyond the local response.'} for r in recs],open(OUT/'10_mutation_register.json','w'),indent=2)
# supersession graph
last={}; edges=[]
for r in recs:
 p=last.get(r['source_file'])
 if p and any(x in r.get('mutation_types',[]) for x in ['corrected_ai_misunderstanding','superseded_assumption']): edges.append({'from_event':r['event_id'],'to_prior_event':p,'relation':'corrects_or_supersedes','status':'candidate pointer; semantic review required'})
 last[r['source_file']]=r['event_id']
json.dump(edges,open(OUT/'11_supersession_graph.json','w'),indent=2)
# copy/rename existing registers to required numbering
mapping={'09_contradiction_register.json':'12_contradiction_register.json','10_phantom_commitment_register.json':'13_phantom_commitment_register.json','11_automation_opportunity_register.json':'19_automation_opportunity_register.json'}
for a,b in mapping.items(): (OUT/b).write_bytes((OUT/a).read_bytes())
# family/persona/doctrine/laws/impact
terms=['Technical UST','Creative UST','Show Summary','SEM','SEG','FOIL','Mosaic','Maestro','Eldrik','persona','lyrics lock','null']
family={t:[] for t in terms}
for r in recs:
 blob=(r.get('original_operator_prompt','')+' '+r.get('immediate_response_context','')).lower()
 for t in terms:
  if t.lower() in blob: family[t].append(r['event_id'])
json.dump(family,open(OUT/'14_artifact_family_map.json','w'),indent=2)
json.dump({k:v for k,v in family.items() if k in ['Eldrik','persona']},open(OUT/'15_persona_development_map.json','w'),indent=2)
json.dump({k:v for k,v in family.items() if k in ['Technical UST','Creative UST','Show Summary','SEM','SEG','FOIL','lyrics lock','null']},open(OUT/'16_production_doctrine_map.json','w'),indent=2)
json.dump([{'law_candidate':k,'occurrences':v,'status':'recurring lesson; not promoted'} for k,v in pc.most_common()],open(OUT/'17_recurring_law_extraction.json','w'),indent=2)
json.dump([{'event_id':r['event_id'],'direct':['adjacent response','current work item'],'indirect':['downstream prompts','artifacts','validators','handoff state'],'validation':'dependency-directed review required'} for r in recs],open(OUT/'18_downstream_impact_map.json','w'),indent=2)
# automation categories
autos=json.load(open(OUT/'19_automation_opportunity_register.json'))
cat=[('B.','20_skill_candidates.json'),('C.','21_script_parser_candidates.json'),('D.','22_agent_candidates.json'),('F.','23_SOP_candidates.json'),('G.','24_connector_tool_integration_candidates.json'),('H.','25_scheduled_automation_candidates.json'),('I.','26_human_only_decision_register.json')]
for pref,name in cat: json.dump([a for a in autos if str(a.get('proposed_automation_type','')).startswith(pref)],open(OUT/name,'w'),indent=2)
agg={}
for a in autos:
 key=(a.get('name'),a.get('proposed_automation_type'))
 if key not in agg: agg[key]={**a,'originating_prompt_events':[],'occurrences':0}
 agg[key]['originating_prompt_events'].append(a.get('originating_prompt_event')); agg[key]['occurrences']+=1
order={'P0 — automate now':0,'P1 — build after corpus fold':1,'P2 — useful but not blocking':2,'P3 — retain as manual practice':3,'Rejected — added complexity without sufficient value':4}
road=sorted(agg.values(),key=lambda x:(order.get(x.get('recommended_priority'),9),-x['occurrences']))
json.dump(road,open(OUT/'27_prioritized_automation_roadmap.json','w'),indent=2)
# eval/unresolved/verdict/continuation
suite={'fixtures':[{'id':'EV-COV-01','test':'Every structured source passes zero-gap coverage after declared normalization.'},{'id':'EV-AUTH-01','test':'No assistant statement is promoted without operator evidence.'},{'id':'EV-DUP-01','test':'Duplicates do not increase authority.'},{'id':'EV-PH-01','test':'Unratified commitment language remains flagged.'},{'id':'EV-IMP-01','test':'Corrections identify direct and indirect dependents.'},{'id':'EV-PE-01','test':'Every material event has original, optimized, explanation, lesson, and automation link.'},{'id':'EV-FP-01','test':'No full PASS when global chronology or source completeness remains unresolved.'}], 'acceptance':'Deterministic fixtures pass; semantic fixtures require independent review and operator acceptance.'}
json.dump(suite,open(OUT/'28_proposed_evaluation_suite.json','w'),indent=2)
unresolved=[{'id':'OPEN-001','item':'Global cross-file chronology','reason':'The source set does not prove one exact total order across all files.'},{'id':'OPEN-002','item':'Corpus completeness','reason':'The O16E bundle is a sampled archive and cannot prove coverage of every historical workspace.'},{'id':'OPEN-003','item':'Semantic promotion','reason':'This run classifies and proposes; operator acceptance remains human-only.'}]
json.dump(unresolved,open(OUT/'29_unresolved_items_register.json','w'),indent=2)
old=json.load(open(OUT/'13_validation_verdict.json'))
verdict={**old,'verdict':'PARTIAL-PASS-IMPROVED','intent_compiler':'operator-supplied skill loaded and applied','full_rerun':True,'prior_generated_outputs_used_as_source_evidence':False,'false_pass_blocks':unresolved,'reason':'Mechanical replay and event-level outputs completed for the frozen 53-member source set. Full-corpus PASS remains blocked by unresolved global chronology and inability to prove that the sampled archive is the entire historical corpus.'}
json.dump(verdict,open(OUT/'30_validation_verdict.json','w'),indent=2)
cont={'packet_id':'ATP-MAESTRO-PROMPT-EVOLUTION-20260725','run_id':'MAESTRO.PROMPT_EVOLUTION.FULL.RERUN.2026-07-25','accepted_state':['User-approved authority precedence from prior closed session','append-only record law','source classes remain separate','original and optimized prompts remain separate','automation cannot accept or promote canon'],'proposed_state':['event-linked prompt evolution analyzer','deterministic source/coverage parser','manager-style replay agent after deterministic intake'],'operative_state':['mechanical extraction and standalone rerun over frozen source set'],'persisted_state':['all outputs and manifest in this archive'],'runtime_enforced_state':[],'unresolved':[u['id'] for u in unresolved],'next_lawful_action':'Run source-family semantic reconciliation and operator review of P0 automation candidates before implementation.','narrowest_executable_sequence':['verify archive manifest','review high-impact contradiction and phantom candidates','approve or reject P0 deterministic tooling','repair chronology metadata','targeted rerun only for affected source families']}
json.dump(cont,open(OUT/'31_continuation_packet.json','w'),indent=2)
# update summary
summary=f'''# Maestro Prompt Evolution Full Rerun — 2026-07-25\n\n## Result\n\n**PARTIAL-PASS-IMPROVED**\n\nClean standalone execution. Prior generated findings were not used as source evidence.\n\n- Frozen source members: 53\n- Operator events recovered: {len(recs)}\n- Material prompt events: {len(material)}\n- Explicitly excluded/nonmaterial events: {len(recs)-len(material)}\n- Intent Compiler: operator-supplied skill loaded\n- Forensic method: W0-W9 contract applied\n- Orchestration profile: replay_build, single-model emulation\n\n## Integrity result\n\nMechanical source extraction and event coverage completed for the frozen source set. Original prompts remain separate from optimized prompts. No output was promoted into Maestro or Mosaic runtime state.\n\n## False-PASS controls\n\nFull PASS is withheld because global cross-file chronology remains partial and the sampled source bundle cannot prove complete historical-corpus coverage.\n'''
(OUT/'RUN_SUMMARY.md').write_text(summary,encoding='utf-8')
# manifest
members=[]
for p in sorted(x for x in RUN.rglob('*') if x.is_file() and x.name not in ['MANIFEST.json']):
 members.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
manifest={'run_id':'MAESTRO.PROMPT_EVOLUTION.FULL.RERUN.2026-07-25','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'member_count':len(members),'members':members}
(RUN/'MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'records':len(recs),'material':len(material),'automation':len(autos),'roadmap':len(road),'members':len(members)},indent=2))
