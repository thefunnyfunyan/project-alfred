from .OutputEngine.OutputEngineInterface import IOutputEngine
from .InputEngine.InputEngineInterface import IInputEngine
from .IOEngine import IOEngine
import unittest


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
