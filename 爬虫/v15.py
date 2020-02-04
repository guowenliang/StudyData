from urllib import request,parse
from http import cookiejar

#创建filecookiejar实例
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)
#生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handler = request.HTTPHandler()
#生成https管理器
https_handler = request.HTTPSHandler()

#创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    '''
    负责初次登录
    '''

    # 次url需要从form的action属性中提取
    url = "http://www.renren.com/PLogin.do"
    #此键值需要从登录form的两个对应input中提取name属性
    data = {
        "email":"736498007@qq.com",
        "password":"******"
    }
    headers = {}
    headers['User-Agent'] = "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"

    #把数据进行编码
    data = parse.urlencode(data)
    #创建一个请求对象
    req = request.Request(url,data=data.encode(),headers=headers)
    #使用opener发起请求
    rsp = opener.open(req)
    #保存cookie到文件
    # ignore_discard表示即使cookie丢弃也保存
    # ignore_expires 表示即使过期也保存
    cookie.save(ignore_discard=True,ignore_expires=True)


def getHomePage():
    url="http://www.renren.com/413961016/newsfeed/photo"
    # 如果已经执行了login函数，则opener自动包含cookie


    try:
        rsp = opener.open(url)
        html = rsp.read().decode('UTF-8')
        print(html)
        with open("rsp_cookie_autologin15.html", "w", errors='ignore') as f:
            f.write(html)  # 用notepad
        print("done")

    except Exception as e:
        print(e)
if __name__ =='__main__':
    login()
    getHomePage()


