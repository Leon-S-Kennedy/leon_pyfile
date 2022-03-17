#直方图
import cv2
import numpy as np
import matplotlib.pyplot as plt
im=cv2.imread('face_gray.png',0)#0表示灰度图
'''
calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) 
images参数表示输入图像，传入时应该用中括号[ ]括起来

channels参数表示传入图像的通道，如果是灰度图像，那就不用说了，只有一个通道，值为0，
如果是彩色图像（有3个通道），那么值为0,1,2,中选择一个，对应着BGR各个通道。这个值也得用[ ]传入。

mask参数表示掩膜图像。如果统计整幅图，那么为None。
主要是如果要统计部分图的直方图，就得构造相应的掩膜来计算。

histSize参数表示灰度级的个数，需要中括号，比如[256]

ranges参数表示像素值的范围，通常[0,256]。此外，假如channels为[0,1],ranges为[0,256,0,180],
则代表0通道范围是0-256,1通道范围0-180。

hist参数表示计算出来的直方图。
'''

#hist=cv2.calcHist([im],[0],None,[256],[0,256])
#print(hist.shape)
plt.hist(im.ravel(),256,[0,256]),plt.show()
'''
#ravel函数功能是将多维数组降为一维数组,统计各个bin的频次，256：bin的个数，[0, 256]：范围
'''
print(im.shape)


#直方图均衡化
eq=cv2.equalizeHist(im)
plt.hist(eq.ravel(),256,[0,256]),plt.show()

res=np.hstack((im,eq))
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#自适应直方图均衡化
clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
res_clahe=clahe.apply(im)
cv2.imshow('res',res_clahe)
cv2.waitKey(0)
cv2.destroyAllWindows()
