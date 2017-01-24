import unittest
from IOEngine.IOEngine import IOEngine
from .JokeModule import JokeModule, StoryJoke, JokeType


class JokeModuleTest(unittest.TestCase):
    def setUp(self):
        self.io_engine = IOEngineFake()
        self.joke_module = JokeModule(self.io_engine)

    def test_InitializationTest(self):
        self.assertNotEqual(self.joke_module, None)

    def test_ShouldGetStoryJokeType(self):
        test_input = [['story'], ['long']]
        for input_word in test_input:
            self.assertEqual(self.joke_module._getJokeTypeFromUserInput(input_word), JokeType.story)

    def test_ShouldReturnStoryJoke(self):
        joke = self.joke_module._getJoke(JokeType.story)
        self.assertTrue(type(joke) is StoryJoke)

    def test_ShouldReturnTrueWhenGivenPositiveResponse(self):
        self.assertTrue(self.joke_module._shouldTellAnotherJoke(['yea']))

    def test_ShouldGetKnockKnockJokeType(self):
        self.assertEqual(self.joke_module._getJokeTypeFromUserInput(['knock', 'knock', 'joke']), JokeType.knock_knock)

    def test_ShouldGetRandomJokeType(self):
        self.assertEqual(self.joke_module._getJokeTypeFromUserInput([]), JokeType.random)

class IOEngineFake(IOEngine):
    def __init__(self):
        pass

    def getInput(self, starter: str = None):
        pass

    def output(self, outputString: str):
        pass
