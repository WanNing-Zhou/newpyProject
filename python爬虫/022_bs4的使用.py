#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :022_bs4的使用.py
# @Time      :2023/3/1 7:49
# @Author    :周万宁

from bs4 import BeautifulSoup

# 通过解析本地文件,来讲bs4的基础语法进行讲解
# 默认打开的文件的编码是gbk 所以在打开文件的时候需要指定编码
soup = BeautifulSoup(open('022_bs4的使用.html', 'r', encoding='utf-8'), 'lxml')

# 根据标签名查找节点
# 找到的是第一个符合条件的语句
# print(soup.a)

# 获取biao'qian
# print(soup.a.attrs)

# bs4的一些函数
# 1) find
# 返回的是第一个符合条件的数据
# print(soup.find('a'))  # 返回的第一个a标签
# 根据title的值来找到对应的标签对象
# print(soup.find('a', title='a2'))
# 根据class的值找到对应的标签对象, 需要注意的是class需要添加下滑线
# print(soup.find('a', class_='a1'))
# 2) find_all
# 返回的是一个列表, 会返回所有符合条件的结果
# print(soup.find_all('a'))
# 如果想获取多个标签的书,那么在find_all的参数中添加的是列表的数据
# print(soup.find_all(['a', 'span']))

# limit的作用是查找前几个书
# print(soup.find_all('li', limit=2))

# 3) select(推荐)
# select方法返回的是一个列表,并且会返回多个数据
# print(soup.select('a'))

# 可以通过. 代表class 我们把这种操作叫做类选择器
# print(soup.select('.a2'))
# 可以通过 "井号" 代表id
# print(soup.select('#l1'))

# 属性选择器 --- 通过属性来寻找对应的标签
# 查找到li标签中有id的标签
# print(soup.select('li[id]'))

# 查找到li标签
# print(soup.select('li[id="l2"]'))


# 层级选择器

# 后代选择器
# 找到的div下面的li
# print(soup.select('div li'))

# 子代选择器
# 某标签的第一级子标签
# 注意很多的计算机编程语言中, 如果不加空格不会输出内容, 但是在bs4中 不会报错,也会显示内容
# print(soup.select('ul > li'))

# 找到a标签和li标签所有的对象
# print(soup.select('a,li'))

# 节点信息
# 获取节点内容
# obj = soup.select('#l1')[0]
# 如果标签对象中 只有内容, 那么string和get_text()都可以使用
# 如果标签中 除了内容还有标签, 那么string就获取不到数据,二get_text()是可以获取数据的
# 一般情况下推荐使用get_text()
# print(obj.string)
# print(obj.get_text())

# 节点的属性
# obj = soup.select('#l1')[0]
# name是标签的名字
# print(obj.name)
# 将属性值作为一个字典返回
# print(obj.attrs)


# 获取节点的属性
obj = soup.select('#l1')[0]
# print(obj.attrs.get('id'))
print(obj.get('id'))
print(obj.attrs['id'])



