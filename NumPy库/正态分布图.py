#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :正态分布图.py
# @Time      :2023/6/10 19:55
# @Author    :周万宁


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
data = np.random.normal(0, 1, 10000)  # 生成10000个均值为0, 方差为1的高斯分布数据

print(data)

print(min(data), max(data))  # 最小值, 最大值

n,bins,patches = plt.hist(data,50,facecolor='red',edgecolor='white') # 直方图函数
plt.grid(True) # 设置显示网络
plt.show() # 显示绘图



