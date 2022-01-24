from matplotlib import pyplot as plt
import random
x=range(120)
y=[random.randint(20,35)for i in range(120)]

#设置中文字体
plt.rcParams['font.family']=['STFangsong']

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#设置坐标轴的刻度为字符串
a=[f'10点{i}分'for i in range(60)]
a+=[f'11点{i}分'for i in range(60)]
plt.xticks(x[::5],a[::5],rotation=45)#通过切片的方式修改步长,rotation=90表示刻度名旋转90度

#添加描述信息
plt.xlabel('时间')
plt.ylabel('温度 单位(℃)')
plt.title('温度变化情况')

#添加网格
plt.grid(alpha=0.5)#alpha=0.9表示透明度为多少
plt.show()


