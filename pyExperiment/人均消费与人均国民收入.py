#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :人均消费与人均国民收入.py
# @Time      :2023/5/16 14:32
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0
import matplotlib.pyplot as plt;
import xlrd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
wb = xlrd.open_workbook("人均消费金额与人均国民收入.xls")
sheet = wb.sheet_by_index(0)  # 通过索引获取表格
col_1 = sheet.col_values(2)  # 获取第2列内容：人均国民收入
col_2 = sheet.col_values(3)  # 获取第3列内容：人均收费金额
x = col_1[1:21];
y = col_2[1:21]  # 获取第1行至20行数据
plt.figure(figsize=(8, 5))  # 设置图片大小
plt.title('人均国民收入与人均消费金额散点图', fontsize=15)  # 标题
plt.xlabel('人均国民收入 x (元)', fontsize=12)  # 设置x标签及字体大小
plt.ylabel('人均消费金额 y (元)', fontsize=12)
plt.scatter(x, y, color='blue', marker='o')  # 散点图：marker表示点的形状

plt.show()

