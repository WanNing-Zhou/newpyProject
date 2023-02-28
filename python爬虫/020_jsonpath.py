#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :020.py
# @Time      :2023/2/28 19:24
# @Author    :周万宁

import jsonpath
import json

if __name__ == "__main__":
    run_code = 0

obj = json.load(open('020_jsonpath.json', 'r', encoding='utf-8'))

# 书店所有书的作者
# author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(author_list)

# 所有的作者
# 7

# store下面的所有的元素
# tag_list = jsonpath.jsonpath(obj, '$.store,*')
# print(tag_list)

# store里面所有的签
# price_list = jsonpath.jsonpath(obj,'$.store..price')
# print(price_list)

# 第三个书
# book = jsonpath.jsonpath(obj, '$..book[2]')
# print(book)

# 最后一本书
# book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# print(book)

# 前面的两本书
# book_list = jsonpath.jsonpath(obj,'$..book[:2]')
# book_list = jsonpath.jsonpath(obj, '$..book[0,1]')
# print(book_list)

# 条件过滤需要在()的前面添加一个?
# 过滤出所有带isbn的书
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
# print(book_list)

# 哪本书超过了10元钱
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
# print(book_list)



