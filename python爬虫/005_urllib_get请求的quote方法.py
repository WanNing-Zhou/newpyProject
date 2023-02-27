#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :005_urllib_get请求的quote方法.py
# @Time      :2023/2/27 9:06
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

import urllib.request
import urllib.parse

# 需求: 获取 https://www.baidu.com/s?wd=周杰伦 的网页源码

url = 'https://www.baidu.com/s?wd='

# 请求对象的定制为了解决反爬的第一种手段
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}

# 将周杰伦三个字编程unicode编码的格式
# 我们需要依赖于urllib.parse
name = urllib.parse.quote('周杰伦')
print('name', name)

url = url + name

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 打印数据
print(content)

