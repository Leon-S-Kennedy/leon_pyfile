#100到999之间的水仙花数
for i in range(100,1000):
    a = 0
    for j in str(i):
        b=int(j)**3
        a+=b
    if a==i:
        print(a)
"""注意当循环嵌套时，存放结果的变量的位置不可弄错，容易出现内层循环时变量未初始化的情况"""
