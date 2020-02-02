'''
urlError使用

'''
from urllib import request,error

url = 'http://www.googol.com.cn/'

try:
    req = request.Request(url)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)

except error.URLError as e:
    print("error:{0}".format(e.reason))
    print("error:{0}".format(e))
except Exception as e:
    print(e)