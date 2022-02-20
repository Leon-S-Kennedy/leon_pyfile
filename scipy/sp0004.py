#scipu积分
import numpy as np
import scipy.integrate as ig
import math
#一重积分
f1=lambda x:np.exp(-x**2)#标准正态分布的lambda表示
#以函数形式定义标准正态分布
def f2(x):
    y=np.exp(-x**2)
    return y
i=ig.quad(f1,0,5)
print(i)#quad函数返回两个值，第一个值是积分的值，第二个值是对积分值的绝对误差估计。
print('------------------------------------------------------')
#含参数的的积分
def f3(x,a,b):
    y=a*(x**2)+b
    return y
i1=ig.quad(f3,0,1,args=(3,1))
print(i1)

#二重积分
f=lambda x,y:19*x*y                     #被积函数
g=lambda x:0                            #y的下限函数
h=lambda y:math.sqrt(1-4*y**2)          #y的上限函数
i2=ig.dblquad(f,0,0.5,g,h)
print(i2)
