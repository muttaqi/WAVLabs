import essentia.standard as es

def detect(file):
    features, features_frames = es.MusicExtractor(lowlevelStats=['mean', 'stdev'],
                                                rhythmStats=['mean', 'stdev'],
                                                tonalStats=['mean', 'stdev'])('1 19.wav')

    bpm = features['rhythm.bpm']

    bpm = round(bpm)
    
    return bpm