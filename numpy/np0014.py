#连接数组
import numpy as np
'''
numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组，格式如下：
numpy.concatenate((a1, a2, ...), axis)
a1, a2, ...：相同类型的数组
axis：沿着它连接数组的轴，默认为 0
'''
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print('--------------------------------------')
print(np.concatenate((a,b)))#默认是0轴
print(np.concatenate((a,b),axis=1))
print('--------------------------------------')
'''
numpy.stack 函数用于沿新轴连接数组序列，格式如下：
numpy.stack(arrays, axis)
arrays相同形状的数组序列
axis：返回数组中的轴，输入数组沿着它来堆叠
'''
print('--------------------------------------')
print(np.stack((a,b)))#默认是0轴
print(np.stack((a,b),1))
print('--------------------------------------')
#numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组。
print(np.hstack((a,b)))
#numpy.vstack 是 numpy.stack 函数的变体，它通过垂直堆叠来生成数组。
print(np.vstack((a,b)))

