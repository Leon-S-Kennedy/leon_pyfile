#else
#if_else是当if的条件不成立时执行else
#while_else以及for_else没有碰到break时循结束执行else
for i in range(1,4):
    password=input('请输入密码：')
    if password =="anykey":
        print('恭喜你，密码正确')
        break
    else:
        b=3-i
        print("密码错误你还有"+str(b)+"次机会")if b>0 else print('你没了')
else:
    print('游戏结束')
    