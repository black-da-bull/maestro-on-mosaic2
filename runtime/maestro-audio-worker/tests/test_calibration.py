from calibration import calibrate_beat_this, calibrate_structure, compare_midi_summaries, calibrate_embedding_threshold


def main():
    beat=calibrate_beat_this({'beats_s':[0,0.6,1.2,1.8],'downbeats_s':[0],'tempo_bpm':100.0},expected_bpm=103.0,expected_duration_s=2.4,midi_tempo_min_bpm=94.8,midi_tempo_max_bpm=102.6,midi_tempo_median_bpm=100.65)
    assert beat['status']=='assessed' and abs(beat['median_ibi_tempo_bpm']-100)<1e-6 and beat['within_midi_observed_range'] is True
    structure=calibrate_structure({'segments':[{'label':'Verse 1','start_s':0,'end_s':10},{'label':'Hook','start_s':10,'end_s':20}]},['Verse','Chorus'],expected_duration_s=20)
    assert structure['sequence_similarity']==1.0
    midi=compare_midi_summaries({'source':{'sha256':'a'},'notes':{'count':100,'pitch_min':40,'pitch_max':80},'tempo':{'bpm_median':100},'duration_s':10},{'source':{'sha256':'b'},'notes':{'count':90,'pitch_min':42,'pitch_max':79},'tempo':{'bpm_median':101},'duration_s':9.5})
    assert midi['note_count_delta']==-10 and midi['tempo_median_delta_bpm']==1.0
    insufficient=calibrate_embedding_threshold([{'label':'positive','distance':.1},{'label':'negative','distance':.7}])
    assert insufficient['status']=='insufficient_data' and insufficient['threshold'] is None
    candidate=calibrate_embedding_threshold([{'label':'positive','distance':x} for x in [.1,.15,.2]]+[{'label':'negative','distance':x} for x in [.7,.8,.9]])
    assert candidate['status']=='candidate' and candidate['universal_quality_score'] is False and candidate['auto_promotion'] is False
    print({'passed':True,'checks':8})


if __name__=='__main__': main()
