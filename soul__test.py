import unittest
from IOEngine.IOEngine import IOEngine
from soul import soul
from Modules.ModuleInterface import IModule

class SoulTest(unittest.TestCase):
    def setUp(self):
        self.ioEngine = IOEngine(None, None)
        self.moduleSpy = moduleMock(self.ioEngine)
    
    # def test_ShouldExecuteMockModuleOnce(self):
    #     testSoul = soul(self.ioEngine, [self.moduleSpy])
        
    #     self.assertEqual(self.ioEngine.output(""), "")
    #     self.assertEqual(self.moduleSpy.executed, False)

    #     testSoul.main()

    #     self.assertEqual(self.ttsEngine.outputText, "end of main loop")
    #     self.assertEqual(self.moduleSpy.executed, True)

    # def test_ShouldChooseSecondMockModule(self):
    #     moduleSpy2 = moduleMock2(self.sttEngine, self.ttsEngine)
    #     testSoul = soul(self.sttEngine, self.ttsEngine, [moduleSpy2, self.moduleSpy])

    #     testSoul.main()

    #     self.assertEqual(self.moduleSpy.executed, True)
    #     self.assertEqual(moduleSpy2.executed, False)
        
    # def test_ShouldChooseFirstOfTwoMockModules(self):
    #     moduleSpy2 = moduleMock2(self.sttEngine, self.ttsEngine)
    #     testSoul = soul(self.sttEngine, self.ttsEngine, [self.moduleSpy, moduleSpy2])

    #     testSoul.main()

    #     self.assertEqual(self.moduleSpy.executed, True)
    #     self.assertEqual(moduleSpy2.executed, False)
    
    # def test_ShouldChooseSpy2ByDefault(self):
    #     moduleSpy2 = moduleMock2(self.sttEngine, self.ttsEngine)
    #     moduleSpy3 = moduleMock2(self.sttEngine, self.ttsEngine)
    #     testSoul = soul(self.sttEngine, self.ttsEngine, [moduleSpy2, moduleSpy3])

    #     testSoul.main()

    #     self.assertEqual(moduleSpy2.executed, True)
    #     self.assertEqual(moduleSpy3.executed, False)

class moduleMock(IModule):
    executed = False
    keyWords = ['first']
    def execute(self, wordList:[str]):
        self.executed = True

class moduleMock2(IModule):
    executed = False
    keyWords = ['second']
    def execute(self, wordList:[str]):
        self.executed = True


if __name__ == "__main__":
    unittest.main()