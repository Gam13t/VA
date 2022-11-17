#  TODO: REPLACE WITH UNIT TESTS

import pytest
import socket

from config import TO_TEST

class TestRequirements():
    def test_tts_engine(self):
        """
        Tests basics of TTS.
        """
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        for voice in voices:
            if voice.name == 'Microsoft Irina Desktop - Russian':
                engine.setProperty('voice', voice.id)  

        engine.say('Пивет!')
        engine.runAndWait()


    def test_index_micros_and_get_main(self):
        """
        Test hardware input.
        """
        import speech_recognition as sr
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))



    def test_internet_connection(self, to_test=TO_TEST):
        """
        Test internet connection
        """
        if not to_test:
            assert True
        else:
            assert self.is_internet() == True


    
    def test_speech_recognition(self, to_test=TO_TEST):
        """
        Test speech recognition, say Привет to check if everything is alright.
        """
        if not self.is_internet() and not to_test:
            assert True
        else:
            import speech_recognition as sr
            r = sr.Recognizer()

            with sr.Microphone(device_index=1) as source:
                audio = r.listen(source)

            query = r.recognize_google(audio, language='ru-RU')
            assert query.lower() == 'привет'

    
    def is_internet(self):
        REMOTE_SERVER = "one.one.one.one"

        try:
            host = socket.gethostbyname(REMOTE_SERVER)

            sock = socket.create_connection((host, 80), 2)
            sock.close()
            
            return True
        except Exception:
            pass

        return False