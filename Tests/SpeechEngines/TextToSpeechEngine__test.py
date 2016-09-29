import unittest
from SpeechEngines.TextToSpeechEngine import TextToSpeechEngine as tssEngine

class TextToSpeechEngineTest(unittest.TestCase):
    def test_initilize(self):
        testEngine = tssEngine()
        self.assertNotEqual(None, testEngine)

if __name__ == "__main__":
    unittest.main()