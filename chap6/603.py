#集合的相关操作

#集合元素的判断操作
a={1,5,'sdf',5,'sdf',7}
print('sdf' in a)
print(8 not in a)

#集合元素的新增操作
a.add(80)#一次添加一个元素
print(a)
a.update({'12138','lbw',484})#一次至少添加一个元素
print(a)
a.update(['12138','lbw',404])
print(a)
a.update(('12138','lbw',360))
print(a)
#集合元素的删除操作
a.remove(360)#一次删除一个元素，不存在就报错。
print(a)
a.discard(4847)#一次删除一个元素，不存在不抛出异常。
print(a)
a.pop()#随机删除一个倒霉的数据，不能指定参数，否则报错。
print(a)
#清空集合中的元素
a.clear()
print(a)
#删除集合
del a
#print(a)
