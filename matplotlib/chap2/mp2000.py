#绘制条形图
from matplotlib import pyplot as plt

a=['a','b','c','d','e','f','g','h','i','j']
b=[11,33,55,77,99,111,222,333,444,555]

#使用plt.figure(名称)独立显示多幅图片
plt.figure(1)
plt.bar(a,b,width=0.3)#竖向显示时用width设置条的宽度

plt.figure(2)
plt.barh(a,b,height=0.3)#横向显示时用height设置条的宽度

plt.show()

