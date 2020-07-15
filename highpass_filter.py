'''
input: wav file
output: wav file with only high frequencies
'''

from scipy.io import wavfile
from scipy import signal
import numpy as np

def highpass_filter(y, sr):
    filter_stop_freq = 1500
    filter_pass_freq = 1500
    filter_order = 1001

    arr = np.asarray(y)
    print(arr[2000000])

    y = np.transpose(y)

    nyquist_rate = sr/2
    desired = (0, 0, 1, 1)
    bands = (0, filter_stop_freq, filter_pass_freq, nyquist_rate)
    filter_coefs = signal.firls(filter_order, bands, desired, nyq=nyquist_rate)

    return signal.filtfilt(filter_coefs, [1], y)

sr, x = wavfile.read('corpus/1 19.wav')

f_x = highpass_filter(x, sr)

f_x = np.transpose(f_x)
wavfile.write('highpass_wavs/1 19.wav', sr, f_x.astype(np.int16))