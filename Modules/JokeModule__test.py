import unittest
from IOEngine.IOEngine import IOEngine
from .JokeModule import JokeModule, StoryJoke, JokeType


class JokeModuleTest(unittest.TestCase):
    def setUp(self):
        self.ioEngine = IOEngineFake()
        self.jokeModule = JokeModule(self.ioEngine)

    def test_InitializationTest(self):
        self.assertNotEqual(self.jokeModule, None)

    def test_ShouldGetStoryJokeType(self):
        testInput = [['story'], ['long']]
        for input in testInput:
            self.assertEqual(self.jokeModule._getJokeTypeFromUserInput(input), JokeType.story)

    def test_ShouldReturnStoryJoke(self):
        joke = self.jokeModule._getJoke(JokeType.story)
        self.assertTrue(type(joke) is StoryJoke)

    def test_ShouldReturnTrueWhenGivenPositiveResponse(self):
        self.assertTrue(self.jokeModule._shouldTellAnotherJoke([]))

    def test_ShouldGetKnockKnockJokeType(self):
        self.assertEqual(self.jokeModule._getJokeTypeFromUserInput(['knock', 'knock', 'joke']), JokeType.knock_knock)

    def test_ShouldGetRandomJokeType(self):
        self.assertEqual(self.jokeModule._getJokeTypeFromUserInput([]), JokeType.random)

class IOEngineFake(IOEngine):
    def __init__(self):
        pass

    def getInput(self, starter: str = None):
        pass

    def output(self, outputString: str):
        pass
