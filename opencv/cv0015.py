import numpy as np
import cv2
from matplotlib import pyplot as plt
# 读取图像
img = cv2.imread('dest00001.png', 0)
# 傅里叶变换
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(dft)
res1 = 20 * np.log(cv2.magnitude(dftshift[:, :, 0], dftshift[:, :, 1]))

# 读取图像
im = cv2.imread('src00001.png', 0)
# 傅里叶变换
dft2 = cv2.dft(np.float32(im), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift2 = np.fft.fftshift(dft2)
res2 = 20 * np.log(cv2.magnitude(dftshift2[:, :, 0], dftshift2[:, :, 1]))


# 显示图像
plt.subplot(121), plt.imshow(res2, 'gray'), plt.title('Original Image')
plt.axis('off')
plt.subplot(122), plt.imshow(res1, 'gray'), plt.title('Fourier Image')
plt.axis('off')
plt.show()