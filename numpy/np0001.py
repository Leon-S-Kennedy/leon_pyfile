#numpy数据类型
#numpy 的数值类型实际上是 dtype 对象的实例，并对应唯一的字符，包括 np.bool_，np.int32，np.float32，等等。
import numpy as np
# 使用标量类型
dt1=np.dtype(np.int64)
print(dt1)

# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt2 = np.dtype('i4')
print(dt2)
print('---------------------------------------------')
f=np.arange(10)
print(f)
print(f.dtype)
print('-----------------------------------------------')
#创建结构化数据类型
dt3 = np.dtype([('age',np.int8)])
print(dt3,type(dt3))

# 类型字段名可以用于存取实际的 age 列
dt4 = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt4)
print(a['age'])

#定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a,type(a))

t5=np.array([1,2,3,4,5,0,0,0],dtype=bool)
print(t5)
print(t5.dtype)
#调整数据类型
t6=t5.astype('i1')
print(t6)
print(t6.dtype)
