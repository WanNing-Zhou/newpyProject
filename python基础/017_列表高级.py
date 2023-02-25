#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :017_列表高级.py
# @Time      :2023/2/25 21:51
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

names = ['勋悟空', '猪八戒', '沙和尚']

# 添加数据

print("添加前的数据", names)  # 添加前的数据 ['勋悟空', '猪八戒', '沙和尚']
# 添加数据
# names.append('唐僧')
# print('添加后的数据', names)  # 添加后的数据 ['勋悟空', '猪八戒', '沙和尚', '唐僧']
#
#
# names.insert(1, 'IKun')
# print('添加后的数据', names)  # 添加后的数据 ['勋悟空', 'IKun', '猪八戒', '沙和尚', '唐僧']

# names1 = ['IKun', '唐僧']
# names.extend(names1)
# print('合并后的数据', names)  # 合并后的数据 ['勋悟空', '猪八戒', '沙和尚', 'IKun', '唐僧']

# 修改元素


# names[1] = 'KunKun'
#
# print('修改后的数据', names)  # 修改后的数据 ['勋悟空', 'KunKun', '沙和尚']

# 查找元素

# findName = input('请输入你要查找的姓名:\n')
# print('查找的名字是否存在', findName in names)  # 返回值为True 或 False

# 指定元素的索引位置
# print('勋悟空的位置', names.index('勋悟空'))

# 指定元素在List中的个数

# print('names中勋悟空有几个', names.count('勋悟空'))  # names中勋悟空有几个 1

# 删除元素

# names.pop()
# print('删除后的列表', names)  # 删除后的列表 ['勋悟空', '猪八戒']
#
# names.pop(1)
# print('删除后的列表', names)  # 删除后的列表 ['勋悟空', '沙和尚']

names.remove('勋悟空')
print('删除后的列表', names)  # 删除后的列表 ['猪八戒', '沙和尚']

