#数据类型转换
name='李博文'
age=21
print(type(name),type(age))
print('我叫'+name+'今年',age)#+作为连接符使用，字符串和整形链接时报错，此时需要使用数据类型转换。
print('我叫'+name+'今年'+str(age))#通过str()将整形转换成字符类型
print(str(age),type(str(age)))

#int()可以将其他数据类型转换成整数类型，文字类和小数类字符串无法转换成整数类型，浮点数为抹零取整。
a='128'
b=3.9
c='9.785'
d='ada'
e=True
print(type(a),type(b),type(c),type(d),type(e))
print(int(a),int(b),int(e))
print(type(int(a)),type(int(b)),type(int(e)))

#float()可以将其他数据类型转换成浮点型,文字类字符串无法转换成浮点型，整数型末尾为.0。
a1='128.98'
b1='76'
c1=True
d1='ada'
e1=128
print(type(a1),type(b1),type(c1),type(d1),type(e1))
print(float(a1),float(b1),float(c1),float(e1))

#python之中的注释
#1单行注释、以#开始直到换行
#2多行注释、一般将一对三引号之间的代码称为多行注释
'''我
是
多
行
注
释'''
"""我
也
是
多
行
注
释"""
#中文编码声明注释，在文件开头加上#coding:gbk，用以指定源码文件的编码格式（默认utf-8）