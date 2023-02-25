#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :015_ 流程控制语句.py
# @Time      :2023/2/25 15:03
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

age = input('请输入你的年龄:\n')
age = int(age)
if age >= 18:
    print('您的年龄是%d,您已经成年,可以进入网吧' % age)
elif age >= 17:
    print('马上就快成年了,再等一等吧')
elif age >= 13:
    print('小朋友, 你的作业写完了吗')
else:
    print('未成年人不允许进入网吧')

