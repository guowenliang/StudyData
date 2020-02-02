import urllib
import urllib.parse as parse

if __name__ == '__main__':
    url ='http://www.baidu.com/s?'         #'http://stock.eastmoney.com/news/1407,20170807763593890.html'

    wd = input("Input your keyword:")

    #要想使用data  需要使用字典结构
    qs = {
        "wd":wd
    }
    #转换url编码
    qs = parse.urlencode(qs)
    fullurl = url + qs

    print(fullurl)

    rsp = urllib.request.urlopen(url)

    html = rsp.read()

    #使用get保证不会出错
    html = html.decode()
    print(html)
