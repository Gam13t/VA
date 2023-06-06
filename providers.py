import os
import openai

import pyttsx3 as base_tts_engine
import speech_recognition as speech_frame
from fuzzywuzzy import fuzz as voice_distortion

from config import filled_config as config


class TTSEngineProvider:
    """
    Class for handling TTS speech engine
    """

    def __init__(self):
        self.engine = base_tts_engine.init()

    @property
    def tts_engine(self):
        self.voices = self.engine.getProperty("voices")

        for voice in self.voices:
            if voice.name == "Microsoft Irina Desktop - Russian":
                self.engine.setProperty("voice", voice.id)

        return self.engine

    def speak(self, sentence_to_announce):
        self.tts_engine.say(sentence_to_announce)
        self.tts_engine.runAndWait()
        self.tts_engine.stop()


class SpeechRecognitionProvider:
    """
    Class for handling SpeechRecognition functionality
    """

    def __init__(self):
        self.voice_recognizer = speech_frame.Recognizer()
        self.input_device = speech_frame.Microphone(device_index=1)
        self.UnknownValueError = speech_frame.UnknownValueError
        self.RequestError = speech_frame.RequestError
        self.voice_distortion = voice_distortion


class ChatGPTApiProvider:
    def __new__(cls):
        if not config or config.gpt_credentials:
            return None

    def __init__(self):
        openai.organization = config.gpt_credentials.chat_gpt_org_key
        openai.api_key = config.gpt_credentials.chat_gpt_api_key
        self.models = openai.Model.list()

    def make_request(self, content: str):
        """
        Make a request to Chat GPT and get a responce
        """
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}]
        )
        print(chat_completion.choices[0].message.content)


class HardwareProvider:
    """
    Class for handling methods that are performing on hardware devices
    """

    def __init__(self):
        pass

    def get_devices():
        pass

    def perform_on_heating_device():
        pass

    def perform_on_telecom_device():
        pass

    def perform_blackout():
        pass


tts_engine = TTSEngineProvider()
speech_recognition_provider = SpeechRecognitionProvider()
