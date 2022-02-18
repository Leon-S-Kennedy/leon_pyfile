#scipy常量
import  scipy.constants as ct
print(ct.c)#真空中的光速
print(ct.e)#基本电荷
print(ct.golden)#黄金分割数
print(ct.h)#普朗克常数
print(ct.G)#万有引力系数
print(ct.Avogadro)#阿伏伽德罗常数
print(ct.k)#玻尔兹曼常量

#查找常量
print(ct.find('bolt'))
#获取常量
print(ct.physical_constants['Boltzmann constant'])
