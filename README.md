WAVLabs is a set of pipelines and a generative audio implementation for creating instrumentals

## Requirements
```bash
pip install magenta
pip install midiutil
pip install flask
pip install midi2audio
```

## Usage
Get some of your favourite songs as wav files and place them in a directory called 'corpus'. Then download the Wavenet checkpoint from [here](http://download.magenta.tensorflow.org/models/nsynth/wavenet-ckpt.tar). Finally, simply run the pipelines! It will handle everything from converting the wavs into MIDI to training the TensorFlow Magenta model for you.

```bash
run_pipelines.sh
```

Drum pattern generation will work best with songs that have crisp kicks and hats. Melody generation will work best when there are some bars of melody at the beginning of the track to use as a sample. These can be checked by simply going through some of the intermediate folders.

## Architecture
![WAVLabs Diagram](/images/wavlabs-diagram.png)

## Demos
The following are raw demos, meaning output from WAVLabs directly overlayed into a wav file with no doctoring

[Drums Demo 1](https://drive.google.com/file/d/1oEGbzYhdsvTDCwdosFX9pfvZfCKioaGi/view?usp=sharing)
[Drums Demo 2](https://drive.google.com/file/d/14FyamkD6eHEWGEJ6TdHz09-38WQWRDnc/view?usp=sharing)
[Drums Demo 3](https://drive.google.com/file/d/1pGQhKfm5IxdI_risaPDiJ1ALMv9a7dx8/view?usp=sharing)

[Melody Demo 1](https://drive.google.com/file/d/1RTJ9O6vZdIFhi1NOPojBhHv89IZWwWjN/view?usp=sharing)
[Melody Demo 2](https://drive.google.com/file/d/17TqvJtGvfY4BTp2ps0Stvr6XPmXDqUnV/view?usp=sharing)
[Melody Demo 3](https://drive.google.com/file/d/16uOnPjXAGZ8fQHPf6i02V9ua1K9lEuLz/view?usp=sharing)

## Notes
The pipelines output some really unique rhythms and timbres. It would be interesting to use these as a groundwork for an industrial hip-hop style music project, refining them with effects and fine-tuning some of the drum patterns. Further, using GANSynth to generate MIDIs for the timbres produced by NSynth would be an interesting mix of the two models, and could produce some interesting melodies.

The field of neural networks for music production is rapidly expanding, and I am excited to see how it will improve in the future!