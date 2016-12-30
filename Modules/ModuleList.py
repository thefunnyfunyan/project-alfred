from .TestModule import TestModule
from .DefaultModule import DefaultModule
from .ModuleInterface import IModule
from IOEngine.IOEngine import IOEngine
from .ExitModule import ExitModule
from .JokeModule import JokeModule


class ModuleList:
  def getModules(ioEngine: IOEngine) -> [IModule]:
    modList = [
      ExitModule(ioEngine),
      TestModule(ioEngine),
      JokeModule(ioEngine),
      DefaultModule(ioEngine)
    ]
    return modList


if __name__ == "__main__":
  None
