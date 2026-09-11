#!/usr/bin/env python3
"""Promotion regression tests. Run with PYTHONDONTWRITEBYTECODE=1.
These exercise workspace validators, not a deployed Maestro song runtime.
"""
import sys, pathlib, tempfile, shutil, contextlib, io, copy
sys.dont_write_bytecode=True
from validate_bundle import sem_config, evaluate_sem, validate_policy, topology_errors, main as bundle_check
from lyric_lock_check import main as lyric_check

def run(bundle):
    b=pathlib.Path(bundle);checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    def rejects(fn):
        try:fn()
        except ValueError:return True
        return False
    c=sem_config((b/'05_GOVERNANCE_SEG.md').read_text())
    # Historical song-local policy is a test fixture, never a current default.
    p={'threshold':97.5,'scope':'run','context_ref':'song_test_2025-12-07_001/decomposer_v1.6_run_001','authority_ref':'DEC-PROMO-01; source transcript operator line 3599'}
    scores={k:3.84 for k in c['weights']}
    result=evaluate_sem(scores,c,p)
    check('run-local 76.8 does not meet its explicit target',abs(result['composite']-76.8)<1e-8 and result['numeric_pass'] is False)
    check('numeric success is not an overall SEG release',evaluate_sem({k:5 for k in scores},c,p)['overall_seg_verdict']=='not_evaluated')
    q={**p,'threshold':76.8};check('explicit alternate fixture boundary',evaluate_sem(scores,c,q)['numeric_pass'])
    for field in p:
        q=copy.deepcopy(p);q.pop(field);check('reject missing '+field,rejects(lambda:validate_policy(q)))
    for field,value in [('scope','global'),('scope','universal'),('threshold',float('nan')),('threshold',float('inf')),('threshold',True),('threshold',101),('authority_ref',''),('context_ref',' ')]:
        check('reject invalid '+field+repr(value),rejects(lambda:validate_policy({**p,field:value})))
    for value in [float('nan'),float('inf'),-1,6,True]:
        q={**scores,'hook':value};check('reject bad score '+repr(value),rejects(lambda:evaluate_sem(q,c,p)))
    q=dict(scores);q.pop('hook');check('reject unscored criterion',rejects(lambda:evaluate_sem(q,c,p)))
    check('policy required',rejects(lambda:evaluate_sem(scores,c,None)))
    with contextlib.redirect_stdout(io.StringIO()):check('bundle passes',bundle_check(str(b))==0)
    with tempfile.TemporaryDirectory() as tmp:
        out=pathlib.Path(tmp)/'bundle';shutil.copytree(b,out)
        f=out/'fixture/dryrun_project.md';f.write_text(f.read_text()+'\nTamper\n')
        with contextlib.redirect_stdout(io.StringIO()):check('actual hash tamper rejected',bundle_check(str(out))!=0)
        shutil.rmtree(out);shutil.copytree(b,out)
        f=out/'05_GOVERNANCE_SEG.md';f.write_text(f.read_text()+'\ncomposite ≥97.5 → G-Card\n')
        with contextlib.redirect_stdout(io.StringIO()) as captured: rc=bundle_check(str(out))
        check('global floor regression rejected semantically',rc!=0 and 'superseded global threshold semantics' in captured.getvalue())
        locked=pathlib.Path(tmp)/'locked.txt';derived=pathlib.Path(tmp)/'derived.txt'
        locked.write_text('"one two"\n"three four"\n"one two"')
        for name,t,expected in [('spacing','"one  two"\n"three four"\n"one two"',0),('edit','"one changed"\n"three four"\n"one two"',2),('reorder','"three four"\n"one two"\n"one two"',2),('delete duplicate','"one two"\n"three four"',2)]:
            derived.write_text(t)
            with contextlib.redirect_stdout(io.StringIO()):check('lyric '+name,lyric_check(str(locked),str(derived))==expected)
    creative=(b/'02_CREATIVE_UST_TEMPLATE.md').read_text();phase=(b/'03_PHASE_CHAIN.md').read_text();workers=(b/'04_COUNCIL_TOPOLOGY.md').read_text()
    check('Creative is derived from locked Technical','Compiled from a LOCKED Technical UST' in creative and 'Derived meso surface' in creative)
    check('lock precedes reverse compilation',phase.index('Definitive technical.ust LOCK')<phase.index('Reverse promotion'))
    check('13 audio workers and separate visual module','13 audio workers' in workers and 'with the VIS/VIG/SEL module set, not the audio runtime' in workers)
    check('phantom not requirement','Q1–Q16 = PHANTOM (never fabricate)' in (b/'05_GOVERNANCE_SEG.md').read_text())
    docs={f.name:f.read_text() for f in b.glob('*.md')}
    check('Technical MAP and Creative omission are consistent',not topology_errors(str(b),docs))
    leaked=dict(docs);leaked['02_CREATIVE_UST_TEMPLATE.md']='[Road-Map]\n'+creative
    check('Creative Roadmap leak rejected without relying on hashes',any('Creative Road-Map' in e for e in topology_errors(str(b),leaked)))
    retired=dict(docs);retired['01_TECHNICAL_UST_CANON.md']=retired['01_TECHNICAL_UST_CANON.md'].replace('MAP.K3','PER.K7')
    check('Technical address renaming rejected without relying on hashes',any('differ' in e for e in topology_errors(str(b),retired)))
    missing=dict(docs);missing['01_TECHNICAL_UST_CANON.md']='\n'.join(line for line in missing['01_TECHNICAL_UST_CANON.md'].splitlines() if not line.startswith('| MAP |'))
    check('Technical MAP registry omission rejected',any('MAP axis row required' in e for e in topology_errors(str(b),missing)))
    print('PASS: '+str(len(checks))+' promotion checks')
    for name in checks:print('  PASS '+name)

if __name__=='__main__':run(sys.argv[1])
