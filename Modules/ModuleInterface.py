from IOEngine.IOEngine import IOEngine


class IModule(object):
  _keyWords = []

  def __init__(self, ioEngine: IOEngine):
    self.io_engine = ioEngine

  def execute(self, wordList: [str]) -> None: raise NotImplementedError


if __name__ == "__main__":
  None
