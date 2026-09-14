from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import tempfile
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_path(path: Path) -> str:
    if path.is_file():
        return sha256_file(path)
    if not path.is_dir():
        raise RuntimeError('basic_pitch_model_artifact_not_found')
    h = hashlib.sha256()
    files = sorted(p for p in path.rglob('*') if p.is_file())
    if not files:
        raise RuntimeError('basic_pitch_model_artifact_directory_empty')
    for child in files:
        rel = child.relative_to(path).as_posix().encode('utf-8')
        h.update(len(rel).to_bytes(8, 'big'))
        h.update(rel)
        digest = bytes.fromhex(sha256_file(child))
        h.update(digest)
    return h.hexdigest()


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--context', required=True)
    args = p.parse_args()

    from basic_pitch import ICASSP_2022_MODEL_PATH
    from basic_pitch.inference import predict

    context = json.loads(Path(args.context).read_text(encoding='utf-8'))
    if not isinstance(context, dict):
        raise ValueError('context_must_be_object')

    model_path = Path(ICASSP_2022_MODEL_PATH).resolve()
    model_sha = sha256_path(model_path)
    _, midi_data, _ = predict(args.input)
    notes = [note for instrument in midi_data.instruments for note in instrument.notes]
    pitches = [int(note.pitch) for note in notes]

    with tempfile.TemporaryDirectory(prefix='maestro-basic-pitch-') as td:
        midi_path = Path(td) / 'transcription.mid'
        midi_data.write(str(midi_path))
        result = {
            'implementation_version': importlib.metadata.version('basic-pitch'),
            'model_family': 'spotify/basic-pitch',
            'runtime': 'isolated-python-3.11-profile',
            'model_artifact_name': model_path.name,
            'model_artifact_sha256': model_sha,
            'midi_sha256': sha256_file(midi_path),
            'midi_size_bytes': midi_path.stat().st_size,
            'midi_artifact_persisted': False,
            'note_count': len(notes),
            'pitch_min': min(pitches) if pitches else None,
            'pitch_max': max(pitches) if pitches else None,
            'duration_s': float(midi_data.get_end_time()),
            'source_surface': context.get('source_surface', 'audio'),
            'source_midi_mutated': False,
            'canonical_transcription_promoted': False,
            'warning': 'Generated MIDI is inferred evidence; this bridge returns its identity/summary and does not replace source MIDI.'
        }

    Path(args.output).write_text(json.dumps(result, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
