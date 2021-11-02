#列表元素的增、删、改

#list.append()向列表的末尾添加一个元素
a=[12,4,468,4842,4,772,755]
print(a,id(a))
a.append(1000)
print(a,id(a))

#list.extend()在列表的末尾至少添加一个元素
b=['a','b','c']
a.append(b)#将列表作为一个元素添加到a中了
print(a,id(a))
a.extend(b)#将b列表中的元素添加到a列表中
print(a,id(a))

#通过list.insert()在列表的任意位置插入一个元素
a.insert(1,90)#在索引为1的位置添加90这一个元素
print(a,id(a))

#在任意的位置添加N多个元素(即通过将切片赋值新的列表实现)
c=[True,False,12138]
d=[1,2,3,4,5,6,7,8,9]
print(d,id(d))
d[::]=c
print(d,id(d))
d[1:2:]=c
print(d,id(d))
d[:3:]=c
print(d)
d[::2]=c
print(d)