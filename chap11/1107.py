#new和init演示创建person类的实例对象的过程
class Student(object):

    def __new__(cls, *args, **kwargs):#重写new方法，使得调用时输出关键值的id值
        print('new方法被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建对象的id是{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):#重写init方法，使得调用时输出关键的id值
        print("init方法被调用了，self的值为{0}".format(id(self)))
        self.name=name
        self.age=age
print('object这个对象的id值为{0}'.format(id(object)))
print('person这个对象的id值为{0}'.format(id(Student)))
print('---------------------这是一条华丽的分割线-------------------------')
p1=Student('Calvin',21)
print('p1这个实例对象的id为{0}'.format(id(p1)))
#以上过程表明了类的实例对象的创建过程

