# text_to_speech

This Python script provides a wrapper class for the pyttsx3 text-to-speech library, enabling quick and easy generation of speech from text in your Python applications.

## Features

* Easy to use
* Supports different speech rates and volumes
* Ability to switch between different available voices
* Provide a list of available voices

## Quick Start

First, make sure you have pyttsx3 installed:

```bash
pip install pyttsx3
```

Then, you can use the 'TextToSpeech' class as follows:

```python
from text_to_speech import TextToSpeech

tts = TextToSpeech(speech_rate=150, volume=0.8, voice_name="David")

# Say something!
tts.say_text("Hello, world!")
```

## Documentation
TextToSpeech has the following methods:

* __init__(self, speech_rate: int = 200, volume: float = 1.0, voice_name: str = None): Initializes the text-to-speech engine with the given speech rate, volume, and voice. If no voice is provided, defaults to the first available voice.
* __str__(self) -> str: Returns a string representation of the TextToSpeech object.
* get_voices(self) -> dict: Returns a dictionary of the available voices.
* set_speech_rate(self, speech_rate: int) -> None: Sets the speech rate of the TTS engine.
* set_volume(self, volume: float) -> None: Sets the volume of the TTS engine.
* set_voice(self, voice_name: str) -> None: Sets the voice of the TTS engine.
* say_text(self, text: str) -> None: Speaks the given text.
* stop(self) -> None: Stops the TTS engine.