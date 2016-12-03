from .TestModule import TestModule
from .ModuleInterface import IModule
from IOEngine.IOEngine import IOEngine

class ModuleList:
    def getModules(ioEngine: IOEngine) -> [IModule]:
        modList = [
            TestModule(ioEngine)
        ]
        return modList

if __name__ == "__main__":
    None