#python中的异常处理机制
# print('---------------------')
# a=int(input('请输入第一个数'))
# b=int(input('请输入第二个数'))
# result=a/b
# print(result)
# print('---------------------')
#try except结构
try:
    a = int(input('请输入第一个数'))
    b = int(input('请输入第二个数'))
    result = a / b
    print(result)
except ZeroDivisionError:
    print('????')
except ValueError:
    print('????')
print('程序结束')
