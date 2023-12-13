# -*- coding: utf-8 -*-

##################################################
# Function: Get weather data
##################################################
# License: MIT License
##################################################
# Author: Jiucheng Zang
# Date: 2023-12-13
# Version: v1.0
# Update:
#   v1.0 at 2023-12-13
#       - Get weather data
##################################################

from translators.server import google
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

class Weather:
    
    def __init__(self,api_key):
        self.__hdr = {'User-Agent': 'Mozilla/5.0'}
        self.soup = self.getSoup()
        self.datas = urlopen("https://api.openweathermap.org/data/2.5/weather?q=Montreal,ca&lang=zh_cn&appid=" + api_key).read().decode("utf-8")
        self.__weather_emoji_dict = {'Clouds': '🌤 ', 'Clear': '☀ ', 'Rain': '🌧️ ', 'Snow': '❄ ', 'Extreme': '⚡ ', 'Drizzle': '💧 ','Fog': '🌫️ ', 'Mist': '🌫️'}
        self.uv_index = self.uvindex() 
        self.temperature = self.max_temp_and_min_temp()
        self.body_temperature = self.body_temp()
        self.wind_speed = self.windSpeed()
        self.wind_direction = self.windDirection()
        self.special_weather = self.special_event()
        self.humidity = self.getHumidity()
        self.cloud_percent = self.Cloud()
        self.message = self.messageDescription()

        self.receiver_mail_adress_list = "None"
    
    def F_temp_to_C_temp(self,F_temp: int) -> int:
            C_temp = (float(F_temp) - 32) / 1.8
            return int(C_temp)
    
    def tranlate(self,string) -> str:
        trans = google(string, to_language="zh-CN")
        return str(trans)
    
    def getSoup(self):
        soup = BeautifulSoup(urlopen(Request("https://weather.com/weather/today/l/45.51,-73.70?par=google", headers=self.__hdr)),
                         'html.parser')
        return soup
    
    def uvindex(self):
        soup = BeautifulSoup(urlopen(Request("https://www.theweathernetwork.com/en/city/ca/quebec/montreal/uv")),
                             'html.parser')
        try:
            uvindex = int(soup.find(
                "div", attrs={"data-testid": "uv-daily-max-report"}).find_all("div")[1].text) # type: ignore
            if uvindex > 5:
                uvindex = "紫外线指数:" + str(uvindex) + "，带好防晒🧴"
            else:
                uvindex = "紫外线指数:" + str(uvindex)
        except:
            uvindex = "Data Error"
        return uvindex
    
    def special_event(self):
        try:
            special_events_list = []
            data = BeautifulSoup(
                urlopen(Request(
                    "https://www.theweathernetwork.com/ca/alerts/high-alert/quebec/montreal", headers=self.__hdr)),
                'html.parser').find("div", attrs={"class": "master-alert"})
            detail = (data.find("div", attrs={"class": "alert-content clearfix"}).text).split("###")[0].strip().replace( # type: ignore
                "\n\n", "\n")
            soup = data.find_all("div", attrs={"class": "title-holder"}) # type: ignore
            for data in soup:
                event = str(data).split("<span>")[1].split("</span>")[0]
                date = str(data).split(
                    '<span class="sub-title">')[1].split("</span>")[0]
                special_events_list.append(event + date)
            special_event = "\n".join(special_events_list)
            out = "特殊天气声明⚡:\n" + self.tranlate(special_event) + "\n详细信息 \n" + self.tranlate(detail)
        except:
            out = "无特别天气声明"
        return out

    def max_temp_and_min_temp(self):
        temps = []
        temps_datas = BeautifulSoup(urlopen(Request(
            "https://weather.gc.ca/forecast/hourly/qc-147_metric_e.html", headers=self.__hdr)),  'html.parser')
        lines = temps_datas.find_all("tr")
        for x in range(2, len(lines)):
            try:
                temp = BeautifulSoup(
                    str(lines[x]), 'html.parser').find_all("td")[1].text
                temps.append(int(temp))
            except:
                break
        max_temperature = max(temps)
        min_temperature = min(temps)
        return max_temperature, min_temperature
    
    def body_temp(self):
        emoji_dict = [" 🥶", " ❄", " 😰", " 😊", " 😀", " 🥵", " 🔥"]
        tempSoup = self.soup.find("div", attrs={"data-testid": "FeelsLikeSection"}).find("span", attrs={ # type: ignore
            "data-testid": "TemperatureValue"}).text # type: ignore
        date_temp = self.F_temp_to_C_temp(int(tempSoup.strip('°')))
        temp = str(date_temp) + "°"
        if date_temp <= -22:
            tempData = temp + emoji_dict[0]
        elif date_temp <= -10:
            tempData = temp + emoji_dict[1]
        elif date_temp <= 0:
            tempData = temp + emoji_dict[2]
        elif date_temp <= 15:
            tempData = temp + emoji_dict[3]
        elif date_temp <= 24:
            tempData = temp + emoji_dict[4]
        elif date_temp <= 30:
            tempData = temp + emoji_dict[5]
        elif date_temp > 30:
            tempData = temp + emoji_dict[6]
        else:
            tempData = ""
        return tempData
    
    def getHumidity(self):
        try:
            humidity = self.datas.split('"humidity":', 1)[1].split('}')[0]
            try:
                humidity = humidity.split(',')[0]
            except:
                pass
        except:
            try:
                humidity = self.datas.split('"humidity":', 1)[1].split(',')[0]
            except:
                humidity = "error"
        return humidity
    
    def Cloud(self):
        return self.datas.split('"clouds":{"all":', 1)[1].split('}')[0]
         
    
    def windDirection(self):
        try:
            wind_deg =  int(self.datas.split('"deg":', 1)[1].split(',')[0])
        except:
            wind_deg = int(self.datas.split('"deg":', 1)[1].split('}')[0])
        if 45 <= wind_deg < 135:
            return "东风 "
        elif 135 <= wind_deg < 225:
            return "南风 "
        elif 225 <= wind_deg < 315:
            return "西风 "
        else:
            return "北风 "
    
    def windSpeed(self):
        return self.datas.split('"wind":{"speed":', 1)[1].split(',"deg"')[0]

    def messageDescription(self):
        weather = self.datas.split('"main":"', 1)[1].split('","description"')[0]
        weather_description = self.datas.split('"description":"', 1)[
            1].split('","icon"')[0]
        try:
            weather_description_temp = weather_description.split("，")
            weather_description = weather_description_temp[0] + \
                "转"+weather_description_temp[1]
        except:
            pass
        try:
            emoji_weather = self.__weather_emoji_dict[weather]
        except:
            emoji_weather = ""

        out = "蒙特利尔24小时天气:\n" + weather_description + emoji_weather + str(self.temperature[0])+"℃" + " ~ " + \
        str(self.temperature[1]) + "\n当前体感温度: " + self.body_temperature + "\n" \
        + self.wind_direction + self.wind_speed + "米/秒 " + "当前湿度:" + self.humidity + "%、\n云覆盖率:" + self.cloud_percent + "% " + self.uv_index + " 😀\n" + self.special_weather

        return out            

        

