#break的使用
#break(用于结束循环结构，通常与分支结构if一起使用)
for i in range(1,4):
    password=input('请输入密码：')
    if password =="anykey":
        print('恭喜你，密码正确')
        break
    else:
        b=3-i
        print("密码错误你还有"+str(b)+"次机会")if b>0 else print('你没了')

#用于while循环时
a=0
while a<3:
    pw=input("请输入密码：")
    if pw =="anykey":
        print('恭喜你，密码正确')
        break
    else:
        c=2-a
        print("密码错误你还有"+str(c)+"次机会")if c>0 else print('你没了')
    a+=1
