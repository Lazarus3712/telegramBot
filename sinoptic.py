import requests
from bs4 import BeautifulSoup


class Weather:
    URL = "https://ua.sinoptik.ua/"
    __DATE = ""
    __TITLE = ""
    __MIN_TEMP = None
    __MAX_TEMP = None
    __WEATHER = ""
    __INFO = "null"

    __region = 'львівська-область/'
    __district = 'жовківський-район/'
    __position = list('')

    def set_region(self, region='львівська-область/'):
        self.__region = region + '/'
        self.__position.append(self.__region)

    def set_district(self, district='жовківський-район/'):
        self.__district = district + '/'
        self.__position.append(self.__district)

    def set_date(self, date):
        self.__DATE = date

    def update(self, path):
        response = requests.get(path).text
        page = BeautifulSoup(response, "lxml")

        main = page.find(class_="main  loaded")

        self.__TITLE = str(page.find(class_="day-link").get("data-link"))[2:]

        self.__MIN_TEMP = int(str(main.find(class_="min").find("span").text)[1:-1])
        self.__MAX_TEMP = int(str(main.find(class_="max").find("span").text)[1:-1])
        self.__WEATHER = str(main.find(class_="weatherIco").get("title"))
        self.__INFO = str(page.find(class_="wDescription clearfix")
                          .find(class_="description").text)[2:]

    def get_list_region(self):
        response = requests.get(self.URL + 'україна/').text
        page = BeautifulSoup(response, 'lxml')
        main = page.find(class_='mapRightCol').find_all('ul')[1].find_all('a')
        return {context.text: context.get('href') for context in main}

    def get_list_district(self):
        response = requests.get(self.URL + 'україна/' + self.__region).text
        page = BeautifulSoup(response, 'lxml')
        main = page.find(class_='mapRightCol').find_all('ul')[1].find_all('a')
        return {context.text: context.get('href') for context in main}

    def get_list_position(self):
        response = requests.get(self.URL + 'україна/' + self.__region + self.__district).text
        page = BeautifulSoup(response, 'lxml')
        main = page.find(class_='mapBotCol').find_all('ul')[1].find_all('a')
        return {context.text: context.get('href')[2:] for context in main}

    def get_title(self) -> str:
        return str(self.__TITLE)

    def get_min_temp(self) -> int:
        return self.__MIN_TEMP

    def get_max_temp(self) -> int:
        return self.__MAX_TEMP

    def get_weather(self) -> str:
        return str(self.__WEATHER)

    def get_info(self) -> str:
        return str(self.__INFO)


s = Weather()
s.update('https://' + s.get_list_position()['с Добросин'])
s.get_list_region()

print(s.get_list_position())
print()
print(s.get_title())
print(s.get_weather())
print(s.get_info())
