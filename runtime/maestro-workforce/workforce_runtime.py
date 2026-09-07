#!/usr/bin/env python3
"""Executable loader/dispatcher for Maestro bounded audio-worker descriptors.

Broad dispatch remains proposal-only. Address-authorized dispatch may be created by a
higher runtime only after the Technical UST ownership overlay has resolved the address
and supplied its lawful reviewers.
"""
import argparse,json,os,sys,uuid,copy
ROOT=os.path.dirname(os.path.abspath(__file__))

def load(name):
    with open(os.path.join(ROOT,name),encoding='utf-8') as f:return json.load(f)

def expand(delta,common):
    c=copy.deepcopy(common); five=delta['five_elements']
    return {'identity':{'employee_id':delta['employee_id'],'role_name':delta['role_name'],'runtime_kind':c['runtime_kind'],'aliases':delta.get('aliases',[])},'five_elements':five,'mission':delta['mission'],'domain_authority':{'owns_domains':delta['owns_domains'],'may_decide':delta['may_decide'],'may_write':delta['writable_zones'],'may_raise_blocking_objection':delta['blocking_objections'],'may_trigger_gate_review':['a blocking objection remains unresolved after lawful peer review','a controller/governance invariant is implicated'],'may_recommend_progression_block':['a blocking objection in this worker lane remains unresolved']},'explicit_non_authority':copy.deepcopy(c['explicit_non_authority']),'owned_decisions':delta['may_decide'],'blocked_decisions':copy.deepcopy(c['blocked_decisions']),'upstream_inputs':copy.deepcopy(c['upstream_inputs']),'downstream_outputs':five['output']+['round_robin_entry_when_triggered'],'readable_zones':copy.deepcopy(c['readable_zones']),'writable_zones':delta['writable_zones'],'scope':{'conditioning':['artist intent governs','operate only on explicitly assigned work','Technical UST ownership must come from the materialized ownership overlay, never role-name inference'],'evaluation_facets':delta['evaluation_facets']},'canvas':copy.deepcopy(c['canvas']),'null_classes_handled':delta['null_classes_handled'],'escalation_targets':copy.deepcopy(c['escalation_targets']),'challenge_obligations':dict(copy.deepcopy(c['challenge_obligations']),must_challenge_when=delta['blocking_objections']),'conflict_precedence':copy.deepcopy(c['conflict_precedence']),'failure_modes':copy.deepcopy(c['failure_modes'])+five['constraints'],'reverse_pass_participation':dict(copy.deepcopy(c['reverse_pass_participation']),may_shape=delta['reverse_may_shape']),'notes_and_artifact_obligations':copy.deepcopy(c['notes_and_artifact_obligations']),'controller_substitution_prohibitions':copy.deepcopy(c['controller_substitution_prohibitions']),'song_excellence_reference_duties':copy.deepcopy(c['song_excellence_reference_duties']),'source_evidence_refs':copy.deepcopy(c['source_evidence_refs'])}

def all_workers():
    data=load('canonical_13_employee_instances.yaml'); out=[]
    for ref in data['roster']:
        with open(os.path.join(ROOT,ref['file']),encoding='utf-8') as f: delta=json.load(f)
        if delta['employee_id']!=ref['employee_id'] or delta['role_name']!=ref['role_name']: raise ValueError('roster/file identity mismatch: '+ref['file'])
        out.append(expand(delta,data['common_contract']))
    return out

def index():
    es=all_workers(); by={}
    for e in es:
        i=e['identity']; by[i['employee_id']]=e; by[i['role_name'].lower()]=e
        for a in i.get('aliases',[]):by[a.lower()]=e
    return es,by

def resolve(ref):
    _,by=index(); return by.get(ref) or by.get(ref.lower())

def envelope(worker,task,context_refs,requested_output,write_target=None,address_ownership=None,required_reviewers=None):
    if not isinstance(task,str) or not task.strip():raise ValueError('nonempty task required')
    if write_target and write_target not in worker['writable_zones']:raise ValueError('write_target outside worker writable_zones; dispatch must remain proposal-only or use lawful target')
    authority={'owns_domains':worker['domain_authority']['owns_domains'],'axis_key_ownership':address_ownership or 'not_claimed_without_address'}
    if address_ownership:
        authority['ownership_source']='technical_ust_ownership_dependency_overlay.yaml'
        authority['required_reviewers']=list(required_reviewers or [])
    return {'dispatch_id':'DSP.'+uuid.uuid4().hex[:12],'worker_id':worker['identity']['employee_id'],'worker_name':worker['identity']['role_name'],'task':task,'context_refs':context_refs,'requested_output':requested_output,'authority_scope':authority,'write_target':write_target,'status':'ready_for_execution_adapter','runtime_limit':'dispatch/state enforcement only; model/provider invocation is not implemented in P0'}

def main():
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest='cmd',required=True);sub.add_parser('list')
    s=sub.add_parser('show');s.add_argument('worker')
    d=sub.add_parser('dispatch');d.add_argument('worker');d.add_argument('--task',required=True);d.add_argument('--context',action='append',default=[]);d.add_argument('--output',default='employee_work_note');d.add_argument('--write-target')
    a=p.parse_args();es,_=index()
    if a.cmd=='list':print(json.dumps([{'id':e['identity']['employee_id'],'name':e['identity']['role_name'],'domains':e['domain_authority']['owns_domains']} for e in es],indent=2));return 0
    w=resolve(a.worker)
    if not w:print('unknown worker',file=sys.stderr);return 2
    if a.cmd=='show':print(json.dumps(w,indent=2));return 0
    print(json.dumps(envelope(w,a.task,a.context,a.output,a.write_target),indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
