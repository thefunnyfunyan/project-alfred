from IOEngine.IOEngine import IOEngine
from IOEngine.InputEngine.StringInputEngine import StringInputEngine
from IOEngine.OutputEngine.StringOutputEngine import StringOutputEngine
# from IOEngine.OutputEngine.SpeechOutputEngine import SpeechOutputEngine
from Modules.ModuleList import ModuleList
from soul import soul


def main():
    io_engine = IOEngine(StringInputEngine(), StringOutputEngine())
    _soul = soul(io_engine, ModuleList.getModules(io_engine))
    _soul.main()


if __name__ == "__main__":
    main()
