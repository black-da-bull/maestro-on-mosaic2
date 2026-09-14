from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def resolve_device(requested: str, torch) -> str:
    requested = requested.strip().lower()
    if requested == 'auto':
        return 'cuda' if torch.cuda.is_available() else 'cpu'
    if requested not in {'cpu', 'cuda'}:
        raise RuntimeError('clap_device_must_be_auto_cpu_or_cuda')
    if requested == 'cuda' and not torch.cuda.is_available():
        raise RuntimeError('clap_cuda_requested_but_unavailable')
    return requested


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--context', required=True)
    args = p.parse_args()

    import laion_clap
    import torch

    context = json.loads(Path(args.context).read_text(encoding='utf-8'))
    if not isinstance(context, dict):
        raise ValueError('context_must_be_object')

    checkpoint = Path(str(context.get('clap_checkpoint') or os.getenv('CLAP_CHECKPOINT') or '')).expanduser().resolve()
    if not checkpoint.is_file():
        raise RuntimeError('CLAP_CHECKPOINT_must_reference_preprovisioned_local_file')

    requested_device = str(context.get('clap_device') or os.getenv('CLAP_DEVICE') or 'auto')
    device_name = resolve_device(requested_device, torch)
    device = torch.device(device_name)
    model_name = str(context.get('clap_model') or os.getenv('CLAP_MODEL') or 'HTSAT-base')
    enable_fusion = bool(context.get('clap_enable_fusion', False))
    model = laion_clap.CLAP_Module(enable_fusion=enable_fusion, amodel=model_name, device=device)
    model.load_ckpt(str(checkpoint))

    input_path = Path(args.input).resolve()
    if not input_path.is_file():
        raise RuntimeError('clap_input_audio_missing')
    audio_embedding = model.get_audio_embedding_from_filelist(x=[str(input_path)], use_tensor=False)[0]
    audio_vector = [float(x) for x in audio_embedding.tolist()]
    text = context.get('clap_text')
    text_vector = None
    if isinstance(text, str) and text.strip():
        text_embedding = model.get_text_embedding([text], use_tensor=False)[0]
        text_vector = [float(x) for x in text_embedding.tolist()]

    payload = {
        'implementation_version': importlib.metadata.version('laion-clap'),
        'model_family': 'LAION-AI/CLAP',
        'model_name': model_name,
        'enable_fusion': enable_fusion,
        'requested_device': requested_device,
        'device': device_name,
        'checkpoint_name': checkpoint.name,
        'checkpoint_sha256': sha256_file(checkpoint),
        'audio_embedding': audio_vector,
        'text_embedding': text_vector,
        'dimensions': len(audio_vector),
        'metric_interpretation': 'requires_project_specific_operator_labeled_calibration',
        'universal_quality_score': False,
        'renderer_policy_promoted': False,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
