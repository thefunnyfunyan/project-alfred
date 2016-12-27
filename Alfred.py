from IOEngine.IOEngine import IOEngine
from IOEngine.InputEngine.StringInputEngine import StringInputEngine
from IOEngine.OutputEngine.StringOutputEngine import StringOutputEngine
from Modules.ModuleList import ModuleList
from soul import soul


def main():
  ioEngine = IOEngine(StringInputEngine(), StringOutputEngine())
  _soul = soul(ioEngine, ModuleList.getModules(ioEngine))
  _soul.main()


if __name__ == "__main__":
  main()
