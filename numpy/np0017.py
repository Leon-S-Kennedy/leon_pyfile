#字符串函数
import numpy as np

#numpy.char.add() 函数依次对两个数组的元素进行字符串连接。
print(np.char.add(['abc'],['def']))
print(np.char.add(['123','456'],['abc','def']))

#numpy.char.multiply() 函数执行多重连接。
print (np.char.multiply('libowen ',3))

#numpy.char.center() 函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充。
print (np.char.center('libowen', 20,fillchar = '*'))

#numpy.char.capitalize() 函数将字符串的第一个字母转换为大写：
print(np.char.capitalize('aaaa'))

#numpy.char.title()函数将字符串的每个单词的第一个字母转换为大写
print (np.char.title('hello woeld'))

#numpy.char.lower() 函数对数组的每个元素转换为小写。它对每个元素调用 str.lower。
print (np.char.lower(['ABCDEFG','HIJKLMN']))

#numpy.char.upper() 函数对数组的每个元素转换为大写。它对每个元素调用 str.upper。
print (np.char.upper(['abcdefg','hijklmn']))

#numpy.char.split() 通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格。
print (np.char.split ('www.bilibili.com', sep = '.'))

#numpy.char.splitlines() 函数以换行符作为分隔符来分割字符串，并返回数组。\n，\r，\r\n 都可用作换行符。
print (np.char.splitlines('a\rbcdef'))

#numpy.char.strip() 函数用于移除开头或结尾处的特定字符。
print (np.char.strip(['apythona','admin','java'],'a'))

#numpy.char.join() 函数通过指定分隔符来连接数组中的元素或字符串
print(np.char.join([':',';'],['abcd','fegh']))

#numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串。
print(np.char.replace(['aooooob','deeeeeeeef'],['o','e'],['c','g']))

#numpy.char.encode() 函数对数组中的每个元素调用 str.encode 函数。 默认编码是 utf-8，可以使用标准 Python 库中的编解码器。
#numpy.char.decode() 函数对编码的元素进行 str.decode() 解码。
a = np.char.encode('runoob', 'cp500')
print (a)
print (np.char.decode(a,'cp500'))

