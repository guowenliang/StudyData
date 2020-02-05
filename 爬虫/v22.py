'''
使用参数headers和params
研究返回结果
'''

import requests

url = "http://www.baidu.com/s?"
#两种请求方式

kw = {
    "wd":"王八蛋"
}


headers = {

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                 " AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/79.0.3945.117 Safari/537.36",
}


#使用get请求
rsp = requests.get(url,params=kw,headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)#返回码





