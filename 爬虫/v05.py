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
    'kw':'girl'

}

#shiyong parse对data进行编码

data = parse.urlencode(data).encode("utf-8")
print(type(data))

# 构造一个请求头，请求头应该至少包含输入数据的长度
# request要求传入的请求头是一个dict格式

header = {
    #因为使用post，至少包含content-length字段
    'Content-Length':len(data)

}

#有了headers，data，url，就可以尝试发出请求了
rsp = request.urlopen(baseurl,data=data)

json_data = rsp.read().decode("utf-8")

print(type(json_data))
print(json_data)

#把json转换成字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'],"--",item['v'])


