#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :绘制沪深指数.py
# @Time      :2023/5/16 14:13
# @Author    :周万宁


import numpy as np
import xlrd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
wb = xlrd.open_workbook("sh000001.xls")  # 沪指综合指数交易数据
sheet = wb.sheet_by_index(0)  # 通过索引获取sheet表格
d = sheet.col_values(0)[3100:3400]  # 第1列：交易日期
y = sheet.col_values(4)[3100:3400]  # 第5列：沪指收盘指数
f = plt.figure(figsize=(8, 4), dpi=80)  # 设置画布大小
plt.xlabel('交易日期', fontsize=12)
plt.ylabel('沪指综合收盘指数', fontsize=12)  # 添加纵轴标签
x = range(0, len(y))
t = []

plt.plot(x, y, marker=',', c='blue')  # 绘制折线图
for i in range(len(d)):  # 交易日期 ： 年月日之间加点“.”
    a = str(int(d[i]));
    b = a[0:4] + "." + a[4:6] + "." + a[6:8]
    t.append(b)
plt.xticks(range(0, 300, 15), t[0:300:15], rotation=45)  # rotation=45：旋转45度
date1 = t[0];
date2 = t[-1];
f.set_facecolor((0.92, 0.92, 0.96))  # 设置坐标轴颜色
plt.title('沪指综合收盘指数' + '(日期：' + date1 + '-' + date2 + ')', fontsize=12)
i_min, Min = np.argmin(y), np.min(y)
i_max, Max = np.argmax(y), np.max(y)
plt.text(i_max + 3, Max - 10, str(Max) + '(最高点)', color='r', fontsize=12)  # 最高点
plt.text(i_min - 25, Min + 6, str(Min) + '(最低点)', color='r', fontsize=12)  # 最低点

plt.show()  # 添加该行代码
