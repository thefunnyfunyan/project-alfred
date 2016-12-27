class logger:
  def __init__(self):
    self._errorFileName = "Logs/ErrorLog.txt"
    self._traceFileName = "Logs/TraceLog.txt"

  def Error(self, errorInfo: str, errorClass: str = None, errorFunction: str = None):
    errorFile = open(self._errorFileName, 'a')
    errorFile.write("<---ERROR--->\n")
    errorFile.write(errorInfo)
    if (errorClass):
      errorFile.write("\nIn Class " + errorClass)
    if (errorFunction):
      errorFile.write("\nIn Function " + errorFunction)
    errorFile.write("\n<---ERROR--->\n")
    errorFile.close()

  def Trace(self, traceMessage: str):
    traceFile = open(self._traceFileName, 'a')
    traceFile.write(traceMessage + "\n")
    traceFile.close()


if __name__ == "__main__":
  None
