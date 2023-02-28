#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :jsonpath解析淘票票.py
# @Time      :2023/2/28 20:06
# @Author    :周万宁

import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1677586044886_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1677586044886_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bx-v': '2.2.3',
    'cookie': 'miid=6182500421269191764; thw=hk; cna=81nFGkvnLWoCAW8oEclwiD0t; t=81dbd5eb5f580d63a5eac8b5bbddf48a; sgcookie=E100lmNrzZoO5eIFe6cQSo4gcVRHVCsHSsNTIlaX10i3QoieL9dJ4QO8FoMxzeP2wzxV2nZ2G0zHVHlDsUbznV1kxKJp7WBe3UxhCATO4igsGgY%3D; tracknick=tb091921008; _cc_=U%2BGCWk%2F7og%3D%3D; enc=OFfIlE7iWuNygoFTVUtMiRolWiFn60n1jJW%2BaCSFJbPRSZlv%2BFEmXak8B%2BgauDYTNFM6kQGQ5eTyp5Vms1%2F9mS4HpeGhvYJ9hj9SDV9JX98%3D; _m_h5_tk=22cfc9b380a33d04c2315a1d6a4a6fd9_1677002622642; _m_h5_tk_enc=e5e74e351dc6743d58422c7c483a6fe2; cookie2=1851cb06f19e31f021938d18fc0018b5; v=0; _tb_token_=5b878e3e36175; xlly_s=1; l=fBIqNfamLk0eyBdNBO5aourza77tnCOb81PzaNbMiIEGa6QP9Er02NCeRxYXWdtjgTfYDeKPDzebMdneJZzK0giMW_N-1NKcfD96-bpU-L5..; tfstk=cQylBSb627lWTJWLlzM5I1MvAe5AZ1drWJPa3i6vh2h3RbyViZA2_4tlmDQ1zB1..; isg=BBwcqY5ek9IcVWZcdHQLrIWh7TrOlcC_n-3qrPYYLof3Qb3LH6VBT8Y3oam5TvgX',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)

resource = urllib.request.urlopen(request)

content = resource.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

# print(content)

with open('021_jsonpath解析淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(open('021_jsonpath解析淘票票.json', 'r', encoding='utf-8'))

city_list = jsonpath.jsonpath(obj, '$..regionName')

print(city_list)
