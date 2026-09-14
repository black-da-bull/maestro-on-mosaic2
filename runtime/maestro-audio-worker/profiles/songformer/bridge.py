from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--context', required=True)
    args = p.parse_args()

    import torch
    from transformers import AutoModel

    context = json.loads(Path(args.context).read_text(encoding='utf-8'))
    if not isinstance(context, dict):
        raise ValueError('context_must_be_object')

    model_dir = str(context.get('songformer_model_dir') or os.getenv('SONGFORMER_MODEL_DIR') or '').strip()
    if not model_dir or not Path(model_dir).is_dir():
        raise RuntimeError('SONGFORMER_MODEL_DIR_must_be_preprovisioned_local_directory')

    requested = str(context.get('songformer_device') or os.getenv('SONGFORMER_DEVICE') or 'auto')
    if requested == 'auto':
        device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    else:
        device = requested
    if device.startswith('cuda') and not torch.cuda.is_available():
        raise RuntimeError('songformer_cuda_requested_but_unavailable')

    model = AutoModel.from_pretrained(model_dir, trust_remote_code=True, low_cpu_mem_usage=False)
    model.to(device)
    model.eval()
    result = model(args.input)
    if not isinstance(result, list):
        raise RuntimeError('songformer_result_must_be_list')

    segments = []
    for index, item in enumerate(result):
        if not isinstance(item, dict):
            raise RuntimeError(f'songformer_segment_{index}_must_be_object')
        start = item.get('start')
        end = item.get('end')
        label = item.get('label')
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)) or not isinstance(label, str):
            raise RuntimeError(f'songformer_segment_{index}_invalid')
        if float(end) < float(start):
            raise RuntimeError(f'songformer_segment_{index}_negative_duration')
        segments.append({'start_s': float(start), 'end_s': float(end), 'label': label})

    payload = {
        'implementation_version': str(os.getenv('SONGFORMER_MODEL_REVISION') or 'local_model_dir'),
        'model_family': 'ASLP-lab/SongFormer',
        'device': device,
        'expected_input_sample_rate_hz': 24000,
        'segments': segments,
        'segment_count': len(segments),
        'canonical_structure_promoted': False,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
