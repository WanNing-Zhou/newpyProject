#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :chromHeadless的封装.py
# @Time      :2023/3/1 18:57
# @Author    :周万宁


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


base_url = "http://www.baidu.com/"
driver = share_browser()
driver.get(base_url + "/")
driver.find_element_by_id("kw").send_keys("Python程序设计")
driver.find_element_by_id("su").click()
driver.save_screenshot('screen.png')
driver.close()