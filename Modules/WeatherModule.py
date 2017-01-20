import requests
from functools import partial
from .ModuleInterface import IModule

class WeatherModule(IModule):
    _keyWords = ['weather', 'temperature', 'forecast']
    _requestUrl = 'https://api.darksky.net/forecast/80ae193703675485dfb06172c87a3911/'
    _location = '39.188771, -96.549764'

    def execute(self, wordList: [str]) -> None:
        returnData = requests.get(self._requestUrl+self._location)
        jsonData = returnData.json()
        self.interpretCommand(word_list=wordList, json_data=jsonData)

    def interpretCommand(self, word_list: [str], json_data: object) -> None:
        hour_summary_keywords = ['now', 'right', 'currently']
        day_summary_keywords = ['today', 'day', 'todays']
        week_summary_keywords = ['week', 'upcoming']

        max_count = 0
        command_index = -1
        for index, command_keywords in enumerate([hour_summary_keywords, day_summary_keywords, week_summary_keywords]):
            count = 0
            for keyword in command_keywords:
                for word in word_list:
                    if keyword.upper() == word.upper():
                        count += 1
            if count > max_count:
                command_index = index

        {
            -1: self.noCommand,
            0: partial(self.getCurrentHourSummary, jsonData=json_data),
            1: partial(self.getCurrentDaySummary, jsonData=json_data),
            2: partial(self.getCurrentWeekSummary, jsonData=json_data)
        }[command_index]()

    def noCommand(self):
        self.ioEngine.output('nothing supplied')

    def getCurrentHourSummary(self, jsonData: str) -> None:
        try:
            currentData = jsonData['minutely']
            self.ioEngine.output(currentData['summary'])
        except Exception as e:
            self.handleWeatherError()

    def getCurrentDaySummary(self, jsonData: str) -> None:
        try:
            currentData = jsonData['hourly']
            self.ioEngine.output(currentData['summary'])
        except Exception as e:
            self.handleWeatherError()

    def getCurrentWeekSummary(self, jsonData: str) -> None:
        try:
            currentData = jsonData['daily']
            self.ioEngine.output(currentData['summary'])
        except Exception as e:
            self.handleWeatherError()

    def handleWeatherError(self):
        self.ioEngine.output('My apologies but there was a problem with the weather data. Please try again')
