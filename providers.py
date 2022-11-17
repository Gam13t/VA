import pyttsx3 as base_tts_engine


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


class SpeechRecognitionProvider:
    """
    Class for handling SpeechRecognition functionality
    """

    pass


tts_engine = TTSEngineProvider()
