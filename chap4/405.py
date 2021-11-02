#列表元素的增、删、改
#使用list.remove(元素)来删除列表中的一个元素
a=[10,20,30,40,50,60,30]
a.remove(30)
print(a)#有重复元素只移除第一个
#a.remove(100)ValueError: list.remove(x): x not in list当没有该元素时会报错

#使用list.pop(索引)来移除指定索引上的元素
a.pop(1)
print(a)
'''
a.pop(9)
print(a)
IndexError: pop index out of range不存在指定索引会报错
'''
a.pop()
print(a)#如果不指定索引，将移除最后一位元素

#使用切片
#使用切片会产生一个新的list
b=a[1:3:]
print('原列表',a)
print('新列表',b)

print('----------不产生新的列表-----------')#相当于将切片替换成空列表
a[1:3:]=[]
print(a)

#使用clear清除列表
a.clear()
print(a)

#使用del删除列表
del a
#print(a)NameError: name 'a' is not defined,a列表已经被清除


