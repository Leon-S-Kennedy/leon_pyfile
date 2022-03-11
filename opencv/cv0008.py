#边缘检测
import cv2
import numpy as np
'''
Canny边缘检测
（1）高斯滤波，平滑图像，滤除噪声
（2）计算每个像素点的梯度强度和方向           
（3）对梯度图像进行非极大值抑制
（4）使用双阈值确定最真实的边界
    （5）抑制孤立的弱边缘最终完成边缘检测
'''
im=cv2.imread('face_gray.png')
c1=cv2.Canny(im,80,150)
c2=cv2.Canny(im,125,127)
res=np.hstack((c1,c2))
cv2.imshow('vs',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
