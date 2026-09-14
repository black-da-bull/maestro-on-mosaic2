from __future__ import annotations

import argparse
import hashlib
import json
import os
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

import mido
import torch


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def resolve_device(requested: str) -> str:
    if requested != 'auto':
        if requested == 'cuda' and not torch.cuda.is_available():
            raise RuntimeError('tsumugi_cuda_requested_but_unavailable')
        if requested == 'mps' and not (hasattr(torch.backends, 'mps') and torch.backends.mps.is_available()):
            raise RuntimeError('tsumugi_mps_requested_but_unavailable')
        return requested
    if torch.cuda.is_available():
        return 'cuda'
    if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
        return 'mps'
    return 'cpu'


def midi_summary(path: Path) -> dict:
    midi = mido.MidiFile(path)
    pitches = []
    tempos = []
    note_on_count = 0
    for track in midi.tracks:
        for msg in track:
            if msg.type == 'note_on' and getattr(msg, 'velocity', 0) > 0:
                note_on_count += 1
                pitches.append(int(msg.note))
            elif msg.type == 'set_tempo':
                tempos.append(float(mido.tempo2bpm(msg.tempo)))
    return {
        'notes': {
            'count': note_on_count,
            'pitch_min': min(pitches) if pitches else None,
            'pitch_max': max(pitches) if pitches else None,
        },
        'tempo': {
            'event_count': len(tempos),
            'bpm_min': min(tempos) if tempos else None,
            'bpm_max': max(tempos) if tempos else None,
            'bpm_median': statistics.median(tempos) if tempos else None,
        },
        'duration_s': float(midi.length),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--context', required=True)
    args = p.parse_args()

    context = json.loads(Path(args.context).read_text(encoding='utf-8'))
    if not isinstance(context, dict):
        raise ValueError('context_must_be_object')

    requested_device = str(context.get('advanced_amt_device') or os.getenv('TSUMUGI_DEVICE') or 'auto')
    device = resolve_device(requested_device)
    model_type = str(context.get('advanced_amt_model_type') or os.getenv('TSUMUGI_MODEL_TYPE') or 'default')
    checkpoint = Path(str(context.get('advanced_amt_checkpoint') or os.getenv('TSUMUGI_CHECKPOINT') or '')).expanduser().resolve()
    if not checkpoint.is_file():
        raise RuntimeError('TSUMUGI_CHECKPOINT_must_reference_preprovisioned_local_file')
    checkpoint_sha = sha256_file(checkpoint)

    with tempfile.TemporaryDirectory(prefix='maestro-tsumugi-') as td:
        midi_path = Path(td) / 'transcription.mid'
        command = [
            sys.executable,
            '-m', 'instrument_agnostic_amt.amt.cli.infer',
            '--audio', str(Path(args.input).resolve()),
            '--output-midi', str(midi_path),
            '--device', device,
            '--type', model_type,
            '--checkpoint', str(checkpoint),
        ]
        proc = subprocess.run(command, capture_output=True, text=True, timeout=int(os.getenv('TSUMUGI_TIMEOUT_S', '7200')))
        if proc.returncode != 0:
            raise RuntimeError(f'tsumugi_inference_failed:{proc.returncode}:{(proc.stderr or proc.stdout)[-2000:]}')
        if not midi_path.is_file():
            raise RuntimeError('tsumugi_produced_no_midi')
        summary = midi_summary(midi_path)
        midi_sha = sha256_file(midi_path)
        midi_size = midi_path.stat().st_size

    payload = {
        'implementation_version': str(os.getenv('TSUMUGI_REVISION') or 'f7411471a4de0ad3d430191de11b8623d67e5b38'),
        'model_family': 'anime-song/tsumugi',
        'model_type': model_type,
        'device': device,
        'checkpoint_name': checkpoint.name,
        'checkpoint_sha256': checkpoint_sha,
        'midi_sha256': midi_sha,
        'midi_size_bytes': midi_size,
        'midi_artifact_persisted': False,
        'midi_summary': summary,
        'source_midi_mutated': False,
        'canonical_transcription_promoted': False,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
