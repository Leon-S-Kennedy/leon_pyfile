#字符串的大小写转换

#使用str.upper()方法会产生一个新的字符串
s='hello,python'
s1=s.upper()
print(s1,s)
print(id(s),id(s1))

#使用str.lower()转换成小写
s2=s1.lower()
print(s2,id(s2))

#使用str.swapcase()的方法将大小写互换
a='Hello,Python'
b=a.swapcase()
print(b)

#使用str.capitalize()将首字母大写，其余小写
c='capitalize'
d=c.capitalize()
print(d)

#使用str.title()将每个单词的首字母大写，其余字母小写
e='hello,world'
f=e.title()
print(f)

