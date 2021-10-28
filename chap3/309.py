# 二重循环之中的break和continue用于控制本层循环
for i in range(5):
    for j in range(11):
        if j % 2 == 0:
            continue
        print(j,end='\t')
    print()
