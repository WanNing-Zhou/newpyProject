#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :初识numpy.py
# @Time      :2023/6/10 18:37
# @Author    :周万宁

import numpy as np  # 导入Numpy库

arr1 = np.array([1, 2, 3, 4])  # 创建一个一位数组,参数为列表
print("数组尺寸", np.shape(arr1))  # (4,)一个元素的元组,表示的是一位数组

arr2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])  # 创建二维数组
print('数组的尺寸：', np.shape(arr2))  # 2个元素的元组:  (3, 4)
print(arr2.shape[0])  # 返回二位数组的行数: 3
print(arr2.shape[1])  # 返回二维数组的列数

# numpy 提供了狠毒专门创建数组的函数

print(np.arange(0, 1, 0.2))  # 创建开始值为1, 不含终止值b 步长为0.2 的一维数组
print(np.linspace(0, 10, 5))  # 创建含开始值0 含终值10, 5各元素的等差数列

print(np.logspace(0, 2, 5)) # 生成10的a次方到10的b次方的n各元素的等比数列

print(np.zeros(3)) # 创建元素全为0的一位数组
print(np.zeros((2,3)))  # 创建元素为0的二位数组

print(np.ones(3)) # 创建元素全为1的一维数组+

print(np.eye(2)) # 创建n阶单位二维数组(对角线上元素为1)

print(np.diag([2,5,-1])) # 创建对角二维数组

print(np.full([2,3],5)) # 生成x行y列元素全为z的二维数组
