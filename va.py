import os
from re import L
import time
import speech_recognition as speech_frame
import fuzzywuzzy as fw
import datetime

from providers import TTSEngineProvider, tts_engine
from constants import PredefinedVocabularity, action_linker
from exceptions import InvalidInstanceException

class VAManager():
    def __init__(self):
        self.tts_engine = tts_engine
        self.action_linker = action_linker

        if not isinstance(self.tts_engine, TTSEngineProvider):
            raise InvalidInstanceException

        if not isinstance(self.action_linker, PredefinedVocabularity):
            raise InvalidInstanceException
    
    def execute_based_on_request(self):
        pass

    def execute_cmd(self, cmd):
        if cmd == 'ctime':
            # сказать текущее время
            now = datetime.datetime.now()
            self.tts_engine.speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    
    def recognize_cmd(cmd):
        RC = {'command': '', 'percent': 0}
        for command, proceeder in action_linker.base_dct_filled['command'].items():
            for proceed in proceeder:
                percent_similarities = fw.ratio(cmd, proceed)
                if percent_similarities > RC['percent']:
                    RC['command'] = proceed
                    RC['percent'] = percent_similarities
        
        return RC

voice_assistant = VAManager()
