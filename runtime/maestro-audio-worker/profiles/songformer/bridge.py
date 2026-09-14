from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_tree(root: Path) -> str:
    files = sorted(p for p in root.rglob('*') if p.is_file())
    if not files:
        raise RuntimeError('songformer_model_directory_empty')
    h = hashlib.sha256()
    for child in files:
        rel = child.relative_to(root).as_posix().encode('utf-8')
        h.update(len(rel).to_bytes(8, 'big'))
        h.update(rel)
        h.update(bytes.fromhex(sha256_file(child)))
    return h.hexdigest()


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

    model_dir = Path(str(context.get('songformer_model_dir') or os.getenv('SONGFORMER_MODEL_DIR') or '')).expanduser().resolve()
    if not model_dir.is_dir():
        raise RuntimeError('SONGFORMER_MODEL_DIR_must_be_preprovisioned_local_directory')
    model_sha = sha256_tree(model_dir)

    requested = str(context.get('songformer_device') or os.getenv('SONGFORMER_DEVICE') or 'auto')
    if requested == 'auto':
        device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    else:
        device = requested
    if device.startswith('cuda') and not torch.cuda.is_available():
        raise RuntimeError('songformer_cuda_requested_but_unavailable')

    model = AutoModel.from_pretrained(str(model_dir), trust_remote_code=True, local_files_only=True, low_cpu_mem_usage=False)
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
        'model_dir_name': model_dir.name,
        'model_dir_sha256': model_sha,
        'device': device,
        'expected_input_sample_rate_hz': 24000,
        'segments': segments,
        'segment_count': len(segments),
        'canonical_structure_promoted': False,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
