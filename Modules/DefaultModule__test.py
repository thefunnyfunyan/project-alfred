import unittest
from IOEngine.IOEngine import IOEngine
from Modules.DefaultModule import DefaultModule
from Modules.ModuleInterface import IModule


class DefaultModuleTest(unittest.TestCase):
  def test_ShouldHaveKeywords(self):
    defMod = DefaultModule(IOEngineFake())
    assert isinstance(defMod, IModule)
    self.assertEqual(len(defMod._keyWords), 0)


class IOEngineFake(IOEngine):
  def __init__(self):
    pass

  def output(self):
    pass

  def getInput(self):
    pass
