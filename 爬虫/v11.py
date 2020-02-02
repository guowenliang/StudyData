# -*- coding: utf-8 -*-”
from urllib import request,error



url = 'http://www.renren.com/973605210/newsfeed/photo'
#1.   直接构造header
headers = {}
headers['User-Agent']="User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"



try:
    req = request.Request(url=url,headers=headers)

    rsp = request.urlopen(req)
    html = rsp.read().decode('UTF-8')
    print(html)
    with open("rsp.html","w") as f:
        f.write(html)   #用notepad打卡
    print("done")

except Exception as e:
    print(e)