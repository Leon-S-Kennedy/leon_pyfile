#python中的异常处理机制
#try except else finally结构
#finally块无论是否发生异常都会被执行，能常用来释放try块之中的申请的资源
try:
    a = int(input('请输入第一个数'))
    b = int(input('请输入第二个数'))
    result = a / b
    print(result)
except ZeroDivisionError as c:
    print('???',c)
except ValueError as d:
    print("???",d)
else:
    print('结果为',result)
finally:
    print('谢谢使用，喵')
