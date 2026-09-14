from __future__ import annotations

from typing import Any
import math
import statistics


def _norm_label(value: str) -> str:
    text = ''.join(ch.lower() if ch.isalnum() else ' ' for ch in value)
    aliases = {'pre chorus': 'prechorus', 'prechorus': 'prechorus', 'intro': 'intro', 'outro': 'outro', 'verse': 'verse', 'chorus': 'chorus', 'hook': 'chorus', 'bridge': 'bridge'}
    parts = ' '.join(text.split())
    for key, val in aliases.items():
        if parts.startswith(key): return val
    return parts


def _levenshtein(a: list[str], b: list[str]) -> int:
    prev = list(range(len(b)+1))
    for i, x in enumerate(a, 1):
        cur = [i]
        for j, y in enumerate(b, 1):
            cur.append(min(cur[-1]+1, prev[j]+1, prev[j-1] + (x != y)))
        prev = cur
    return prev[-1]


def calibrate_beat_this(result: dict[str, Any] | None, *, expected_bpm: float | None = None,
                        expected_duration_s: float | None = None, midi_tempo_min_bpm: float | None = None,
                        midi_tempo_max_bpm: float | None = None, midi_tempo_median_bpm: float | None = None) -> dict[str, Any]:
    if not result:
        return {'status':'not_assessed','notes':['Beat This did not return a validated result.']}
    beats = [float(x) for x in result.get('beats_s') or []]
    downbeats = [float(x) for x in result.get('downbeats_s') or []]
    reported = result.get('tempo_bpm')
    if len(beats) < 2:
        return {'status':'not_assessed','beat_count':len(beats),'downbeat_count':len(downbeats),'reported_tempo_bpm':reported,'notes':['At least two beats are required.']}
    ibis = [b-a for a,b in zip(beats, beats[1:]) if b-a > 1e-9]
    median_ibi = statistics.median(ibis) if ibis else None
    median_tempo = 60.0 / median_ibi if median_ibi else None
    mean_ibi = statistics.fmean(ibis) if ibis else None
    cv = statistics.pstdev(ibis) / mean_ibi if ibis and mean_ibi and len(ibis)>1 else 0.0 if ibis else None
    coverage = None
    if expected_duration_s and expected_duration_s > 0:
        coverage = max(0.0, min(1.0, (beats[-1]-beats[0]) / expected_duration_s))
    return {
        'status':'assessed','beat_count':len(beats),'downbeat_count':len(downbeats),
        'reported_tempo_bpm':float(reported) if reported is not None else None,
        'median_ibi_tempo_bpm':median_tempo,'beat_interval_cv':cv,'expected_bpm':expected_bpm,
        'expected_bpm_delta':(float(reported)-expected_bpm) if reported is not None and expected_bpm is not None else None,
        'first_beat_s':beats[0],'last_beat_s':beats[-1],'coverage_fraction':coverage,
        'midi_tempo_median_delta_bpm':(median_tempo-midi_tempo_median_bpm) if median_tempo is not None and midi_tempo_median_bpm is not None else None,
        'within_midi_observed_range':(midi_tempo_min_bpm <= median_tempo <= midi_tempo_max_bpm) if median_tempo is not None and midi_tempo_min_bpm is not None and midi_tempo_max_bpm is not None else None,
        'notes':['Agreement/stability evidence only; no canonical tempo promotion.']
    }


def calibrate_structure(result: dict[str, Any] | None, declared_sections: list[Any], *, expected_duration_s: float | None = None) -> dict[str, Any]:
    if not result:
        return {'status':'not_assessed','notes':['SongFormer did not return a validated result.']}
    segments = result.get('segments') or []
    detected = [_norm_label(str(s.get('label',''))) for s in segments]
    declared = []
    declared_starts = []
    for s in declared_sections:
        if isinstance(s, str):
            declared.append(_norm_label(s)); declared_starts.append(None)
        elif isinstance(s, dict):
            declared.append(_norm_label(str(s.get('label','')))); declared_starts.append(s.get('start_s'))
    edit = _levenshtein(declared, detected) if declared else None
    sim = 1.0 - edit/max(len(declared),len(detected),1) if edit is not None else None
    coverage = None
    if segments and expected_duration_s:
        coverage=max(0.0,min(1.0,(float(segments[-1]['end_s'])-float(segments[0]['start_s']))/expected_duration_s))
    boundary_errors=[]
    starts=[float(s['start_s']) for s in segments if 'start_s' in s]
    for x in declared_starts:
        if x is not None and starts: boundary_errors.append(min(abs(float(x)-v) for v in starts))
    return {'status':'assessed','detected_count':len(detected),'declared_count':len(declared),'normalized_declared':declared,'normalized_detected':detected,'sequence_edit_distance':edit,'sequence_similarity':sim,'duration_coverage_fraction':coverage,'boundary_mean_abs_error_s':statistics.fmean(boundary_errors) if boundary_errors else None,'notes':['Functional labels normalized for comparison only; no MAP/canon promotion.']}


def compare_midi_summaries(reference: dict[str, Any] | None, inferred: dict[str, Any] | None) -> dict[str, Any]:
    if not reference or not inferred:
        return {'status':'not_assessed','notes':['Both reference and inferred MIDI summaries are required.']}
    rcount=int(reference['notes']['count']); icount=int(inferred['notes']['count'])
    def delta(a,b): return None if a is None or b is None else int(b)-int(a)
    rt=reference.get('tempo',{}).get('bpm_median'); it=inferred.get('tempo',{}).get('bpm_median')
    rdur=float(reference.get('duration_s') or 0); idur=float(inferred.get('duration_s') or 0)
    return {'status':'assessed','reference_sha256':reference.get('source',{}).get('sha256'),'inferred_sha256':inferred.get('source',{}).get('sha256'),'note_count_ratio':icount/rcount if rcount else None,'note_count_delta':icount-rcount,'pitch_min_delta':delta(reference['notes'].get('pitch_min'),inferred['notes'].get('pitch_min')),'pitch_max_delta':delta(reference['notes'].get('pitch_max'),inferred['notes'].get('pitch_max')),'tempo_median_delta_bpm':float(it-rt) if it is not None and rt is not None else None,'duration_ratio':idur/rdur if rdur>0 else None,'notes':['Summary-level agreement only; source MIDI remains distinct from inferred MIDI.']}


def _score(samples, threshold):
    pos=[s for s in samples if s['label']=='positive']; neg=[s for s in samples if s['label']=='negative']
    sens=sum(float(s['distance'])<=threshold for s in pos)/len(pos)
    spec=sum(float(s['distance'])>threshold for s in neg)/len(neg)
    return (sens+spec)/2,sens,spec


def _best(samples):
    values=sorted(set(float(s['distance']) for s in samples)); candidates=[]
    if values:
        candidates=[max(0.0,values[0]-1e-12), *[(a+b)/2 for a,b in zip(values,values[1:])], values[-1]+1e-12]
    best=None
    for threshold in candidates:
        score,sens,spec=_score(samples,threshold); key=(score,min(sens,spec),-threshold)
        if best is None or key>best[0]: best=(key,threshold,score,sens,spec)
    if best is None: raise ValueError('no_calibration_samples')
    return best[1:]


def calibrate_embedding_threshold(samples: list[dict[str, Any]], *, minimum_per_class: int = 3, metric: str = 'cosine_distance') -> dict[str, Any]:
    clean=[]
    for s in samples:
        if s.get('label') not in {'positive','negative'}: raise ValueError('invalid_label')
        d=float(s['distance'])
        if not math.isfinite(d) or d<0: raise ValueError('invalid_distance')
        clean.append({'label':s['label'],'distance':d})
    pos=sum(s['label']=='positive' for s in clean); neg=sum(s['label']=='negative' for s in clean)
    if pos<minimum_per_class or neg<minimum_per_class:
        return {'status':'insufficient_data','metric':metric,'positive_n':pos,'negative_n':neg,'threshold':None,'balanced_accuracy':None,'jackknife_threshold_min':None,'jackknife_threshold_max':None,'universal_quality_score':False,'auto_promotion':False,'notes':[f'Need at least {minimum_per_class} operator-labeled examples per class; no threshold promoted.']}
    threshold,score,sens,spec=_best(clean); jack=[]
    for i in range(len(clean)):
        subset=clean[:i]+clean[i+1:]
        if any(s['label']=='positive' for s in subset) and any(s['label']=='negative' for s in subset): jack.append(_best(subset)[0])
    return {'status':'candidate','metric':metric,'positive_n':pos,'negative_n':neg,'threshold':threshold,'balanced_accuracy':score,'sensitivity':sens,'specificity':spec,'jackknife_threshold_min':min(jack) if jack else None,'jackknife_threshold_max':max(jack) if jack else None,'universal_quality_score':False,'auto_promotion':False,'notes':['Candidate threshold is corpus-specific evidence only; renderer policy requires replication and operator promotion.']}
