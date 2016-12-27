from IOEngine.IOEngine import IOEngine
from Modules.ModuleInterface import IModule


class soul:
  def __init__(self, ioEngine: IOEngine, moduleList: [IModule]):
    assert isinstance(ioEngine, IOEngine)
    self.ioEngine = ioEngine
    self._moduleList = moduleList

  def main(self):
    self.giveIntro()
    while (True):
      wordList = self.ioEngine.getInput('Alfred')
      moduleToRun = self.getModuleToRun(wordList)
      if (moduleToRun.execute(wordList) == 'exit'):
        return

  def getModuleToRun(self, wordList: [str]) -> IModule:
    maxMatchNumber, moduleToRunIndex = 0, 0

    for index, module in enumerate(self._moduleList):
      tempMatchNumber = self.getMatchCount(wordList, module._keyWords)

      if (tempMatchNumber >= maxMatchNumber):
        maxMatchNumber, moduleToRunIndex = tempMatchNumber, index

    return self._moduleList[moduleToRunIndex]

  def getMatchCount(self, wordList: [str], moduleKeyWords: [str]) -> int:
    matchCount = 0

    for keyWord in wordList:
      for moduleKeyWord in moduleKeyWords:
        if (keyWord.upper() == moduleKeyWord.upper()):
          matchCount += 1
    return matchCount

  def giveIntro(self):
    self.ioEngine.output('Hello, My name is Alfred.')
    self.ioEngine.output('I am the beginnings of a personal assistant,')
    self.ioEngine.output('I was developed slowly by Brandon Runyan.')
    self.ioEngine.output('If you need me, just start with "Alfred" and then your request.')


if __name__ == "__main__":
  pass
