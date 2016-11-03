from SpeechEngines.SpeechToTextInterface import ISpeechToText
from SpeechEngines.TextToSpeechInterface import ITextToSpeech
from Modules.ModuleInterface import IModule

class soul:
    def __init__(self, stt: ISpeechToText, tts: ITextToSpeech, moduleList: [IModule] ):
        self._stt = stt
        self._tts = tts
        self._moduleList = moduleList

    def main(self):
        wordList = self._stt.listenForConversation('Alfred')
        moduleToRun = self.getModuleToRun(wordList)
        moduleToRun.execute(wordList)
        self._tts.output("end of main loop")

    def getModuleToRun(self, wordList:[str]) ->  IModule:
        maxMatchNumber = 0
        moduleToRunIndex = -1
        index = 0
        for module in self._moduleList:
            tempMatchNumber = 0
            tempKeyWords = module.keyWords

            for keyWord in wordList:
                for moduleKey in tempKeyWords:
                    if(keyWord.upper() == moduleKey.upper()):
                        tempMatchNumber += 1
            
            if(tempMatchNumber > maxMatchNumer):
                maxMatchNumber = tempMatchNumber
                moduleToRunIndex = index
            index +=1


if __name__ == "__main__":
    main()
