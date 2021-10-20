#input函数
#作用是接受来自用户的输入
#输入值的类型是str
#使用=对输入的值进行储存
a=input()
print(int(a)*int(a))
b=input("魔镜啊魔镜，谁是这个世家上最漂亮的女人？\n")
print('是白雪公主')
print(input(''))

c=input('请输入一个数字:\n')
d=input('请输入另外一个数:\n')
print('两个数的和是',float(c)+float(d))
print(c+d,'如果不改变数据类型，这个结果就是把两个str连接起来')

#或者在输入时就转换数据类型，即c=float(input())

