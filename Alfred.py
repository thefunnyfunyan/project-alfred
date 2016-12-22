from IOEngine.IOEngine import IOEngine
from IOEngine.InputEngine.StringInputEngine import StringInputEngine
from IOEngine.OutputEngine.StringOutputEngine import StringOutputEngine
from Modules.ModuleList import ModuleList

def main():
  strIn = StringInputEngine()
  strOut = StringOutputEngine()
  strOut.output(strIn.getInput())


if __name__ == "__main__":
  main()