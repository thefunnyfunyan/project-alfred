from SpeechEngines.SpeechToTextInterface import ISpeechToText
from logger import logger as Log

class StringReadingEngine(ISpeechToText):
  def __init__(self):
    self._TraceLogEnabled = False

  def getInput(self, starter: str = None):
    while(True):
      text = input("start command with " + str(starter) + " :")
      splitText = text.split(" ")
      log(text, splitText)

      if(starter and checkForStarter(starter, splitText)):
        return splitText
      elif(not starter):
        return splitText

    def getInputWithStarter(starter: str, splitText: [str]) -> bool:
      for word in splitText:
        if word.upper() == starter.upper():
          return True
      return False

    def log(text: str, splitText: [str]) -> None:
      if(self._TraceLogEnabled):
        Log.Trace("String Reading Engine captured this text: " + text)
        Log.Trace("String Reading Engine split text into this array: " + str(splitText))
      
    
if __name__ == "__main__":
  getInput()
    