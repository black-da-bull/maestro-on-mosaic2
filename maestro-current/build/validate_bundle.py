#!/usr/bin/env python3
"""Bundle validator v3.1: scoped SEM policy, structured parse, references, hashes and P0 workforce.
Build-time validation only; does not assert deployed song-runtime enforcement.
Usage: validate_bundle.py BUNDLEDIR
"""
import sys,os,re,json,yaml,hashlib,math,subprocess
POLICY_FIELDS=('threshold','scope','context_ref','authority_ref');SCOPES=('run','policy','version','context')
def number(x):return type(x) in (int,float) and math.isfinite(x)
def sem_config(text):
 found=[]
 for block in re.findall(r'```yaml\n(.*?)```',text,re.S):
  value=yaml.safe_load(block)
  if isinstance(value,dict) and 'sem_configuration' in value:found.append(value['sem_configuration'])
 if len(found)!=1:raise ValueError('exactly one sem_configuration required')
 c=found[0];weights=c.get('weights')
 if not isinstance(weights,dict) or len(weights)!=12 or not all(number(v) and v>0 for v in weights.values()) or sum(weights.values())!=100:raise ValueError('12 positive SEM weights must sum to 100')
 if c.get('score_max')!=5:raise ValueError('SEM score scale must be 0–5')
 if c.get('threshold_selection')!='explicit_applicable_context':raise ValueError('explicit applicable context required')
 if 'default_threshold' not in c or c['default_threshold'] is not None:raise ValueError('no numeric default authorized')
 if c.get('allowed_scopes')!=list(SCOPES):raise ValueError('scope declaration invalid')
 if c.get('required_policy_fields')!=list(POLICY_FIELDS):raise ValueError('policy evidence fields invalid')
 return c
def validate_policy(policy):
 if not isinstance(policy,dict) or any(k not in policy for k in POLICY_FIELDS):raise ValueError('explicit policy with threshold/scope/context/authority required')
 if policy['scope'] not in SCOPES:raise ValueError('unsupported threshold scope')
 if not number(policy['threshold']) or not 0<=policy['threshold']<=100:raise ValueError('threshold must be finite on SEM 0–100 scale')
 for field in ('context_ref','authority_ref'):
  if not isinstance(policy[field],str) or not policy[field].strip():raise ValueError('nonempty '+field+' required')
 return policy
def evaluate_sem(scores,config,policy):
 validate_policy(policy)
 if not isinstance(scores,dict) or set(scores)!=set(config['weights']):raise ValueError('every SEM criterion must be scored exactly once')
 if any(not number(v) or not 0<=v<=config['score_max'] for v in scores.values()):raise ValueError('score out of range or nonfinite')
 composite=sum(scores[k]/config['score_max']*w for k,w in config['weights'].items());return {'composite':composite,'numeric_pass':composite>=policy['threshold'],'scope':policy['scope'],'context_ref':policy['context_ref'],'authority_ref':policy['authority_ref'],'overall_seg_verdict':'not_evaluated'}
def main(d):
 errs=[];allt={}
 for f in sorted(os.listdir(d)):
  if f.endswith('.md'):allt[f]=open(os.path.join(d,f),encoding='utf-8').read()
 nums={f[:2] for f in allt};manifest=yaml.safe_load(open(os.path.join(d,'MANIFEST.yaml'),encoding='utf-8'))
 for f,t in allt.items():
  for block in re.findall(r'```yaml\n(.*?)```',t,re.S):
   try:yaml.safe_load(block)
   except yaml.YAMLError as e:errs.append(f'A1 {f}: {e}')
  for ref in re.findall(r'(\d\d_[A-Z_]+\.md)',t):
   if ref not in allt:errs.append(f'A2 {f}: dangling {ref}')
  for m in re.finditer(r'(?:documented in|Per |per |see )(\d\d)(?![\d.])',t):
   if m.group(1) not in nums:errs.append(f'A2 {f}: shorthand ref unresolved')
  if re.search(r'\bPERF\b',t):errs.append(f'A3 {f}: retired token')
  if re.search(r'composite\s*≥\s*97\.5|release floor\s*\*\*97\.5|locked operator values \(97\.5\)|floor 97\.5 terminal|97\.5 floor present',t):errs.append(f'A5 {f}: superseded global threshold semantics')
 if re.search(r'\|\s*MAP\s*\|',allt['01_TECHNICAL_UST_CANON.md']):errs.append('A3 MAP axis row')
 try:sem_config(allt['05_GOVERNANCE_SEG.md'])
 except (ValueError,yaml.YAMLError) as e:errs.append('A5 '+str(e))
 if 'composite = Σ((score/5)×weight)' not in allt['05_GOVERNANCE_SEG.md']:errs.append('A5 formula missing')
 for root,_,files in os.walk(d):
  for fn in sorted(files):
   p=os.path.join(root,fn);rel=os.path.relpath(p,d)
   try:
    if fn.endswith(('.yaml','.yml')):yaml.safe_load(open(p,encoding='utf-8'))
    elif fn.endswith('.json'):json.load(open(p,encoding='utf-8'))
   except Exception as e:errs.append(f'A10 {rel}: {str(e).splitlines()[0]}')
 listed=manifest.get('files',{});on_disk=set()
 for root,_,files in os.walk(d):
  for fn in files:
   rel=os.path.relpath(os.path.join(root,fn),d).replace(os.sep,'/')
   if rel!='MANIFEST.yaml':on_disk.add(rel)
 for miss in sorted(on_disk-set(listed)):errs.append('A11 unlisted: '+miss)
 for ghost in sorted(set(listed)-on_disk):errs.append('A11 absent: '+ghost)
 for rel in sorted(set(listed)&on_disk):
  actual=hashlib.md5(open(os.path.join(d,rel),'rb').read()).hexdigest()
  if listed[rel]!=actual:errs.append('A11 hash mismatch: '+rel)
 for name in allt:
  template=os.path.join(d,'build','templates',name)
  if os.path.isfile(template) and open(template,'rb').read()!=open(os.path.join(d,name),'rb').read():errs.append('A9 template mismatch: '+name)
 wf=os.path.join(d,'workforce','validate_workforce.py')
 if not os.path.isfile(wf):errs.append('A12 workforce validator missing')
 else:
  r=subprocess.run([sys.executable,wf],cwd=d,text=True,capture_output=True)
  if r.returncode!=0:errs.append('A12 '+(r.stdout.strip() or r.stderr.strip() or 'workforce validation failed'))
 print('PASS' if not errs else 'FAIL: '+'; '.join(errs));return 0 if not errs else 2
if __name__=='__main__':sys.exit(main(sys.argv[1]))
