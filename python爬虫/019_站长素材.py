#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :019_站长素材.py
# @Time      :2023/2/28 14:33
# @Author    :周万宁


# https://sc.chinaz.com/tupian/fengjingtupian.html

# (1) 请求对象的定制
# (2) 获取玩也的源码
# 需求 下载的前十页的图片

import urllib.request
from lxml import etree

def create_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/fengjingtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/fengjingtupian'+str(page)+'.html'

    headers = {
        # 用户代理 浏览器等用户信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    tree = etree.HTML(content)
    tree.xpath('//')

    # 下载图片
    urllib.request.urlretrieve('图片地址', '文件的名字')


if __name__ == "__main__":
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(page)
        # 获取网页的源码
        content = get_content(request)
        # 下载
        down_load(content)
