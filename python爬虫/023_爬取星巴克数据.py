#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :023_爬取星巴克数据.py
# @Time      :2023/3/1 8:49
# @Author    :周万宁


import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

# //ul[@class="grid padded-3 product"]//strong//text()

soup = BeautifulSoup(content, 'lxml')
name_list = soup.select('.grid strong')

for name in name_list:
    print(name)

# print(name_list)
# print(content)
