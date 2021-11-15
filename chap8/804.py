#变量的作用域（程序代码能访问该变量的区域）
#根据变量的有效范围可以分为’局部变量‘和’全局变量‘
#函数内部通过global可以将局部变量变成全局变量
def fun():
    age=21
    print(age)
fun()
#print(age)
def fun():
    global age
    age=21
    print(age)
fun()
print(age)


