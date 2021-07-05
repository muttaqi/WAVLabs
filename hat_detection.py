import os
from midiutil import MIDIFile
import math
import numpy as np
import tempo_detection

# returns the closest value to a given value in an array
def closest_val(arr, val):
    arr = np.asarray(arr)
    idx = (np.abs(arr - val)).argmin()
    #also return the index
    return arr[idx], idx

# finds the closest quantized time for a given timestamp
def closest_dist(quants, time):
    quants = np.asarray(quants)
    dists = np.abs(quants - time)
    # minimum of differences
    idx = dists.argmin()
    #                 also return the timestamp of the closest quant
    return dists[idx], quants[idx]

# returns the sum of distances between two sets of times, one actual and one ideal
def sum_dists(times, quants):
    c = 0
    quantized_times = []
    # for every time find the closest quantized time and get the distance and add it to the count
    for time in times:
        dist, quantized_time = closest_dist(quants, time)
        c += dist
        quantized_times.append(quantized_time)

    #         also return the quantized times
    return c, list(dict.fromkeys(quantized_times))

# returns the best quantize increment for a hat roll
def best_quantize(times, current_set):
    quant_increments = [0.5, 0.25, 0.25/2, 0.25/3, 0.25/4, 0.25/6]
    least_quants = []
    least_dist = 100
    for inc in quant_increments:
        # get the quantized roll times for each increment
        c = current_set
        quants = []
        while c < current_set + 0.25:
            quants.append(c)
            c += inc

        # get the distance between these quantized times and the actual times
        total_dist, quantized_times = sum_dists(times, quants)

        # select for the smallest of these distances which we consider the best fit for quantizing
        if total_dist < least_dist:
            least_dist = total_dist
            least_quants = quantized_times

    return least_quants

for filename in os.listdir('./highpass_wavs'):
    # get onsets of high-pass audio
    os.system("aubio onset \"highpass_wavs\\" + filename + "\" -t 0.8 -s -70 -m hfc > tmp")
    result = open('tmp').read()
    os.remove('tmp')

    onsets = result.split("\n")

    # midi file parameters
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

    times = []
    # get times as list, normalized by bpm
    for onset in onsets:
        if onset != "":
            sec = float(onset.strip())
            time = (sec / 60) * bpm
            
            times.append(time)

    assert(len(times) > 0)

    # shift onsets back so first is at time = 0
    shifted_times = []
    for time in times:
        shifted_times.append(time - times[0])

    i = 0.
    # quantize on 0.5 multiples, merging onsets that are close together
    while i < math.ceil(shifted_times[len(shifted_times) - 1]):
        close, cI = closest_val(shifted_times, i)
        if abs(close - i) < 0.125:
            shifted_times[cI] = i

        i += 0.5


    all_quantized_times = []

    current_set = 0.
    # quantize at a higher rate for hi hat rolls
    while current_set < shifted_times[len(shifted_times) - 1]:
        roll_times = [x for x in shifted_times if x >= current_set and x < current_set + 0.5]

        if len(roll_times) > 0 and roll_times[0] == current_set:
            quantized_times = best_quantize(roll_times, current_set)
            all_quantized_times.extend(quantized_times)

        current_set += 0.5
    
    # fill our quantized notes into a midi file and output into new folder
    for time in all_quantized_times:
        midi.addNote(track, channel, pitch, time, duration, volume)

    with open("detected_hats/" + "".join(filename.split(".")[:-1]) + ".mid", "wb") as out:
        midi.writeFile(out)