#转义字符

print('hello\nworld')#\n表示换行
print('hello\tworld')#\t表示水平制表符
print('helloooo\rworld')#\r表示回车即移动光标到本行的开头
print('hello\bworld')#\b表示退格一个字符

#字符串之中包含反斜杠、单引号、双引号等有特殊用途的字符时，需要加反斜杠进行转义
print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')

#不希望字符串中的转义字符起作用，就使用原字符，即字符串之前加R或r
print(R'hello\nworld')#最后一个字符不能是奇数个反斜杠
