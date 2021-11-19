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
st1.eat()#对象名.方法名
print(st1.name)
print(st1.age)
print('----------这是一条分割线----------')
Student.eat(st1)#类名.方法名(类的对象)
#27行与23行的作用是一样的，都是调用Student类之中的参数

