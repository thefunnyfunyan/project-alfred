from IOEngine.IOEngine import IOEngine
from .TestModule import TestModule
from .DefaultModule import DefaultModule
from .ModuleInterface import IModule
from .ExitModule import ExitModule
from .WeatherModule import WeatherModule


class ModuleList:
    def getModules(ioEngine: IOEngine) -> [IModule]:
        modList = [
            ExitModule(ioEngine),
            TestModule(ioEngine),
            WeatherModule(ioEngine),
            DefaultModule(ioEngine)  # has to be last
        ]
        return modList


if __name__ == "__main__":
    None
