#ndarray对象的内容可以通过索引或切片来访问和修改，与 Python 中 list 的切片操作一样。
import numpy as np
a=np.arange(10)
print(a[1::2])
s=slice(1,10,2)
print(a[s])
print(a[5])
print('--------------------------------------------------------')
b=a[:9:].reshape(3,3)
print(b)
# 从某个索引处开始切割
print('从数组索引 b[1:] 处开始切割')
print(b[1:])

print('------------------取子数组-------------------')#由此可见 : 和 ... 的作用一样，但是 : 似乎更加方便
print (b[:,1])   # 第2列元素
print (b[1,...])   # 第2行元素
print('-----------------------------------------------')
print (b[...,1:])  # 第2列及剩下的所有元素
print(b[1:,...])
print('-----------------------------------------------')
print(b[1:,1:])

#对于取不连续行或列的情况
print('-------------------------------对于不连续的行--------------------------------')
print(b[[2,0,0]])
print('------------------------------对于不连续的列------------------------------------')
print(b[:,[1,2,0]])

#如果要取2，3，4行以及1，3列的交叉元素
print(b)
rows=np.array([[1,1],[2,2],[3,3]])
cols=np.array([[0,2],[0,2],[0,2]])
#c=b[rows,cols]
#print(c)