from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def parse_lab(path: Path) -> list[dict]:
    segments = []
    for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        text = line.strip()
        if not text:
            continue
        parts = text.split(maxsplit=2)
        if len(parts) != 3:
            raise RuntimeError(f'invalid_lab_line:{line_number}')
        start, end, label = float(parts[0]), float(parts[1]), parts[2]
        if end < start:
            raise RuntimeError(f'negative_lab_duration:{line_number}')
        segments.append({'start_s': start, 'end_s': end, 'label': label})
    return segments


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--context', required=True)
    args = p.parse_args()

    context = json.loads(Path(args.context).read_text(encoding='utf-8'))
    if not isinstance(context, dict):
        raise ValueError('context_must_be_object')

    root = Path(os.getenv('CHORDMINI_ROOT', '/opt/ChordMini')).resolve()
    checkpoint = Path(str(context.get('chordmini_checkpoint') or os.getenv('CHORDMINI_CHECKPOINT') or '')).expanduser()
    if not checkpoint.is_absolute():
        checkpoint = root / checkpoint
    checkpoint = checkpoint.resolve()
    if not checkpoint.is_file():
        raise RuntimeError('CHORDMINI_CHECKPOINT_must_reference_preprovisioned_file')
    checkpoint_sha = sha256_file(checkpoint)
    model_type = str(context.get('chordmini_model_type') or os.getenv('CHORDMINI_MODEL_TYPE') or 'ChordNet')
    if model_type not in {'ChordNet', 'BTC'}:
        raise RuntimeError('invalid_chordmini_model_type')

    with tempfile.TemporaryDirectory(prefix='maestro-chordmini-') as td:
        save_dir = Path(td) / 'labs'
        command = [
            sys.executable,
            str(root / 'src' / 'evaluation' / 'test.py'),
            '--audio_dir', str(Path(args.input).resolve()),
            '--save_dir', str(save_dir),
            '--checkpoint', str(checkpoint),
            '--model_type', model_type,
            '--smooth_predictions',
        ]
        proc = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=int(os.getenv('CHORDMINI_TIMEOUT_S', '3600')))
        if proc.returncode != 0:
            raise RuntimeError(f'chordmini_inference_failed:{proc.returncode}:{(proc.stderr or proc.stdout)[-2000:]}')
        lab_files = sorted(save_dir.glob('*.lab'))
        if len(lab_files) != 1:
            raise RuntimeError(f'chordmini_expected_one_lab_got:{len(lab_files)}')
        segments = parse_lab(lab_files[0])

    payload = {
        'implementation_version': str(os.getenv('CHORDMINI_REVISION') or 'aa6e3a8d7b017f082fd2aaff9329d5c26af49c03'),
        'model_family': 'ptnghia-j/ChordMini',
        'model_type': model_type,
        'checkpoint_name': checkpoint.name,
        'checkpoint_sha256': checkpoint_sha,
        'segments': segments,
        'segment_count': len(segments),
        'canonical_harmony_promoted': False,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
