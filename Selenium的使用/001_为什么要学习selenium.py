#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :001_为什么要学习selenium.py
# @Time      :2023/3/1 9:14
# @Author    :周万宁

import urllib.request

url = 'https://www.jd.com/'
response = urllib.request.urlopen(url)
# 不会获取所有的数据
content = response.read().decode('utf-8')

print(content)

