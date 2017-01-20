from .ModuleInterface import IModule
from IOEngine.IOEngine import IOEngine


class TestModule(IModule):
  _keyWords = ["test", "testing"]

  def execute(self, wordList: [str]):
    self.io_engine.output("executing test module")


if __name__ == "__main__":
  None
