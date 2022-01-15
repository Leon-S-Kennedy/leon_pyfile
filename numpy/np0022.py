#numpy的排序

import numpy as np
'''
函数	                                        描述
msort(a)	                                数组按第一个轴排序，返回排序后的数组副本。np.msort(a) 相等于 np.sort(a, axis=0)。
sort_complex(a)	                            对复数按照先实部后虚部的顺序进行排序。
partition(a, kth[, axis, kind, order])	    指定一个数，对数组进行分区
argpartition(a, kth[, axis, kind, order])	可以通过关键字 kind 指定算法沿着指定轴对数组进行分区
'''
#复数排序
a=np.array([1+1j,2+1j,2+3j,3+2j,4+5j,5+4j])
print(np.sort_complex(a))
'''
numpy.argmax() 和 numpy.argmin()函数分别沿给定轴返回最大和最小元素的索引。

'''
print('-----------------------------------------------------')
b=np.array([[1,2,4],[2,4,8],[3,14,9]])
print(b)
print(np.argmax(b))
print('-----------------------------------------------------')
#沿0轴方向最大值的索引
print(np.argmax(b,axis=0))
#沿1轴方向最大值的索引
print(np.argmax(b,axis=1))
'''
numpy.nonzero() 函数返回输入数组中非零元素的索引。
'''
print('--------------------------------------------------')
c=np.array([[1,2,3],[2,0,4],[0,0,4]])
print(c)
print(np.nonzero(c))

'''
numpy.where() 函数返回输入数组中满足给定条件的元素的索引。
'''
print('-----------------------------------------------------')
x=np.arange(9).reshape(3,3)
print(x)
y=np.where(x>3)
print(y)
print(x[y])

'''
numpy.extract() 函数根据某个条件从数组中抽取元素，返回满条件的元素。
'''
print('-----------------------------------------------')
print(x)
print(x%2 == 0)
print(np.extract(x%2==0,x))



