#range函数的3种创建方式
#range(stop)表示创建一个(0,stop)之间的整数序列，其步长为1
a=range(10)
print(list(a))
#range(start,stop)表示创建一个(start,stop)之间的整数序列，步长为1
b=range(2,10)
print(list(b))
#range(start,stop,step)表示创建一个(start,stop)之间的整数序列，步长为step
c=range(1,10,2)
print(list(c))
#其返回值是一个迭代器对象
#in与not in判断整数序列之中是否存在（不存在）指定的整数
print(7 in c)
print(8 in c)