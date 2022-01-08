#数组元素的添加与删除
import numpy as np
'''
numpy.resize 函数返回指定大小的新数组。
如果新数组大小大于原始大小，则包含原始数组中的元素的副本。
numpy.resize(arr, shape)
arr：要修改大小的数组
shape：返回数组的新形状
'''
a=np.array([[1,2],[3,4],[5,6]])
print(a,a.shape)
b=np.resize(a,(2,3))
print(b,b.shape)
print('-------------------------------------------------')
c=np.resize(a,(5,5))
print(c,c.shape)
'''
numpy.append 函数在数组的末尾添加值。 追加操作会分配整个数组，并把原来的数组复制到新数组中。
此外，输入数组的维度必须匹配否则将生成ValueError。
append 函数返回的始终是一个一维数组。
numpy.append(arr, values, axis=None)
arr：输入数组
values：要向arr添加的值，需要和arr形状相同（除了要添加的轴）
axis：默认为 None。当axis无定义时，是横向加成，返回总是为一维数组！
当axis有定义的时候，分别为0和1的时候。当axis有定义的时候，分别为0和1的时候（列数要相同）。当axis为1时，数组是加在右边（行数要相同）。
'''
print('----------------------------------------------------')
print(np.append(b,[7,8,9]))
print(np.append(b,[[7,8,9]],axis=0))#可以和数组的拼接比较一下
print(np.append(a,[[3],[5],[7]],axis=1))#可以和数组的拼接比较一下
'''
numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值。
如果值的类型转换为要插入，则它与输入数组不同。 插入没有原地的，函数会返回一个新数组。 此外，如果未提供轴，则输入数组会被展开。
numpy.insert(arr, obj, values, axis)
arr：输入数组
obj：在其之前插入值的索引
values：要插入的值
axis：沿着它插入的轴，如果未提供，则输入数组会被展开
'''
print('---------------------------------------------------')
print(a)
print(np.insert(a,2,[99,98]))
print(np.insert(a,3,[7,8],axis=0))
print(np.insert(a,1,11,axis=1))
'''
numpy.delete 函数返回从输入数组中删除指定子数组的新数组。 与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开。
Numpy.delete(arr, obj, axis)
arr：输入数组
obj：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组
axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开
'''
print('------------------------------------------------------')
print(np.delete(a,0))#未指定轴，数组被展开，索引为0的元素被删除
print(np.delete(a,0,axis=0))#删除索引为0的行
x = np.array([1,2,3,4,5,6,7,8,9,10])
print (np.delete(x,x[::2]))
'''
numpy.unique 函数用于去除数组中的重复元素。
numpy.unique(arr, return_index, return_inverse, return_counts)
arr：输入数组，如果不是一维数组则会展开
return_index：如果为true，返回 新列表元素 在旧列表中的位置（下标），并以列表形式储
return_inverse：如果为true，返回 旧列表元素 在新列表中的位置（下标），并以列表形式储
return_counts：如果为true，返回 去重数组 中的元素在原数组中的出现次数
'''
print('-------------------------------------------------------------')
y = np.array([5,2,6,2,7,5,6,8,2,9])
print(y)
print(np.unique(y))
print('-------------------------------------------------------------')
print(np.unique(y,return_index = True))
m,n=np.unique(y,return_index = True)
print(n)#新列表元素 在 旧列表中的位置
print('---------------------------------------------------------------')
print(np.unique(y,return_inverse = True))
i,j=np.unique(y,return_inverse = True)
print(j)#旧列表元素 在 新列表中的位置
print('------------------------------------------------------------')
print(m[j])#重构原数组
print('-----------------------------------------------------------')
print(np.unique(y,return_counts=True))
p,q=np.unique(y,return_counts=True)
print(q)#返回去重元素的重复数量
