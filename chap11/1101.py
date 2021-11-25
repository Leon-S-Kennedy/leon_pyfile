#面向对象的三大特征————继承
#继承用来提高代码的复用性

#语法class 子类类名(父类类名):
class Person():#默认继承object类
    a=123
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,num):
        super().__init__(name,age)
        self.num=num

class Teacher(Person):
    def __init__(self,name,age,t_year):
        super().__init__(name,age)
        self.t_year=t_year

st=Student('calvin',21,200421088)
th=Teacher('合法公民',33,10)
st.show()
th.show()
#python中支持多继承
class A:
    pass
class B(object):
    pass
class C(A,B):
    pass