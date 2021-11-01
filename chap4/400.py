#列表相当于(数组)
#数组的元素只能是同一类型，列表的元素可以是不同类型
list1=['hello',"world",'98']
print(id(list1),type(list1),list1)
#列表的创建
#使用中括号如上所示
#使用内置函数list()
list2=list(['hello','world',98])
list3=list['hello','world',98]
print(list2)
print(list3)
#列表的特点
'''列表元素按顺序有序排列、索引映射唯一一个数据、列表可以存储重复数据、任意数据类型混存、根据需要动态分配和回收内存'''

r=range(10)
print(type(r))
b=list[r]
c=list(r)
print(type(b),b)
print(type(b),c)


