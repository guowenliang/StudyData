import re

'''
search使用案例
'''

#以下正则分为两个组，以小括号为单位
s = r'\d+'
pattern = re.compile(s)#s.I表示忽略大小写

m = pattern.search("one12tuw456three678")

print(m.group())


#参数表明搜查的起止范围

m = pattern.search("one123tuw456three678",10,40)


print(m.group())

