import unittest
from SpeechEngines.TextToSpeechInterface import ITextToSpeech
from SpeechEngines.SpeechToTextInterface import ISpeechToText
from Modules.ModuleList import ModuleList

class ModuleListTest(unittest.TestCase):
    def test_ShouldListWithOneModule(self):
        modList = ModuleList.getModules(sttMock(), ttsMock())
        self.assertEqual(len(modList), 1)

class sttMock(ISpeechToText):
    None

class ttsMock(ITextToSpeech):
    None