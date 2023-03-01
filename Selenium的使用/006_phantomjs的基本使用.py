#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :006_phantomjs的基本使用.py
# @Time      :2023/3/1 17:16
# @Author    :周万宁

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = 'phantom.exe'

browser = webdriver.PhantomJS(path)

url = 'https://www.baidu.com'
browser.get(url)

browser.save_screenshot('baidu.png')
time.sleep(2)

input = browser.find_element_bt_id('kw')
input.send_keys('昆凌')

time.sleep(3)

browser.save_screenshot('kunling.png')




