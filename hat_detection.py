import os
from midiutil import MIDIFile

os.system("aubio onset \"highpass_wavs\\1 19.wav\" -t 0.8 -s -70 -m hfc > tmp")
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

for onset in onsets:
    if onset != "":
        sec = float(onset.strip())
        time = (sec / 60) * bpm
        midi.addNote(track, channel, pitch, time, duration, volume)

with open("detected_hats/1 19.mid", "wb") as out:
    midi.writeFile(out)