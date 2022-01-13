#统计函数
import numpy as np
'''
numpy.amin() 和 numpy.amax()
numpy.amin() 用于计算数组中的元素沿指定轴的最小值。
numpy.amax() 用于计算数组中的元素沿指定轴的最大值。
'''
a=np.array([[1,23,34],[23,43,24],[54,12,78]])
print(a)
print('-----------------------------------------------------------')
print(np.amin(a,0))#行方向上的最小值，即每一列的最小值
print(np.amin(a,1))#列方向上的最小值，即每一行的最小值
print(np.amax(a,0))#行方向上的最大值，即每一列的最大值
print(np.amax(a,1))#列方向上的最大值，即每一行的最大值
'''
numpy.ptp()函数计算数组中元素最大值与最小值的差（最大值 - 最小值）。
'''
print('-------------------------------------------------------------')
print(np.ptp(a))
print(np.ptp(a,0))
print(np.ptp(a,1))
'''
numpy.percentile()常用于求中位数
百分位数是统计中使用的度量，表示小于这个值的观察值的百分比。 函数numpy.percentile()接受以下参数。

numpy.percentile(a, q, axis)
a: 输入数组
q: 要计算的百分位数，在 0 ~ 100 之间
axis: 沿着它计算百分位数的轴
'''
print('---------------------------------------------------------------')
print(np.percentile(a,50))
print (np.percentile(a, 50, axis=0))
print (np.percentile(a, 50, axis=1))
print (np.percentile(a, 50, axis=1, keepdims=True))
'''
numpy.median() 函数用于计算数组 a 中元素的中位数（中值）
'''
print("-----------------------------------------------------------------")
print(np.median(a))
print(np.median(a,0))
print(np.median(a,1))
'''
numpy.mean() 函数返回数组中元素的算术平均值。 如果提供了轴，则沿其计算。
算术平均值是沿轴的元素的总和除以元素的数量。
'''
print('-------------------------------------------------------------------')
print(np.mean(a))
print(np.mean(a,0))
print(np.mean(a,1))
'''
numpy.average() 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。
该函数可以接受一个轴参数。 如果没有指定轴，则数组会被展开。
加权平均值即将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数。
注意，分母是权重的和
'''
print('------------------------------------------------------------------')
x=np.arange(1,5)
print(a)
print(np.average(a))#不指定权重的时候相当于mean()
print('-------------------------------------------------------------------')
y=np.arange(9).reshape(3,3)
z=np.array([[2,1,1],[1,1,1],[1,1,1]])
print(np.average(y,weights=z, returned =  True))# 如果 returned 参数设为 true，则返回权重的和
#可以指定轴的方向
z1=np.array([1,1,1])
print(np.average(y,axis=1,weights=z1))
print(np.average(y,axis=1,weights=z1,returned=True))
'''
标准差是一组数据平均值分散程度的一种度量。
标准差是方差的算术平方根。
标准差公式如下：
std = sqrt(mean((x - x.mean())**2))
'''
print('-------------------------------------------------------------------------')
print(np.std([[1,2,3,4],[5,6,7,8]]))#会将这个数组展开整体计算标准差
print (np.var([[1,2,3,4],[5,6,7,8]]))#同理


