class logger:
    def __init__(self):
        self._errorFileName = "Logs/ErrorLog.txt"

    def Error(self, errorInfo: str):
        errorFile = open(self._errorFileName, 'a')
        errorFile.write("<---ERROR--->\n")
        errorFile.write(errorInfo)
        errorFile.write("\n<---ERROR--->\n")
        errorFile.close()

if __name__ == "__main__":
    None