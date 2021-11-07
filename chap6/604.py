#集合之间的关系
#判断两个集合是否相等
a={1,2,3,4,5}
b={5,4,2,1,3}
print(a==b)
#一个集合是否是另外一个集合的子集
c={1,2,3,4,5,6,7,8,9}
print(a.issubset(c))#使用a.issubset(b)判断a是否是b的子集
print(c.issubset(b))
print(a.issubset(b))

#一个集合是否是另外一个集合的超集
print(c.issuperset(a))
print(b.issuperset(a))

#判断两个集合是否没有交集
d={'a','b','c','1'}
print(a.isdisjoint(b))
print(b.isdisjoint(d))
