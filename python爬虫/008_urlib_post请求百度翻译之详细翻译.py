#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :008_urlib_post请求百度翻译之详细翻译.py
# @Time      :2023/2/27 10:19
# @Author    :周万宁


if __name__ == "__main__":
    run_code = 0

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
    # 用户代理 浏览器等用户信息
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'en-US,en;q=0.9',
    # 'Acs-Token': '1677402009280_1677477646822_ytrXK5TP73qFD/LLXLE0Eevx+oyOH5IvDdnQiZ4EWFthHn4owL7cL6WvT1kKln9tGxJFy6JlPjRV+maqErGg3d4SivgvGd1OXJr837a7dfvQGmc7i8UqseXq4BHnIn0cbMkwfihWEQQIirNi4zj06rPFF6H1cFpsQvlVUced//pxFcxOgE9tW5I4J/Odk0vztKEe8bunyxN1emFLGuGrV0MxEyH5nAcFQOYzzTWs+PBlVp24JyE662b9PWGvZw2QVRWHhbUHNfgou1AbHu/x3ay1LwvGFa5m92p0GYCown0K+gaZWwxDowHUdxcMaD1R',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '135',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=5261275156B2892DDB6194B4F8ECD843:FG=1; BAIDUID_BFESS=5261275156B2892DDB6194B4F8ECD843:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1677464260,1677477634; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1677477634; ab_sr=1.0.1_YTllMzI1MGM2ZDk1ZGQzNDYzNDlhZmUwMzE1NDY4ZDY2NjE0NTJkNzgwNWZmZjkxZDc2ZTAxZWE5YTdjOWM2N2RmN2QyZjQyMGNkODEwN2FlNzg1Y2Q2Yzk3MzAxN2MyNjE4N2IwMzllZDhhYjlhZDhmMzExMWZmN2E5MThkZDcyYmMyY2FmNmFkZDA3NmZjMzQ2ZWZjMGZmMjQ0ZDZmNw==',
    # 'Host': 'fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    # 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
}

# 请求数据的字典
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': 'd7f3b249426240ff5d266441c0929273',
    'domain': 'common',
}

# post请求的参数,必须调用encode
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象的定制
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

obj = json.loads(content)
# 输出
print(obj)
