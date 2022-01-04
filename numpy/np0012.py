#numpy数组操作
#翻转数组
import numpy as np
a=np.arange(12).reshape(3,4)
print(a)

print('---------------------------------------')
print(np.transpose(a))

print('----------------------------------------')
print(a.T)

#numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，格式如下：
print('-*---------------------------------------------*-')
b=np.arange(8).reshape(2,2,2)
print(b)
print(np.where(b==6))#一层一层的剥开，翻开外层括号，是第1个，翻开中层括号，是第1个，翻开内层括号是第0个索引是（1，1，0）
print(b[1,1,0])
print ('调用 rollaxis 函数：')
c = np.rollaxis(b,2,0)
print('------------------------------------------------------')
print(c)
print(np.where(c==6))
'''
numpy.swapaxes 函数用于交换数组的两个轴，格式如下：
numpy.swapaxes(arr, axis1, axis2)
arr：输入的数组
axis1：对应第一个轴的整数
axis2：对应第二个轴的整数
'''
print('-------------------------这是一条华丽的分割线------------------------')
print(b)
print(np.swapaxes(b,2,0))
print(np.where(np.swapaxes(b,2,0)==6))

#numpy.broadcast 用于模仿广播的对象，它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。
#该函数使用两个数组作为输入参数，如下实例：
print('-------------------------这是一条华丽的分割线------------------------')
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
z = np.broadcast(x,y)
print(z.shape,type(z))
c=[u+v for (u,v)in z]
print(c,type(c))
c1=np.asarray(c).reshape(3,3)
print(c1,type(c1))
print(x+y)
'''
显然z不能直接转成数组，使用for循环将z中的数据拿出来，形成一个列表，再转成数组
'''
'''
numpy.broadcast_to 函数将数组广播到新形状。它在原始数组上返回只读视图。 
它通常不连续。 如果新形状不符合 NumPy 的广播规则，该函数可能会抛出ValueError。
'''
print('-----------------------------------------------------------------')
d=np.arange(4).reshape(1,4)
print(d)
print(np.broadcast_to(d,(4,4)))
