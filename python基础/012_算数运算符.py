#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :012_算数运算符.py
# @Time      :2023/2/25 11:36
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

a = 3
b = 2
# 加法运算
print('a+b=', a + b)  # 5
# 减法运算
print('a-b=', a - b)  # 1
# 乘法运算
print('a*b=', a * b)  # 6
# 除法运算,结果可以为浮点类型
print('a/b=', a / b)  # 1.5
# 取整除, 结果只会保留整数部分
print('a//b=', a // b)  # 1
# 指数运算
print('a**b=', a ** b)  # 9
# 括号运算: 会改变运算优先级
print('(a+b)*b=', (a + b) * b)  # 10

