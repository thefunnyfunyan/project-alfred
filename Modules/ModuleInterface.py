from IOEngine.IOEngine import IOEngine


class IModule(object):
  _keyWords = []

  def __init__(self, ioEngine: IOEngine):
    assert isinstance(ioEngine, IOEngine)
    self.ioEngine = ioEngine

  def execute(self, wordList: [str]) -> None: raise NotImplementedError


if __name__ == "__main__":
  None
