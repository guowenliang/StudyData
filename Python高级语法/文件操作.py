#coding:utf-8
#打开文件，用写的方式
#r表示后边字符串不需要转义
# f称之为句柄
'''f = open(r"test01.txt","w")
#文件打开后必须关闭
f.close()
'''

####

#with 案例


with open(r"test01.txt","r",encoding='utf-8') as f:
    #按行读取
    strline = f.readline()
    #次结构保证能够完整读取 文件直到结束
    while strline:
        print(strline)
        strline = f.readline()
print("*"*40)
# list能用打开的文件作为参数，吧文件每一行内容作为一个元素
with open(r"test01.txt","r",encoding='utf-8') as f:
    #以打开的文件作为参数，创建列表
    l = list(f)
    for line in l:
        print(line)
print("*"*40)

with open(r"test01.txt","r",encoding='utf-8') as f:
    strChar = f.read()
    print(len(strChar))
    print(strChar)

#seek案例
#打开文件后，从第五字节开始读取

#打开后读写指针在0处
with open(r"test01.txt","r",encoding='utf-8') as ff:
    #seek移动单位是字节
    ff.seek(3,0)
    print("seek案例")
    strChar = ff.read()
    print(strChar)
import time
#打开后读写指针在0处
# with open(r"test01.txt","r",encoding='utf-8') as ff:
#     print("read延时案例")
#     #read参数的单位是字符，可认为一个汉字就是一个字符
#     strChar = ff.read(3)
#     while strChar:
#         print(strChar)
#         time.sleep(1)
#         strChar = ff.read(3)
#
# # tell函数：用来显示文件读写指针的当前位置
# with open(r"test01.txt","r",encoding='utf-8') as f:
#     print("tell函数案例")
#     strChar = f.read(3)
#     pos = f.tell()
#     while strChar:
#         print(pos)
#         print(strChar)
#         strChar = f.read(3)
#         pos = f.tell()
#     # tell返回单位是字节
#     #read是字符

with open(r"test01.txt","a",encoding='utf-8') as f:
    print("write操作")
    f.write("\n生活真操蛋1")

# 也可以直接写入行，同writeline
#
with open(r"test01.txt","a",encoding='utf-8') as f:
    print("writeline操作")
    l = ["I","AM","SDASD"]
    f.writelines("生活真操蛋lines")
    f.writelines("生活真操蛋lines11")
    f.writelines(l)

#序列化案例
import pickle
age = 19
a = ["19","185",["asdas"],"woshishui"]
with open(r"test02.txt","wb") as ff:
    pickle.dump(age,ff)
    pickle.dump(a, ff)
with open(r"test02.txt","rb") as ff:
    age = pickle.load(ff)
    a = pickle.load(ff)
    print(age)
    print(a)

import shelve
#shv相当于一个字典
shv = shelve.open(r'shv.db')
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()
#以上案例发现，shelve自动创建文件
#读取案例
shv = shelve.open(r'shv.db')
try:
    print(shv['one'])
    print(shv['three'])
finally:
    shv.close()
###  testttt