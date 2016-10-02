import unittest
from Modules.Interpreter import Interpreter
from SpeechEngines.SpeechToTextInterface import ISpeechToText
from SpeechEngines.TextToSpeechInterface import ITextToSpeech

class InterpreterTest(unittest.TestCase):
    def test_initilize(self):
        print("test")
        testStt = sttMock()
        testTts = ttsMock()
        testInterp = Interpreter(testStt, testTts)
        self.assertNotEqual(None, testInterp)

class sttMock(ISpeechToText):
    def none() -> None:
        return None

class ttsMock(ITextToSpeech):
    def none() -> None:
        return None 

if __name__ == "__main__":
    unittest.main() 