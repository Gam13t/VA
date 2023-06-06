import logging
import datetime
import subprocess

import webbrowser as browser_controller

from pathlib import Path
from typing import Dict
from playsound import playsound

from providers import TTSEngineProvider, tts_engine, speech_recognition_provider
from constants import PredefinedVocabularity, action_linker
from config import filled_config as config
from config import Config
from exceptions import InvalidInstanceException

logger = logging.getLogger(__name__)


class VAProviderHelper:
    def __init__(self):
        self.tts_engine = tts_engine
        self.action_linker = action_linker
        self.speech_frame = speech_recognition_provider
        self.browser_controller = (
            browser_controller  # TODO(Rostyslav): change to discuss
        )
        self.config = config

    def play(self, audio_file_path="acdc-back-in-black.wav"):
        current_path = Path(__file__).parent.resolve()
        sound_path = str(current_path / "sounds" / audio_file_path)
        playsound(sound_path, block=False)


class VACommandsRealisation(VAProviderHelper):
    """
    Base class for demonstration the functionality
    """

    def response(func):
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            tts_engine.speak(config.va_behavior_config.base_reply[0])
            logger.debug(f"User has requested for {func}. Proceeding...")
            return result

        return wrap

    def current_time(self):
        current_time = datetime.datetime.now()
        self.tts_engine.speak(
            "Сейчас " + str(current_time.hour) + ":" + str(current_time.minute)
        )

    def open_google(self):
        browser_controller.open(self.config.action_spec_config.web_explorer_link)

    @response
    def open_command_communications(self):
        for link in self.config.action_spec_config.working_directory:
            browser_controller.open(link)

    @response
    def open_music_player(self):
        browser_controller.open(self.config.action_spec_config.music_provider_link)

    @response
    def open_video_provider(self):
        browser_controller.open(self.config.action_spec_config.video_provider_link)

    def working_protocol(self):
        """
        Example of using multiple requests
        """
        path_to_application = self.config.action_spec_config.application_path
        self.play()
        self.open_command_communications()
        self.open_google()
        subprocess.call(path_to_application)

    def joke_question(self):
        """
        Retrieve random joke from internet and TTS
        """
        self.tts_engine.speak("Я готова служить вам, господин!")


class VAExecutor(VACommandsRealisation):
    def __init__(self):
        self.tts_engine = tts_engine
        self.action_linker = action_linker
        self.speech_frame = speech_recognition_provider
        self.config = config

        if not isinstance(self.tts_engine, TTSEngineProvider):
            raise InvalidInstanceException

        if not isinstance(self.action_linker, PredefinedVocabularity):
            raise InvalidInstanceException

        if not isinstance(self.config, Config):
            raise InvalidInstanceException

    @property
    def linked_commands(self) -> Dict[str, str]:
        return {
            "current_time": self.current_time,
            "open_google": self.open_google,
            "open_command_communications": self.open_command_communications,
            "open_music_player": self.open_music_player,
            "open_video_provider": self.open_video_provider,
            "working_protocol": self.working_protocol,
            "joke_question": self.joke_question,
        }


class VAInterface(VAExecutor):
    def execute_command_by_link(self, command):
        self.linked_commands[command]()

    def callback(self, user_input):
        try:
            query = self.speech_frame.voice_recognizer.recognize_google(
                user_input, language=self.config.language
            )
            self.check_query_contains_command(query.lower())
            print("Распознаная речь: " + query)
            logger.debug("Распознаная речь: " + query)
        except self.speech_frame.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(
                    e
                )
            )
        except self.speech_frame.UnknownValueError:
            logger.debug("Ошибка во время обработки голоса, idle...")

    def listen_for_input(self):
        with self.speech_frame.input_device as source:
            self.speech_frame.voice_recognizer.adjust_for_ambient_noise(
                source, duration=0.5
            )
            user_input = self.speech_frame.voice_recognizer.listen(
                source=self.speech_frame.input_device
            )
            self.callback(user_input)

    def check_query_contains_command(self, query):
        """
        Proceed only sentance with VA name inside
        """
        va_name_index = query.find(config.va_behavior_config.va_name)
        if va_name_index != -1:
            request = query[va_name_index:]
            self.get_commmand(request)
        pass

    def get_commmand(self, command):
        """
        TODO:
            - make the algo less complicated and more effective.
            - refactor a bit
            - make listener async to work in background
        """
        SUGGESTED_COMMAND = {"command": "", "percent": 0, "action": ""}
        for key, parced_action in self.action_linker.base_dct_filled["command"].items():
            for action in parced_action:
                percent_similarities = self.speech_frame.voice_distortion.ratio(
                    command, action
                )
                if percent_similarities > SUGGESTED_COMMAND["percent"]:
                    SUGGESTED_COMMAND["command"] = action
                    SUGGESTED_COMMAND["percent"] = percent_similarities
                    SUGGESTED_COMMAND["action"] = key

        self.execute_command_by_link(SUGGESTED_COMMAND["action"])
