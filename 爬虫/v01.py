'''
使用urllib.request请求一个网页内容，并且把内容打开
'''
from urllib import request

UserAgent='Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko'



if __name__ == '__main__':

    url = 'https://jobs.zhaopin.com/CC638054836J00166622709.htm'
    # 打开相应的url并把相应页面作为返回
    rsp = request.urlopen(url)
    # 把返回的结果读取出来
    html = rsp.read()
    html = html.decode()

    print(html)


