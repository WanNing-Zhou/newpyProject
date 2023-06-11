#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :matplotlib的使用.py
# @Time      :2023/6/11 10:48
# @Author    :周万宁

import numpy as np
import matplotlib.pyplot as plt  # 引入绘图库

x = np.arange(11)  # 从0开始步长为1的11个整数
y = np.array([0.15, 0.16, 0.14, 0.17, 0.12, 0.16, 0.1, 0.08, 0.05, 0.07, 0.06])  # 取11个数
plt.plot(x, y, color='red', marker='o') # 回值11个点的折线图,红色,点型
plt.show()

x = np.linspace(0, 2*np.pi, 30)                               # 将[0,2*PI]等分为30份的一维数组
y = np.sin(x)
plt.scatter(x, y,  marker='.', color='blue')
plt.savefig("2.jpg", dpi=48)
#  marker 点型, 颜色color为blue
plt.show()




