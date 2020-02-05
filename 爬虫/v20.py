'''
爬取豆瓣电影数据
了解ajax的基本爬取方式
https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20

'''
from urllib import request,parse
import json

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"

headers = {}
headers['User-Agent'] = "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
# 创建一个请求对象
req = request.Request(url, headers=headers)

rsp = request.urlopen(req)
data = rsp.read().decode()

data = json.loads(data)

print(data)
