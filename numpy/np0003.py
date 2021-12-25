#除了可以使用底层 ndarray 构造器来创建外，也可以通过以下几种方式来创建。
import numpy as np
print('---------------.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：-----------------')
x = np.empty([3,2], dtype = int)
print (x)#输出的值是未被初始化的辣鸡值

print('-------------.zeros方法创建一个指定大小的以0填充的数组-----------------')
y=np.zeros([3,2],dtype='i4')
print(y)#默认为浮点数

print('-------------.ones方法创建一个指定大小的以1填充的数组-----------------')
z=np.ones([3,4],dtype='i8')
print(z)#默认为浮点数

#从已有数组创建数组
print('----------将列表和元组转换成数组----------')
a=[1,2,3,4,5]
b=np.asarray(a)
print(b,type(b))

c=[(123,321,456,564),(90,80,70),(30,20)]
d=np.asarray(c)
print(d,d.size)

#从数值范围创建数组
print('-----------使用 arange 函数创建数值范围并返回 ndarray 对象-------------')
i = np.arange(5)
print (i)

print('-----------linspace 函数用于创建一个一维数组，数组是一个等差数列构成的-------------')
j = np.linspace(0,100,11)#np.linspace(start,stop,num)
print(j)
'''
start	序列的起始值
stop	序列的终止值，如果endpoint为true，该值包含于数列中
num	要生成的等步长的样本数量，默认为50
endpoint	该值为 true 时，数列中包含stop值，反之不包含，默认是True。
retstep	如果为 True 时，生成的数组中会显示间距，反之不显示。
'''

print('------------logspace 函数用于创建一个于等比数列--------------')
k = np.logspace(1,10, num =  10)#在base的start次方和stop次方之间生成一个样本数量为num的等比数列
print (k)
'''
start	序列的起始值为：base ** start
stop	序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
num	要生成的等步长的样本数量，默认为50
endpoint	该值为 true 时，数列中中包含stop值，反之不包含，默认是True。
base	对数 log 的底数。
'''