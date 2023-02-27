#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :014_handler的基本使用.py
# @Time      :2023/2/27 23:54
# @Author    :周万宁
# 需求 使用handler来访问百度 获取网页代码
import urllib.request

if __name__ == "__main__":
    run_code = 0

url = 'http://www.baidu.com'

headers = {
    # 用户代理 浏览器等用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# handler build_opener open

# 1) 获取handler对象
handler = urllib.request.HTTPHandler()

# 2) 获取opener对象
opener = urllib.request.build_opener(handler)

# 3) 调用open方法

response = opener.open(request)
content = response.read().decode('utf-8')

print(content)
