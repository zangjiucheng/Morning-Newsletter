# -*- coding: utf-8 -*-

##################################################
# Function: Grab the picture of XiaoHongShu
##################################################
# License: MIT License
##################################################
# Author: Jiucheng Zang
# Date: 2023-12-13
# Version: v1.0
# Update:
#   v1.0 at 2023-12-13
#       - Grab the picture of XiaoHongShu
##################################################

import requests
from bs4 import BeautifulSoup
from random import randint
from sys import argv

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text

def html_to_markdown(html):
    soup = BeautifulSoup(html, 'html.parser')

    allInfos = soup.find('div', id='userPostedFeeds')

    infoList = allInfos.findAll('section', class_='note-item')
    for info in infoList:
        info = BeautifulSoup(str(info), 'html.parser')
        info = info.find('a')
        newurl = "https://www.xiaohongshu.com"+info.get('href')
        data = get_html(newurl)
        soup = BeautifulSoup(data, 'html.parser')
        url = soup.find(attrs={"name":"og:image"})["content"]
        getImg(url)

def getImg(url):
    r = requests.get(url)
    num = random_with_N_digits(6)

    with open(f'./img/{num}.jpg', 'wb') as f:
        f.write(r.content)
    print(url)
    print(r.status_code)

if __name__ == "__main__":
    url = argv[1] 
    html = get_html(url)
    html_to_markdown(html)
