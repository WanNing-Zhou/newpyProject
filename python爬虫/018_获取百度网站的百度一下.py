#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :018_获取百度网站的百度一下.py
# @Time      :2023/2/28 14:00
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

# 1) 获取网页的源码
# 2) 解析   解析的服务器响应的文件 etree.HTML
# 3) 打印

import urllib.request
from lxml import etree

url = 'https://www.baidu.com'

headers = {
    # 用户代理 浏览器等用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}
# 请求对象的定制
request = urllib.request.Request(url = url, headers=headers)

# 模拟浏览器访问服务器

response = urllib.request.urlopen(request)

# 获取网页源码
content = response.read().decode('utf-8')

# print(content)

# 解析网页源码, 来获取我们想要的数据
# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据 xpath的返回值是一个列表类型的数据
result = tree.xpath('//input[@type="submit" and @id="su"]/@value')

print(result)






