#字典的常用操作
a={'a':1,'b':2,'c':3}
print('a' in a)
print('a'not in a)
#字典元素的删除
#通过del dict["key"]删除字典中特定的”key“以及”值“
del a['a']
print(a)

a.clear()#清空字典
print(a)

#字典键值对的添加或者修改dict['key']=value
a['d']=4
print(a)

#获取字典视图
#使用dict.keys()获取字典的所有键
b={'a':1,'b':2,'c':3}
keys=b.keys()
print(keys)
print(type(keys))
print(list(keys))
#使用dict.values()获取字典的所有的值
c={'a':1,'b':2,'c':3}
values=c.values()
print(values)
print(type(values))
print(list(values))

#使用dict.items()获取字典的所有的键值对
d={'a':1,'b':2,'c':3}
items=d.items()
print(items)#用方括号括起来的叫元组
print(type(items))
print(list(items))#每一个小括号叫元组，转换之后的列表是由元组组成的。
