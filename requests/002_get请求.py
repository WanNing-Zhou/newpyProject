#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :002_get请求.py
# @Time      :2023/3/1 19:20
# @Author    :周万宁

# urllib
# (1) 一个类型以及六个方法
# (2) get请求
# (3) post请求 百度翻译
# (4) ajax的get请求
# (5) ajax的post请求
# (6) cookie登录  微博
# (7) 代理
# (8) 代理池


# requests
# 1) 一个类型以及六个属性
# 2) get请求
# 3) post请求
# 4) 代理
# 5) cookie 验证码

import requests

url = 'http://www.baidu.com/s'

headers = {
    # 用户代理 浏览器等用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}

params = {
    'wd': '北京'
}

# url 请求资源路径
# params 请求参数
# kwargs 字典
response = requests.get(url=url, params=params, headers=headers)
# response.encoding = 'utf-8'
print(response.text)

# 总结
# 参数使用params传递
# 参数无需urlencode编码
# 不需要请求对象的定制
# 请求资源路径中?可加可不加
