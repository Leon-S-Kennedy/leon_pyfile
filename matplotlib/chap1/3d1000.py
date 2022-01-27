#绘制3维散点图
import matplotlib.pyplot as plt
#生成3d窗
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#传入数据参数
a =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b =[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
c =[100, 300, 500, 220, 123, 234, 456, 234, 111, 213]
ax.scatter(a, b, c, marker='<')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
