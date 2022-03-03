#图片的读取
#opencv默认读取格式是BGR格式
import cv2
import matplotlib.pyplot as plt
import numpy as np
im=cv2.imread('D:\\pythonFile\\pywork\\scipy\\face.png')
print(im,type(im),im.shape)
cv2.imshow('figure1',im)
cv2.waitKey(0)#零表示任意键终止，其他数值表示多少毫秒关闭窗口。

def cv_show(name,im):
    cv2.imshow(name,im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#cv_show('figure2',im)
print(im.shape)#输出图像的[h,w,c]（数组的z,y,x）

#读取灰度图像
im1=cv2.imread('D:\\pythonFile\\pywork\\scipy\\face.png',cv2.IMREAD_GRAYSCALE)#此时读取灰度图像
cv_show('figure3',im1)
print(im1.shape)

#图像的保存
cv2.imwrite('face_gray.png',im1)
print(type(im1))
print(im1.size)
