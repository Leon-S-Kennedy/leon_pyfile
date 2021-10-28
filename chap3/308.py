#嵌套循环
#输出矩形
for i in range(1,4):
    for j in range(1,5):
        print('*',end="\t")#不换行输出
    print()#起换行的作用(很重要的哦)
#输出三角形
for a in range(2,11):
    for b in range(1,a):
        print('*',end="\t")#不换行输出
    print()
#输出九九乘法表
for a in range(2,11):
    for b in range(1,a):
        print(str(b)+'*'+str(a-1)+'='+str(b*(a-1)),end="\t")#不换行输出
    print('')
