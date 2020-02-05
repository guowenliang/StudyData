'''
破解有道词典
v2
'''
from urllib import request,parse
import time
import random
import hashlib


#通过查找，js中操作代码
#salt值为：
# r = "" + (new Date).getTime(),
# i = r + parseInt(10 * Math.random(), 10)

#sign值为

# e  查找的单词
# sign：n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")



def getSalt():
    '''
    salt公式变成python代码
    '''
    salt = int(time.time()*1000)+random.randint(0,10)
    return salt



def getMD5(v):
    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()

    return sign
def getSign(key,salt):

    sign = "fanyideskweb" +  key + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = getMD5(sign)

    return sign

def youdao(key):

    salt = getSalt()
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data={
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign":getSign(key,salt), #加密的部分
        "ts": "1580796212150",
        "bv": "75a84f6fbcebd913f0a4e81b6ee54608",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
        #"typeResult":False
    }
    print(data)
    # 参数编码
    data = parse.urlencode((data)).encode()

    headers ={

            "Accept":" application/json, text/javascript, */*; q=0.01",
            #"Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": len(data),
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie":" OUTFOX_SEARCH_USER_ID=1037764811@10.108.160.19; JSESSIONID=aaavkpaeeovrwbf48Yoax; OUTFOX_SEARCH_USER_ID_NCOO=1252451128.1879268; ___rl__test__cookies=1580796212147",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer":" http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url=url,data=data,headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    print(html)

if __name__ == '__main__':
    youdao("buy")
