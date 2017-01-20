from IOEngine.IOEngine import IOEngine
from Modules.ModuleInterface import IModule


class DefaultModule(IModule):
  def execute(self, wordList: [str]):
    self.io_engine.output('sorry, but I am not sure what you mean.')
    self.io_engine.output('Future functionality will allow me to learn')
    self.io_engine.output('what you want me to do, but for now please')
    self.io_engine.output('try a different command.')


if __name__ == '__main__':
  print(type(DefaultModule))
