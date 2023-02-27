#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :009_urllib_豆瓣电影爬取.py
# @Time      :2023/2/27 14:13
# @Author    :周万宁

# get请求
# 获取豆瓣电影的第一页数据


if __name__ == "__main__":
    run_code = 0

# 爬取豆瓣电影前10页数据

import urllib.request
import urllib.parse

# 下载前10页数据
# 下载的步骤:  1. 请求对象的定制 2. 响应数据的获取 3. 下载


# 每次执行一次返回一个request对象
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    # 用户代理 浏览器等用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)

# (3) 数据下载到本地
# open方法默认情况使用的是GBK的编码 如果我们想要保存汉字, 那么需要在open方法中指定编码格式为utf-8
# encodeing = 'utf-8'
# fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(content)
# fp.close()

with open('douban1.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
