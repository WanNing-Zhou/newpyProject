#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :NumPy_Experiment.py
# @Time      :2023/5/16 13:50
# @Author    :周万宁

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    run_code = 0

# 生成服从均值为 0 方差为1 的正态分布数据
data = np.random.normal(0, 1, 10000)

# 绘制数据直方图

plt.hist(data, bins=50)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Normal Distribution with $\mu=0$, $\sigma=1$')
plt.show()



# 生成两个3行3列的矩阵
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

# 矩阵加法
print("Matrix addition:")
matrix_addition = matrix1 + matrix2
print(matrix_addition)

# 矩阵减法
print("Matrix subtraction:")
matrix_subtraction = matrix1 - matrix2
print(matrix_subtraction)

# 矩阵乘法
print("Matrix multiplication:")
matrix_multiplication = np.dot(matrix1, matrix2)
print(matrix_multiplication)










