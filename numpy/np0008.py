#广播
#广播(Broadcast)是 numpy 对  不同形状(shape)  的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。
#如果两个数组 a 和 b 形状相同，那么 a*b 的结果就是 a 与 b 数组对应位相乘。
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b
print(c)
#显然a和b的形状相同，可以直接相乘。

d=np.array([[0,0,0],[10,10,10],[20,20,20],[30,30,30]])
e=np.array([1,2,3])
print(d+e)
print(d*e)
#显然d和e的形状不同，此时相加会触发广播机制



