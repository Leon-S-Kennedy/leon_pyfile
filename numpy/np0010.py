#修改数组中元素的值
import numpy as  np
a=np.array(range(0,60,5)).reshape(3,4)
print(a,id(a))
print('---------------------------------------------------------')
for x in np.nditer(a,op_flags=['readwrite']):
    x[...]=2*x#x[...] 是修改原 numpy 元素，x 只是个拷贝。
print(a,id(a))
'''
nditer 对象有另一个可选参数 op_flags。 
默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only），
为了在遍历数组的同时，实现对数组元素值得修改，必须指定 read-write 或者 write-only 的模式。
'''
print('------------------------------------------------------------')
for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):
   print (x, end=", " )
#迭代器遍历对应于每列，并组合为一维数组。

#广播迭代
print('\n------------------------------------------------------------------')
j = np.arange(0,60,5)
j = j.reshape(3,4)
print  ('第一个数组为：')
print (j)
print  ('\n')
print ('第二个数组为：')
b = np.array([1,  2,  3,  4], dtype =  int)
print (b)
print ('\n')
print ('修改后的数组为：')
for x,y in np.nditer([j,b]):
    print ("%d:%d"  %  (x,y), end=", " )
