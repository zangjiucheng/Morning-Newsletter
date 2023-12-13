# -*- coding: utf-8 -*-

##################################################
# Function: Get the date and festival
##################################################
# License: MIT License
##################################################
# Author: Jiucheng Zang
# Date: 2023-12-13
# Version: v1.0
# Update:
#   v1.0 at 2023-12-13
#       - Get the date and festival
##################################################

import collectInfo.DateData as DateData
import collectInfo.WeatherData as WeatherData
from json import dumps


class Data:
    def __init__(self,abs_path,api_key):
        Date = DateData.DateData(abs_path)
        Weather = WeatherData.Weather(api_key)
        self.date = Date.date
        self.chinese_date = Date.chinese_date
        self.festival = Date.festival
        self.sunrise_sunset_times = Date.sunrise_sunset_times
        self.weather = Weather.message

        self.mail_data = self.mailData()
        self.json_data = self.jsonData()

        # self.writeJsonData()

    def mailData(self):
        return "早上好！今天是" + self.date + self.sunrise_sunset_times + self.chinese_date+ \
            self.festival + self.weather + "\n祝您有愉快的一天！\n\n" 
    
    def jsonData(self):
        data = {
           "date": self.date,
           "sunrise_sunset_times": self.sunrise_sunset_times,
           "chinese_date": self.chinese_date,
           "festival": self.festival,
           "weather": self.weather
        }
        return dumps(data,ensure_ascii=False,indent=4)
    
    def writeJsonData(self):
        if self.json_data != "":
            f = open('/var/www/html/datajson/morningpost.json', 'w+')
            f.write(self.json_data)
    
    def __str__(self):
        return self.mail_data