#函数的参数定义

#定义默认值参数
def fun(a,b=10):#a没有指定默认值，b的默认值为10
    print(a,b)
fun(100)#此时会将100传递给a,b使用默认值10
fun(20,30)
print()#选中函数按ctrl+b查看函数源码

#个数可变的位置参数(只能定义1个)
#定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
#使用*定义个数可变的位置形参
#结果为一个元组
def fun1(*args):
    print(args)
fun1(10)
fun1(100,200)

#个数可变的关键字形参（只能定义1个）
#定义函数时，无法事先确定传递的关键字实参的个数时，使用可变的关键字形参
#使用**定义个数可变的关键字形参
#结果为一个字典
def fun2(**args):
    print(args)
fun2(a=10)
fun2(a=100,b=200,c=300)

#在函数的定义过程中，既有“*”又有“**”时，要求“*”放在“**”之前。