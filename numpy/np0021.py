#numpy的排序
'''
常见的排序算法：
quicksort'（快速排序）
'mergesort'（归并排序）
'heapsort'（堆排序）
这些排序函数实现不同的排序算法，每个排序算法的特征在于执行速度，最坏情况性能，所需的工作空间和算法的稳定性。
'''
import numpy as np
'''
numpy.sort() 函数返回输入数组的排序副本。函数格式如下：

numpy.sort(a, axis, kind, order)
a: 要排序的数组
axis: 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序， axis=0 按列排序，axis=1 按行排序
kind: 默认为'quicksort'（快速排序）
order: 如果数组包含字段，则是要排序的字段
'''
a=np.array([[5,2],[4,3]])
print(a)
print(np.sort(a))#默认是按行排序（展开后最后的轴是列的方向，即1轴，即按行排序）
print(np.sort(a,axis=0))#行的方向，即按列排序
print('--------------------------------------------------------------------')
dt=np.dtype([('name', 'S10'),('age', int)])#此处的S为大写，小写会报错
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)],dtype=dt)
print(np.sort(a,order='name'))
print('--------------------------------------------------------------------')

#numpy.argsort()
#numpy.argsort() 函数返回的是数组值从小到大的索引值。
x=np.array([1,2,3,5,4])
y=np.argsort(x)
print(y)#相当于先排序，然会输出排序后的索引
print(x[y])#可以看到排序后的数组
for i in y:
    print(x[i],end='\t')

'''
numpy.lexsort() 用于对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列。
这里举一个应用场景：
小升初考试，重点班录取学生按照总成绩录取。
在总成绩相同时，数学成绩高的优先录取，在总成绩和数学成绩都相同时，按照英语成绩录取…… 
这里，总成绩排在电子表格的最后一列，数学成绩在倒数第二列，英语成绩在倒数第三列。
'''
print('\n-------------------这是一条华丽的分割线--------------------')
# 录入了四位同学的成绩，按照总分排序，总分相同时语文高的优先
math    = (10, 20, 50, 10)
chinese = (30, 50, 40, 60)
total   = (40, 70, 90, 70)
# 将优先级高的项放在后面
ind = np.lexsort((math, chinese, total))

for i in ind:
    print(total[i],chinese[i],math[i])
