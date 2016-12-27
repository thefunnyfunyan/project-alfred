from IOEngine.IOEngine import IOEngine
from Modules.ModuleInterface import IModule


class DefaultModule(IModule):
  def execute(self, wordList: [str]):
    self.ioEngine.output('sorry, but I am not sure what you mean.')
    self.ioEngine.output('Future functionality will allow me to learn')
    self.ioEngine.output('what you want me to do, but for now please')
    self.ioEngine.output('try a different command.')


if __name__ == '__main__':
  print(type(DefaultModule))
