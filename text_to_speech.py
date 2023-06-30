# text_to_speech.py

import pyttsx3

class TextToSpeech():
    """
    A class for handling Text-to-Speech (TTS) operations.

    Args:
    speech_rate: int - The speed at which the TTS engine will speak.
    volume: float - The volume level of the TTS engine speech. Should be between 0.0 and 1.0.
    voice_name: str - The name of the voice to use for speech. If not provided, defaults to the first available voice.
    """
    
    def __init__(
            self,
            speech_rate: int = 200,
            volume: float = 1.0,
            voice_name: str = None
        ) -> None:
        self.engine = pyttsx3.init()

        # Retrieves all available voices, and creates a dictionary
        self.voices = self.engine.getProperty('voices') 
        self.voice_names = {voice.name: voice.id for voice in self.voices}

        # Sets speech rate, volume, and voice
        self.set_speech_rate(speech_rate)
        self.set_volume(volume)
        self.set_voice(voice_name if voice_name else self.voices[0].name)
        
    def __str__(self) -> str:
        speech_rate = self.engine.getProperty('rate')
        volume = self.engine.getProperty('volume')
        
        # Returns a string representation of the TextToSpeech object
        return f"TextToSpeech(rate={speech_rate}, volume={volume}, voice={self.voice_name})"
    
    def get_voices(self) -> dict:
        """
        Returns the dict of available voices.
        
        Args:
            None

        Returns:
            dict: dictionary of available voices to pick from
        """
        return self.voice_names
        
    def set_speech_rate(self, speech_rate: int) -> None:
        """
        Set the speech rate of the TTS engine.
        
        Args:
            speech_rate: int - The new speech rate.

        Returns:
            None
        """
        if speech_rate > 0:
            self.engine.setProperty('rate', speech_rate)
        else:
            raise ValueError(f"Speech rate must be a positive integer. Provided value is {speech_rate}")
        
    def set_volume(self, volume: float) -> None:
        """
        Set the volume of the TTS engine.
        
        Args:
            volume: float - The new volume level
            
        Returns:
            None
        """
        if 0.0 <= volume <= 1.0:
            self.engine.setProperty('volume', volume)
        else:
            raise ValueError(f"Volume must be a float between 0 and 1. Provided value is {volume}")
        
    def set_voice(self, voice_name: str) -> None:
        """
        Set the voice of the TTS engine.
        
        Args:
            voice_name: str - The nane of the new voice.
        
        Returns:
            None
        """
        try:
            voice_id = self.voice_names[voice_name]
            self.engine.setProperty('voice', voice_id)
            self.voice_name = voice_name
        except KeyError:
            raise ValueError(f'Voice "{voice_name}" not found. Available voices are: {list(self.voice_names.keys())}')               
        
    def say_text(self, text: str) -> None:
        """
        Speak the given text using the TTS engine.
        
        Args:
            text: str - The text to be spoken

        Returns:
            None
        """
        self.engine.say(text)
        self.engine.runAndWait()
        
    def stop(self) -> None:
        """
        Stop the TTS engine.
        
        Args:
            None

        Returns:
            None
        """
        self.engine.stop()