#object类
#object类是所有类的父类，所有类都有object类的属性和方法。
#可以通过内置函数dir()可以查看指定对象的所有属性
#object有一个_str_()方法，用于返回一个对于'对象的描述'
class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'我叫{self.name},今年{self.age}岁'#复习下字符串的格式化
st1=A('李博文',21)
print(dir(st1))
print(st1)#默认调用__str__方法
print(type(st1))
