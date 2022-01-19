#numpy矩阵库
import numpy as np
a=np.arange(12).reshape(3,4)
print(a)
print(a.T)
'''
matlib.empty() 函数返回一个新的矩阵，语法格式为：
numpy.matlib.empty(shape, dtype, order)
shape: 定义新矩阵形状的整数或整数元组
Dtype: 可选，数据类型
order: C（行序优先） 或者 F（列序优先）
'''
b=np.empty((2,2))
print(b)

c=np.zeros((2,3))
print(c)

d=np.ones((2,4))
print(d)

e=np.eye(3,3)
print(e)

f=np.identity(5)
print(f)

g=np.random.rand(3,3)
print(g)

print('---------------这是一条华丽的分割线------------------')
h=np.matrix('1,2;3,4')
print(h,type(h))

i=np.asarray(h)
print(i,type(i))

j=np.asmatrix(i)
print(j,type(j))


