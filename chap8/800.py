#函数的创建和调用
def calc(a,b):#a,b称为形式参数，简称形参（位于函数的定义处）
    c=a+b
    return c
s=calc(10,20)#10，20称为实参（位置位于函数的调用处）
print(s)

#函数的参数传递
#位置实参，根据形参对应的位置进行传递
'''如上所示'''

#关键字实参，根据形参名称进行实参传递
res=calc(b=10,a=20)#等号左侧变量的名字称为关键字参数
print(res)

#函数的参数传递的内存分析
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    print(id(arg1),id(arg2))
    arg1=100
    arg2.append(10)
    print(id(arg1),id(arg2))
    print('arg1',arg1)
    print('arg2',arg2)
n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
print(id(n1),id(n2))
fun(n1,n2)#位置传参
print(id(n1),id(n2))
print('n1',n1)
print('n2',n2)
'''arg1,arg2是函数定义处的形参，n1,n2是函数调用处的实参，由此可见实参名称与形参名称可以不同'''
'''由地址的值可以看出
如果是不可变对象，在函数体的修改不会影响实参的值
如果是可变对象，在函数体内的修改会影响到实参的值
'''



