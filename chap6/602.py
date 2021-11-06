#集合是没有value的字典，与列表、字典一样属于可变类型的序列(不要与列表弄混)
#集合的创建（不要与字典弄混了）
a={1,5,'sdf',5,'sdf',7}#集合中的元素不允许重复
print(a,type(a))

b=set(range(6))
print(b,type(b))

c=set([1,2,3,'780','asdf'])#列表和元组可以通过set()转换成集合
print(c,type(c))#输出结果表明集合中的元素是无序的

d={'hello'}
print(d,type(d))
e=set('hello')
print(e,type(e))

#定义一个空集合
f={}
print(f,type(f))
g=set()
print(g,type(g))

