#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :010_ajax的get请求豆瓣电影前十页.py
# @Time      :2023/2/27 16:23
# @Author    :周万宁

import json
import urllib.parse
import urllib.request


def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    data = {
        'start': 20 * (page - 1),
        'limit': 20
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
        # 用户代理 浏览器等用户信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


# 获取响应的数据
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content, page):
    page = str(page)
    with open('doubanPages/douban' + page + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


# 程序的入口
if __name__ == "__main__":
    start_page = int(input('请数据起始的页码'))
    end_page = int(input('请输入结束的页码'))

    for page in range(start_page, end_page + 1):
        # 每一页都有自己的请求对象的定制
        request = create_request(page)
        # 获取响应的数据
        content = get_content(request)
        # content = json.loads(content)
        # 下载
        down_load(content, page)

# 下载豆瓣电影前10页的数据
# 1. 请求对象的定制
# 2. 获取响应的数据
# 3. 下载数据
