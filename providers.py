import pyttsx3

class TTSEngineProvider():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')

        for voice in self.voices:
            if voice.name == 'Microsoft Irina Desktop - Russian':
                self.engine.setProperty('voice', voice.id)  

    @property
    def tts_engine(self):
        return self.tts_engine

    def speak(self, sentence_to_announce):
        print(sentence_to_announce)
        self.tts_engine.say(sentence_to_announce)
        self.tts_engine.runAndWait()
        self.tts_engine.stop()

tts_engine = TTSEngineProvider()