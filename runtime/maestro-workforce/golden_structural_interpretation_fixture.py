#!/usr/bin/env python3
"""P0.3 golden structural-interpretation fixture."""
import json,sys
from technical_ust_runtime import TechnicalUSTRuntime, RuntimeBlockError

DAVE='MAESTRO.AUDIO.09.DAVE'
VANESSA='MAESTRO.AUDIO.10.VANESSA'
SAGE='MAESTRO.AUDIO.07.SAGE'

def check(cond,msg):
    if not cond: raise AssertionError(msg)

def main():
    rt=TechnicalUSTRuntime(values={
        'THY.K3.S2':72,
        'PER.K2':'straight pocket with restrained drag',
        'LYR.K4.S1':'I keep the truth where the hurt still lives',
        'MAP.K3.S1':{'Chorus':['THY.K3.S2'],'Bridge':['THY.K1.S2']},
    },lyrics_locked=True)
    proofs={}

    dsp=rt.dispatch('THY.K3.S2','re-evaluate base tempo from the structural interpretation fixture','rhythmic_theory_proposal')
    check(dsp['worker_id']==DAVE,'THY.K3.S2 did not dispatch to Dave')
    check(dsp['authority_scope']['axis_key_ownership']=='THY.K3.S2','dispatch did not carry address authority')
    proofs['dispatch']={'pass':True,'address':'THY.K3.S2','worker_id':dsp['worker_id'],'required_reviewers':dsp['technical_ust']['required_reviewers']}

    change=rt.apply_change(DAVE,'THY.K3.S2',78)
    labor=[x for x in change['impacts'] if x['kind']=='labor_review' and x.get('target')=='LYR.K4']
    check(labor,'THY.K3 change did not propagate to LYR.K4 review dependency')
    check(rt.status.get('LYR.K4')=='reopened_dependency','LYR.K4 not reopened as impacted dependency')
    proofs['dependency_propagation']={'pass':True,'changed':'THY.K3.S2','reopened':['LYR.K4']}

    map_hits=[x for x in change['impacts'] if x['kind']=='map_k3_reference' and x.get('target')=='MAP.K3.S1@Chorus']
    check(map_hits,'referenced THY.K3.S2 did not propagate into MAP.K3.S1 Chorus reference')
    check(rt.status.get('MAP.K3.S1@Chorus')=='reopened_dependency','MAP.K3 referenced section not reopened')
    proofs['map_k3_reference_propagation']={'pass':True,'changed':'THY.K3.S2','reference':'MAP.K3.S1@Chorus','references':map_hits[0]['references']}

    lyric_before=rt.values['LYR.K4.S1']
    try:
        rt.apply_change(SAGE,'LYR.K4.S1','I changed the locked lyric without permission')
        raise AssertionError('locked lyric mutation unexpectedly succeeded')
    except RuntimeBlockError:
        pass
    check(rt.values['LYR.K4.S1']==lyric_before,'locked lyric value changed despite block')
    proofs['lyric_lock']={'pass':True,'address':'LYR.K4.S1','unchanged':True,'operator_authorization':False}

    rt.apply_change(VANESSA,'PER.K2','more aggressive forward-push execution')
    rt.raise_peer_objection(DAVE,'PER.K2','the push destroys the intended pocket and cadence usability')
    try:
        rt.finalize('PER.K2')
        raise AssertionError('PER.K2 finalized despite Dave lawful peer objection')
    except RuntimeBlockError:
        pass
    check(rt.status['PER.K2']!='accepted','peer-blocked address became accepted')
    proofs['peer_authority_blocking']={'pass':True,'address':'PER.K2','primary_owner':VANESSA,'blocking_peer':DAVE,'final_status':rt.status['PER.K2']}

    required=['dispatch','dependency_propagation','peer_authority_blocking','lyric_lock','map_k3_reference_propagation']
    passed=all(proofs[k]['pass'] for k in required)
    report={'fixture':'P0.3.golden_structural_interpretation','passed':passed,'proofs':proofs,'event_log':rt.events}
    print(json.dumps(report,indent=2,sort_keys=True))
    return 0 if passed else 2

if __name__=='__main__':
    try: raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({'fixture':'P0.3.golden_structural_interpretation','passed':False,'error':str(exc)},indent=2),file=sys.stderr)
        raise
