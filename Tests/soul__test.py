import unittest
from SpeechEngines.TextToSpeechInterface import ITextToSpeech
from SpeechEngines.SpeechToTextInterface import ISpeechToText
from soul import soul

class SoulTest(unittest.TestCase):
    def setUp(self):
        self.sttEngine = inputEngine()
        self.ttsEngine = outputEngine()
        self.moduleSpy = moduleMock()
    
    def test_ShouldExecuteMockModuleOnce(self):
        testSoul = soul(self.sttEngine, self.ttsEngine, [self.moduleSpy])
        
        self.assertEqual(self.ttsEngine.outputText, "")
        self.assertEqual(self.moduleSpy.executed, False)

        testSoul.main()

        self.assertEqual(self.ttsEngine.outputText, "end of main loop")
        self.assertEqual(self.moduleSpy.executed, True)

    def test_ShouldChooseSecondMockModule(self):
        self.assertTrue(True)



class inputEngine(ISpeechToText):
    def listenForConversation(self, starter: str):
        return ""

class outputEngine(ITextToSpeech):
    outputText = ""

    def output(self, outputText: str):
        self.outputText = outputText

class moduleMock(IModule):
    executed = False

    def execute(self, wordList:[str]):
        self.executed = True

if __name__ == "__main__":
    unittest.main()