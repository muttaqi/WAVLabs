from pydub import AudioSegment
import os

for filename in os.listdir('./lowpass_wavs'):
    print('Splicing: ' + filename + '...')

    # get onsets of each low-passed wav file
    os.system("aubio onset \"lowpass_wavs\\" + filename + "\" -t 0.9 -s -20 -m hfc > tmp")
    result = open('tmp').read()

    onsets = result.split("\n")

    # extract the first onset from the aubio output
    firstOnset = 0
    for onset in onsets:
        if onset != "":
            firstOnset = float(onset.strip())
            break
    
    # splice until first onset
    spliced = AudioSegment.from_wav("corpus/" + filename)
    spliced = spliced[:(firstOnset * 1000)]
    spliced.export('samples/' + filename, format="wav")
    
