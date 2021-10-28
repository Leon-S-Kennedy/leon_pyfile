#continue(流程控制语句)
#用于结束当前循环进入下一个循环通常与分支结构的if一起使用
print("--------输出1到50之间的所有5的倍数---------")
for i in range(1,51):
    if i%5==0:
        print(i)

for j in range(1,51):
    if j%5!=0:
        continue
    print(j)

for k in range(1,51):
    if k%5!=0:
        pass
    else:
        print(k)