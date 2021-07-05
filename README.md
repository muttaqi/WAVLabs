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

## Demo
[Demo 1](https://drive.google.com/file/d/1oEGbzYhdsvTDCwdosFX9pfvZfCKioaGi/view?usp=sharing)
[Demo 2](https://drive.google.com/file/d/14FyamkD6eHEWGEJ6TdHz09-38WQWRDnc/view?usp=sharing)
[Demo 3](https://drive.google.com/file/d/1pGQhKfm5IxdI_risaPDiJ1ALMv9a7dx8/view?usp=sharing)

## Future Plans
I'm currently working on integrating the pipelines into a synthesizer generator with unique timbres using GANSynth.
