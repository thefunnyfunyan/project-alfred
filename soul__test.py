import unittest
from IOEngine.IOEngine import IOEngine
from soul import soul
from Modules.ModuleInterface import IModule


class SoulTest(unittest.TestCase):
  def setUp(self):
    self.ioEngine = IOEngineMock()
    self.moduleSpy = moduleMock(self.ioEngine)
    self.moduleSpy2 = moduleMock2(self.ioEngine)

  def test_ShouldExecuteMockModule(self):
    _soul = soul(self.ioEngine, [self.moduleSpy])
    self.assertEqual(self.moduleSpy.executed, False)
    self.assertEqual(self.ioEngine.inputText, "")
    self.assertEqual(self.ioEngine.outputText, "")

    _soul.main()
    self.assertEqual(self.moduleSpy.executed, True)
    self.assertEqual(self.ioEngine.starterText, "Alfred")

  def test_ShouldChooseSecondMockModule(self):
    self.ioEngine.inputText = 'second'

    _soul = soul(self.ioEngine, [self.moduleSpy, self.moduleSpy2])
    self.assertEqual(self.moduleSpy.executed, False)
    self.assertEqual(self.moduleSpy2.executed, False)

    _soul.main()
    self.assertEqual(self.moduleSpy.executed, False)
    self.assertEqual(self.moduleSpy2.executed, True)
    self.assertEqual(self.ioEngine.outputText, 'ran module two')

  def test_ShouldChooseFirstOfTwoMockModules(self):
    self.ioEngine.inputText = 'first'

    _soul = soul(self.ioEngine, [self.moduleSpy, self.moduleSpy2])
    self.assertEqual(self.moduleSpy.executed, False)
    self.assertEqual(self.moduleSpy2.executed, False)

    _soul.main()
    self.assertEqual(self.moduleSpy.executed, True)
    self.assertEqual(self.moduleSpy2.executed, False)
    self.assertEqual(self.ioEngine.outputText, 'ran module one')

  def test_ShouldChooseSpy2ByDefault(self):
    _soul = soul(self.ioEngine, [self.moduleSpy, self.moduleSpy2])
    self.assertEqual(self.moduleSpy.executed, False)
    self.assertEqual(self.moduleSpy2.executed, False)

    _soul.main()
    self.assertEqual(self.moduleSpy.executed, False)
    self.assertEqual(self.moduleSpy2.executed, True)
    self.assertEqual(self.ioEngine.outputText, 'ran module two')


class moduleMock(IModule):
  executed = False
  _keyWords = ['first']

  def execute(self, wordList: [str]):
    self.executed = True
    self.ioEngine.output('ran module one')
    return 'exit'


class moduleMock2(IModule):
  executed = False
  _keyWords = ['second']

  def execute(self, wordList: [str]):
    self.ioEngine.output('ran module two')
    self.executed = True
    return 'exit'


class IOEngineMock(IOEngine):
  inputText = ''
  outputText = ''
  starterText = ''

  def __init__(self):
    pass

  def output(self, outputText):
    self.outputText = outputText

  def getInput(self, starter):
    self.starterText = starter
    return [self.inputText]


if __name__ == "__main__":
  unittest.main()
