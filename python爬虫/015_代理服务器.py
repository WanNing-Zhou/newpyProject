#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :015_代理服务器.py
# @Time      :2023/2/28 8:09
# @Author    :周万宁

import urllib.request

if __name__ == "__main__":
    run_code = 0

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    # 用户代理 浏览器等用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

proxies = {'http': '117.94.113.72:9000'}

# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)

# handler build_opener open
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应信息
content = response.read().decode('utf-8')

# 保存
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
