#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :007_urllib_post请求百度翻译.py
# @Time      :2023/2/27 9:52
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

import urllib.request
import urllib.parse
import json

# post 请求
url = 'https://fanyi.baidu.com/sug'

headers = {
    # 用户代理 浏览器等用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
}

data = {
    'kw': 'spider'
}
# post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求的参数,是不会拼接在url的后面的,而是需要放在请求对象定制的参数中
# post亲求的参数 必须要进行编码
request = urllib.request.Request(url=url, data=data, headers=headers)

# print(request)

# 模拟六零奶骑向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

print('content')
print(content)
# 字符串->json对象
obj = json.loads(content)
print(obj)

# post请求方式的参数 必须编码
# 编码之后
# 请求参数放在请求对象定制的方法中

