#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :001_requests的基本使用.py
# @Time      :2023/3/1 19:11
# @Author    :周万宁

import requests

url = 'http://www.baidu.com'

response = requests.get(url=url)

# 一个类型和六个属性
# Response类型
# print(type(response))

# 以字符串的形式来返回了网页的源码获取网站的源码 可能会产生乱码
# print(response.text)

# 设置响应的编码格式
# response.encoding = 'utf-8'
# print(response.text)

# 返回一个url地址
# print(response.url)

# 返回的是二进制的数据
print(response.content)

# 返回响应的状态码
print(response.status_code)

# 返回响应头
print(response.headers)

