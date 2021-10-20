print(chr(0b100111001011000))
print(ord('乘'))

#python中的标识符与保留字
import keyword
print(keyword.kwlist)#python之中的保留字

#变量、函数、类、模块和其他对象的起的名字就叫标识符
#字母、数字、下划线
#不能以数字开头
#不能是保留字
#严格区分大小写

#变量的使用
name='wdmmd'
print(name,'name')
#变量的定义
print('地址',id(name))
print('类型',type(name))
print('值',name)

#数据类型
#整形
print(178,0b10111001,0o14537,0x1a2c3f)#0b表示2进制、0o表示8进制、0x表示16进制、10进制为默认

#浮点型
#浮点型数据由于存储方式会导致一定的误差
print(3.14,type(3.14))
print(1.1+2.2)
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型
#Ture表示真，False表示假
#布尔值可以转化成整数
print(True,type(True),True+1)
print(False,type(False),False+1)

#字符串类型
#字符串又被称为不可变字符序列，可以用单引号或双引号或多引号来定义，单引号和双引号定义的字符串必须在一行，多引号可以多行。
str1='人生苦短，我用python'
str2='''人生苦短，
        我用python'''
print(str1,type(str1))
print(str2,type(str2))



