#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :025_文件的写入.py
# @Time      :2023/2/26 10:17
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0


# 文件的读写
# 打开一个文件
f = open('test.txt', 'a')
# 向文件中写入数据
f.write('hello world\n')
# 关闭文件
f.close()

# 读数据
fp = open('test.txt', 'r')
# 默认情况下 read是一字节一字节的读效率比较低
# content = fp.read()
# print(content)

# readline只能读取一行
# content = fp.readline()
# print(content)

content = fp.readlines()
print(content)

