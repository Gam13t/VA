import os
from re import L
import time
import speech_recognition as speech_frame
import fuzzywuzzy as fw
import datetime

from providers import TTSEngineProvider, tts_engine
from constants import PredefinedVocabularity, action_linker
from exceptions import InvalidInstanceException


class VAManager:
    def __init__(self):
        self.tts_engine = tts_engine
        self.action_linker = action_linker

        if not isinstance(self.tts_engine, TTSEngineProvider):
            raise InvalidInstanceException

        if not isinstance(self.action_linker, PredefinedVocabularity):
            raise InvalidInstanceException

    def execute_command(self, command):
        """
        Dummy method for test
        """
        if command == "ctime":
            now = datetime.datetime.now()
            self.tts_engine.speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    def action_controller(self, command):
        SUGGESTED_COMMAND = {"command": "", "percent": 0}
        for _, parced_action in action_linker.base_dct_filled["command"].items():
            for action in parced_action:
                percent_similarities = fw.ratio(command, action)
                if percent_similarities > SUGGESTED_COMMAND["percent"]:
                    SUGGESTED_COMMAND["command"] = action
                    SUGGESTED_COMMAND["percent"] = percent_similarities

        return SUGGESTED_COMMAND


voice_assistant = VAManager()
