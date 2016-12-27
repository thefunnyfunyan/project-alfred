from .ModuleInterface import IModule


class ExitModule(IModule):
  _keyWords = ['exit', 'quit']

  def execute(self, wordList: [str]) -> None:
    return 'exit'
