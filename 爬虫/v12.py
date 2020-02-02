# -*- coding: utf-8 -*-”
from urllib import request,error



url = 'http://www.renren.com/973605210/newsfeed/photo'
#1.   直接构造header
headers = {}
headers['User-Agent']="User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
headers['Cookie']="anonymid=k64xrw3h-y0w5vi; depovince=GW; jebecookies=41953237-5080-4bfd-8a2f-de48d41dc3f0|||||; _r01_=1; JSESSIONID=abc41utRkCMOXf-e4Ofax; ick_login=31304ed1-467b-4762-a1f0-b60b95fd7695; taihe_bi_sdk_uid=1edf43b99d21060296dfa8eb693c5c54; taihe_bi_sdk_session=3a280775e41a947bf5ba17454fb3564a; t=79d5704199e2724bfa556ce54ee435960; societyguester=79d5704199e2724bfa556ce54ee435960; id=973605210; xnsid=fa5c41ed; ver=7.0; loginfrom=null; springskin=set; jebe_key=9de64af4-e928-4efa-b74b-a8bef66ed974%7Cdf48a178a4eef8c64ccc26e440f21665%7C1580642584415%7C1%7C1580642583856; jebe_key=9de64af4-e928-4efa-b74b-a8bef66ed974%7Cdf48a178a4eef8c64ccc26e440f21665%7C1580642584415%7C1%7C1580642583858; vip=1; wp_fold=0; __utma=151146938.1361428733.1580644083.1580644083.1580644083.1; __utmb=151146938.1.10.1580644083; __utmc=151146938; __utmz=151146938.1580644083.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1"



try:
    req = request.Request(url=url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode('UTF-8')
    print(html)
    with open("rsp_cookie.html","w",errors='ignore') as f:
        f.write(html)   #用notepad
    print("done")

except Exception as e:
    print(e)