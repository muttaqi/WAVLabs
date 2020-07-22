WAVLabs is a set of pipelines and a generative audio implementation for creating instrumentals

## Requirements
```bash
pip install magenta
pip install midiutil
pip install flask
pip install midi2audio
```

## Usage
Acquire a directory of wav files and place them in a directory called 'corpus'. Then simply run the pipelines! It will handle everything from converting the wavs into MIDI to training the TensorFlow Magenta model for you.

```bash
run_pipelines.sh
```

## Architecture
![WAVLabs Diagram](/images/WAVLabs_Diagram.png)

## Future Plans
I'm currently working on integrating the pipelines into a synthesizer generator with unique timbres using GANSynth.