#特殊属性和特殊方法
#特殊属性
print(dir(object))
#对象名.__dict__获得类对象或实例对象所绑定所有属性和方法的字典
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
#创建一个C类的对象
x=C('calvin',21)
print(x.__dict__)#实例对象的属性字典
print(C.__dict__)#类对象的属性以及方法字典
print(x.__class__)#输出对象所属的类
print(C.__bases__)#输出C类的父类类型的元素
print(C.__base__)#输出最近的一个父类类型
print(C.__mro__)#输出类的层次结构
print(A.__subclasses__())#输出子类的列表


