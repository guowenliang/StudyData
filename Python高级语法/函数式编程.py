stm = lambda x: 100 * x
print(stm(89))
stm2 = lambda x, y, z: x + y * 10 + z * 100
print(stm2(4, 5, 6))

#高阶函数

#函数名称就是个变量

def funA():
    print("In funA")

funB=funA
funB()



#高阶函数举例
#funA是普通函数，返回100倍输入
def FunA(n):
    return n * 100
#再写一个函数，把传入参数乘以300倍，利用高阶函数
def FunB(n):
    return FunA(n)*3

print(FunB(9))

#再一个高阶函数

def FunC(n,f):
    #n*300
    return f(n)*3

print(FunC(9,FunA))


#map 举例

#有一个列表，相对列表的每个元素都乘以10，并获取新的列表

l1 = [i for i in range(10)]
l2 = []
for i in l1:
    l2.append(i * 10)
print(l2)

#利用map
l3=map(lambda x:x*10,l1)
print(l3)
#map类型是一个可迭代的结构，可以使用for便利
for i in l3:
    print(i,end=",")

#列表生成式
l4 = [i for i in l3]
print(l4)


import functools
def myAdd(x , y):
    return x + y
print(functools.reduce(myAdd,[1,2,3,4,5,6]))
