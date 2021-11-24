#面向对象的三大特征————封装
#封装用来提高程序的安全性

#将数据（属性）和行为（方法）包装到类对象中，在内部对属性进行操作，在外部调用方法。无须关心内部细节，从而隔离复杂度。
class Car:
    def __init__(self,brand):
        self.brand=brand
    def sart(self):
        print('汽车人变形')
c=Car('科迈罗')
print(c.brand)
c.sart()

#如果不想该属性在类对象的外部被访问，前边使用两个__
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#当不希望被外部访问时，加了__
    def show(self):
        print(self.name,self.__age)
st1=Student('calvin',21)
st1.show()
#print(st1.__age)#此时会报错

#此时可以通过以下方法来使用
print(dir(Student('calvin',21)))
print(st1._Student__age)

