#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :002_selenium的基本使用.py
# @Time      :2023/3/1 9:26
# @Author    :周万宁

# # 导入selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
#
# # 2) 创建浏览器操作对象
# path = Service(r'E:\PROJECT\newpyProject\chromeDriver\chromedriver.exe')
#
# browser = webdriver.Chrome(service=path)
#
# # 3) 访问网站
# url = 'https://www.baidu.com'
#
# browser.get(url)
#
# browser.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 尝试传参
s = Service("../chromeDriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# driver.get('https://www.baidu.com/')
# 使用浏览器驱动可以获取京东的秒杀页面
driver.get('https://www.jd.com/')
# driver.quit()

