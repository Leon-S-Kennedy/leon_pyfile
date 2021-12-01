#特殊属性和特殊方法
#特殊方法
a=20
b=10
c=a+b#其原理就是用a对象的add方法，如下所示
print(c)

d=a.__add__(b)
print(d)
print('-------------这是一条华丽的分割线-------------')
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
st1=Student('李博文')
st2=Student('Calvin')

e=st1.__add__(st2)
print(e)

f=st1+st2
print(f)

#len函数
lst=[11,22,33,44,55,66]
print(len(lst))
print(lst.__len__())
print(Student.__len__(st1))




