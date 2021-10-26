# 选择结构
# 单分支结构
money = 1000
a = int(input("请输入您的取款金额"))
if money >= a:
    money = money - a
    print("取款成功余额为", money)

#双分支结构
num=int(input('请输入一个整数'))
if num%2==0:
    print(num,'是偶数')
else:
    print(num,"是奇数")

#多分支结构
score=int(input("请输入你的成绩："))
if score>=90 and score <=100:
    print("你的成绩是A级")
elif score >= 80 and score <= 89:
        print("你的成绩是B级")
elif score >= 70 and score <= 79:
        print("你的成绩是c级")
elif score >= 60and score <= 69:
        print("你的成绩是D级")
elif score >= 0and score <= 59:
        print("你的成绩是E级")
else:
    print("你输的是个啥？？？")
