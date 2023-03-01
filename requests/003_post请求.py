#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :003_post请求.py
# @Time      :2023/3/1 19:54
# @Author    :周万宁

import requests
import json
# post 请求
url = 'https://fanyi.baidu.com/sug'

headers = {
    # 用户代理 浏览器等用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}

data = {
    "kw": "eye"
}
# url 请求地址
# data 请求参数
# kwargs 字典

response = requests.post(url=url, data=data, headers=headers)
content = response.text
obj = json.loads(content)
print(obj)
print(response.json())

# 总结
# 1_ post请求 是不需要编解码
# 2. post需要传递data
