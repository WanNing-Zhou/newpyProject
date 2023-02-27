#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :011_post请求肯德基官网.py
# @Time      :2023/2/27 17:01
# @Author    :周万宁

# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

import urllib.request
import urllib.parse
import json


def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': 10
    }

    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        # 用户代理 浏览器等用户信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
    }

    request = urllib.request.Request(url=base_url, data=data, headers=headers)
    return request


# 获取响应的数据
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content, page):
    page = str(page)
    with open('kfcPages/kfcPage' + page + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == "__main__":
    start_page = int(input('清输入起始页码'))
    end_page = int(input('清输入结束页码'))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(content, page)
