from SpeechEngines.TextToSpeechInterface import ITextToSpeech
from SpeechEngines.SpeechToTextInterface import ISpeechToText

class Interpreter:
    def __init__(self, sttEngine: ISpeechToText, ttsEngine: ITextToSpeech ):
        self.sttEngine = sttEngine
        self.ttsEngine = ttsEngine

    def f(self) -> str:
        return 'hello'