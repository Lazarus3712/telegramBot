import requests
from bs4 import BeautifulSoup


class Weather:
    URL = "https://ua.sinoptik.ua/"
    __LOCAL = "погода-львів"
    __DATE = ""
    __TITLE = ""
    __MIN_TEMP = None
    __MAX_TEMP = None
    __WEATHER = ""
    __INFO = "null"

    __region = 'львівська-область/'
    __district = 'жовківський-район/'
    __position = list('')
    '''village = 'львівська-область/'''

    list_region = {}
    list_district = {}
    list_position = {}

    def set_region(self, region='львівська-область/'):
        self.__region = region + '/'
        self.__position.append(self.__region)

    def set_district(self, district='жовківський-район/'):
        self.__district = district + '/'
        self.__position.append(self.__district)

    def get_list_region(self):
        response = requests.get(self.URL + 'україна/').text
        page = BeautifulSoup(response, 'lxml')
        main = page.find(class_='mapRightCol').find_all('ul')[1].find_all('a')
        self.list_region = {context.text: context.get('href') for context in main}
        return self.list_region

    def get_list_district(self):
        response = requests.get(self.URL + 'україна/' + self.__region).text
        page = BeautifulSoup(response, 'lxml')
        main = page.find(class_='mapRightCol').find_all('ul')[1].find_all('a')
        self.list_district = {context.text: context.get('href') for context in main}
        return self.list_district

    def set_local(self, local='львів'):
        self.__LOCAL = 'погода-' + str(local).lower()

    '''def set_region(self, region):
        self.__LOCAL += self.URL + '/україна/' + region'''

    def set_date(self, date):
        self.__DATE = date

    def update(self):
        response = requests.get(self.URL + self.__LOCAL + "/" + self.__DATE).text
        page = BeautifulSoup(response, "lxml")

        main = page.find(class_="main  loaded")

        self.__TITLE = str(page.find(class_="day-link").get("data-link"))[2:]

        self.__MIN_TEMP = int(str(main.find(class_="min").find("span").text)[1:-1])
        self.__MAX_TEMP = int(str(main.find(class_="max").find("span").text)[1:-1])
        self.__WEATHER = str(main.find(class_="weatherIco").get("title"))
        self.__INFO = str(page.find(class_="wDescription clearfix")
                          .find(class_="description").text)[2:]

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
s.get_list_region()
print(s.get_list_region())
print(s.get_list_district())

# s.set_region()
# s.update()
# print(s.get_list_region())
