#插值
import numpy as np
import scipy.interpolate as itp
import matplotlib.pyplot as plt
x=np.linspace(0,4,12)#在[0,12]生成12个间隔均匀的点
print(x)
y=np.cos(x**2/3+4)
print(y)
#绘制离散函数
plt.figure(1)
plt.plot(x,y,'o')

f1=itp.interp1d(x,y,kind='linear')
f2=itp.interp1d(x,y,kind='cubic')
xnew=np.linspace(0,4,30)

#绘制插值后的函数图像
plt.plot(xnew,f1(xnew),'-',xnew,f2(xnew),'--')
plt.legend(['data','linear','cubic'],loc='upper left')
plt.show()

