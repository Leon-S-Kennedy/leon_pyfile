#绘制三维折线图
from matplotlib import pyplot as plt

#生成3d窗
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
#传入数据参数
a,b,c=[1,2,3,4,5,6,7,8,9,10],[5,6,3,13,4,1,2,4,8,7],[2,1,3,4,5,6,7,8,4,5]

ax.plot(a,b,c)

plt.show()
