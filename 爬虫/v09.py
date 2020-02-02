'''
访问网站
更改useragent
'''


from urllib import request,error


url = 'https://www.baidu.com/'


#1.   直接构造header
#headers = {}
#因为使用post，至少包含content-length字段
#headers['User-Agent']="User-Agent:Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"





#已经构造了Request ，所有的请求就封装在request里

try:

    #req = request.Request(url=url,headers=headers)
    req = request.Request(url=url)
    # 2. 使用add_header方法
    req.add_header("User-Agent","User-Agent:Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5")
    rsp = request.urlopen(req)



    html = rsp.read().decode()
    print(html)

except error.URLError as e:
    print("error:{0}".format(e.reason))
    print("error:{0}".format(e))
except Exception as e:
    print(e)


