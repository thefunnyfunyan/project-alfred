from IOEngine.OutputEngine.OutputEngineInterface import IOutputEngine
from IOEngine.InputEngine.InputEngineInterface import IInputEngine
from IOEngine.IOEngine import IOEngine
import unittest

#from OutputEngine.OutputEngineInterface import IOutputEngine
#from InputEngine.InputEngineInterface import IInputEngine
#from IOEngine import IOEngine

class StringInputEngineTest(unittest.TestCase):
  def test_NoStarterReturnInput(self):
    out = OutputMock()
    inEn = InputMock()
    assert isinstance(out, IOutputEngine)
    
    assert isinstance(inEn, IInputEngine)

class OutputMock(IOutputEngine):
  pass

class InputMock(IInputEngine):
  pass
