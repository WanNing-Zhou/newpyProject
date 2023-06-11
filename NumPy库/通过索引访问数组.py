#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :通过索引访问数组.py
# @Time      :2023/6/10 20:16
# @Author    :周万宁


import numpy as np

arr = np.arange(10)
print('arr', arr)
print(arr[5])  # 首个索引号从0开始输出5
print(arr[3:5])
print(arr[6:-1:2]) # 索引号从第6个,到最后一个, 2为步长, 表示每隔一个元素

print(np.random.__doc__)

help(np.random.permutation)
