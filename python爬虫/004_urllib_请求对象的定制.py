#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :004_urllib_请求对象的定制.py
# @Time      :2023/2/27 8:45
# @Author    :周万宁
import urllib.request

if __name__ == "__main__":
    run_code = 0

url = 'https://www.baidu.com'

# url的组成
# 1. 协议 http/https (https 加了ssl 更加安全)
# 2. 主机
# 3. 端口号    http80   https 443  mysql3306 redis6379 mongodb27017
# 4. 路径
# 5. 参数
# 6. 锚点


# 因为urlopen方法中不能存储字典, 所以headers不能传递进去
# 请求对象的定制
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}
# 注意 因为参数顺序的问题,不能直接写url和headers 中间还有data,所以我们需要关键字传参
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode()

print(content)
