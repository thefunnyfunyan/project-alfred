from .OutputEngineInterface import IOutputEngine

class StringOutputEngine(IOutputEngine):
  def output(self, outputString: str):
      print(outputString)