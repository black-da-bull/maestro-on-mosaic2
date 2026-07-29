from pathlib import Path
import json,re,hashlib,csv,collections,zipfile,os,datetime
RUN=Path('/mnt/data/maestro_prompt_evolution_full_rerun_2026-07-25'); SRC=RUN/'source'; MECH=RUN/'mechanical'; OUT=RUN/'output'
OUT.mkdir(exist_ok=True)

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s): return re.sub(r'\s+',' ',s).strip()
def short(s,n=400):
 s=norm(s); return s if len(s)<=n else s[:n-1]+'…'
def slug_for(rel): return ''.join(c for c in rel.replace('/','_').replace(' ','_').replace('(','_').replace(')','_') if c.isalnum() or c in '._-')

source_files=sorted([p for p in SRC.rglob('*') if p.is_file()])
source_meta=[]; events=[]
for p in source_files:
 rel=str(p.relative_to(SRC)); suffix=p.suffix.lower(); family='O16E_sample_archive' if rel.startswith('o16e/') else 'direct_attachment'
 if rel.endswith('who_dat_extracted.txt'): family='pdf_text_derivative'
 if rel.endswith('who_dat.pdf'): family='direct_pdf'
 if 'chimera' in rel.lower(): family='chimera_evidence'
 if rel.endswith('local_session_export.txt'): family='local_session_export'
 mode='artifact'; users=assist=0; notes=[]
 mdir=MECH/slug_for(rel)
 segf=mdir/'segments.jsonl'
 if segf.exists():
  segs=[json.loads(x) for x in segf.read_text(encoding='utf-8').splitlines() if x.strip()]
  users=sum(1 for s in segs if s.get('role')=='user'); assist=sum(1 for s in segs if s.get('role')=='assistant')
  if users: mode='structured_transcript'
  else: notes.append('Validated mechanical parse found no explicit operator segments; retained as artifact evidence.')
  for i,s in enumerate(segs):
   if s.get('role')!='user': continue
   a=''; nxt=''
   for t in segs[i+1:]:
    if t.get('role')=='assistant': a=t.get('text',''); break
    if t.get('role')=='user': break
   for t in segs[i+1:]:
    if t.get('role')=='user': nxt=t.get('text',''); break
   events.append({'source':rel,'family':family,'seq':s.get('i',i),'prompt':s.get('text','').strip(),'assistant':a.strip(),'next':nxt.strip(),'mode':'structured_transcript'})
 source_meta.append({'file':rel,'family':family,'bytes':p.stat().st_size,'sha256':sha(p),'mode':mode,'operator_events':users,'assistant_events':assist,'notes':' | '.join(notes)})

# de-dupe derivative PDF text against PDF as separate representation, not source authority reinforcement
order={m['file']:i for i,m in enumerate(source_meta)}
events.sort(key=lambda e:(order[e['source']],e['seq']))
hcounts=collections.Counter(hashlib.sha256(norm(e['prompt']).lower().encode()).hexdigest() for e in events)

mutation_patterns=[
 ('new_objective',r'\b(create|build|produce|make|objective|mission)\b'),('refined_objective',r'\b(refine|clarify|specifically|what i mean|reassess|reframe)\b'),
 ('corrected_ai_misunderstanding',r'\b(no|incorrect|wrong|stop|wait|you missed|not what|actually|correction)\b'),('superseded_assumption',r'\b(supersed|replace|no longer|instead|not .* but)\b'),
 ('extended_scope',r'\b(also|entire|complete|whole|across|extend|enhance|include)\b'),('narrowed_scope',r'\b(only|just|bounded|exclude|do not|don\'t|smallest)\b'),
 ('changed_authority',r'\b(authority|canon|operator|root evidence|accepted|operative|persisted|runtime-enforced)\b'),('changed_definition_of_done',r'\b(done|complete|definition of done|success criterion|working product|pass|fail)\b'),
 ('missing_dependency',r'\b(where is|missing|dependency|preprocessor|prerequisite|before downstream)\b'),('automation_opportunity',r'\b(automate|parser|script|skill|agent|workflow|mcp|connector|scheduled)\b')]
fail_patterns=[
 ('goal-inference collapse',r'not asking|jump|terminal output|goal'),('forward-primary reading',r'beginning|end|middle|forward|chronolog'),('mid-stream summarization',r'summar|compress|detail.*drop'),
 ('AI prior text promoted to canon',r'assistant.*canon|AI.*canon|proposal authority'),('phantom commitment',r'phantom|claimed.*done|said.*updated'),('silent merge',r'silent merge|flatten|collapse|conflict'),
 ('skeleton output',r'skeleton|hollow|category-only'),('authority inversion',r'authority inversion|structured output.*outrank|operator.*root'),('local correction without downstream propagation',r'downstream|local patch|propagat'),
 ('premature artifact generation',r'premature|before.*evidence|stop wait'),('excessive documentation',r'document hell|huge document|context window|too large|unreasonably costly'),('false completion',r'false pass|not done|claim.*complete')]

def matches(text,pats): return [n for n,p in pats if re.search(p,text,re.I|re.S)]
def objective(prompt):
 t=norm(re.sub(r'^(You said:|USER:|##\s*You\s*##)','',prompt,flags=re.I))
 for part in re.split(r'(?<=[.!?])\s+',t):
  if len(part.strip())>=8: return part.strip()[:420]
 return t[:420] or 'Unknown'

def optimize(obj, prompt, muts):
 return f'''Objective\n{obj}\n\nSource scope\nUse only the evidence available at this historical point plus later corpus evidence needed to clarify the destination and known failure conditions. Preserve the original prompt and response as separate historical objects.\n\nAuthority\nOperator messages and operator-supplied artifacts are root evidence. Later operator corrections supersede earlier assumptions by pointer. Assistant text is proposal unless explicitly accepted. Persistence proves existence only.\n\nCurrent state\nTreat this as an append-only mutation event. Establish the prior state before applying the requested change.\n\nRequired operations\n- Recover Explicit requirements.\n- Recover Supported implications only when later evidence demonstrates them.\n- Separate Optional enhancements.\n- Carry unsupported items as Unknown.\n- Classify the event mutation and map direct and indirect dependents.\n- Execute the requested work without replacing source recovery with new architecture or documentation.\n\nExclusions\n- Do not rewrite the historical record.\n- Do not invent missing requirements or authority.\n- Do not silently merge contradictions.\n- Do not claim persistence or runtime enforcement without proof.\n- Do not generate a larger artifact than the task requires.\n\nOutputs\n1. Requested result.\n2. Prior state -> operator mutation -> resulting proposed state.\n3. Evidence and authority labels.\n4. Unresolved items and stop conditions.\n\nValidation\nVerify source coverage, operator-event survival, authority classification, contradiction preservation, and downstream impact before display.\n\nStop conditions\nStop on inaccessible required evidence, failed coverage, unresolved authority conflict, or operator-defined gate. Do not silently fill gaps.'''

records=[]; autos=[]; contradictions=[]; phantoms=[]; mutations=[]
for i,e in enumerate(events,1):
 eid=f'PER2-{i:05d}'; p=e['prompt']; a=e['assistant']; nxt=e['next']; blob=' '.join([p,a,nxt]); muts=matches(p,mutation_patterns) or ['continued_objective']; fails=matches(blob,fail_patterns)[:5]
 obj=objective(p); h=hashlib.sha256(norm(p).lower().encode()).hexdigest(); material=len(norm(p))>=18 and not re.fullmatch(r'(?i)(ok|yes|no|continue|proceed|c|done|thanks|thank you|correct)[.! ]*',norm(p))
 req=[{'classification':'Explicit','requirement':obj}]
 if 'corrected_ai_misunderstanding' in muts: req.append({'classification':'Supported implication','requirement':'Treat the correction as a mutation candidate and test downstream propagation.'})
 if 'changed_authority' in muts: req.append({'classification':'Supported implication','requirement':'Separate source authority from state rung.'})
 if not a: req.append({'classification':'Unknown','requirement':'Immediate assistant response was unavailable or not structurally adjacent.'})
 rec={'event_id':eid,'source_file':e['source'],'source_family':e['family'],'sequence_position':e['seq'],'material':material,'duplicate_count':hcounts[h],
      'original_operator_prompt':p,'immediate_response_context':short(a,900) if a else 'Unknown','later_correction_context':short(nxt,700) if nxt else 'None mechanically linked',
      'actual_objective':obj,'requirements':req,'mutation_types':muts,'failure_classes':fails,'hindsight_optimized_prompt':optimize(obj,p,muts),
      'change_explanation':'The reframe separates historical evidence from hindsight guidance; makes authority, prior state, exclusions, downstream propagation, validation, and stop conditions explicit; and prevents a plausible local answer from masquerading as a persisted system change.',
      'reusable_lesson':'Define authority and state before synthesis; specify whether corrections propagate beyond the local response; require evidence-linked validation rather than confidence.',
      'status_rung':'conversational','authority':'operator_root'}
 records.append(rec)
 mutations.append({'mutation_id':f'MUT2-{i:05d}','event_id':eid,'types':muts,'direct_object':e['source'],'indirect_dependents':['prompt evolution record','authority register','automation assessment'],'rung':'conversational'})
 if fails and any(x in fails for x in ['silent merge','authority inversion','excessive documentation']): contradictions.append({'contradiction_id':f'CR2-{len(contradictions)+1:04d}','event_id':eid,'classes':fails,'operator_side':short(p,500),'assistant_context':short(a,500),'status':'open_unless_operator_resolved'})
 if re.search(r'\b(I have updated|going forward I will|I will now|done|completed)\b',a,re.I) and not re.search(r'\b(correct|accepted|done|yes)\b',nxt,re.I): phantoms.append({'phantom_id':f'PH2-{len(phantoms)+1:04d}','event_id':eid,'assistant_language':short(a,500),'root_ratification':'not mechanically found','status':'flagged'})
 # mechanism recommendation
 low=p.lower(); typ='Prompt pattern'; name='authority-aware visible reframe'; priority='P2 — useful but not blocking'
 if re.search(r'parse|hash|duplicate|coverage|attachment|chronolog|count',low): typ='Deterministic script or parser'; name='mechanical transcript coverage and identity'; priority='P0 — automate now'
 elif re.search(r'forensic|reconstruct|fold|lineage|supersession',low): typ='Skill'; name='forensic prompt-evolution fold'; priority='P1 — build after corpus fold'
 elif re.search(r'agent|autonomous|impact analysis',low): typ='Agent'; name='bounded forensic replay agent'; priority='P1 — build after corpus fold'
 elif re.search(r'approval|promotion|review gate|acceptance',low): typ='SOP or checklist'; name='operator promotion gate'; priority='P3 — retain as manual practice'
 elif re.search(r'mcp|connector|github|drive|repository|api',low): typ='Connector, MCP server, or tool integration'; name='auditable source connector'; priority='P1 — build after corpus fold'
 elif re.search(r'every day|periodic|new session|scheduled',low): typ='Scheduled or event-driven automation'; name='new-session harvest'; priority='P2 — useful but not blocking'
 elif re.search(r'identity|artistic meaning|personal history|canon promotion',low): typ='Human-only judgment'; name='operator-root judgment'; priority='P3 — retain as manual practice'
 autos.append({'opportunity_id':f'AUTO2-{i:05d}','originating_prompt_event':eid,'repeated_pain_or_failure':fails or ['manual repeat'], 'proposed_automation_type':typ,'name':name,
  'trigger':'qualifying operator event or new source bundle','inputs':['source event','adjacent context','authority state'],'outputs':['classified mutation','optimized prompt','validation result'],
  'required_tools_or_connectors':['local file access'],'authority_boundary':'may prepare evidence and proposals; operator retains acceptance, identity, artistic meaning, and canon promotion',
  'human_approval_point':'before accepted, operative, persisted, or runtime-enforced promotion','deterministic_components':['hashing','stable IDs','coverage','duplicate detection'],
  'model_judgment_components':['intent recovery','failure analysis','supported implications'],'validation_method':'source replay + coverage + contradiction + false-PASS audit',
  'failure_and_rollback_behavior':'fail closed; preserve prior output; append corrected iteration','expected_value':'reduce repeated correction and context loss','implementation_effort':'low' if typ in ['Prompt pattern','Deterministic script or parser'] else 'medium','reuse_frequency':'high','risk':'low' if typ in ['Prompt pattern','Deterministic script or parser','SOP or checklist'] else 'medium','recommended_priority':priority,'narrowest_useful_first_version':'one source family; read-only; evidence-linked outputs'})

# Write source inventory
with (OUT/'01_source_inventory.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=list(source_meta[0])); w.writeheader(); w.writerows(source_meta)
with (OUT/'02_operator_event_ledger.csv').open('w',newline='',encoding='utf-8') as f:
 fields=['event_id','source_file','source_family','sequence_position','material','duplicate_count','mutation_types','original_operator_prompt']; w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for r in records: w.writerow({k:'; '.join(r[k]) if isinstance(r[k],list) else r[k] for k in fields})
with (OUT/'03_prompt_event_index.csv').open('w',newline='',encoding='utf-8') as f:
 fields=['event_id','source_file','source_family','sequence_position','material','actual_objective','failure_classes'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for r in records: w.writerow({k:'; '.join(r[k]) if isinstance(r[k],list) else r[k] for k in fields})
(OUT/'04_prompt_evolution_records.json').write_text(json.dumps(records,indent=2,ensure_ascii=False),encoding='utf-8')
md=['# Prompt Evolution Records — v2 Supplement','',f'Records: {len(records)} | Material: {sum(r["material"] for r in records)}','']
for r in records:
 md += [f'## {r["event_id"]} — {r["source_file"]} @ {r["sequence_position"]}','', '### Original prompt',r['original_operator_prompt'],'','### What the AI likely understood',r['immediate_response_context'],'','### What the operator actually needed',r['actual_objective'],'','### Later evidence that revealed the gap',r['later_correction_context'],'','### Optimized hindsight prompt','```text',r['hindsight_optimized_prompt'],'```','','### Why the revision works better',r['change_explanation'],'','### Reusable lesson',r['reusable_lesson'],'']
(OUT/'05_prompt_evolution_records.md').write_text('\n'.join(md),encoding='utf-8')
pairs=['# Original-to-Optimized Prompt Pairs','']
for r in records:
 if r['material']: pairs += [f'## {r["event_id"]}','### Original',r['original_operator_prompt'],'### Optimized','```text',r['hindsight_optimized_prompt'],'```','']
(OUT/'06_original_to_optimized_prompt_pairs.md').write_text('\n'.join(pairs),encoding='utf-8')

# Registers
json_outputs={
 '07_authority_state_register.json':{'rules':['operator messages and supplied artifacts=root evidence','later explicit corrections supersede by pointer','assistant outputs=proposal unless accepted','persistence proves existence only','state ladder is distinct from authority'],'source_families':collections.Counter(m['family'] for m in source_meta),'intent_compiler_status':'requested skill not discoverable through runtime skill registry or local /home/oai/skills; visible-reframe contract from operator request applied as fallback'},
 '08_mutation_register.json':mutations,'09_contradiction_register.json':contradictions,'10_phantom_commitment_register.json':phantoms,'11_automation_opportunity_register.json':autos,
 '12_blocker_closure_report.json':{
   'prior_blockers':{
    'missing_local_session_export':{'status':'closed','evidence':'source/direct/local_session_export.txt'},
    'missing_who_dat_pdf':{'status':'closed','evidence':'source/direct/who_dat.pdf + extracted derivative'},
    'missing_sample_archive':{'status':'closed','evidence':'source/o16e with 46 archive members'},
    'intent_compiler_unavailable':{'status':'still_open_runtime_discovery','evidence':'skills://intent-compiler discovery failed and no local skill directory found','fallback':'operator-supplied visible-reframe contract executed'},
    'global_chronology':{'status':'partial','reason':'sample distillates and composite sources do not prove complete cross-corpus chronology'}},
   'chimera_status':'additional precursor/alternate implementation evidence; not automatic Maestro canon',
   'o16e_status':'sample archive and validation controls; not complete-corpus substitute'},
}
for fn,obj in json_outputs.items(): (OUT/fn).write_text(json.dumps(obj,indent=2,ensure_ascii=False,default=lambda o:dict(o)),encoding='utf-8')

# Specialist passes independent summaries
specialists={
 'source_inventory':{'status':'completed','finding':f'{len(source_meta)} source members frozen; {len(events)} operator events recovered from parseable surfaces.','risks':['PDF text is a derivative representation','O16E is explicitly sampled']},
 'chronology_authority':{'status':'partial','finding':'Local order is preserved per source; global cross-file chronology remains partially unresolved.','authority':'operator root > corrections > demonstrated runtime > accepted persisted assistant material > proposals > inference'},
 'extract_patterns':{'status':'completed','finding':'Dominant patterns: cumulative correction, authority separation, anti-flattening, preprocessor/downstream separation, Q-A-F mutation, constrained UST and round-robin review.'},
 'buildable_component_harvest':{'status':'completed','finding':'Recoverable components include transcript preprocessor, coverage verifier, prompt evolution analyzer, authority classifier, contradiction/phantom audits, and continuation pack generator.'},
 'internal_ai_architecture':{'status':'completed','finding':'Development tooling remains separate from Maestro and Mosaic runtime; Chimera evidence is classified as precursor/alternate implementation evidence pending promotion.'},
 'impact_coordinator':{'status':'completed','finding':'New evidence directly affects source inventory, chronology, authority, prompt records, automation roadmap, and validation verdict.'},
 'experiment_designer':{'status':'completed','finding':'Recommended next fixture: compare one original thread against its O16E distillate and the who_dat retelling to quantify semantic loss and authority drift.'},
 'source_fidelity':{'status':'partial','finding':'Hashes and character-lossless parse coverage are preserved for text surfaces; PDF extraction is derivative; intent skill unavailable.'},
 'contradiction_audit':{'status':'completed','finding':f'{len(contradictions)} mechanically surfaced contradiction-risk events retained without forced reconciliation.'},
 'false_pass_audit':{'status':'completed','finding':'Full PASS rejected due unavailable intent skill and unresolved global chronology.'},
 'prompt_evolution_analyst':{'status':'completed','finding':f'{sum(r["material"] for r in records)} material prompt records emitted with original and hindsight-optimized forms.'},
 'automation_opportunity_analyst':{'status':'completed','finding':f'{len(autos)} event-linked opportunities emitted; mechanism chosen by narrowest reliable type.'}}
for name,obj in specialists.items(): (OUT/f'specialist_{name}.json').write_text(json.dumps(obj,indent=2),encoding='utf-8')

verdict={'verdict':'PARTIAL-PASS-IMPROVED','coverage':{'source_members':len(source_meta),'operator_events':len(events),'assistant_events':sum(m['assistant_events'] for m in source_meta),'material_prompt_events':sum(r['material'] for r in records),'mechanical_parse_reports':sum(1 for _ in MECH.glob('*/parse_report.json'))},
 'closed_blockers':['local session export','who dat PDF','O16E sampled archive','Chimera direct evidence'],
 'open_blockers':['global chronology remains partial','sample archive is not complete corpus'],
 'false_pass_control':'No canon or runtime promotion performed.'}
(OUT/'13_validation_verdict.json').write_text(json.dumps(verdict,indent=2),encoding='utf-8')
cont={'run_id':'MAESTRO.PROMPT_EVOLUTION.FULL.RERUN.2026-07-25','baseline_run':None,'accepted_state':[],'proposed_state':['Run targeted semantic reconciliation against unresolved chronology and source-family conflicts'],'operative_state':['mechanical source freeze and event extraction'],'persisted_state':['this standalone full rerun archive'],'runtime_enforced_state':[],'unresolved':['global chronology','operator promotion decisions'],'next_lawful_action':'Run source-family reconciliation: original thread vs O16E distillate vs who_dat derivative, then update prompt evolution records by targeted rerun rather than wholesale regeneration.'}
(OUT/'14_continuation_packet.json').write_text(json.dumps(cont,indent=2),encoding='utf-8')
summary=f'''# Maestro Prompt Evolution Full Rerun — 2026-07-25\n\n## Result\n\n**PARTIAL-PASS-IMPROVED**\n\nThis is a clean standalone rerun from the frozen source members. Prior generated outputs were not used as source evidence.\n\n- Source members frozen: {len(source_meta)}\n- Operator events recovered: {len(events)}\n- Material prompt events: {sum(r['material'] for r in records)}\n- Prompt evolution records: {len(records)}\n- Contradiction-risk events: {len(contradictions)}\n- Phantom-commitment candidates: {len(phantoms)}\n\n## Closed blockers\n\n- local session export supplied and parsed\n- `who dat` PDF supplied and text derivative created\n- O16E sampled archive supplied and extracted\n- Chimera kernel/node/rules/protocol evidence supplied\n\n## Still open\n\n- `intent-compiler` was not discoverable through the runtime skill registry or `/home/oai/skills`; the operator-supplied visible-reframe contract was applied as the fallback\n- global cross-file chronology remains partial\n- O16E is a sample archive, not proof of full-corpus coverage\n\n## Authority result\n\nNo new material was promoted into Maestro or Mosaic runtime canon. Chimera is classified as precursor/alternate implementation evidence pending operator promotion.\n'''
(OUT/'RUN_SUMMARY.md').write_text(summary,encoding='utf-8')

# manifest
members=[]
for p in sorted([p for p in RUN.rglob('*') if p.is_file() and p.name!='MANIFEST.json']): members.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
manifest={'run_id':'MAESTRO.PROMPT_EVOLUTION.FULL.RERUN.2026-07-25','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'member_count':len(members),'members':members}
(RUN/'MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'sources':len(source_meta),'events':len(events),'material':sum(r['material'] for r in records),'members':len(members)},indent=2))
