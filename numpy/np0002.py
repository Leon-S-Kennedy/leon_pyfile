#NumPy 数组的维数称为秩（rank），秩就是轴的数量，即数组的维度，一维数组的秩为 1，二维数组的秩为 2，以此类推。
#可以理解为2维数组就是矩阵，依次类推
import numpy as np
print('----------ndim用于输出数组的秩----------')
a = np.arange(24)
print(a)
print (a.ndim)             # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print(b)
print (b.ndim)

print('-----------shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目-----------')
print(b.shape)#(Z,Y,X)方向的元素的个数

print('-------------------itemsize 以字节的形式返回数组中每一个元素的大小-----------------------')
x = np.array([1,2,3,4,5], dtype = np.int8)
print (x.itemsize)

print('----------------size	数组元素的总个数，相当于 .shape 中 n*m 的值-------------------')
print(b.size)