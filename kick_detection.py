import os
from midiutil import MIDIFile
import math
import numpy as np
import tempo_detection

# returns the closest value in an array to some other value (min of distances)
def closest_val(arr, val):
    arr = np.asarray(arr)
    idx = (np.abs(arr - val)).argmin()
    # also return the index of the value
    return arr[idx], idx

for filename in os.listdir('./lowpass_wavs'):
    # get onsets of each low-passed wav file
    os.system("aubio onset \"lowpass_wavs\\" + filename + "\" -t 0.30 -s -70 -m hfc > tmp")
    result = open('tmp').read()

    onsets = result.split("\n")

    # midi parameters
    pitch = 60
    track = 0
    channel = 0
    duration = 0.25
    inS = open('tempos.txt').read()
    # tempo detection done through essentia
    bpm = int(tempo_detection.detect(filename))
    volume = 100

    midi = MIDIFile(1)
    midi.addTempo(track, 0, bpm)

    # extract the times from the aubio output as a list, normalized by bpm
    times = []
    for onset in onsets:
        if onset != "":
            sec = float(onset.strip())
            time = (sec / 60) * bpm

            times.append(time)

    assert(len(times) > 0)

    # shift back so that the first onset starts from 0
    shifted_times = []
    for time in times:
        shifted_times.append(time - times[0])

    # quantize based on 0.25 of a beat
    i = 0.
    while i < math.ceil(shifted_times[len(shifted_times) - 1]):
        close, cI = closest_val(shifted_times, i)

        if abs(close - i) < 0.1:
            shifted_times[cI] = i

        i += 0.25

    # fill in notes into midi file and output to new folder
    for time in shifted_times:
        midi.addNote(track, channel, pitch, time, duration, volume)

    with open("detected_kicks/" + "".join(filename.split(".")[:-1]) + ".mid", "wb") as out:
        midi.writeFile(out)