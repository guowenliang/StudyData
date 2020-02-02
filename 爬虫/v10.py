'''
使用代理访问百度网站

'''

from urllib import request,error

url = 'http://www.baidu.com/'

#1. 设置代理地址
proxy = {'http':'101.4.136.34:81'}
# 2. 创建ProxyHandler
proxy_handler = request.ProxyHandler(proxy)
#3. 创建Opener
opener = request.build_opener(proxy_handler)
#4. 安装Opener
request.install_opener(opener)

#现在访问url，就是使用代理服务器

try:
    rsp = request.urlopen(url)

    html = rsp.read().decode()
    print(html)

except error.URLError as e:
    print("error:{0}".format(e.reason))
    print("error:{0}".format(e))
except Exception as e:
    print(e)



