#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :026_序列化与反序列化.py
# @Time      :2023/2/26 10:57
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

import json

# file = open('names.txt', 'w')
# names = ['勋悟空', '猪八戒', '沙和尚', '唐僧']

# file.write(names)  # 出错,不能直接将列表写入到文件里

# 可以调用 json 的 dupms 方法, 传入一个对象参数
# result = json.dumps(names)
#
# # dumps 方法得到的结果是一个字符串
# print(type(result))  # <class 'str'>
#
# # 可以将字符出啊写入到文件里
# file.write(result)
#
# json.dump(names, file)
#
# file.close()

# names = ['勋悟空', '猪八戒', '沙和尚', '唐僧']
#
# fp = open('names.txt', 'r')
#
# content = fp.read()
# print(content)
# print(type(content))  # <class 'str'>
# result = json.loads(content)
# print(result)
# print(type(result))  # <class 'list'>

fp = open('names.txt', 'r')
result = json.load(fp)
print(result)
print(type(result))

