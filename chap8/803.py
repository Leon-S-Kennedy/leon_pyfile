#函数的参数总结
#使用*list将序列中的每个元素都转换为位置实参
def fun(a,b,c):
    print(a)
    print(b)
    print(c)
fun(10,20,30)
lst=[11,22,33]
fun(*range(0,3))

#使用**dict将字典中的每个键值对都转换成为关键字实参
fun(a=100,c=300,b=200)
dic={'a':100,'b':200,'c':300}
fun(**dic)

def fun1(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

fun1(10,20,c=30,d=40)
print('----------如何让c和d只能采用关键字实参传递-----------')
def fun1(a,b,*,c,d):#*之后的形参在函数调用时只能采用关键字传递，我们称这样的形参为关键字形参
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
fun1(10,20,c=30,d=40)

def f5(a,b,*,c,d,**args):
    pass

def f6(*args,**args2):
    pass

def f7(a,b=10,*c,d,**arg2):
    pass

