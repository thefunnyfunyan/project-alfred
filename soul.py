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
        maxMatchNumber, moduleToRunIndex = 0, 0

        for index, module in enumerate(self._moduleList):
            tempMatchNumber = self.getMatchCount(wordList, module.keyWords)
            
            if(tempMatchNumber > maxMatchNumber):
                maxMatchNumber, moduleToRunIndex = tempMatchNumber, index
        
        return self._moduleList[moduleToRunIndex]
    
    def getMatchCount(self, wordList: [str], moduleKeyWords: [str]) -> int:
        matchCount = 0

        for keyWord in wordList:
            for moduleKeyWord in moduleKeyWords:
                if(keyWord.upper() == moduleKeyWord.upper()):
                    matchCount += 1
        return matchCount        


if __name__ == "__main__":
    main()
