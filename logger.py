class logger:
    def __init__(self):
        self._errorFileName = "Logs/ErrorLog.txt"

    def Error(self, errorInfo: str, errorClass: str = None, errorMethod: str = None):
        errorFile = open(self._errorFileName, 'a')
        errorFile.write("<---ERROR--->\n")
        errorFile.write(errorInfo)
        if(errorClass):
            errorFile.write("\nIn Class " + errorClass)
        if(errorMethod):
            errorFile.write("\nIn Method " + errorMethod)
        errorFile.write("\n<---ERROR--->\n")
        errorFile.close()

if __name__ == "__main__":
    None