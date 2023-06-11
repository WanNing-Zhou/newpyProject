#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :统计分析.py
# @Time      :2023/6/10 21:16
# @Author    :周万宁
import numpy as np

arr = np.arange(20).reshape(4, 5)
print('arr', arr)
print('arr.sum', arr.sum(axis=0))
print('arr.sum', arr.sum(axis=1))
print('arr.mean', arr.mean())
print('arr.mean', arr.std())
print('arr.var', arr.var())
print('arr.argmin', arr.argmin())  # 输出最小元素的索引
print(arr.argmin(axis=0))  # 按行返回数组最小元素的索引

print(arr.cumsum())  # 计算素有元素的累计和, 输出;
print(arr.cumprod())  # 计算所有元素的累计积
print(np.prod(arr))  # 求所有元素的积
print(np.ptp(arr, axis=0))  # 按逐行求最大元素与最小元素的差

# numpy可以对数组中的元素,进行直接排序,
# sort函数是最常用的排序方法, arr.sort. 默认axis = 1
# sort函数也可以执行一个axis参数,使得sort函数可以验证执行轴对数据进行排序, axis-1 为沿横轴x轴排序, axis=0 沿y中排序

arr1 = np.array([[8, -2, 3, 1], [2, 5, 0, 7], [7, 4, 9, 6]])
arr1.sort()  # 默认axis = 1(x轴)
print('arr1', arr1)
arr1.sort(axis=0)  # 验证y轴进行排序
print('arr1', arr1, sep='\n')

# 在数组中插入一行或一列

a_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

n, m = {2, 3}

print(n, m)

n, m = np.shape(a_array)  # 获取数组的形状
b_array = np.ones(3)

c1 = np.insert(a_array, 0, values=b_array, axis=0)   # 在第0行前插入一行
c2 = np.insert(a_array, 1, values=b_array, axis=0)   # 在第1行前插入一行
c3 = np.insert(a_array, n, values=b_array, axis=0)   # 在最后一行后插入一行





