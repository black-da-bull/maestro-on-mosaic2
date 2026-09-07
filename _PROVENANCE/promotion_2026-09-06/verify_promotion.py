#!/usr/bin/env python3
"""Reproduce current bundle, reference, history and scoped-policy checks.
Usage: PYTHONDONTWRITEBYTECODE=1 python _PROVENANCE/promotion_2026-09-06/verify_promotion.py REPO
The full-corpus occurrence audit remains incomplete for named unreadable historical objects.
"""
import pathlib,sys,subprocess,tempfile,hashlib,json,csv,re,os

def run(repo):
    r=pathlib.Path(repo).resolve();b=r/'maestro-current';p=r/'_PROVENANCE/promotion_2026-09-06'
    env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'};commands=[]
    def cmd(args):
        result=subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True,env=env)
        commands.append({'command':'python '+' '.join(map(str,args)),'exit':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
        if result.returncode:raise RuntimeError(result.stdout+result.stderr)
    def hashes(root):return {str(x.relative_to(root)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(root.rglob('*')) if x.is_file()}
    cmd([b/'build/validate_bundle.py',b]);cmd([b/'build/test_promotion.py',b])
    with tempfile.TemporaryDirectory() as tmp:
        t=pathlib.Path(tmp)
        for name in ['one','two']:cmd([b/'build/build_maestro_current.py',t/name,b])
        h=hashes(b)
        assert h==hashes(t/'one')==hashes(t/'two'),'byte drift'
        cmd([b/'build/compile_current.py',r/'artifacts/D-Maestro/Maestro/technical.ust.template.txt',t/'compiled'])
        for f in (t/'compiled').iterdir():assert f.read_bytes()==(b/'compiled'/f.name).read_bytes(),f.name
    inventory={x['path']:x for x in csv.DictReader((p/'REPOSITORY_INVENTORY.csv').open())}
    # Source locations are migration aliases, not newly fabricated files.
    aliases=['','maestro-current/','maestro-current/compiled/','code/D-Maestro/maestro-ai-music-system-main/','artifacts/D-Maestro/','code/D-Maestro/maestro-ai-music-system-main/legacy/maestro_v5b_coldstart/']
    references=[]
    for f in b.glob('*.md'):
        for ref in re.findall(r'`([^`\n]+\.(?:md|yaml|json|py|txt)/?)`',f.read_text()):
            candidates=[a+ref for a in aliases]
            resolved=next((q for q in candidates if q in inventory or (r/q).is_file()),None)
            assert resolved,('unresolved reference',f.name,ref)
            references.append({'document':f.name,'reference':ref,'resolved':resolved})
    base=json.loads((p/'BASELINE.json').read_text())['files'];preserved=[]
    for name in ['02_CREATIVE_UST_TEMPLATE.md','03_PHASE_CHAIN.md','04_COUNCIL_TOPOLOGY.md']:
        for rel in ['maestro-current/'+name,'maestro-current/build/templates/'+name]:
            assert hashlib.sha256((r/rel).read_bytes()).hexdigest()==base[rel]['sha256'],rel
            preserved.append(rel)
    state=(r/'_PROVENANCE/STATE.md').read_text().split('## Preserved state snapshots')[0]
    for marker in ['| O-03 | CLOSED','| O-13 | CLOSED','| O-04 | OPEN, provenance','forensic_replay_required','external_asset_preservation_blocker','experiment_required','PHANTOM']:
        assert marker in state,marker
    return {'current_bundle_checks':'PASS','deterministic_members':len(h),'sha256':h,'references':references,'verified_no_change':preserved,'commands':commands,'corpus_audit':'PARTIAL: see SOURCE_LIMITATIONS.md; this script does not waive it'}

if __name__=='__main__':print(json.dumps(run(sys.argv[1]),indent=2))
