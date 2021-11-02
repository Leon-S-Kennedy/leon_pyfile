#列表元素的排序

#通过list.sort()对列表进行升排序
a=[10,64,87.5,-12,78,0,64,100]
print('排序前的列表',a,id(a))
a.sort()
print('排序后的列表',a,id(a))

#通过指定参数可以实现降排序(reverse=Ture表示降序，reverse=False表示升序，默认为升序)
a.sort(reverse=True)
print('排序后的列表',a,id(a))

print('-----------使用内置函数sorted(),将产生一个新的列表对象------------')
b=[48.2,12.5,-45,-12,64,0,64,100]
c=sorted(b)
print('原列表',b,id(b))
print('新列表',c,id(c))

#通过指定参数可以实现降排序(reverse=Ture表示降序，reverse=False表示升序，默认为升序)
d=sorted(b,reverse=True)
print('排序后的列表',d,id(d))