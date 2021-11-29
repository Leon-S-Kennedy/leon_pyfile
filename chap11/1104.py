#面向对象的三大特征————多态
'''多态就是“具有多种形态”即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法在运行过程中
根据变量所引用对象的类型，动态决定调用哪个对象中的方法
'''
class Animal:
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person():
    def eat(self):
        print('人全都要')
def f(obj):
    obj.eat()
#注意此处的括号，这表示你必须输入一个类的实例对象，否则报错
f(Animal())
f(Dog())
f(Cat())
f(Person())
#或者通过这种方法，先创建一个类的对象，再输入
p=Person()
f(p)
'''动态语言的多态崇尚'鸭子类型'，当看到一只行为举止像鸭子的鸟的时候，那么这只鸟就可以被称为鸭子。
不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为
'''
