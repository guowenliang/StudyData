# 写在前面的话

- 邮箱
    - 教给大家用python发送邮件
    - 对邮箱进行设置，只要设置好了，通过邮箱地址和授权码就可以发送邮件

- 下周前端课程并行进行

# OOP- Python面向对象
- Python面向对象
- 面向对象编程
    - 基础
    - 公有私有
    - 继承
    - 组合、Mixin
- 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数
    
 # 1. 面向对象概述（Object Oriented）
 - OOP思想 
     - 接触到任意一个任务，首先想到的是任务这个世界的构成，是由模型构成的e
 - 几个名词
       - OO：面向对象
       - OOA：面向对象的分析
       - OOD：面向对象的设计
       - OOI：面向对象的实现
       - OOP：面向对象的编程
       - OOA->OOD->OOI：面向对象的实现过程 
 - 类和对象的概念
     - 类： 抽象名词，代表一个集合，共性的事物
     -  对象：具象的事物，单个个体
     - 类跟对象的关系   个体和集合
            - 一个具象，代表一类事物的某一个个体
            - 一个抽象，代表一大类事物
 - 类中的内容，应该具有两个内容
     - 表明事物的特征，叫做属性（变量）
      - 表明事物的功能或动作，称为成员方法（函数）
# 2. 类的基本实现
- 类的命名
    - 遵守变量命名的规范
    - 大驼峰（由一个或者多个单词构成，每个单词首字符大写，单词跟单词直接相连
    - 尽量避免跟系统命名相似的命名 
- 如何声明一个类
    - 必须用class关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值，允许使用None
    - 案例 01.py
- 实例化类
            
              变量= 类名()  #实例化了一个对象
- 访问对象成员
    - 使用点操作符
            
            obj.成员函数名称
            obj.成员方法
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有成员检查
            
            #dice前后各有两个下划线
            obj.__dict__

         
    
# 3. anaconda 基本使用
- anaconda主要是一个虚拟环境管理器
- 安装包管理器
- conda list：显示anaconda安装的包
- conda env list :显示anaconda的虚拟环境列表
- -conda creat -m xxx python=3.7:创建python版本为3.7的虚拟环境，命名为xxx


# 4. 类和对象的成员分析
- 类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
- 类存储成员时使用的是与类关联的一个对象
- 独享存储成员是存储在当前对象中
- 对象访问一个成员时，如果对象中没有该成员，尝试访问类中同名成员，如果对象中有次成员，一定使用对象中的成员
- 创建对象的时候，类中成员不会放人对象中，而是一个空对象，，没有成员
- 通过对象对类中成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，不会修改类成员


# 5. 关与self
- self在对象的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数中
- self并不是关键字，只是一个用于接收对象的普通参数，理论上可以用任何一个普通变量名代替
- 方法中有self形参的方法成为非绑定类的方法，可以通过对象访问，没有self的是绑定类的方法，只能通过类访问。
- 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过__class__成员名来访问

# 6. 面向对象的三大特性
- 封装
- 继承
- 多态
## 6.1 封装
- 封装就是对对象成员进行访问限制
- 封装的三个级别：
    - 公开：public
    - 受保护的：protected
    - 私有的： private
    - 以上三个P 不是关键字
 - 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
 - [https://study.163.com/course/courseLearn.htm?courseId=1004987028#/learn/live?lessonId=1051621582&courseId=1004987028]
 - 私有
    - 私有成员时最高级别的封装，只有在当前类或对象中访问
    - 在成员对象钱包添加两个下划线
    
            class Person():
                # name是公有的
                name="william"
                ##__age是私有的
                __age=19
    - Python的私有不是真私有，是一种称为name mangling的改名策略，
    可以使用对象名._classname_arrributename来访问 
- 受保护的封装 protected
    - 受保护的封装是将对象成员进行一定级别的封装，然后在类中或者子类中
    都可以进行访问，但是在外部不可以访问
    - 封装方法:在成员名称前添加一个下划线._name
- 公开的 公共的 public、
    - 公共的封装实际对成员没有任何操作。
    
## 3.2 继承
- 继承就是一个类可以获得另一个类中的成员属性和成员方法
- 作用： 减少代码，增加代码的服用功能，同时可以设置类与类直接的关系
- 继承与被继承的概念的概念：
    - 被继承的类叫做父类，也叫基类，也叫超类
    - 用于继承的类，叫做子类，也叫派生类
    - 继承与被继承存在一个 is A 关系
        
             #继承的语法
             #在python中，任何类都有一个共同父类叫object
             class Person():
                name = "NoName"
                __age = 0          #私有类
                _petname = "sec"   #受保护的
                def slepp(self):
                    print(“SLEEPING”)
                def work(self):
                    print("make some money")
                
             #父类写在括号内   
             class Teacher(Person):
             
                def MakeTest(self):
                    print("Test")
                def work(self)：
                    #扩充父类功能
                    #先调用父类
                    super().work()   / Person.work()
                    self.MakeTest()
                
- 继承的特性
    - 所有的类都继承自object类，即所有的类都是objcet类的子类
    - 子类一旦继承父类，则可以使用父类中出去私有成员的所有内容
    - 子类继承父类后并没有将父类成员完全继承到子类中，而是通过引用关系访问调用
    - 子类中可以定义独有的成员属性和方法
    - 子类中定义的成员和父类如果相同，优先调用子类成员
    - 子类中如果想扩充父类的方法， 可以再定义新方法的同时访问父类成员来进行代码重用，
    可以使用  父类名.父类成员 的格式来调用父类成员，也可以使用super().父类成员的格式来调用
- 继承变量函数的查找顺利问题
    - 优先查找自己的变量
    - 没有则查找父类
    - 构造函数如果本类中没有定义，则自动查找调用父类的构造函数
    - 如果本类有定义，则不再继续查找
- 构造函数
    - 是一类特殊的函数，类在实例化的时候第一次调用
    - 继承中的构造函数，如果子类中有定义构造函数，调用子类中的，如果没有，调用父类。
    
          
          # 继承中的构造函数  1.
          class Animal():
                pass
                
          class BuruAni():
                pass
          
          class Dog(BuruAni):
           #__init__ 就是构造函数
           # 每次实例化 第一次被调用
           #因为主要工作是进行初始化
            def __init__(self):
                print("It's a init !")
           
   
                
- super 
     - super不是一个关键字，而是一个类
     - super的作用是后去MRO（Method Resolution Order）列表中的第一个类
     - super与父类直接没任何实质性关系，通过super可以调用父类
     - super使用的两个方法，参见在构造函数中调用父类的构造函数
            
            
            class A():
                pass
            class B(A):
                pass
            class C(B,A):
                pass             
            print(A.__mro__) #查询类的关系列表
            print(B.__mro__)
            
- 单继承和多继承
    - 单继承：每个类只能继承一个类
    - 多继承：每个类允许继承多个类
- 单继承和多继承的优缺点
    - 单继承：
        - 传承有序 逻辑清晰 语法简单 隐患少  
        - 功能不能无限扩展，只能在当前唯一继承链中扩展
        
    - 多继承：
        - 优点：功能扩展方便
        - 缺点：继承关系混乱
        
            
            #多继承的例子
             class  Fish():
                def __init__(self,name):
                    self.name = name 
                def swim(self):
                    print("swimming")
             class Bird():
                def __init__(self,name):
                    self.name=name
                def fly(self):
                    print("flying")    
             class Man():
                def __init__(self,name):
                    self.name=name
                def work(self):
                    print("working") 
                     
             class SuperMan(Man,Bird,Fish):  #按照顺序
                def __init__(self,name):
                    self.name=name
                pass
             s=SuperMan("Clark")
             s.fly()
             s.swim()       
               
          
- 菱形继承和钻石继承的问题
    - 多个子类继承自同一个父类，这些子类又被同一个类继承，于是继承关系图形形成一个菱形图谱
    - [MRO](http://www.cnblogs.com/whatisfantasy/p/6046991.html)              
    - 关于多继承的MRO
        - MRO就是多继承中，用于保存继承顺序的一个列表
        - python本身采用C3算法来进行多继承的菱形继承进行计算的结果
        - MRO列表的计算原则：
            - 子类永远在父类前面
            - 如果多个父类，则根据继承语法中括号内类的书写顺序存放
            - 如果多个类继承了同一个父类，孙子类中只会选取继承语法括号中第一个父类的父类
- 构造函数
    - 在对象进行实例化的时候，系统自动调用的一个函数叫构造函数，通常次函数用来对实例对象进行初始化
    - 构造函数会按照MRO顺序往上查找
    
## 3.3 多态
- 多态就是同一个对象在不同情况下有不同状态出现
- 多态不是语法，是一种设计思想
- 多态性：一种调用方式，不同的执行结果
- 多态：同一事物的多种形态，动物分为人类、狗、猪

- Mixin设计模式
    - 主要采用多继承方式对类的功能进行扩展
    - [Mixin概念](https://www.jianshu.com/p/a578bd2c42aa)
- 我们使用多继承语法来实现Mixin
- 使用Mixin实现多继承的时候注意：
    - 首先他必须表示某一单一功能，而不是某个物品
    - 职责必须单一，如果有多个功能，则写多个Mixin
    - Mixin不能依赖子类实现
    - 子类即使没有继承这个Mixin类，也能照样工作，只是缺少了某个功能
- 优点：
    - 使用Mixin可以再不对类进行任何修改的情况下，扩充功能
    - 可以方便的组织和维护不同功能组件的划分
    - 可以根据需要任意调整功能类的组合
    - 可以避免创建很多新的类，导致类的继承混乱
    
# 4 类相关函数
- issubclass:检测一个类是不是另一个的子类

                class A（）：
                    pass
                class B(A):
                    pass          
                class C（）：
                    PASS
                print(issubclass(B,A))   
- isinstance:检测一个对象是否是一个类的对象实例
- hasattr:检测一个对象是否有成员属性  hasattr(对象名，属性名)               
 - getattr
 - setattr
 - selattr:
 - dir():获取成员列表
 
 # 5. 类的成员描述符(属性)
- 类的成员描述符是为了在类中对类的成员属性进行相关操作而创建的一种方式
    - get：获取属性的操作
    - set: 修改或者添加属性操作
    - delete：删除属性的操作
- 如果想使用类的成员描述符，有三种方法
    - 使用类实现描述器
    - 使用属性修饰符
    - 使用property函数
        - property函数很简单
        - property(fget,gset,fdel,doc)
    - 案例 
                
                #property案例
                #定义一个Person类，具有name,age属性
                #对于任意输入的姓名，我们希望用大写方式保存
                #年龄，内部统一用整数保存
                # x = property(fget,fset,fdel,doc)
                class Person():
                    #函数名称可以任意
                    def fget(self):
                        return self._name * 2
                    
                    def fset(self,name)
                        self._name = name.upper() #大写 
                    def fdel(self):
                        self._name = "NoName" 
                                    ##  四个参数顺序是固定的
                                    #第一个读取  第二个写入，第三个删除
                    name = property(fget,fset,fdel,"对name操作")
                    
                p1 = Person()
                p1.name = "TuLing"
                print(p1._name)    
- 无论哪种修饰符都是为了对成员属性进行相应的控制
    - 类的方式： 十二和多个类中的多个属性共用一个描述符
    - property：使用当前类中使用，可以控制一个类中多个属性
    - 属性修饰符：适用于当前类中使用，控制一个类中的一个属性
# 6. 类的内置属性

            __dict__:以字典的形式显示类的成员组成
            __doc__:类的文本信息
            __name__:获取类的名称
            __bases__:获取某个类的所有父类，以元组的形式显示
            
             print(Person.__dict__)
             print(Person.__doc__)  ##在类定义下边三引号
             print(Person.__name__)
             
# 7. 类的常用魔术方法
- 魔术方法就是不需要人为调用的方法，基本是在特定的时候自动触发
- 魔术方法的统一特征，方法名被前后各两个下换线包裹
- 操作类
    - `__init__`:构造函数
    - `__new__`:对象实例化方法，此函数较特殊，一般不需要使用
    - `__call__`: 对象当做函数使用的时候，调用call函数
    - `__str__`:对象被当做字符串的使用的时候
    `__repr__`:返回字符串
- 描述符相关
    - `__set__`
    - `__get__`
    - `__delete__`
- 属性相关操作
    - `__getattr__`:访问一个不存在的属性时触发
    - `__setattr__`:对成员属性进行设置的时候触发
        - 参数：
            - self用来获取当前对象，
            - 被设置的属性名称，以字符串的形式出现
            - 需要对属性名称设置的值
        - 作用：进行属性设置的时候进行验证或者修改
        - 注意：该方法中不能对属性直接进行赋值操作，否则会进入死循环
- 运算分类相关魔术方法（类似于C++函数重载）
    - `__gt__`:进行大于判断的时候触发的函数
        - 参数：
            - self
            - 第二个参数是第二个对象
            - 返回值可以是任意值，推荐返回布尔值
            
# 8 . 类和对象的三种方法
- 实例方法
    - 需要实例化对象才能使用的方法，使用过程中可能需要截止对象的其他对象的方法完成
- 静态方法
    - 不需要实例化，通过类直接访问
    
            @staticmethod
            # 不需要参数
            def say（）：
                pass
    
- 类方法
    - 不需要实例化
    
            @classmethod
            def play(cls): #一般是cls
                pass
                
- 三个方法的区别：： 百度


# 9

# 10. 抽象类
- 抽象方法：没有具体实现内容的方法成为抽象方法
- 抽象方法的主要意义是规范了子类的行为和接口
- 抽象类的使用需要借助abc模块
            
            import abc
- 抽象类：包含抽象方法的类叫做抽象类，通常称为ABC            
        
              import abc
              #声明一个类并且制定当前类的元类
              class Human(metaclass=abc.ABCMeta)
                #定义抽象方法
                @abc.abstractmethod
                def smoking(self):
                    pass
                #定义类抽象方法
              @abc.abstractclassmethod
              def drink():
                pass
              #定义静态抽象方法
              @abc.abstractstaticmethod
              def play():
                pass
- 抽象类的使用
    - 抽象类可以包含抽象方法，也可以包含具体方法
    - 抽象类中可以有方法也可以有属性
    - 抽象类不允许直接实例化
    - 必须继承才能使用，而且被继承的子类必须实现所有继承来的抽象方法
    - 假定子类没有实现所有继承的抽象方法，则子类也不能实例化
    - 抽象类主要作用是设定类的标准，以便于开发的时候具有统一的规范

# 11.自定义类
-  类其实是一个类定义和各种方法的自由组合
- 函数名可以当变量来用（组装）

            class A():
                pass
            
            def say(self):
                print("say****")
            
            say(9)    
            A.say=say   #变量等于函数
            a=A()   # 变量既是函数，又是变量
            a.say()
                       
- MethodType使用
            
            from types import MethodType
           
           # 定一个空类
            class A():
                pass
            #定义一个函数
            def say(self)：
                print("say....")
            
            a=A()  #实例化对象
            a.say = MethodType(say,A)  #将say 方法赋值给 类 A，say就成为A的一个方法
            a.say()    
                        
- 借助type实现  type(name,bases,dict) -> a new type
                
                #利用type造一个类
                  
                 # 定义成员函数
                 def say(self):
                    print("say..")
                 def talk(self):
                    print("Talking..")
                 #      base 元组      dict  字典
                 A = type("Aname",(object,){"class_say":say,"class_talk":talk})
- 利用元类实现- MetaClass
    - 元类是类
    - 用来创造类的类
    - 元类写法固定，必须继承自type
            
            #元类一般命名以MetaClass结尾
            class  AaaMetaClass(type)：
            #注意写法
                #def __new__(cls,name,bases,attrs):
                    #do something
                    print("元类")
                    attrs['id'] = '0000'
                    attrs['addr'] = "beijing110110road"
                    return type.__new__(cls,name,bases,attrs)
            #元类定义完就可以使用，注意写法
            
            class Teacher(object,metaclass = AaaMetaClass):
                pass
            
            t = Teacher()
            t.__dict__
            

                  
                             