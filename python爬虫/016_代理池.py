#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :016_代理池.py
# @Time      :2023/2/28 9:11
# @Author    :周万宁

import random
import urllib.request

if __name__ == "__main__":
    run_code = 0

proxies_pool = [
    {
        'http': '118.24.219.151:16817'
    },
    {
        'http': '118.24.219.151:11648'
    },
]

proxies = random.choice(proxies_pool)
print(proxies)

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    # 用户代理 浏览器等用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}

request = urllib.request.Request(url=url,headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)


