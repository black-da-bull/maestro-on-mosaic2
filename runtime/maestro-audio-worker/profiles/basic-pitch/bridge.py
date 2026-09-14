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


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--context', required=True)
    args = p.parse_args()

    from basic_pitch.inference import predict

    context = json.loads(Path(args.context).read_text(encoding='utf-8'))
    if not isinstance(context, dict):
        raise ValueError('context_must_be_object')

    _, midi_data, _ = predict(args.input)
    notes = [note for instrument in midi_data.instruments for note in instrument.notes]
    pitches = [int(note.pitch) for note in notes]

    with tempfile.TemporaryDirectory(prefix='maestro-basic-pitch-') as td:
        midi_path = Path(td) / 'transcription.mid'
        midi_data.write(str(midi_path))
        result = {
            'implementation_version': importlib.metadata.version('basic-pitch'),
            'model_family': 'spotify/basic-pitch',
            'runtime': 'python-3.11-sidecar',
            'midi_sha256': sha256_file(midi_path),
            'midi_size_bytes': midi_path.stat().st_size,
            'midi_artifact_persisted': False,
            'note_count': len(notes),
            'pitch_min': min(pitches) if pitches else None,
            'pitch_max': max(pitches) if pitches else None,
            'duration_s': float(midi_data.get_end_time()),
            'source_surface': context.get('source_surface', 'audio'),
            'warning': 'Generated MIDI is an inferred transcription; this bridge returns its identity/summary but does not replace or mutate source MIDI.'
        }

    Path(args.output).write_text(json.dumps(result, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
