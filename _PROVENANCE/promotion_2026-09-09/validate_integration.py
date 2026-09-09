#!/usr/bin/env python3
"""Reproduce this promotion's source/build/runtime boundary checks; no renderer calls."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

import yaml

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / 'maestro-current'
sys.path.insert(0, str(BUNDLE / 'build'))
from compile_current import AXES, main as compile_source, topology


def snapshot(path):
    return {str(p.relative_to(path)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(path.rglob('*')) if p.is_file()}


def run():
    result = {'scope': 'source-to-bundle identity and existing deterministic runtime; no audible or LLM execution claim', 'checks': []}
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        result['checks'].append({'name': name, 'passed': True})
    source = ROOT / 'artifacts/D-Maestro/Maestro/technical.ust.template.txt'
    compiled = BUNDLE / 'compiled/TECHNICAL_UST_TOPOLOGY_MATERIALIZED.md'
    axes, keys, subs = topology(compiled.read_text())
    overlay = yaml.safe_load((ROOT / 'runtime/maestro-workforce/technical_ust_ownership_dependency_overlay.yaml').read_text())
    check('compiled axes match existing runtime axes', axes == AXES and set(axes) == set(overlay['axis_bindings']))
    bound = set()
    for axis, data in overlay['axis_bindings'].items():
        for key, key_data in data.get('key_bindings', {}).items():
            bound.add(key)
            bound.update(key_data.get('subkey_bindings', {}))
            bound.update(key_data.get('subkey_reviewers', {}))
    check('every explicitly bound runtime address exists in compiled canon', bound <= set(keys + subs))
    for edge in overlay['crossstream_dependencies']['hard_schema_edges']:
        for side in ('from', 'to'):
            check('dependency endpoint exists: ' + str(edge[side]), edge[side] in axes + keys + subs)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for index in (1, 2):
            out = tmp / f'topology{index}'
            with contextlib.redirect_stdout(io.StringIO()):
                check(f'source compiler run {index}', compile_source(str(source), str(out)) == 0)
            check(f'source-derived topology run {index} equals checked-in output', all((BUNDLE / 'compiled' / p.name).read_bytes() == p.read_bytes() for p in out.iterdir()))
        check('independent source compiles byte-identical', snapshot(tmp/'topology1') == snapshot(tmp/'topology2'))
        corrupted = tmp / 'bad-source.txt'
        corrupted.write_bytes(source.read_bytes() + b'\nchanged')
        with contextlib.redirect_stdout(io.StringIO()):
            check('changed predecessor fails hash gate', compile_source(str(corrupted), str(tmp/'bad-output')) == 2)
        check('failed source emits no artifacts', not (tmp/'bad-output').exists())
        for index in (1, 2):
            out = tmp / f'bundle{index}'
            command = subprocess.run([sys.executable, '-B', str(BUNDLE/'build/build_maestro_current.py'), str(out), str(BUNDLE)], capture_output=True, text=True)
            check(f'full clean rebuild {index}', command.returncode == 0)
            check(f'full clean rebuild {index} equals checked-in bundle', snapshot(out) == snapshot(BUNDLE))
        check('independent complete bundles byte-identical', snapshot(tmp/'bundle1') == snapshot(tmp/'bundle2'))
        result['bundle_files'] = len(snapshot(tmp/'bundle1'))
    commands = [
        ['maestro-current/build/validate_bundle.py', 'maestro-current'],
        ['maestro-current/build/test_promotion.py', 'maestro-current'],
        ['runtime/maestro-workforce/validate_workforce.py'],
        ['runtime/maestro-workforce/golden_structural_interpretation_fixture.py'],
    ]
    result['commands'] = []
    for command in commands:
        proc = subprocess.run([sys.executable, '-B', *command], cwd=ROOT, capture_output=True, text=True)
        result['commands'].append({'argv': command, 'exit_code': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr})
        check('command passed: ' + command[0], proc.returncode == 0)
    result['runtime_bound_addresses_checked'] = len(bound)
    result['bundle_sha256'] = snapshot(BUNDLE)
    result['passed'] = True
    return result


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
