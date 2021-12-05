#模块(modules)
#模块由N多个函数N多个类以及N多个语句组成
#在python中一个扩展名为py的文件就是一个模块

#自定义模块之模块的导入
#import 模块名称 [as 别名]    导入一个模块中的所有内容
#from 模块名称 import 函数/变量/类   从模块中导入相应的函数/变量/类
import math as m
print(id(m))
print(type(m))
print(m)
print(m.e)
print(dir(m))

from math import pi
print(pi)
