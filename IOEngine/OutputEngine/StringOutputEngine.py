from .OutputEngineInterface import IOutputEngine


class StringOutputEngine(IOutputEngine):
    def output(self, output_string: str):
        print(output_string)
