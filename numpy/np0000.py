#NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。
#ndarray 对象是用于存放同类型元素的多维数组。
#ndarray 中的每个元素在内存中都有相同存储大小的区域。

import numpy as np
a=np.array([4,5,6])
print(a,type(a))

b=np.array([[4,5,6],[7,8,9]])
print(b,type(b))

c=np.array([1,121341,34,56],ndmin=3)
print(c)

d=np.array([1,2,3],dtype=complex)
print(d)

e=np.array(range(10))
print(e)

f=np.arange(10)
print(f)
print(f.dtype)
