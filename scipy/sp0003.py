#快速傅里叶变换
import numpy as np
import scipy.fftpack as fftp
np.random.seed(0)
i=np.random.uniform(-10,10,5)
print(i)
print('---------------------------------------')
#对数组进行快速傅里叶变换
y=fftp.fft(i)
print(y)
print('----------------------------------------')
#快速傅里叶反变换
z=fftp.ifft(y)
print(z)

#离散余弦变换(略)

