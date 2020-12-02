'''
input: wav file
output: wav file with only high frequencies
'''

from scipy.io import wavfile
from scipy import signal
import numpy as np
import os

def highpass_filter(y, sr):
    filter_stop_freq = 4000
    filter_pass_freq = 4000
    filter_order = 1001

    y = np.transpose(y)

    nyquist_rate = sr/2
    desired = (0, 0, 1, 1)
    bands = (0, filter_stop_freq, filter_pass_freq, nyquist_rate)
    filter_coefs = signal.firls(filter_order, bands, desired, nyq=nyquist_rate)

    return signal.filtfilt(filter_coefs, [1], y)

for filename in os.listdir('./corpus'):
    sr, x = wavfile.read('corpus/' + filename)

    f_x = highpass_filter(x, sr)

    f_x = np.transpose(f_x)
    wavfile.write('highpass_wavs/' + filename, sr, f_x.astype(np.int16))