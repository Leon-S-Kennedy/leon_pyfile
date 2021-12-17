#判断数据是否是数据
pwd=input('随便输入纯数字:')
print(type(pwd))
if pwd.isdigit():
    print('你输的很对')
else:
    print('你输的是个锤子')
#enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
year=[96,97,96,98,99,00,89]
print('原列表',year)
for i,v in enumerate(year):
    if str(v)!='0':
        year[i]=int('19'+str(v))
    if str(v)=='0':
        year[i]=int('200'+str(v))
print('修改之后的列表是',year)

