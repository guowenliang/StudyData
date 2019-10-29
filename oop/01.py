
'''
定义一个学生类，用来形容学生

'''
# 定义一个空的类
class Student():
    #一个空类，pass代表直接跳过
    pass
# 定义一个对象
mingyue  = Student()


#再定义一个类，描述听python的学生
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"
    #注意缩进层级
    #默认的self参数
    def doHomework(self):
        print("I am doing homework.")
        #推荐函数末尾使用return
        return None

#实例化一个学生
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()


