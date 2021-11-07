#集合的数学操作

#交集
a={1,2,3,4,5,11,12,13,14}
b={1,2,3,4,5,6,7,8,9}
print(a.intersection(b))
print(a&b)#切记不要与'按位与'记混了

#并集
print(a.union(b))
print(a|b)#不要与“按位或”记混

#差集
print(a.difference(b))
print(a-b)
print(b.difference(a))
print(b-a)

#对称差集（并集-交集）
print(a.symmetric_difference(b))
print(a^b)
print(b.symmetric_difference(a))
print(b^a)
