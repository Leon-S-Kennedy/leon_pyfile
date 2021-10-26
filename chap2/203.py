#pass语句
#当你不知道程序怎么写的时候可以先写一个pass占用位置，这样程序语法并不会报错
if int(input("输入大于10的整数"))>10:
    pass
else:
    print('你输入错了')
#由于一切皆对象，对象都有Bool值，所以对象可以直接用在if后作条件判断
i=int(input('请输入一个非零整数'))
if i:
    print (i)
else:
    print('你输入的是0')
