import os
from midiutil import MIDIFile
import math
import numpy as np

def closest_val(arr, val):
    arr = np.asarray(arr)
    idx = (np.abs(arr - val)).argmin()
    #also return the index
    return arr[idx], idx

def closest_dist(quants, time):
    quants = np.asarray(quants)
    dists = np.abs(quants - time)
    idx = dists.argmin()
    #also return the closes quant
    return dists[idx], quants[idx]

def sum_dists(times, quants):
    c = 0
    quantized_times = []
    for time in times:
        dist, quantized_time = closest_dist(quants, time)
        c += dist
        quantized_times.append(quantized_time)

    #also return the quantized times
    return c, list(dict.fromkeys(quantized_times))

def best_quantize(times):
    quant_increments = [0.5, 0.25, 0.25/2, 0.25/3, 0.25/4, 0.25/6]
    least_quants = []
    least_dist = 100
    for inc in quant_increments: 
        c = current_set
        quants = []
        while c < current_set + 0.25:
            quants.append(c)
            c += inc

        #print("quants: ", quants)

        total_dist, quantized_times = sum_dists(times, quants)

        #print("total_dist: ", total_dist)
        #print("quantized_times: ", quantized_times)

        if total_dist < least_dist:
            least_dist = total_dist
            least_quants = quantized_times

    return least_quants

for filename in os.listdir('./highpass_wavs'):
    os.system("aubio onset \"highpass_wavs\\" + filename + "\" -t 0.8 -s -70 -m hfc > tmp")
    result = open('tmp').read()
    os.remove('tmp')

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

    i = 0.
    while i < math.ceil(shifted_times[len(shifted_times) - 1]):
        close, cI = closest_val(shifted_times, i)
        #print("quarters: ", i, close)
        if abs(close - i) < 0.125:
            shifted_times[cI] = i

        i += 0.5

    #print("shifted_times: ", shifted_times)

    all_quantized_times = []

    #now we handle the rest which are rolls

    current_set = 0.
    #set_roll_times = []
    while current_set < shifted_times[len(shifted_times) - 1]:
        roll_times = [x for x in shifted_times if x >= current_set and x < current_set + 0.5]

        if len(roll_times) > 0 and roll_times[0] == current_set:
            quantized_times = best_quantize(roll_times)
            all_quantized_times.extend(quantized_times)

        current_set += 0.5
    '''
    for j, time in enumerate(shifted_times):
        print("set_roll_times: ", set_roll_times)

        if j > 20:
            break

        if time > current_set + 0.25 and len(set_roll_times) == 1:
            current_set = math.floor(time * 4)/4

        print("checking: ", time, current_set)

        if time < current_set + 0.25:
            print("adding: ", time)
            set_roll_times.append(time)
        
        else:
            print("trying: ", set_roll_times)
            if len(set_roll_times) == 0 or set_roll_times[0] != current_set:
                all_quantized_times.append(current_set)
                current_set += 0.25
                set_roll_times = [time]

            else:

                #print("set_roll_times: ", set_roll_times)
                
                quantized_times = best_quantize(set_roll_times)

                all_quantized_times.extend(quantized_times)
                #print("quantized_times: ", quantized_times)

                current_set += 0.25
                set_roll_times = [time]
                #print("current_set: ", current_set)
    '''
    for time in all_quantized_times:
        midi.addNote(track, channel, pitch, time, duration, volume)

    with open("detected_hats/" + "".join(filename.split(".")[:-1]) + ".mid", "wb") as out:
        midi.writeFile(out)