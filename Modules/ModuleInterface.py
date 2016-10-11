from SpeechEngines.TextToSpeechInterface import ITextToSpeech
from SpeechEngines.SpeechToTextInterface import ISpeechToText

class IModule:
    keyWords = []

    def __init__(self, stt:ISpeechToText, tss:ITextToSpeech):
        self._stt = stt
        self._tts = tss

    def execute(self, wordList: [str]): raise NotImplementedError

if __name__ == "__main__":
    None