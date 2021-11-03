#字典中元素的获取
#使用dic['key']
a={'a':1,'b':2,'c':3}
print(a['b'])
#使用dict.get("key")

print(a.get("c"))
print(a.get("e",0),)#0是在查找“e”所对应的值不存在时提供的一个返回值

