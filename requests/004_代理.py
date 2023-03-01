#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :004_代理.py
# @Time      :2023/3/1 20:27
# @Author    :周万宁
import requests

url = 'http://www.baidu.com/s'
headers = {
    # 用户代理 浏览器等用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}
data = {
    'wd': 'ip'
}

proxy = {
    'http': '183.236.232.160:8080'
}

response = requests.get(url=url, params=data, headers=headers, proxies=proxy)
response.encoding = 'utf-8'
content = response.text

with open('daili.html', 'w', encoding='utf-8') as fq:
    fq.write(content)
