'''
任务要求和v5相同，因为v5
利用requestshixan
分析百度翻译
1. 打开F12
2.输入单词，发现每敲一个字母都有请求
3. 请求地址是http://fanyi.baidu.com/sug
4. 利用NetWorkAllHeader，查看发现FormData是kw：girl
5.检查返回内容格式，发现是json格式

'''


import urllib.request as request
import urllib.parse as parse
import json

'''
大致流程是：
1.利用data构造内容，然后urlopen打开
2.返回一个json格式的结果、
3.结果就是girl的释义
'''
baseurl = 'https://fanyi.baidu.com/sug'

#存放模拟form的数据一定是dict格式
data = {
    #girl 是翻译输入的英文内容，应该用户输入，此处使用硬编码。
    'kw':'girls',

}

#shiyong parse对data进行编码

data = parse.urlencode(data).encode("utf-8")
print(type(data))

# 构造一个请求头，请求头应该至少包含输入数据的长度
# request要求传入的请求头是一个dict格式

headers = {
    #因为使用post，至少包含content-length字段
    'Content-Length':len(data),
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
}

# 狗仔一个request的实力

req = request.Request(url=baseurl,data=data,headers=headers)

#已经构造了Request ，所有的请求就封装在request里

rsp = request.urlopen(req)

json_data = rsp.read().decode("utf-8")

print(type(json_data))
print(json_data)

#把json转换成字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'],"--",item['v'])


