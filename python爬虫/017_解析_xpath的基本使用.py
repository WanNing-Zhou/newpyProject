#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :017_解析_xpath的基本使用.py
# @Time      :2023/2/28 11:00
# @Author    :周万宁

from lxml import etree

if __name__ == "__main__":
    run_code = 0

# xpath解析
# 1) 本地文件 etree.parse
# 2) 服务器响应的数据, response.read().decode('utf-8')  etree.HTML()

# xpath解析本地文件
tree = etree.parse('017_解析_xpath的基本使用.html')
print(tree)

# tree.xpath('xpath路径')
# 查找ul下面的li
# li_list = tree.xpath('//body//li')

# 查找所有有id属性的li标签
# text() 获取标签中的内容
# li_list = tree.xpath('//ul/li[@id]/text()')

# 找到id为beijing的标签 注意引号的问题
# li_list = tree.xpath('//ul/li[@id="beijing"]/text()')

# 查找到id为bejing的标签的class的属性值

# li = tree.xpath('//ul/li[@id="beijing"]/@class')
# print(li)

# 查询id包含l的标签
# li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')
# 查询id值以b开头的标签
li_list = tree.xpath('//ul/li[starts-with(@id,"b")]/text()')

# 查询id为beijing和calss为hello的标签
# li_list = tree.xpath('//ul/li[@id="beijing" and @class="hello"]/text()')

li_list = tree.xpath('//ul/li[@id="beijing"]/text() | //ul/li[@id="shanghai"]/text() ')

# 判断列表的长度
print(li_list)
print(len(li_list))




