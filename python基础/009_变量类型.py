#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :009_变量类型.py
# @Time      :2023/2/25 9:18
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

# 数据类型
# Number 数值 : int float
# boolean: 布尔
# string 字符串
# list 列表
#  tuple 元组
# dict 字典

money = 5000  # int类型
money1 = 2.33  # float类型

# boolean 布尔
# 流程控制语句

# 字符串: 使用的是单引号 或者 双引号
name = '勋悟空'
name1 = '猪八戒'

# list 列表
# tuple 元组
# dict 字典

# 应用场景: 当获取到了很多个数据的时候,那么我们可以将它们存储到列表中,然后直接使用列表访问
name_list = ['勋悟空', '猪八戒', '白骨精']
print('name', name_list[1])

# tuple 元组
age_tuple = (18, 20, 21)
print('age_tuple', age_tuple)

# dict 字典
# 应用场景: scrapy框架使用

# 格式: 变量的名字 = {key: value}
person = {
    'name': '勋悟空',
    'age': 20
}

print('person', person)
