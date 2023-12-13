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

from time import strftime, localtime
from borax.calendars.lunardate import LunarDate
from urllib.request import urlopen
from bs4 import BeautifulSoup

class DateData:
    def __init__(self,abs_path):
        self.__abs_path = abs_path
        self.chinese_date = self.get_chinese_date() # type: ignore
        self.date = self.get_date()
        self.festival = self.get_festival() # type: ignore
        self.sunrise_sunset_times = self.sunrise_sunset() # type: ignore
        

    def get_date(self):
        chinese_week_dict = {'Monday': '星期一', 'Tuesday': '星期二', 'Wednesday': '星期三', 'Thursday': '星期四',
                            'Friday': '星期五', 'Saturday': '星期六', 'Sunday': '星期天'}
        week_day = chinese_week_dict[strftime("%A", localtime())]
        date = strftime("%Y年%m月%d日 ", localtime()) + week_day + " "
        return date
    
    def get_chinese_date(self) -> str:
        today = LunarDate.today()
        return today.strftime('%G %M月%D')
    
    def get_festival(self):
        festival_dict = {}
        format_date = strftime("%m%d", localtime())
        with open(self.__abs_path + "festival.txt") as f:
            festivals = f.readlines()
            f.close()
        for festival in festivals:
            festival = festival.split("：")
            data, name = festival
            data_list = str(data).split("月")
            new_date = data_list[0].zfill(2) + data_list[1][:-1].zfill(2)
            festival_dict[new_date] = name
        try:
            festival = "。" + str(festival_dict[format_date])
            return festival
        except:
            festival = "\n"
            return festival
        
    def sunrise_sunset(self):
        soups = BeautifulSoup(urlopen('https://www.timeanddate.com/sun/canada/montreal'), 'html.parser').find("p", attrs={
            "class": "dn-mob"}).text # type: ignore
        soups = soups.split("pm", 1)[0].split(" ")
        soups = "(日出 " + soups[0] + "/日落 " + soups[3] + ")\n"
        return soups