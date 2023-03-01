#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :002_selenium的基本使用.py
# @Time      :2023/3/1 9:26
# @Author    :周万宁

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# driver的地址
s = Service("../chromeDriver/chromedriver.exe")
# 使用chromedriver驱动
driver = webdriver.Chrome(service=s)

# 使用驱动打开网页
driver.get('https://www.baidu.com/')

# 元素定位

# 根据id来找到对象
# button = driver.find_element(By.ID, 'su')
# print(button)

# 根究name来获取对象
# button = driver.find_element(By.NAME, 'wd')
# print(button.get_attribute('class'))

# 退出驱动
# driver.quit()
# 获取网站源码
# content = driver.page_source

# print(content)

# 根据xpath语句来获取队形
# button = driver.find_element_by_xpath('//input[@id="su"]')
# button = driver.find_element(By.XPATH, '//input[@id="su"]')
# print(button)

# 根据标签的名字来获取对象列表
# buttons = driver.find_elements(By.NAME, 'wd')
# print(buttons)

# 使用css选择器获取对象
# button = driver.find_element(By.CSS_SELECTOR, '#su')
# print(button)

# 根据链文本获取对象
button = driver.find_elements(By.LINK_TEXT, '新闻')
print(button)

