#面向对象的三大特征————继承
#方法重写
#如果子类对继承自父类的某个属性或方法不满意，可以在字类中对其（方法体）进行重写
#子类重写后的方法中可以通过super().方法名()调用父类中被重写过的方法，也可以像17行的方法直接重写
class Person():#默认继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,num):
        super().__init__(name,age)
        self.abcdefg=list(range(12))
        self.num=num
    def show(self):
        print(self.name, self.age,self.num,self.abcdefg)

        super().show()
        print(self.num)

class Teacher(Person):
    def __init__(self,name,age,t_year):
        super().__init__(name,age)
        self.t_year=t_year
    def show(self):
        super().show()
        print(self.t_year)
st=Student('calvin',21,200421088)
th=Teacher('合法公民',33,10)

st.show()
th.show()