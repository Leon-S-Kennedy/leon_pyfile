#字符串的判断

#使用str.isindentifier()判断是否合法标识符（字母，数字，下划线）
a='hello,python'
print('1.',a.isidentifier())
print('2.','hello_123张三'.isidentifier())#众所周知“汉字”是字母

#使用str.isspace()判断是否全空格(换行，回车，水平制表符)
b='\n\r\t'
print(b.isspace() )

#使用str.isalpha()判断是否全字母
c='abcdefg'
print(c.isalpha())

#使用str.isdecimal()判断是否十进制
d='0000110010010'
print(d.isdecimal())

#使用str.isnumeric()判断字符串是否全部由数字组成（包括汉字，罗马数字）
print('四Ⅰ5'.isnumeric())

#使用str.alnum()判断字符串是否全部由字母或字符串组成
print('a1b2c3d4DW7张三'.isalnum())
