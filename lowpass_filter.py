'''
input: wav file
output: wav file with only low frequencies
'''

from pydub import AudioSegment

song = AudioSegment.from_wav('corpus/1 19.wav')
new = song.low_pass_filter(300)

AudioSegment.export(new, 'lowpass_wavs/1 19.wav', format='wav')