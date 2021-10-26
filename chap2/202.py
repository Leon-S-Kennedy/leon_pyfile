#嵌套if的使用
a=int(input('请输入你的消费金额'))
if input("是否有会员卡？如果有请回答y")=='y':

    if a>=200:
        print ('你可以享受8折优惠')
    elif a>=100:
        print('你可以享受9折优惠')
    elif a>0:
        print('你没有优惠哦亲')
    else:
        print('???')
elif a>=200:
    print('你可以享受9折优惠')
else:
    print('要不要考虑充个会员啊亲')

#条件表达式
num=int(input('请输入一个[0,10]的整数'))
print('你输入的数字在区间内') if 0<=num<=10 else print('你输入的数字不在区间内')