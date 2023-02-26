#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :023_文件的打开与关闭.py
# @Time      :2023/2/26 9:47
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0


# 打开文件
fp = open('test.txt', 'w')

fp.write('hello world')

fp.close()


