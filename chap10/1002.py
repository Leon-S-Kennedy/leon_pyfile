#类属性，类方法，静态方法
#类属性；类之中方法外的变量称为类属性，被该类的所有对象共享
#类方法；使用@classmethod修饰的方法，使用类名直接访问的方法
#静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法
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
#类属性的使用方式
print(Student.native_place)#类名.类属性
st1=Student('李博文',21)
st2=Student('calvin',21)
print(st1.native_place)
print(st2.native_place)
Student.native_place='荆州'
print(st1.native_place)
print(st2.native_place)
Student.cm()
Student.method()


