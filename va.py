# TODO: add logs
# TODO: speed up a little

import datetime

from providers import TTSEngineProvider, tts_engine, speech_recognition_provider
from constants import PredefinedVocabularity, action_linker
from config import filled_config as config
from config import Config
from exceptions import InvalidInstanceException


class VAExecutor:
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

    def current_time(self):
        now = datetime.datetime.now()
        self.tts_engine.speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    @property
    def linked_commands(self):
        return {"current_time": self.current_time}


class VAInterface(VAExecutor):
    def execute_command_by_link(self, command):
        self.linked_commands[command]()

    def listen_for_input(self):
        try:

            with self.speech_frame.input_device as source:
                self.speech_frame.voice_recognizer.adjust_for_ambient_noise(
                    source, duration=0.5
                )
                user_input = self.speech_frame.voice_recognizer.listen(
                    source=self.speech_frame.input_device
                )
                query = self.speech_frame.voice_recognizer.recognize_google(
                    user_input, language="ru-RU"
                )
                self.check_query_contains_command(query.lower())

                print("Распознаная речь: " + query)  # PUT INTO LOGS

        except self.speech_frame.UnknownValueError:
            #  return self.tts_engine.speak('Не смог понять ваш запрос, повторите пожалуйста еще раз!')
            print("Ошибка во время обработки голоса, idle...")

    def check_query_contains_command(self, query):
        """
        Proceed only sentance with VA name inside
        """
        va_name_index = query.find(config.va_name)
        if va_name_index != -1:
            request = query[va_name_index:]
            self.get_commmand(request)
        pass

    def get_commmand(self, command):
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
