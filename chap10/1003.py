#动态绑定属性和方法
#python是一门动态的语言，在创建对象后，可以动态的绑定属性和方法
class Student:
    def __init__(self,a,b):
        self.aaa=a
        self.bbb=b
    def eat(self):
        print(self.aaa+'干饭小王子')
st1=Student('李博文',16)
st2=Student('calvin',21)
st2.eat()
print(id(st1))
print(id(st2))
#一个类可以创建N多个类的实例对象，每个实例对象的属性值不同
print('-----------为st1绑定性别属性-------------')
st1.c='♂'
print(st1.aaa,st1.bbb,st1.c)
print(st2.aaa,st2.bbb)
print('---------为st1单独绑定一个方法---------')
def show():
    print('这是我为st1单独绑定的一个方法')
st1.show=show#此处没有括号
st1.show()
