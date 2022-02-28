import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
from scipy import misc
im=plt.imread('face.png')
#plt.imshow(im[:,:,0],cmap=plt.cm.gray)
#plt.show()
#通过设置最小和最大值增加对比度
#plt.imshow(im[:,:,0],cmap=plt.cm.gray)
a=scipy.ndimage.gaussian_filter(im,sigma=3)
b=scipy.ndimage.gaussian_filter(im,sigma=5)
plt.figure(1)
plt.imshow(a)
plt.figure(2)
plt.imshow(b)
plt.show()

