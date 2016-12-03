from IOEngine.IOEngine import IOEngine
from Modules.ModuleInterface import IModule

class soul:
    def __init__(self, ioEngine: IOEngine, moduleList: [IModule] ):
        assert isinstance(ioEngine, IOEngine)
        self.ioEngine = ioEngine
        self._moduleList = moduleList

    def main(self):
        wordList = self.ioEngine.getInput('Alfred')
        moduleToRun = self.getModuleToRun(wordList)
        moduleToRun.execute(wordList)
        self.ioEngine.output("end of main loop")

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
