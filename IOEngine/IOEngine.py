from .InputEngine.InputEngineInterface import IInputEngine
from .OutputEngine.OutputEngineInterface import IOutputEngine

class IOEngine(object):
    def __init__(self, inputEngine: IInputEngine, outputEngine: IOutputEngine):
        assert isinstance(inputEngine, IInputEngine)
        assert isinstance(outputEngine, IOutputEngine)
        self.inputEngine = inputEngine
        self.outputEngine = outputEngine   
        

    def output(self, outputString: str):
        self.outputEngine.output(outputString)
    
    def getInput(self, starter: str = None):
        return self.inputEngine.getInput(starter)
