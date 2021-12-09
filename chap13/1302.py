#文件的类型按文件中数据的组织形式，文件分为以下两大类
    #文本文件：储存的是普通字符文本，默认为Unicode字符集，可以使用记事本程序打开
    #二进制文件：把数据内容用字节进行储存，无法用记事本打开，必须使用专用的软件打开例如.mp3.jpg.doc等

#常用的文件打开模式

#   r表示以只读模式打开文件，文件的指针将会放在文件的开头
file=open('a.txt','r')
print(file.readlines())
file.close()

#   w表示以只写模式打开文件，文件不存在则创建，文件存在则覆盖原有内容，文件指针在文件开头
fileb=open('b.txt','w')
fileb.write('八百标兵奔北坡')
fileb.close()

#   a表示以追加模式打开文件，如果文件不存在则创建，文件指针在文件的开头，如果文件存在，则在文件的末尾添加内容，文件指针在原文件末尾
filec=open('b.txt','a')
filec.write('告辞')
filec.close()

#   b表示以二进制的方式打开文件，不能单独使用，需要与其他的模式一起使用，如rb,wb
filed=open('pika.jpg','rb')
filee=open('copy_pika.png','wb')
print(filee.write(filed.read()))#一边读一边写，达成复制
filed.close()
filee.close()

#   +表示以读写方式打开文件，不能单独使用，需要和其他模式一起使用如a+
