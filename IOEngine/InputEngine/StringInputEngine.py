from .InputEngineInterface import IInputEngine


class StringInputEngine(IInputEngine):
  def getInput(self, starter: str = None) -> [str]:
    if (starter):
      while (True):
        inputList = input().split(' ')
        for word in inputList:
          if (word.upper() == starter.upper()):
            return inputList
    return input().split(' ')
