#图像模糊
import cv2
import numpy as np
im=cv2.imread(r'D:\pythonFile\pywork\scipy\face.png')
'''
均值滤波，原理不解释，卷积核越大越模糊，在图像去噪的同时也破坏了图像的细节部分
'''
blur=cv2.blur(im,(7,7))
cv2.imshow('blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
方框滤波，和均值基本一样，可选择是否归一化,normalize默认为True，为False时不进行归一化
'''
box=cv2.boxFilter(im,-1,(9,9),normalize=True)#ddepth输出图像的深度，-1代表使用原图深度
cv2.imshow('box',box)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
高斯滤波，卷积核的数值满足高斯分布，更重视中间的内容
'''
gauss=cv2.GaussianBlur(im,(5,5),1)#1表示高斯核函数在X方向的的标准差
cv2.imshow('gauss',gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
中值滤波，用中值代替，不解释
'''
median=cv2.medianBlur(im,5)#（5，5）可以用单个5表示,以上的不可以这样操作
cv2.imshow('median',median)
cv2.waitKey(0)
cv2.destroyAllWindows()

#对比或展示多个图片
'''
可以根据numpy的数组堆叠实现
'''
res=np.hstack((blur,gauss))
cv2.imshow('vs',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
