#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :020_字典高级.py
# @Time      :2023/2/26 7:59
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

# 查看元素

# info = {'name': '勋悟空', 'age': 3200}
# print(info['name'])  # 勋悟空
# # print(info['sex'])  # 如果key不存在,就会发生异常
#
# print(info.get('sex'))   # None # 获取不存在的key, 获取到空的内容, 不会出现异常
# print(info.get('sex', '男'))   # 男 # 获取不存在的key, 可以提供一个默认值

# 删除
# info = {'name': '勋悟空', 'age': 3200}
# del info['age']
# print('删除age后的字典为 %s:' % info)

# del info
# print('删除info字典%s' % info)  # 报错: NameError: name 'info' is not defined

# info.clear()
# print('清空info字典后为%s' % info)  # 清空info字典后为{}

# 遍历
# info = {'name': '勋悟空', 'age': 3200}
# for key in info.keys():
#     print(key)
#
# # 输出结果
# # name
# # age

# info = {'name': '勋悟空', 'age': 3200}
# for value in info.values():
#     print(value)

# 输出结果
# 勋悟空
# 3200
# info = {'name': '勋悟空', 'age': 3200}
# for key, value in info.items():
#     print(key, value)
# 输出结果
# name 勋悟空
# age 3200

info = {'name': '勋悟空', 'age': 3200}
for item in info.items():
    print(item)
# 输出结果
# ('name', '勋悟空')
# ('age', 3200)


