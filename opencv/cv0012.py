import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
#模板匹配
模板在原图像上滑动，计算模板与原图的差别程度
'''
im=cv2.imread('D:\pythonFile\pywork\scipy\pikapika.png')
temppika=cv2.imread('temppika.png')
h,w=temppika.shape[:2]
print(temppika.shape)
print(h,w)

res=cv2.matchTemplate(im,temppika,cv2.TM_SQDIFF)
print(res.shape)

min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)

print(min_loc)
img=im[273:403,167:269,:]
# vs=np.hstack((temppika,img))
#cv2.imshow('vs',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
