#函数的返回值
def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
list=[1,2,3,4,5,6,7,8,9,0]
print(fun(list))
'''
1、如果函数没有返回值（函数执行完毕后，不需要给调用处提供数据）return可以省略不写
2、函数的返回值如果是1个，直接返回原类型
3、函数的返回值如果是多个，返回值是元组
'''
