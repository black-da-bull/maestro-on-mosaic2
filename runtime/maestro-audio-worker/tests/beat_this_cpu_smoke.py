from __future__ import annotations

import json
import statistics
import tempfile
import wave
from pathlib import Path

import numpy as np


def make_clicks(path: Path, bpm: float = 100.0, seconds: float = 24.0, sr: int = 22050) -> None:
    samples = np.zeros(int(seconds * sr), dtype=np.float32)
    step = int(sr * 60.0 / bpm)
    pulse = max(64, int(0.012 * sr))
    window = np.hanning(pulse * 2)[:pulse].astype(np.float32)
    for i in range(0, len(samples), step):
        end = min(i + pulse, len(samples))
        samples[i:end] += 0.8 * window[:end-i]
    pcm = (np.clip(samples, -1, 1) * 32767).astype('<i2')
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(pcm.tobytes())


def main() -> None:
    from beat_this.inference import File2Beats
    with tempfile.TemporaryDirectory() as td:
        wav = Path(td) / 'clicks.wav'
        make_clicks(wav)
        tracker = File2Beats(checkpoint_path='small0', device='cpu', dbn=False)
        beats, downbeats = tracker(str(wav))
        beats = [float(x) for x in beats]
        assert len(beats) >= 8, beats
        ibis = [b-a for a,b in zip(beats, beats[1:]) if b > a]
        bpm = 60.0 / statistics.median(ibis)
        assert 80.0 <= bpm <= 120.0, bpm
        print(json.dumps({'passed': True, 'device': 'cpu', 'checkpoint': 'small0', 'beat_count': len(beats), 'median_ibi_bpm': bpm}, indent=2))


if __name__ == '__main__': main()
