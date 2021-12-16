#使用print函数输出
a=open('D:\pythonFile\pywork\chap15\print.txt','a+',encoding='utf-8')
print('这句话用于演示print函数的作用',file=a)
a.close()
#使用上下文管理器
with open('D:\pythonFile\pywork\chap15\print.txt','w',encoding='utf-8')as file:
    file.write('这句话用于演示上下文管理器')

#更改控制台显示颜色
print('\033[1;33m这句话用来搞颜色\033[m')

#不同的进制表示以及格式化字符串
def f():
    num=int(input('请输入一个10进制的数：'))
    print(f'{num}的二进制数是{bin(num)}')
    print('{0}的八进制数是{1}'.format(num,oct(num)))
    print('%s的十六进制数是%s'%(num,hex(num)))

#演示一种正确输入的思路
'''
if __name__ == '__main__':
    try:
        f()
    except:
        print('报错')
        f()
'''
if __name__ == '__main__':
    while True:
        try:
            f()
            break
        except:
            print('报错请重输')
