from .TestModule import TestModule
from .DefaultModule import DefaultModule
from .ModuleInterface import IModule
from IOEngine.IOEngine import IOEngine


class ModuleList:
  def getModules(ioEngine: IOEngine) -> [IModule]:
    modList = [
      TestModule(ioEngine),
      DefaultModule(ioEngine)
    ]
    return modList


if __name__ == "__main__":
  None
