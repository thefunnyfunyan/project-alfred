import unittest
from SpeechEngines.StringReadingEngine import StringReadingEngine

class StringInputEngineTest(unittest.TestCase):
  def test_initilize(self):
    testEngine = StringReadingEngine()
    self.assertNotEqual(testEngine, None)

if __name__ == "__main__":
  unittest.main()