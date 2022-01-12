#算术函数
import numpy as np
'''
NumPy 算术函数包含简单的加减乘除: add()，subtract()，multiply() 和 divide()。
需要注意的是数组必须具有相同的形状或符合数组广播规则。
'''
a=np.arange(9,dtype=np.float_).reshape(3,3)
b=np.array([1,2,3])
print(a)
print(b)
print('----------------------------------------------------')
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print('-----------------------------------------------------')
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
'''
numpy.reciprocal() 函数返回参数逐元素的倒数。如 1/4 倒数为 4/1。
'''
print('-----------------------这是一条华丽的分割线---------------------')
c=np.array([1/4,1/3,3,4])
print(c)
print('------------------------------------------------------')
print(np.reciprocal(c))

'''
numpy.power() 函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。
'''
print('-----------------------这是第二条华丽的分割线---------------------')
d=np.arange(9).reshape(3,3)
e=np.arange(1,4).reshape(1,3)
print(d)
print(e)
print('-----------------------------------------------------------')
print(np.power(d,e))
print(d**e)
'''
numpy.mod() 计算输入数组中相应元素的相除后的余数。 函数 numpy.remainder() 也产生相同的结果。
'''
print('-----------------------这是第三条华丽的分割线---------------------')
f=np.arange(10,100,10).reshape(3,3)
g=np.array([7,7,7])
print(f)
print(g)
print('-------------------------------------------------')
print(np.mod(f,g))
print(np.remainder(f,g))
print(f%g)
