#直方图的生成
from matplotlib import pyplot as plt
import numpy as np
x=np.random.randint(0,11,50)#随机生成50个0到10之间的随机数
print(x)

plt.figure(1)

res=plt.hist(x,bins=5)#bins的值可以为整数序列或字符串，整数表示等宽区间的个数，序列则表示区间的范围（均含左不含右）
#density=True的话表示返回的是归一化的概率密度，所有区间的概率和为1
#cumulative=True表示累加求和

print(res)#由此可见其返回值为一个元组

plt.show()
