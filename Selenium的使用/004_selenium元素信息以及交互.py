#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :004_selenium元素信息以及交互.py
# @Time      :2023/3/1 16:15
# @Author    :周万宁

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('../chromeDriver/chromedriver.exe')
driver = webdriver.Chrome(service=service)

url = 'http://www.baidu.com'

driver.get(url)
# 根据id获取对象
input = driver.find_element(By.ID, 'su')
print(input.get_attribute('class'))
# 获取标签名
print(input.tag_name)
# 获取元素文本
print(input.text)



