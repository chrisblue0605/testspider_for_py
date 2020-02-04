#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time   : 2020/2/4 16:50
#  @Author  : Chris
# 引入第三方库requests
import requests

# 注入headers,绕过豆瓣爬虫检测
headers = {
    'Cookie': 'll="108288"; bid=_fqbG_YqzUI; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.648520984.1580482021.1580482021.1580482021.1; __utmb=30149280.0.10.1580482021; __utmc=30149280; __utmz=30149280.1580482021.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1804897645.1580482021.1580482021.1580482021.1; __utmb=223695111.0.10.1580482021; __utmc=223695111; __utmz=223695111.1580482021.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=Umw8doDenYOfT2arPgi61MTNkONfp6mr; _vwo_uuid_v2=D82E7ABEE9BDB32B5A35E0E4915F422BB|7a3ceb17f70b79cc54955671233ac044; __gads=ID=4f8d6c739570a25c:T=1580482069:S=ALNI_Ma4tbv9wgaiuwGrH0wOhsv38PS3EA; _pk_id.100001.4cf6=fdc31e57578732c7.1580482021.1.1580483039.1580482021.',
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

# 发送第一个网页请求，通过get请求，直接请求网页https://movie.douban.com/top250
r = requests.get(url="https://movie.douban.com/top250", headers=headers)

# 打印网页主体
print(r.text)
