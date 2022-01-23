#matplotlib的基本作图以及基本操作
from matplotlib import pyplot as plt

x=range(6)
phase_spectrum=[11,17,29,42,50,53]
amplitude_spectrum=[12,22,28,24,19,17]
#设置图片的大小
plt.figure(figsize=(8,6),dpi=80)#figsize调整图片的大小，图像模糊时传入dpi参数，让图像更加清晰

plt.plot(x,phase_spectrum,label='phase spectrum')#传入数据，绘制图形
plt.plot(x,amplitude_spectrum,label='amplitude spectrum')
plt.xlabel('times of up-sampling')
plt.ylabel('average value of pixel difference')
plt.legend()
#plt.title('温度变化情况')

#设置x轴y轴的刻度
# plt.xticks(x)#参数为可迭代对象
# plt.yticks(range(min(y),max(y)+1))#参数为可迭代对象
#
# plt.savefig('D:\pythonFile\pywork\matplotlib\chap0\plot0.png')#可以保存.svg矢量图的格式，放大不会有锯齿。

plt.show()#展示图形


