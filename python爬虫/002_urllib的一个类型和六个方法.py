#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :002_urllib的一个类型和六个方法.py
# @Time      :2023/2/26 22:45
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

import urllib.request


url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response 是 HTTPResponse的类型
# print(type(response))  # <class 'http.client.HTTPResponse'>

# 按照一字节一字节的去读
# content = response.read()
# print(content)

# 返回多少歌字节
# content = response.read(5)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# 返回状态码 如果是200 那么就证明我们的逻辑没有错
# print(response.getcode())

# 返回的是url地址
# print(response.geturl())

# 获取的是一些状态信息,
print(response.getheaders())

# 一个类型 HTTPResponse
# 六个方法 read readline readlines getcode geturl getheaders

