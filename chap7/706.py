#字符串的其他操作

#使用str.replace('被替换子串'，'替换字符串'，最大替换次数)对字符串进行替换
s='hello,python'
s1=s.replace('python','java')
print(s1)
s='hello,python,python,python'
s2=s.replace('python','java',2)
print(s2)

#使用'str'.join(list|tuple|str)进行连接
lst=['hello','world','python']
lst1='*'.join(lst)
print(lst1)

print('*'.join('python'))
