#字符串的分割操作

#通过使用str.split(sep='',maxsplit='')对字符串进行劈分
#从左往右劈分，返回值是列表
s='hello world python'
lst=s.split()
print(lst,type(lst))
t='hello*world*python'
lst1=t.split(sep='*')
print(lst1)
lst2=t.split(sep='*',maxsplit=1)
print(lst2)

#使用str.rsplit(sep='',maxsplit='')从右往左劈分