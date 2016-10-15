import unittest
from logger import logger

class LoggerTest(unittest.TestCase):
    def setUp(self):
        self.testLogger = logger()
        self.errorFile = 'Logs/ErrorLog.txt'
        f = open("Logs/ErrorLog.txt", 'w')
        f.write("")
        f.close()
        
    def test_ShouldInitializeLogger(self):
        self.assertNotEqual(self.testLogger, None)

    def test_ShouldWriteErrorToFile(self):
        testStatement = "Test Statment"
        self.testLogger.Error(testStatement)
        f = open(self.errorFile, 'r')
        actualLine = f.read()
        f.close()

        self.assertEqual("<---ERROR--->\nTest Statment\n<---ERROR--->\n", actualLine)

    def test_ShouldPrintTestAndClassToFile(self):
        testError = "This is an error"
        testClass = "error Class"
        self.testLogger.Error(testError, testClass)
        f = open(self.errorFile, 'r')
        self.assertEqual(f.readline(), "<---ERROR--->\n")
        self.assertEqual(f.readline(), "This is an error\n")
        self.assertEqual(f.readline(), "In Class error Class\n")
        self.assertEqual(f.readline(), "<---ERROR--->\n")
        f.close()
        

if __name__ == "__main__":
    unittest.main()