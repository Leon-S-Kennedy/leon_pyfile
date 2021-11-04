#字典元素的遍历
a={'a':1,'b':2,'c':3}
for i in a:
    print(i)#输出的是字典的是'键'值
    print(a[i],a.get(i))#通过两个获取函数输出字典中的value


    