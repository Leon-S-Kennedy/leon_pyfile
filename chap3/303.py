#for_in 循环
#in表示从（字符串、序列等）中依次取值，又称遍历
#for_in遍历的对象必须是可迭代对象

#字符串是可迭代对象
for a in "python":
    print(a)

#range()产生的整数序列也是一个可迭代对象
for b in range(10):
    print(b)

#循环体中不需要使用到自定义变量可以用_代替
for _ in "123456789":
    print('人生苦短，我用python')

print('使用for循环计算1到100的偶数和')
s=0
for i in range(0,101,2):
    s+=i
print("0到100的偶数和为：",s)

