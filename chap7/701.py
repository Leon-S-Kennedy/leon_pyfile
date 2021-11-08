#字符串的查询
#获得子串的索引
s='hello,hello'
print(s.index("lo"))
print(s.find("lo"))
print(s.rindex('lo'))
print(s.rfind('lo'))

#str.index()方法会报错
#print(s.index("k"))
#print(s.rindex("k"))
print(s.find('k'))
print(s.rfind('k'))
