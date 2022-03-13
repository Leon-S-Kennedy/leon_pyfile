#图像轮廓
import cv2
import numpy as np
'''
cv2.findContours(img,mode,method)
mode:常用RETR_TREE
method:轮廓逼近方法
'''
img=cv2.imread('D:\pythonFile\pywork\scipy\pikapika.png')
im=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#化为灰度图
ret,thresh=cv2.threshold(im,127,255,cv2.THRESH_BINARY)#化为二值图像



c,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(type(c),type(hierarchy))

copyimg=img.copy()#使用copy的原因是会改变原图像
res=cv2.drawContours(copyimg,c,-1,(255,255,255),2)
'''
-1表示把所有轮廓画进去
（255，255，255）轮廓线颜色的bgr的格式
2表示线条的宽度
'''

cv2.imshow('copyimg',copyimg)#copy图像被改变了
cv2.waitKey(0)
cv2.destroyAllWindows()

