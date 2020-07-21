import os
from midiutil import MIDIFile
import math
import numpy as np

os.system("aubio onset \"lowpass_wavs\\1 19.wav\" -t 0.30 -s -70 -m hfc > tmp")
result = open('tmp').read()
#os.remove('tmp')

print(result)
onsets = result.split("\n")

pitch = 60
track = 0
channel = 0
duration = 0.25
inS = open('tempos.txt').read()
bpm = int(inS.strip())
volume = 100

midi = MIDIFile(1)
midi.addTempo(track, 0, bpm)

times = []
for onset in onsets:
    if onset != "":
        sec = float(onset.strip())
        time = (sec / 60) * bpm

        times.append(time)

assert(len(times) > 0)

shifted_times = []
for time in times:
    shifted_times.append(time - times[0])

def closest_val(arr, val):
    arr = np.asarray(arr)
    idx = (np.abs(arr - val)).argmin()
    #also return the index
    return arr[idx], idx

i = 0.
while i < math.ceil(shifted_times[len(shifted_times) - 1]):
    close, cI = closest_val(shifted_times, i)
    #print("quarters: ", i, close)
    if abs(close - i) < 0.1:
        shifted_times[cI] = i

    i += 0.25

for time in shifted_times:
    midi.addNote(track, channel, pitch, time, duration, volume)

with open("detected_kicks/1 19.mid", "wb") as out:
    midi.writeFile(out)