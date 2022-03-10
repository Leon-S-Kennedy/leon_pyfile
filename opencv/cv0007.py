#图像梯度
import cv2
import numpy as np
'''
sobel算子      Gx=[[-1,0,+1],[-2,0,+2],[-1,0,+1]]
              Gy=Gx.T
'''
im=cv2.imread('face_gray.png')
sobelx=cv2.Sobel(im,cv2.CV_64F,1,0,3)
sobelx=cv2.convertScaleAbs(sobelx)

sobely=cv2.Sobel(im,cv2.CV_64F,0,1,3)
sobely=cv2.convertScaleAbs(sobely)

sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
cv2.imshow('sobel',sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
不建议直接计算，效果没有分别计算效果好
'''
sobelxy1=cv2.Sobel(im,cv2.CV_64F,1,1,3)
sobelxy1=cv2.convertScaleAbs(sobelxy1)
cv2.imshow('sobel1',sobelxy1)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
scharr算子        Gx=[[-3,0,+3],[-10,0,+10],[-3,0,+3]]
                 Gy=Gx.T
相对sobel算子具有更丰富的细节信息
'''

'''
laplacian算子     G=[[0,1,0],[1,-4,1],[0,1,0]]
对噪音点比较敏感，一般不单独使用
'''
la=cv2.Laplacian(im,cv2.CV_64F,ksize=3)
la=cv2.convertScaleAbs(la)
cv2.imshow('la',la)
cv2.waitKey(0)
cv2.destroyAllWindows()
