#python的异常处理机制
#try except else结构
#如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
try:
    a = int(input('请输入第一个数'))
    b = int(input('请输入第二个数'))
    result = a / b
except ZeroDivisionError as c:
    print('???',c)
except ValueError as d:
    print("???",d)
else:
    print('结果为',result)
