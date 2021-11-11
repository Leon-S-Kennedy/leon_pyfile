#字符串的格式化
#%作为占位符(%s表示字符串，%d、%i表示整数，%f表示小数)
name='李博文'
age=21
print('我叫%s,今年%d岁'%(name,age))

#使用{}作为占位符
print('我叫{0},今年{1}岁'.format(name,age))

#使用f-string
print(f'我叫{name},今年{age}岁')

