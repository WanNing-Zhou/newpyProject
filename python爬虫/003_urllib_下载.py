#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :003_urllib_下载.py
# @Time      :2023/2/26 23:22
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'

# url代表的是下载的路径 名字
# 在python中 可以写变量的名字, 也可以直接写值
# urllib.request.urlretrieve(url_page, 'baidu.html')


# 下载图片
# url_img = 'https://i1.wp.com/blackpinkupdate.com/wp-content/uploads/2019/02/BLACKPINK-Lisa-Instagram-Moonshot.jpg?ssl=1'
#
# urllib.request.urlretrieve(url=url_img, filename='lisa.jpg')
# 下载视频

url_video = 'blob:https://www.bilibili.com/faf6e086-8bd9-4b2c-b361-f94565508eb5'
urllib.request.urlretrieve(url_video, '一人之下.mp4')
