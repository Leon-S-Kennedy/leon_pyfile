#os模块的常用函数
import os
#os.system('notepad.exe')
#os.system('calc.exe')
#直接调用可执行文件
#os.startfile("D:\XMind\XMind.exe")#转义字符不要忘哦，好像不加也可以。
#os.startfile("D:\pythonFile\pywork\chap13\os_function.png")

#   getcwd()返回当前的工作目录
print(os.getcwd())

#   listdir(path)返回指定路径下的文件和目录信息
lst=os.listdir('../chap13')#返回上级目录
print(lst)

#   mkdir()创建目录
#os.mkdir('newdir')#当文件已存在时会报错

#   makedirs()创建多级目录
#os.makedirs('A/B/C')

#删除目录
#os.rmdir('newdir2')
#os.removedirs('A/B/C')

#   chdir()将path设置为当前工作目录
os.chdir('D:\pythonFile\pywork\chap13')
print(os.getcwd())
