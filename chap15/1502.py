#手动抛出异常
try:
    s=int(input('请输入分数：'))
    if 0<s<=100:
        print('分数为',s)
    else:
        raise Exception('分数不正确')#raise Exception用于手动抛出异常
except Exception as e:
    print(e)
