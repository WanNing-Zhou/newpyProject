#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :006_urllib_get请求的urlencode方法.py
# @Time      :2023/2/27 9:21
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0
import urllib.request
import urllib.parse

# urlencode应用场景: 多个参数的时候
# url = 'https://www.baidu.com/s?wd=周杰伦&sex=男'
base_url = 'https://www.baidu.com/s?'
# 定义一个字典
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}
# 将字典中的数据转成请求参数并且进行编码
new_data = urllib.parse.urlencode(data)

print(new_data)
# 将url 进行拼接
url = base_url + new_data
# 请求头信息
headers = {
    # 用户代理 浏览器等用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器发送请求
response = urllib.request.urlopen(request)

# 获取网页的数据
content = response.read().decode('utf-8')

print(content)

