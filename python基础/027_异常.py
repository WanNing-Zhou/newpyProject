#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :027_异常.py
# @Time      :2023/2/26 11:47
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

try:
    f = open('卡卡西.txt', 'r')
    print(f.read())
except FileNotFoundError:
    print('文件不存在')

