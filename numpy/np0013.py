#numpy数组操作
import numpy as np
'''
numpy.expand_dims 函数通过在指定位置插入新的轴来扩展数组形状，函数格式如下:
 numpy.expand_dims(arr, axis)
arr：输入数组
axis：新轴插入的位置
'''
x=np.array([[1,2],[3,4]])
print(x)
y1=np.expand_dims(x,axis=0)#[[[1,2],[3,4]]]
y2=np.expand_dims(x,axis=1)#[[[1,2]],[[3,4]]]
print('-----------------------------------')
print(y1,y1.shape)
print(y2,y2.shape)
print('-----------------------------------')
print(x.ndim)
print(y1.ndim)
print(y2.ndim)
'''
numpy.squeeze 函数从给定数组的形状中删除一维的条目，函数格式如下：
numpy.squeeze(arr, axis)
arr：输入数组
axis：整数或整数元组，用于选择形状中一维条目的子集
'''
y=np.arange(9).reshape(1,3,3)
print(y)
z=np.squeeze(y,0)
print(z)
print(y.shape,z.shape)


