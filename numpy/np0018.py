#numpy数学函数

#三角函数、反三角函数、双曲函数、反双曲函数
import numpy as np
a=np.array([0,30,60,90])
print(np.sin(a*np.pi/180))#化为弧度制
print(np.cos(a*np.pi/180))#显然cos90°为0
print(np.tan(a*np.pi/180))#显然tan90°不存在

print(np.degrees(np.arcsin(0.5)))#可以通过 numpy.degrees() 函数将弧度转换为角度。

'''
舍入函数
numpy.around() 函数返回指定数字的四舍五入值。
numpy.around(a,decimals)
a: 数组
decimals: 舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
'''
b=np.array([1.0,2.4,3.5,0.618,123.532])
print(b)
print('-----------------------这是一条华丽的分割线----------------------')
print(np.around(b))
print(np.around(b,decimals=1))
print(np.around(b,decimals=2))
print(np.around(b,decimals=-1))

#取整函数

#numpy.floor() 返回小于或者等于指定表达式的最大整数，即向下取整。
c=np.array([1.12,6.45,-13.1,-0.68,0.13])
print('------------------向下取整-------------------')
print(c)
print(np.floor(c))

#numpy.ceil() 返回大于或者等于指定表达式的最小整数，即向上取整。
print('------------------向下取整-------------------')
print(np.ceil(c))