#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :013_微博的cookie登录.py
# @Time      :2023/2/27 21:47
# @Author    :周万宁

# 适用的场景: 数据采集的时候 需要绕过登录,然后登录到某个页面
# 个人信息页面时utf-8 但是还报错了编码错误, 因为并没有进入到个人信息页面, 而是跳转了登录页面
# 登录页面不是utf-8 而报错

# 什么情况下访问不成功?
# 因为请求头信息不够 所以访问不成功

import urllib.request


if __name__ == "__main__":

    url = 'https://weibo.cn/个人信息'
    #解决60
    # cookie中携带者你的登录信息 如果又登录之后的cookie 那么我们就可以携带者cookie进入到任何页面
    # referer 破案段当前路径是不是由上一个路径的  一般情况下  是做图片防盗链

    headers = {
        # 用户代理 浏览器等用户信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56}'
    }

    request = urllib.request.Request(url=url,headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    # 将数据保存到本地
    with open('weibo.html', 'w', ecoding='utf-8') as fp:
        fp.write(content)


