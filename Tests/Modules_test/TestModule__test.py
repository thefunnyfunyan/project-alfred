import unittest
from SpeechEngines.TextToSpeechInterface import ITextToSpeech
from SpeechEngines.SpeechToTextInterface import ISpeechToText
from Modules.TestModule import TestModule

class TestModuleTest(unittest.TestCase):
    def test_initialize(self):
        stMock = sttMock()
        tsMock = ttsMock()
        testMod = TestModule(stMock, tsMock)

        self.assertEqual(None, tsMock.outputText)
        self.assertNotEqual(None, testMod)
        testMod.execute([])
        self.assertEqual(tsMock.outputText, "executing test module")


class sttMock(ISpeechToText):
    None

class ttsMock(ITextToSpeech):
    outputText = None
    def output(self, outputText: str):
        self.outputText = outputText