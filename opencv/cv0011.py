#轮廓特征
import cv2
import numpy as np
imo=cv2.imread('dragonball.png')
imp=cv2.cvtColor(imo,cv2.COLOR_BGR2GRAY)#化为灰度图
re,thresh1=cv2.threshold(imp,127,255,cv2.THRESH_BINARY)#化为二值图像

c1,hierarchy1=cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
copyimo=imo.copy()#使用copy的原因是会改变原图像
res1=cv2.drawContours(copyimo,c1,-1,(0,0,255),3)
# cv2.imshow('copyimo',res1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cnt=c1[0]
print(type(cnt),cnt.shape)

#计算周长
i1=cv2.arcLength(cnt,True)
print(i1)

#计算面积
i2=cv2.contourArea(cnt)
print(i2)

