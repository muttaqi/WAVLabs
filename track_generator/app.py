from flask import Flask
import magenta
import os, os.path
import midi
from midi2audio import FluidSynth
import random

app = Flask(__name__)

os.system(
    'drums_rnn_generate --config=one_drum --run_dir=kick_log_dir/run --hparams="batch_size=64,rnn_layer_sizes=[64.64]" --output_dir=generated_kicks --num_outputs=1 --num_steps=32 --primer_drums="[(60,)]"'
)

os.system(
    'drums_rnn_generate --config=one_drum --run_dir=hat_log_dir/run --hparams="batch_size=64,rnn_layer_sizes=[64.64]" --output_dir=generated_hats --num_outputs=1 --num_steps=32 --primer_drums="[(60,)]"'
)

num_hats = len([name for name in os.listdir('./hats') if os.path.isfile(name)])
num_kicks = len([name for name in os.listdir('./hats') if os.path.isfile(name)])

hatI = random.randint(0, num_hats)
kickI = random.randint(0, num_kicks)

fsHat = FluidSynth('hats/{}.sf2'.format(hatI))
fsKick = FluidSynth('kicks/{}.sf2'.format(kickI))

generated_hats = os.listdir('generated_hats')[0]
generated_kicks = os.listdir('generated_kicks')[0]

fsHat.midi_to_audio(generated_hats, 'generated_hats/hats.wav')
fsKick.midi_to_audio(generated_kicks, 'generated_kicks/kicks.wav')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)