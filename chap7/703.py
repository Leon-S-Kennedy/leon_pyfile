#字符串的对齐操作

#使用str.center(宽度，填充字符（默认空格）)居中对齐
a='hello,Python'
print(a.center(20,'*'))

#使用str.ljust(宽度，填充字符（默认空格）)左对齐
print(a.ljust(20,'*'))
#使用str.rjust(宽度，填充字符（默认空格）)右对齐
print(a.rjust(20,'*'))
#使用str.zfill(宽度)用0填充的右对齐
print(a.zfill(20))
print('-8999'.zfill(10))
