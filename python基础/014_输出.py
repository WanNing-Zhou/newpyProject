#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :014_输出.py
# @Time      :2023/2/25 14:44
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

# 普通输出
print('你好')

# 格式化输出
# scrapy框架的时候使用 存在excel文件,mysql,redis中

# %s 字符串
# %d 数字
name = '勋悟空'
age = 18
print('我是%s' % name)  # 我是勋悟空
print('我是%s,我今年%d岁了' % (name, age))  # 我是勋悟空,我今年18岁了
