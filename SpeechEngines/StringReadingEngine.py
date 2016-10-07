from SpeechEngines.SpeechToTextInterface import ISpeechToText

class StringReadingEngine(ISpeechToText):
  def getInput(self, starter: str = None):
    validCommand = False
    while(not validCommand):
      text = input("start command with " + str(starter) + " :")
      splitText = text.split(" ")

      if(starter):
        starterIncluded = False
        for word in splitText:
          if word.upper() == starter.upper():
            StarterIncluded = True
            return splitText
          
      else:
        return splitText
      
if __name__ == "__main__":
  getInput()
      