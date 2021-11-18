#类与对象
#不同的数据类型属于不同的类
#比如100，99，520都是int类之下包含的相似的不同的个例，这些个例专业术语称为实例或对象。

#类的创建
class Student1:#Student为类的名称，由一个或多个单词组成，每个单词的首字母大写，其余小写
    pass
#python中一切皆对象，对象都有id（内存空间)type（类型）值（value）
print(id(Student1))
print(type(Student1))
print(Student1)
print('----------------------这是一条分割线-------------------------')
#类的组成
class Student:
    # 类属性
    native_place='湖北'#直接写在类里面的变量，称为类属性
    #初始化方法
    def __init__(self,name,age):
        self.name=name#self.name称为实体属性，进行了一个赋值的操作，将局部变量name的值赋给实体属性
        self.age=age
    # 实例方法
    def eat(self):
        print('干饭人干饭魂')#类之内定义的叫方法，类之外定义的叫函数
    #静态方法
    @staticmethod
    def method():
        print('这是一个静态方法')
    #类方法
    @classmethod
    def cm(cls):
        print('这是一个类方法')
#实际上我所声明的类也是一个类对象
#对象的创建（又称类的实例化）
print('---------------创建Student类的对象------------------')
st1=Student('李博文',21)#st1就是根据类对象创建出来的实例对象
print(id(st1))
print(type(st1))
print(st1)
print(id(Student))
print(type(Student))
print(Student)
