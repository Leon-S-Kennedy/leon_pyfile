from matplotlib import pyplot as plt
#设置字体
plt.rcParams['font.family']=['STFangsong']

x=range(1,11)
y1=[2,3,5,7,2,4,6,1,8,3]
y2=[6,2,3,4,2,5,2,4,6,5]

plt.figure()

#设置x轴y轴的刻度
plt.xticks(x)

#设置坐标轴的标签
plt.title('title')
plt.xlabel('时间')
plt.ylabel('温度 单位(℃)')

plt.plot(x,y1,label='y1',c='pink',linestyle='-.',linewidth=5,alpha=0.9)#指定线的风格
plt.plot(x,y2,label='y2',c='green')

#添加图例
plt.legend()

#添加网格
plt.grid(alpha=0.5)

plt.show()
