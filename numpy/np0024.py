#numpy 副本和视图
import numpy as np
'''
副本:是一个数据的完整的拷贝，如果我们对副本进行修改，它不会影响到原始数据，物理内存不在同一位置。
视图:是数据的一个别称或引用，通过该别称或引用亦便可访问、操作原有数据，但原有数据不会产生拷贝。
    如果我们对视图进行修改，它会影响到原始数据，物理内存在同一位置。
'''
a = np.arange(6)
print ('我们的数组是：')
print (a)
print ('调用 id() 函数：')
print (id(a))
print ('a 赋值给 b：')
b = a
print (b)
print ('b 拥有相同 id()：')
print (id(b))
print ('修改 b 的形状：')
b.shape =  3,2
print (b)
print ('a 的形状也修改了：')
print (a)

#ndarray.view() 方会创建一个新的数组对象，该方法创建的新数组的维数更改不会更改原始数据的维数。
print('-----------------------------------------------------------------------')
x=np.arange(6).reshape(3,2)
print(x)
y=x.view()
print(id(x),id(y))
y.shape=2,3
print(y)
print(x)

