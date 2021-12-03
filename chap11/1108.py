#类的浅拷贝与深拷贝
#变量的赋值操作
class CPU:
    pass
class Disk:
    pass
class Computer:
        def __init__(self,cpu,disk):
            self.cpu=cpu
            self.disk=disk
cpu1=CPU()
cpu2=cpu1
print(cpu1)
print(cpu2)
#python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此源对象与拷贝对象会引用同一个子对象
print('---------------这是一条华丽的分割线---------------')
disk=Disk()
com=Computer(cpu1,disk)#创建一个计算机类的对象
#浅拷贝
import copy
com2=copy.copy(com)
print(com,com.cpu,com.disk)
print(com2,com2.cpu,com2.disk)
#深拷贝，使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象拷贝对象所有的子对象也不相同
print('------------------------------------深拷贝----------------------------------------------')
com3=copy.deepcopy(com)
print(com,com.cpu,com.disk)
print(com3,com3.cpu,com3.disk)



