#os.path模块操作目录相关函数
import os#此处不需要.path(可以但没必要)

#获取文件或目录的绝对路径
print(os.path.abspath('1307.py'))

#判断文件或目录是否存在，存在返回True，不存在返回False
print(os.path.exists('1307.py'),os.path.exists('1308.py'))

#分离目录和文件名
print(os.path.split("D:\\pythonFile\\pywork\\chap13\\1307.py"))#此处是数字之间的转义字符，不加会搞错

#分离文件和扩展名
print(os.path.splitext("1307.py"))

#从一个目录之中提取文件名
print(os.path.basename("D:\\pythonFile\\pywork\\chap13\\1307.py"))

#从一个路径之中提取文件路径，不包括文件名
print(os.path.dirname("D:\\pythonFile\\pywork\\chap13\\1307.py"))

#用于判断是否为路径
print(os.path.isdir("D:\\pythonFile\\pywork\\chap13\\"))
