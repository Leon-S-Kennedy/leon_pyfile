#print的用法

#输出数字
print(13227677101)

#输出字符串
print("单引号、双引号都可以")

#输出含有运算符的表达式
print(4*5+1)

#将数据输出到文件中
fp=open('D:/text.txt','a+')#a+不存在就创建，存在就追加
print('黑化肥挥发会发灰',file=fp)
fp.close()

#不进行换行输
print('hello','world')
