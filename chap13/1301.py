#读取磁盘文件中的内容
#file=open(文件名[,mode,encoding])#默认模式为只读，默认文本文件中的字符编码为GBk
file=open('a.txt','r')
print(file.readlines())
file.close()
