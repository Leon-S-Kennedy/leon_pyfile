#花式索引
import numpy as np
x=np.arange(32).reshape(8,4)
print(x)
print('----------------------------------------------------------------')
print(x[4,2])#此次操作取的是原数组第5行第3列的元素

x2=x[4],x[2]
print(x2,type(x2))#此操作取的是分别取出原数组的第5行以及第3行的元素组成一个元组

x3=[x[4],x[2]]
print(x3,type(x3))#此操作取的是分别取出原数组的第5行以及第3行的元素组成一个列表

x4=x[[4,2]]#以1维数组进行作为索引
print(x4,type(x4))#此操作取的是原数组的第5行以及第3行组成的新的数组
print(id(x),id(x4))#地址明显会变化

#传入倒序索引数组
print (x[[-4,-2,-1,-7]])

#入多个索引数组（要使用np.ix_）
print (x[np.ix_([1,5,7,2],[0,3,1,2])])
'''
这句话会输出一个4*4的矩阵，其中的元素分别是：
x[1,0] x[1,3] x[1,1] x[1,2]
x[5,0] x[5,3] x[5,1] x[5,2]
x[7,0] x[7,3] x[7,1] x[7,2]
x[2,0] x[2,3] x[2,1] x[2,2]
'''