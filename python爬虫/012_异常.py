#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :012_异常.py
# @Time      :2023/2/27 17:24
# @Author    :周万宁

import urllib.request
import urllib.error

if __name__ == "__main__":
    run_code = 0


url = 'https://blog.csdn.net/sulixu/article/details/119818949'

headers = {
    # 用户代理 浏览器等用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}
try:
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode()
    print(content)
except urllib.error.HTTPError:
    print('系统这正在升级')
except urllib.error.URLError:
    print('都说过了, 系统正在升级')


