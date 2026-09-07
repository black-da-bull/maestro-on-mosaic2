#!/usr/bin/env python3
"""Fail-closed validator for Maestro P0 workforce materialization (stdlib only)."""
import json,os,sys,subprocess,importlib.util
ROOT=os.path.dirname(os.path.abspath(__file__))
EXPECTED=['Mo','Canon Orchestrator','Megazord Orchestrator','Sibling Architect','Metro Craft','Melody Scout','Sage','Alan','Dave','Vanessa','Analog Confessor','Anva','Eldrik']
VISUAL={'Visual Director','Identity Keeper','Motion Editor','Distribution Strategist'}
REQ=['identity','five_elements','mission','domain_authority','explicit_non_authority','owned_decisions','blocked_decisions','upstream_inputs','downstream_outputs','readable_zones','writable_zones','scope','canvas','null_classes_handled','escalation_targets','challenge_obligations','conflict_precedence','failure_modes','reverse_pass_participation','notes_and_artifact_obligations','controller_substitution_prohibitions','song_excellence_reference_duties']

def load(n):
    with open(os.path.join(ROOT,n),encoding='utf-8') as f:return json.load(f)
def runtime_module():
    spec=importlib.util.spec_from_file_location('wr',os.path.join(ROOT,'workforce_runtime.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def main():
    errs=[];raw=load('canonical_13_employee_instances.yaml');reg=load('employee_workforce_registry_contract.yaml');rt=runtime_module();es=rt.all_workers()
    if len(raw.get('roster',[]))!=13 or len(es)!=13:errs.append('expected exactly 13 employees')
    names=[e.get('identity',{}).get('role_name') for e in es]
    if names!=EXPECTED:errs.append('roster/order mismatch')
    ids=[e.get('identity',{}).get('employee_id') for e in es]
    if len(ids)!=len(set(ids)):errs.append('employee ids not unique')
    if VISUAL & set(names):errs.append('visual role leaked into audio roster')
    for e in es:
        n=e.get('identity',{}).get('role_name','?')
        for k in REQ:
            if k not in e:errs.append(f'{n}: missing {k}')
        if e.get('identity',{}).get('runtime_kind')!='bounded_employee_module':errs.append(f'{n}: runtime_kind')
        if e.get('explicit_non_authority',{}).get('may_not_gate_or_progress_phases_directly') is not True:errs.append(f'{n}: phase-gate prohibition')
        if e.get('reverse_pass_participation',{}).get('allowed_after')!='definitive_technical_ust_lock':errs.append(f'{n}: reverse pass timing')
        forbidden=set(e.keys()) & {'owns_axes','axis_key_ownership','owned_addresses'}
        if forbidden:errs.append(f'{n}: premature ownership fields {sorted(forbidden)}')
        if e.get('conflict_precedence',{}).get('may_override'):errs.append(f'{n}: worker override authority forbidden in P0')
    if reg.get('audio_runtime',{}).get('expected_worker_count')!=13:errs.append('registry count')
    if reg.get('audio_runtime',{}).get('worker_names')!=EXPECTED:errs.append('registry roster mismatch')
    if set(reg.get('audio_runtime',{}).get('visual_roles_excluded',[]))!=VISUAL:errs.append('visual exclusion mismatch')
    if reg.get('registry_law',{}).get('axis_key_ownership')!='deferred_next_task':errs.append('axis ownership not deferred')
    if reg.get('registry_law',{}).get('crossstream_dependency_overlay')!='deferred_next_task':errs.append('dependency overlay not deferred')
    if reg.get('controller_boundary',{}).get('controller_may')!=['route','validate','log','gate','freeze','promote','package']:errs.append('controller boundary widened/drifted')
    mo=next((e for e in es if e['identity']['role_name']=='Mo'),None)
    if not mo or not any('live operator' in s for s in mo['five_elements']['constraints']):errs.append('Mo operator-impersonation guard missing')
    try:
        out=subprocess.check_output([sys.executable,os.path.join(ROOT,'workforce_runtime.py'),'list'],text=True)
        if len(json.loads(out))!=13:errs.append('runtime list count')
        pkt=subprocess.check_output([sys.executable,os.path.join(ROOT,'workforce_runtime.py'),'dispatch','Dave','--task','evaluate pocket readability'],text=True)
        if json.loads(pkt)['authority_scope']['axis_key_ownership']!='not_inferred_p0':errs.append('dispatch ownership leak')
    except Exception as ex:errs.append('runtime smoke failed: '+str(ex))
    print('PASS: 13 bounded audio workers materialized; registry/runtime smoke clean; ownership overlay deferred' if not errs else 'FAIL: '+'; '.join(errs))
    return 0 if not errs else 2
if __name__=='__main__':raise SystemExit(main())
