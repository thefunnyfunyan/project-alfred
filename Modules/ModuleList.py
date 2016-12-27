from .TestModule import TestModule
from .DefaultModule import DefaultModule
from .ModuleInterface import IModule
from IOEngine.IOEngine import IOEngine
from .ExitModule import ExitModule


class ModuleList:
  def getModules(ioEngine: IOEngine) -> [IModule]:
    modList = [
      ExitModule(ioEngine),
      TestModule(ioEngine),
      DefaultModule(ioEngine)
    ]
    return modList


if __name__ == "__main__":
  None
