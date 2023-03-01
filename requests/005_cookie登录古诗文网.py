#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :005_cookie登录古诗文网.py
# @Time      :2023/3/1 20:44
# @Author    :周万宁


# 通过登录然后登录接口

# 通过找登录接口发现, 登录的时候需要的参数很多
# __VIEWSTATE: IO2Kgc8pWVjRvJCTPc1hjQcYERMnCFsYyok3xp4F7n5BfLm/kherP8cC+BjmS+tDpraq7yTqbWGpd4HIxrNPycBFs9Lq/diTHF/wU0mL/5H0t7bLmQBejgnB4bCIiXnaKQSiOBPQ4A8ITNTbygyVayhSqYg=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx?type=s
# email: 1879154660@qq.com
# pwd: dsojflkjds
# code: 82MN
# denglu: 登录

# 有时候会观察到前两个请求参数是一个变化的值

# 难点: 1) 没有见过的请求参数 一般情况下看不到的数据 都是在页面的源码中
# 我们观察到这两个数据在页面的源码中,所以问哦们获取到页面的源码,然后进行解析就可以获取了
# 2) 验证码
import urllib.request

import requests
from bs4 import BeautifulSoup

# 这是登录页面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

# 获取页源码
response = requests.get(url=url, headers=headers)
content = response.text
# print(content)

# 解析页面源码 然后获取_V _VI
soup = BeautifulSoup(content, 'lxml')
viewState = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewStateGenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# print(viewState)
# print(viewStateGenerator)

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
# print(code)
code_url = 'https://so.gushiwen.cn' + code

# 坑
# 下载的时候请求了一次和看到的就不一样了
# urllib.request.urlretrieve(url=code_url, filename='code.jpg')

# requests 里面有一个方法 session() 通过session的返回值,就能使请求变成一个对象
session = requests.session()
# 验证码url的内容
response_code = session.get(code_url)
# 此时要使用二进制数据,因为我们要使用的是图片的下载
content_code = response_code.content
# wb的模式就是将二进制文件写入到文件
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)
# 获取了验证码的图片之后 下载到本地, 然后观察验证码, 观察之后 然后再控制台输入这个验证码 ,就可以将这个值给code的参数, 就可以登录了
code_name = input('请输入你的验证码')

# 点击登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
data_post = {
    '__VIEWSTATE': viewState,
    '__VIEWSTATEGENERATOR': viewStateGenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx?type=s',
    'email': '1879154660@qq.com',
    'pwd': '19491001ljs',
    'code': code_name,
    'denglu': '登录',
}

response_post = requests.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
# print(response_post.json())
with open('gushiwen.html', 'w', encoding='utf-8') as fq:
    fq.write(content_post)

# 难点
# (1) 隐藏域
# (2) 验证码
