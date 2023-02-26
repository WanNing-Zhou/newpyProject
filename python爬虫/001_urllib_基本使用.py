#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :001_urllib_基本使用.py
# @Time      :2023/2/26 22:07
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0
# 导入urllib库
import urllib.request

# 使用urllib获取百度首页的源码
# (1)定义一个url,就是访问的地址
url = 'http://www.baidu.com'

# (2)模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# (3) 获取响应中的页面的源码
# read方法返回的是字节形式的二进制数据
# 我们要将二进制的数转换成字符串
# 二进制--> 字符串 节码 decode('编码的格式')
content = response.read().decode('utf-8')

# (4) 打印数据
print(content)



