#迭代数组
import numpy as np
a=np.arange(6).reshape(2,3)
print(a)
print(a.T)
print('------------------------------------------------------')
for i in a:
    print(i)
#注意这两种的主要的区别
for x in np.nditer(a):
    print(x,end='\t')
print('\n')

for y in np.nditer(a.T):
    print (y, end="\t" )
print ('\n')

for z in np.nditer(a.T.copy(order='C')):
    print (z, end="\t" )
print ('\n')
'''
a 和 a.T 的遍历顺序是一样的，也就是他们在内存中的存储顺序也是一样的，但是 a.T.copy(order = 'C') 的遍历结果是不同的
，那是因为它和前两种的存储方式是不一样的，默认是按行访问。order='F'即列序优先。
'''