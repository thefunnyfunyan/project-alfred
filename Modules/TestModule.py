from SpeechEngines.TextToSpeechInterface import ITextToSpeech
from SpeechEngines.SpeechToTextInterface import ISpeechToText
from Modules.ModuleInterface import IModule

class TestModule(IModule):
    keyWords = ["test", "testing"]

    def execute(self, wordList: str[]):
        self._tts.output("executing test module")

if __name__ == "__main__":
    return