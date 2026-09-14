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


def require_file(path: Path, label: str) -> Path:
    path = path.expanduser().resolve()
    if not path.is_file():
        raise RuntimeError(f'{label}_must_reference_preprovisioned_local_file')
    return path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--context', required=True)
    args = p.parse_args()

    import torch

    context = json.loads(Path(args.context).read_text(encoding='utf-8'))
    if not isinstance(context, dict):
        raise ValueError('context_must_be_object')
    if not torch.cuda.is_available():
        raise RuntimeError('songformer_cuda_required_by_upstream_inference_path')

    repo_root = Path(os.getenv('SONGFORMER_ROOT', '/opt/SongFormer')).resolve()
    runtime_root = repo_root / 'src' / 'SongFormer'
    infer_script = require_file(runtime_root / 'infer' / 'infer.py', 'SONGFORMER_INFER_SCRIPT')

    checkpoint = require_file(
        Path(str(context.get('songformer_checkpoint') or os.getenv('SONGFORMER_CHECKPOINT') or '/models/songformer/ckpts/SongFormer.safetensors')),
        'SONGFORMER_CHECKPOINT',
    )
    config = require_file(
        Path(str(context.get('songformer_config') or os.getenv('SONGFORMER_CONFIG') or runtime_root / 'configs' / 'SongFormer.yaml')),
        'SONGFORMER_CONFIG',
    )
    musicfm_model = require_file(
        Path(str(context.get('songformer_musicfm_checkpoint') or os.getenv('SONGFORMER_MUSICFM_CHECKPOINT') or '/models/songformer/ckpts/MusicFM/pretrained_msd.pt')),
        'SONGFORMER_MUSICFM_CHECKPOINT',
    )
    musicfm_stats = require_file(
        Path(str(context.get('songformer_musicfm_stats') or os.getenv('SONGFORMER_MUSICFM_STATS') or '/models/songformer/ckpts/MusicFM/msd_stats.json')),
        'SONGFORMER_MUSICFM_STATS',
    )
    hf_home = Path(str(context.get('songformer_hf_home') or os.getenv('SONGFORMER_HF_HOME') or '/models/songformer/hf')).expanduser().resolve()
    if not hf_home.is_dir() or not any(p.is_file() for p in hf_home.rglob('*')):
        raise RuntimeError('SONGFORMER_HF_HOME_must_contain_preprovisioned_MuQ_cache')

    # Upstream infer.py expects MusicFM under cwd/ckpts/MusicFM. The profile
    # Docker image symlinks that directory to the mounted /models tree.
    expected_musicfm_model = (runtime_root / 'ckpts' / 'MusicFM' / 'pretrained_msd.pt').resolve()
    expected_musicfm_stats = (runtime_root / 'ckpts' / 'MusicFM' / 'msd_stats.json').resolve()
    if expected_musicfm_model != musicfm_model or expected_musicfm_stats != musicfm_stats:
        raise RuntimeError('songformer_musicfm_mount_must_match_profile_ckpts_symlink')

    input_audio = Path(args.input).resolve()
    if not input_audio.is_file():
        raise RuntimeError('songformer_input_audio_missing')

    gpu_visible = str(context.get('songformer_cuda_visible_devices') or os.getenv('SONGFORMER_CUDA_VISIBLE_DEVICES') or '0')
    with tempfile.TemporaryDirectory(prefix='maestro-songformer-') as td:
        td_path = Path(td)
        scp = td_path / 'input.scp'
        out_dir = td_path / 'output'
        scp.write_text(str(input_audio) + '\n', encoding='utf-8')
        out_dir.mkdir()

        env = os.environ.copy()
        third_party = str(repo_root / 'src' / 'third_party')
        env['PYTHONPATH'] = third_party + (os.pathsep + env['PYTHONPATH'] if env.get('PYTHONPATH') else '')
        env['CUDA_VISIBLE_DEVICES'] = gpu_visible
        env['HF_HOME'] = str(hf_home)
        env['HF_HUB_OFFLINE'] = '1'
        env['TRANSFORMERS_OFFLINE'] = '1'
        env.setdefault('OMP_NUM_THREADS', '1')
        env.setdefault('MPI_NUM_THREADS', '1')
        env.setdefault('NCCL_P2P_DISABLE', '1')
        env.setdefault('NCCL_IB_DISABLE', '1')

        command = [
            sys.executable,
            str(infer_script),
            '-i', str(scp),
            '-o', str(out_dir),
            '--model', 'SongFormer',
            '--checkpoint', str(checkpoint),
            '--config_path', str(config),
            '-gn', '1',
            '-tn', '1',
        ]
        if bool(context.get('songformer_no_rule_post_processing', False)):
            command.append('--no_rule_post_processing')

        proc = subprocess.run(
            command,
            cwd=runtime_root,
            env=env,
            capture_output=True,
            text=True,
            timeout=int(os.getenv('SONGFORMER_TIMEOUT_S', '7200')),
        )
        if proc.returncode != 0:
            raise RuntimeError(f'songformer_inference_failed:{proc.returncode}:{(proc.stderr or proc.stdout)[-3000:]}')

        result_path = out_dir / f'{input_audio.stem}.json'
        if not result_path.is_file():
            raise RuntimeError(f'songformer_produced_no_result:{(proc.stderr or proc.stdout)[-3000:]}')
        result = json.loads(result_path.read_text(encoding='utf-8'))

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
        'implementation_version': str(os.getenv('SONGFORMER_MODEL_REVISION') or '139b2aa3b14bd1c6d961d0994e9fc975f1ef7fd5'),
        'model_family': 'ASLP-lab/SongFormer',
        'device': 'cuda',
        'cuda_visible_devices': gpu_visible,
        'checkpoint_name': checkpoint.name,
        'checkpoint_sha256': sha256_file(checkpoint),
        'musicfm_checkpoint_sha256': sha256_file(musicfm_model),
        'musicfm_stats_sha256': sha256_file(musicfm_stats),
        'muq_cache_sha256': sha256_tree(hf_home),
        'config_sha256': sha256_file(config),
        'expected_input_sample_rate_hz': 24000,
        'segments': segments,
        'segment_count': len(segments),
        'canonical_structure_promoted': False,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
