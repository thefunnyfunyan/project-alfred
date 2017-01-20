from .ModuleInterface import IModule
from  IOEngine.IOEngine import IOEngine


class Joke(object):
    def tellJoke(self, ioEngine: IOEngine) -> None:
        pass


class StoryJoke(Joke):
    def __init__(self, story):
        self._story = story

    def tellJoke(self, ioEngine: IOEngine) -> None:
        ioEngine.output(self._story)


class JokeModule(IModule):
    _keyWords = ['joke', 'laugh', 'funny']

    def execute(self, wordList: [str]) -> None:
        self.ioEngine.output('What kind of joke would you like to hear?')
        userInput = self.ioEngine.getInput()
        jokeType = self._getJokeTypeFromUserInput(userInput)
        joke = self._getJoke(jokeType)
        joke.tellJoke(self.ioEngine)
        self.ioEngine.output('Would you like to hear another one?')
        userInput = self.ioEngine.getInput()
        if not self._shouldTellAnotherJoke(userInput):
            return

    def _getJokeTypeFromUserInput(self, userInput: [str]) -> str:
        return 'story'

    def _getJoke(self, jokeType: str) -> Joke:
        if (jokeType == 'story'):
            return StoryJoke('Three men walk into a bar. The fourth one ducks')

    def _shouldTellAnotherJoke(self, userInput: [str]) -> bool:
        return False
