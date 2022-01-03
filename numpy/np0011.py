#numpy数组操作
#reshape不解释

#numpy.ndarray.flat是一个数组元素迭代器
import numpy as np
a=np.arange(9).reshape(3,3)
print(a,id(a))
print('-*--------------------*-')
for i in a:
    print(i)
#输出的是每一行
print('-----------------------------------------')

for j in a.flat:
    print(j)
#输出的是每一个元素

#numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：
#ndarray.flatten(order='C')
#order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
print('------------------------数组展开--------------------------')
print(a.flatten(),id(a.flatten()))
print(a.flatten(order='F'),id(a.flatten(order='F')))
'''
numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图（view，有点类似 C/C++引用reference的意味），修改会影响原始数组。
该函数接收两个参数：
numpy.ravel(a, order='C')
order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
'''
print('-----------------------------------------------------------')
print(a.ravel(),id(a.ravel()))
print(a.ravel(order='F'),id(a.ravel(order='F')))
a.ravel()[2]=12
print(a,id(a))

