#形态学操作

#腐蚀操作(黑的腐蚀白的)
import cv2
import numpy as np
im=cv2.imread('triangle.png')#这个例子膨胀的结果类似于腐蚀，腐蚀的结果类似于膨胀
print(im,im.shape)
# cv2.imshow('triangle',im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

kernel=np.ones([5,5],np.uint8)#kernel可以自己写，也可以生成
erosion=cv2.erode(im,kernel,iterations=5)
'''
kernel：腐蚀操作的核，通常这个参数由函数getStructuringElement得到（稍后会讲）
iterations：自身迭代的次数，默认值为1
'''
# cv2.imshow('erosion',erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#膨胀操作
# kernel1=np.ones([3,3])
# dilate=cv2.dilate(im,kernel1,iterations=15)
# cv2.imshow('dilate',dilate)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#开运算，先腐蚀，再膨胀        它具有消除细小物体，在纤细处分离物体和平滑较大物体边界的作用。
#闭运算，先膨胀，再腐蚀        它具有填充物体内细小空洞，连接邻近物体和平滑边界的作用。

#下面演示下去个毛刺
kernel2=np.ones([5,5])
# closing=cv2.morphologyEx(im,cv2.MORPH_CLOSE,kernel2)
# cv2.imshow('closing',closing)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#梯度运算
#梯度=膨胀-腐蚀（得到轮廓信息）
kernel3=np.ones([7,7])
# gradient=cv2.morphologyEx(im,cv2.MORPH_GRADIENT,kernel3)
# cv2.imshow('gradient',gradient)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#礼帽与黑帽
#礼帽=原始输入-开运算结果
#黑帽=闭运算结果-原始输入

#礼帽
kernel4=np.ones([3,3])
# tophat=cv2.morphologyEx(im,cv2.MORPH_TOPHAT,kernel4)
# cv2.imshow('tophat',tophat)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#黑帽
kernel5=np.ones([5,5])
blackhat=cv2.morphologyEx(im,cv2.MORPH_BLACKHAT,kernel5)
cv2.imshow('blackhat',blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()

