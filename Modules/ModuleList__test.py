import unittest
from IOEngine.IOEngine import IOEngine
from IOEngine.InputEngine.InputEngineInterface import IInputEngine
from IOEngine.OutputEngine.OutputEngineInterface import IOutputEngine
from Modules.ModuleList import ModuleList

class ModuleListTest(unittest.TestCase):
    def test_ShouldListWithOneModule(self):
        modList = ModuleList.getModules(IOEngine(inputStub(), outputStub()))
        self.assertEqual(len(modList), 1)

class inputStub(IInputEngine):
    pass

class outputStub(IOutputEngine):
    pass
