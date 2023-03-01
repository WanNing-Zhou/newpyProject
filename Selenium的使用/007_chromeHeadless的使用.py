#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :007_chromeHeadless的使用.py
# @Time      :2023/3/1 18:35
# @Author    :周万宁


# # 封装的headless
# from selenium import webdriver
# # 这个是浏览器自带的 不需要我们再做额外的操作
# from selenium.webdriver.chrome.options import Options
#
#
# def share_browser():
#     # 初始化
#     chrome_options = Options()
#     chrome_options.add_argument('‐‐headless')
#     chrome_options.add_argument('‐‐disable‐gpu')
#     # 浏览器的安装路径 打开文件位置
#     # 这个路径是你谷歌浏览器的路径
#     path = r'"C:\Users\周万宁\AppData\Local\Google\Chrome\Application\chrome.exe"'
#     chrome_options.binary_location = path
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver
#
#
# browser = share_browser()
#
# url = 'https://www.baidu.com'
#
# browser.get(url)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
base_url = "http://www.baidu.com/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(base_url + "/")
driver.find_element_by_id("kw").send_keys("Python程序设计")
driver.find_element_by_id("su").click()
driver.save_screenshot('screen.png')
driver.close()
