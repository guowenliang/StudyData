'''
破解有道词典
v1
'''
from urllib import request,parse


def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data={
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15807962121504",
        "sign":"6a55185d565f1e88ac0e07f08e0e08d7", #加密的部分
        "ts": "1580796212150",
        "bv": "75a84f6fbcebd913f0a4e81b6ee54608",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
        #"typeResult":False
    }
    # 参数编码
    data = parse.urlencode((data)).encode()

    headers ={

            "Accept":" application/json, text/javascript, */*; q=0.01",
            #"Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "237",
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