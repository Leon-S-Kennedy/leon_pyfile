#布尔索引
import numpy as np

a1=np.arange(12)
a=a1.reshape(4,3)
print(a,id(a))
#打印大于5的数
print(a[a>5])
a[a>5]=10
print(a,id(a))

a0=np.where(a<5,5,10)
print(a0,id(a0))

c=np.nan
print(c,type(c))
d=np.array([np.nan,1,1,2,3,np.nan,5,7,5.68])
print(d[~np.isnan(d)])#打印d中是nan的补集，即打印不是nan的数

#过滤掉非复数元素
e=np.array([1,1+2j,2+3j])
f=e[np.iscomplex(e)]
print(f)
