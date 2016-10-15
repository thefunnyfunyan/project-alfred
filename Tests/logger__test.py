import unittest
from logger import logger

class LoggerTest(unittest.TestCase):
    def setUp(self):
        self.testLogger = logger()
        self.errorFile = "Logs/ErrorLog.txt"
        self.traceFile = "Logs/TraceLog.txt"
        f = open(self.errorFile, 'w')
        f.write("")
        f.close()
        f = open(self.traceFile, 'w')
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

    def test_ShouldPrintErrorAndClassAndMethodToFile(self):
        self.testLogger.Error("This is an Error", "errorClass", "errorFunction")
        f = open(self.errorFile, 'r')
        self.assertEqual(f.readline(), "<---ERROR--->\n")
        self.assertEqual(f.readline(), "This is an Error\n")
        self.assertEqual(f.readline(), "In Class errorClass\n")
        self.assertEqual(f.readline(), "In Function errorFunction\n")
        self.assertEqual(f.readline(), "<---ERROR--->\n")
        f.close()
    
    def test_ShouldPrintTraceLogsToFile(self):
        self.testLogger.Trace("This is a trace message")
        self.testLogger.Trace("This is another trace message")
        f = open(self.traceFile, 'r')
        self.assertEqual(f.readline(), "This is a trace message\n")
        self.assertEqual(f.readline(), "This is another trace message\n")
        f.close()

if __name__ == "__main__":
    unittest.main()