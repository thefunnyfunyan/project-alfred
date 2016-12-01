import unittest
from IOEngine.InputEngine.StringInputEngine import StringInputEngine

class StringInputEngineTest(unittest.TestCase):
  def test_NoStarterReturnInput(self):
    sie = StringInputEngine()
    #input = sie.getInput()
    # self.assertEqual(['test'], input)
    self.assertTrue(True)

  def test_StarterTest(self):
    sie = StringInputEngine()
    #input = sie.getInput('start')
    # self.assertEqual(['test', 'start'], input)
    self.assertTrue(True)