#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :005_selenium交互.py
# @Time      :2023/3/1 16:39
# @Author    :周万宁

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# 可以使程序休眠
import time

# 创建浏览器服务对象
s = Service(r'../chromeDriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)

# url
url = 'https://www.baidu.com'
driver.get(url)  # 打开网页

time.sleep(2)

# 获取文本框的对象
input = driver.find_element(By.ID, 'kw')

# 在文本框中输入周杰伦
input.send_keys('周杰伦')

time.sleep(2)

# 获取百度一下的按钮
button = driver.find_element(By.ID, 'su')

# 点击按钮
button.click()
time.sleep(2)

# 滑倒底部
js_bottom = 'document.documentElement.scrollTop=100000'
driver.execute_script(js_bottom)  # 执行js代码

time.sleep(2)

# 获取下一页的按钮
next = driver.find_element(By.XPATH, '//a[@class="n"]')
# 点击下一页
next.click()

time.sleep(2)

# 回到上一页
driver.back()

time.sleep(2)

# 回去
driver.forward()

time.sleep(3)

# 退出
driver.quit()

