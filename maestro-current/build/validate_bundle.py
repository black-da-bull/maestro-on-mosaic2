#!/usr/bin/env python3
"""Bundle validator v3: scoped SEM policy, structured parse, references and actual hashes.
Build-time validation only; does not assert deployed song-runtime enforcement.
Usage: validate_bundle.py BUNDLEDIR
"""
import sys, os, re, json, yaml, hashlib, math
from compile_current import AXES, topology

POLICY_FIELDS = ('threshold', 'scope', 'context_ref', 'authority_ref')
SCOPES = ('run', 'policy', 'version', 'context')

def number(x):
    return type(x) in (int, float) and math.isfinite(x)

def sem_config(text):
    found = []
    for block in re.findall(r'```yaml\n(.*?)```', text, re.S):
        value = yaml.safe_load(block)
        if isinstance(value, dict) and 'sem_configuration' in value:
            found.append(value['sem_configuration'])
    if len(found) != 1:
        raise ValueError('exactly one sem_configuration required')
    c = found[0]
    if not isinstance(c, dict): raise ValueError('SEM config mapping required')
    weights = c.get('weights')
    if not isinstance(weights, dict) or len(weights) != 12 or not all(number(v) and v > 0 for v in weights.values()) or sum(weights.values()) != 100:
        raise ValueError('12 positive SEM weights must sum to 100')
    if c.get('score_max') != 5: raise ValueError('SEM score scale must be 0–5')
    if c.get('threshold_selection') != 'explicit_applicable_context': raise ValueError('explicit applicable context required')
    if 'default_threshold' not in c or c['default_threshold'] is not None: raise ValueError('no numeric default authorized')
    if c.get('allowed_scopes') != list(SCOPES): raise ValueError('scope declaration invalid')
    if c.get('required_policy_fields') != list(POLICY_FIELDS): raise ValueError('policy evidence fields invalid')
    return c

def validate_policy(policy):
    if not isinstance(policy, dict) or any(k not in policy for k in POLICY_FIELDS):
        raise ValueError('explicit policy with threshold/scope/context/authority required')
    if policy['scope'] not in SCOPES: raise ValueError('unsupported threshold scope')
    if not number(policy['threshold']) or not 0 <= policy['threshold'] <= 100:
        raise ValueError('threshold must be finite on SEM 0–100 scale')
    for field in ('context_ref', 'authority_ref'):
        if not isinstance(policy[field], str) or not policy[field].strip():
            raise ValueError('nonempty ' + field + ' required')
    return policy

def evaluate_sem(scores, config, policy):
    """Explicit-policy numeric oracle for build tests; never an overall SEG verdict.
    Nonempty references prove structural binding only, not operator authenticity/applicability.
    Runtime must resolve those references and independent hard gates (D4 obligation).
    """
    validate_policy(policy)
    if not isinstance(scores, dict) or set(scores) != set(config['weights']):
        raise ValueError('every SEM criterion must be scored exactly once')
    if any(not number(v) or not 0 <= v <= config['score_max'] for v in scores.values()):
        raise ValueError('score out of range or nonfinite')
    composite = sum(scores[k] / config['score_max'] * w for k,w in config['weights'].items())
    return {'composite': composite, 'numeric_pass': composite >= policy['threshold'],
            'scope': policy['scope'], 'context_ref': policy['context_ref'],
            'authority_ref': policy['authority_ref'], 'overall_seg_verdict': 'not_evaluated'}

def topology_errors(d, allt):
    """Validate layer identity independently of a restamped manifest (DEC-PROMO-16)."""
    errors = []
    try:
        technical = allt['01_TECHNICAL_UST_CANON.md']
        compiled = open(os.path.join(d, 'compiled/TECHNICAL_UST_TOPOLOGY_MATERIALIZED.md'), encoding='utf-8').read()
        axes, keys, subs = topology(compiled)
        if axes != AXES or len(keys) != 33 or len(subs) != 165 or len(set(keys + subs)) != 198:
            errors.append('A3 Technical topology must retain 8 source axes and 198 distinct addresses')
        if topology(technical) != (axes, keys, subs):
            errors.append('A3 embedded and compiled Technical topology differ')
        marker = '# TECHNICAL.UST'
        if marker not in technical or marker not in compiled or technical[technical.index(marker):] != compiled[compiled.index(marker):]:
            errors.append('A3 embedded and compiled skeleton bytes differ')
        if not re.search(r'\|\s*MAP\s*\|', technical):
            errors.append('A3 Technical MAP axis row required')
        if any(re.match(r'PER\.K[5-8](?:\.|$)', a) for a in keys + subs):
            errors.append('A3 Technical MAP-to-PER migration forbidden')
        creative = allt['02_CREATIVE_UST_TEMPLATE.md'].split('## Era layer')[0]
        if re.search(r'^\s*\[road[- _]?map\b', creative, re.I | re.M):
            errors.append('A3 Creative Road-Map container forbidden')
        migration = yaml.safe_load(open(os.path.join(d, 'compiled/TECHNICAL_UST_ADDRESS_MIGRATION.yaml'), encoding='utf-8'))
        expected_map = sorted(a for a in keys + subs if a.startswith('MAP.'))
        if migration.get('migrated') != {} or migration.get('identity_addresses') != 198 or migration.get('preserved_map_addresses') != expected_map or len(expected_map) != 24:
            errors.append('A3 Technical MAP identity report inconsistent')
        coverage = yaml.safe_load(open(os.path.join(d, 'compiled/FULL_CANON_COVERAGE_MATRIX.yaml'), encoding='utf-8'))
        if coverage.get('source_axes') != AXES or coverage.get('current_axes') != AXES or coverage.get('migrated_addresses') != 0 or coverage.get('unexplained_omissions') != 0:
            errors.append('A3 Technical axis coverage inconsistent')
    except (OSError, KeyError, ValueError, TypeError, AttributeError, yaml.YAMLError) as exc:
        errors.append('A3 topology validation failed: ' + str(exc))
    return errors


def main(d):
    errs = []; allt = {}
    for f in sorted(os.listdir(d)):
        if f.endswith('.md'):
            allt[f] = open(os.path.join(d,f),encoding='utf-8').read()
    nums = {f[:2] for f in allt}
    manifest = yaml.safe_load(open(os.path.join(d,'MANIFEST.yaml'),encoding='utf-8'))
    for f,t in allt.items():
        for block in re.findall(r'```yaml\n(.*?)```',t,re.S):
            try: yaml.safe_load(block)
            except yaml.YAMLError as e: errs.append(f'A1 {f}: {e}')
        for ref in re.findall(r'(\d\d_[A-Z_]+\.md)',t):
            if ref not in allt: errs.append(f'A2 {f}: dangling {ref}')
        for m in re.finditer(r'(?:documented in|Per |per |see )(\d\d)(?![\d.])',t):
            if m.group(1) not in nums: errs.append(f'A2 {f}: shorthand ref unresolved')
        if re.search(r'\bPERF\b',t): errs.append(f'A3 {f}: retired token')
        # Reject the exact historical-to-current promotion defect, including inherited templates.
        if re.search(r'composite\s*≥\s*97\.5|release floor\s*\*\*97\.5|locked operator values \(97\.5\)|floor 97\.5 terminal|97\.5 floor present',t):
            errs.append(f'A5 {f}: superseded global threshold semantics')
    errs.extend(topology_errors(d, allt))
    try: sem_config(allt['05_GOVERNANCE_SEG.md'])
    except (ValueError, yaml.YAMLError) as e: errs.append('A5 '+str(e))
    if 'composite = Σ((score/5)×weight)' not in allt['05_GOVERNANCE_SEG.md']: errs.append('A5 formula missing')
    for root,_,files in os.walk(d):
        for fn in sorted(files):
            p=os.path.join(root,fn);rel=os.path.relpath(p,d)
            try:
                if fn.endswith(('.yaml','.yml')): yaml.safe_load(open(p,encoding='utf-8'))
                elif fn.endswith('.json'): json.load(open(p,encoding='utf-8'))
            except Exception as e: errs.append(f'A10 {rel}: {str(e).splitlines()[0]}')
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
    # Source/template drift cannot hide behind a freshly stamped manifest.
    for name in allt:
        template=os.path.join(d,'build','templates',name)
        if os.path.isfile(template) and open(template,'rb').read()!=open(os.path.join(d,name),'rb').read():
            errs.append('A9 template mismatch: '+name)
    print('PASS' if not errs else 'FAIL: '+'; '.join(errs))
    return 0 if not errs else 2

if __name__=='__main__':sys.exit(main(sys.argv[1]))
