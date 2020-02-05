import re

'''
正则结果match的使用案例
'''

#以下正则分为两个组，以小括号为单位
s = r'([a-z]+) ([a-z]+)'
pattern = re.compile(s,re.I)#s.I表示忽略大小写

m = pattern.match("Hello world wide web!")

#group(0)表示返回匹配成功的整个字符
s = m.group(0)
print(s)

a = m.span(0)#返回匹配成功的整个子串的跨度
print(a)

#group（1）表示返回的第一个分组匹配成功的子串
s = m.group(1)
print(s)


a = m.span(1)#返回匹配成功的第一个子串的跨度
print(a)

s = m.group()#等价于m.group(1)， （2）


