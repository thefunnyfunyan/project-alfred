import unittest
from Interpreter import Interpreter
from SpeechEngines import ISpeechToText
from SpeechEngines import ITextToSpeech

class InterpreterTest(unittest.TestCase):
    def test_initilize(self):
        testStt = sttMock()
        testTts = ttsMock()
        testTerp = Interpreter(testStt, testTts)
        self.assertNotEqual(None, testTerp)

if __name__ == "__main__":
    unittest.main() 

class sttMock(ISpeechToText):
    def none() -> None:
        return None

class ttsMock(ITextToSpeech):
    def none() -> None:
        return None 