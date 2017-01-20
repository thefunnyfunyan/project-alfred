from .ModuleInterface import IModule
from  IOEngine.IOEngine import IOEngine
from enum import Enum

class JokeType(Enum):
    random = 0
    story = 1
    knock_knock = 2

class Joke(object):
    def tellJoke(self, iofEngine: IOEngine) -> None:
        pass

class StoryJoke(Joke):
    def __init__(self, story: str):
        self._story = story

    def tellJoke(self, ioEngine: IOEngine) -> None:
        ioEngine.output(self._story)

class KnockKnockJoke(Joke):
    def __init__(self, setUp: str, punchLine: str):
        self._setUp = setUp
        self._punchLine = punchLine

    def tellJoke(self, ioEngine: IOEngine) -> None:
        ioEngine.output('Knock knock')
        ioEngine.getInput()
        ioEngine.output(self._setUp)
        ioEngine.getInput()
        ioEngine.output(self._punchLine)


class JokeModule(IModule):
    _keyWords = ['joke', 'laugh', 'funny']

    def execute(self, wordList: [str]) -> None:
        self.io_engine.output('What kind of joke would you like to hear?')
        user_input = self.io_engine.getInput()
        joke_type = self._getJokeTypeFromUserInput(user_input)
        joke = self._getJoke(joke_type)
        joke.tellJoke(self.io_engine)
        self.io_engine.output('Would you like to hear another one?')
        user_input = self.io_engine.getInput()
        if not self._shouldTellAnotherJoke(user_input):
            return

    def _getJokeTypeFromUserInput(self, user_input: [str]) -> JokeType:
        story_keywords = ['story', 'long']
        knock_knock_keywords = ['knock']

        max_count = 0
        final_index = -1
        for index, keyword_list in enumerate([story_keywords, knock_knock_keywords]):
            count = 0
            for keyword in keyword_list:
                for user_keyword in user_input:
                    if keyword.upper() == user_keyword.upper():
                        count += 1
            if count > max_count:
                max_count = count
                final_index = index

        return {
            -1: JokeType.random,
            0: JokeType.story,
            1: JokeType.knock_knock
        }[final_index]

    def _getJoke(self, jokeType: JokeType) -> Joke:
        if (jokeType == JokeType.story):
            return StoryJoke('Three men walk into a bar. The fourth one ducks')
        elif (jokeType == jokeType.knock_knock):
            return KnockKnockJoke('boo', 'dont cry, its only a joke')
        else:
            return StoryJoke('random joke. haha')

    def _shouldTellAnotherJoke(self, userInput: [str]) -> bool:
        return False
