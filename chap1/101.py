#python中常见的运算符

#算术运算符（标准算术、取余、幂运算）
print(1+1,2*3,9-5,9/7)
print(9//2)#整除运算
print(9%2)#取余运算符
print(2**8)#幂运算符
#含负数的整除取余运算
print(9//-4)
print(-9%4)

#赋值运算符，执行顺序为从右到左
#链式赋值
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))

#参数赋值
i=1
i+=1
print(i)

j=10
j-=1
print(j)

k=2
k*=8
print(k)

l=9
l/=2
print(l)

m=48.7851
m//=3
print(m)

n=2
n**=8
print(n)

o=9
o%=2
print(o)

#系列解包赋值
x,y,z=7,8,9
print(x,y,z)
#交换两个变量的值
a1=10
b1=20
print('交换变量之前',a1,b1)
a1,b1=b1,a1
print('交换变量之后',a1,b1)

#比较运算符(结果是bool类型)
#>,<,>=,<=,!=,==(比较的是对象的值)
d,e=10,20
print(d>e)
print(d!=e)
#is,is not(比较的是对象的标识(地址))
f=12
g=12
print(f==g,f is g)#都是Ture表示f和g的值与标识都相同
#以下结果表明
list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1==list2,list1 is list2,list1 is not list2)
print(id(list1),id(list2))

#bool运算符
#and,or,not,in,not in(与，或，非，字符串在其中，字符串不在其中)
p="17898151"
q="898"
print(q in p)

#位运算符
#按位与&：对应位数都是1结果位数才是1，否则是0
#按位或|：对应位数都是0结果位数才是0，否则是1
#<<左移位运算符，高位溢出舍弃，低位补0
#>>右移位运算符，低位溢出舍弃，高位补0
print(0b00000100&0b00001000)
print(0b00000100|0b00001000)
print(0b00000100<<2)
print(0b00000100>>1)

#运算符的优先级
#(有括号先算括号)--算术运算符--位运算符（左右移位、按位与、按位或）--比较运算符--布尔运算符--赋值运算符

