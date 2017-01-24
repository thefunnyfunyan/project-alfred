from .ModuleInterface import IModule
from  IOEngine.IOEngine import IOEngine
from enum import Enum


class JokeType(Enum):
    random = 0
    story = 1
    knock_knock = 2


class Joke(object):
    def tellJoke(self, io_engine: IOEngine) -> None:
        pass


class StoryJoke(Joke):
    def __init__(self, story: str):
        self._story = story

    def tellJoke(self, io_engine: IOEngine) -> None:
        io_engine.output(self._story)


class KnockKnockJoke(Joke):
    def __init__(self, set_up: str, punch_line: str):
        self._setUp = set_up
        self._punchLine = punch_line

    def tellJoke(self, io_engine: IOEngine) -> None:
        io_engine.output('Knock knock')
        io_engine.getInput()
        io_engine.output(self._setUp)
        io_engine.getInput()
        io_engine.output(self._punchLine)


class JokeModule(IModule):
    _keyWords = ['joke', 'laugh', 'funny']

    def execute(self, word_list: [str]) -> None:
        while True:
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

    def _getJoke(self, joke_type: JokeType) -> Joke:
        if joke_type == JokeType.story:
            return StoryJoke('Three men walk into a bar. The fourth one ducks')
        elif joke_type == joke_type.knock_knock:
            return KnockKnockJoke('boo', 'dont cry, its only a joke')
        else:
            return StoryJoke('random joke. haha')

    def _shouldTellAnotherJoke(self, user_input: [str]) -> bool:
        _yes_words = ['yes', 'yea', 'sure', 'ok']
        for input_word in user_input:
            for word in _yes_words:
                if input_word == word:
                    return True
        return False
