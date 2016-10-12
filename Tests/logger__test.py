import unittest
from logger import logger

class LoggerTest(unittest.TestCase):
    def setUp(self):
        self.testLogger = logger()
        f = open("Logs/ErrorLog.txt", 'w')
        f.write("")
        f.close()
        
    def test_ShouldInitializeLogger(self):
        self.assertNotEqual(self.testLogger, None)

    def test_ShouldWriteErrorToFile(self):
        testStatement = "Test Statment"
        self.testLogger.Error(testStatement)
        f = open("Logs/ErrorLog.txt", 'r')
        actualLine = f.read()
        f.close()

        self.assertEqual("<---ERROR--->\nTest Statment\n<---ERROR--->\n", actualLine)

    def test_ShouldPrintTestAndClassToFile(self):
        testError = "This is an error"
        testClass = "Class"
        

if __name__ == "__main__":
    unittest.main()