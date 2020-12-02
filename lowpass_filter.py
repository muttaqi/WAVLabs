'''
input: wav file
output: wav file with only low frequencies
'''

from scipy.io import wavfile
import numpy as np
from scipy.signal import butter,filtfilt
import os

# Filter requirements.
T = 5.0         # Sample Period
fs = 30.0       # sample rate, Hz
cutoff = 0.3      # desired cutoff frequency of the filter, Hz ,      slightly higher than actual 1.2 Hz
nyq = 0.5 * fs  # Nyquist Frequency
order = 2       # sin wave can be approx represented as quadratic
n = int(T * fs) # total number of samples

def butter_lowpass_filter(data, cutoff, fs, order):
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients 
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

for filename in os.listdir('./corpus'):
    sr, x = wavfile.read('corpus/' + filename)

    x = x[:, 0]

    # Filter the data, and plot both the original and filtered signals.
    y = butter_lowpass_filter(x, cutoff, fs, order)

    y = np.asarray(y, dtype=np.int16)

    wavfile.write('lowpass_wavs/' + filename, sr, y)