from SpeechEngines.SpeechToTextInterface import ISpeechToText
from SpeechEngines.TextToSpeechInterface import ITextToSpeech
from Modules.ModuleInterface import IModule
# need to deal with the modules some how. module list or something

class soul:
    def __init__(self, stt: ISpeechToText, tts: ITextToSpeech, moduleList: [IModule] ):
        self._stt = stt
        self._tts= tts
        self._moduleList = moduleList

    def main(self):
        wordList = self._stt.listenForConversation('Alfred')
        moduleToRun = self.getModuleToRun(wordList)
        moduleToRun.execute(wordList)
        self._tts.output("end of main loop")

    def getModuleToRun(self, wordList:[str]) ->  IModule:
        return self._moduleList[0]

if __name__ == "__main__":
    main()
