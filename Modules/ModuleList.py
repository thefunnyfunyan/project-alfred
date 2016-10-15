from Modules.TestModule import TestModule
from Modules.ModuleInterface import IModule
from SpeechEngines.TextToSpeechInterface import ITextToSpeech
from SpeechEngines.SpeechToTextInterface import ISpeechToText


class ModuleList:
    def getModules(stt:ISpeechToText, tss:ITextToSpeech) -> [IModule]:
        modList = [
            TestModule(stt, tss)
        ]
        return modList

if __name__ == "__main__":
    None