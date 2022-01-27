#散点图的绘制
from matplotlib import pyplot as plt
plt.rcParams['font.family']=['STFangsong']

x1=range(25)
x2=range(30,55)
y1=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15]
y2=[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17]

plt.scatter(x1,y1,label='3月份')
plt.scatter(x2,y2,label='十月份')
plt.title('标题')
plt.xlabel('时间')
plt.ylabel('温度')

plt.legend(loc='upper left')

plt.show()