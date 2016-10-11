import unittest
from SpeechEngines.StringReadingEngine import StringReadingEngine

class StringInputEngineTest(unittest.TestCase):
  def test_initilize(self):
    print("testing string input engine")

  def testingWithoutAStarter(self):
    testEngine = StringReadingEngine()
    print(testEngine.getInput())

  def testingWithAStarter(self):
    testEngine = StringReadingEngine()
    print(testEngine.getInput("Alfred"))

if __name__ == "__main__":
  unittest.main()