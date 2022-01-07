#分割数组
import numpy as np
'''
numpy.split 函数沿特定的轴将数组分割为子数组，格式如下：
numpy.split(ary, indices_or_sections, axis)
ary：被分割的数组
indices_or_sections：如果是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的位置（左开右闭）
axis：设置沿着哪个方向进行切分，默认为 0，横向切分，即水平方向。为 1 时，纵向切分，即竖直方向。
'''
a=np.arange(9)
b=np.split(a,3)#将数组分割成为3份
c=np.split(a,[4,7])#4和7分别是余下子数组的首个元素的索引
print(a)
print(b)
print(c)
print('-------------------------------------------------------')
d=np.arange(16).reshape(4,4)
e=np.split(d,2)
f=np.split(d,2,1)
g=np.split(d,[1,3])
print(e)
print(f)
print(g)
print('--------------------------------------------------------')
#numpy.hsplit 函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组。
m=np.floor(10*np.random.random((2,6)))
print(m)
print(np.hsplit(m,3))#【------|------|------】就是这样切
print('--------------------------------------------------------')
n=m.reshape(6,2)
print(n)
print(np.vsplit(n,3))
'''
|
|
---
|
|
---
|
|
就是这样切
'''