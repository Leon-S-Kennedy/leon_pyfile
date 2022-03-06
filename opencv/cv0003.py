#边界填充
import numpy as np
import cv2
import matplotlib.pyplot as plt
im=cv2.imread(r'D:\pythonFile\pywork\scipy\face.png')

#指定边界的大小，a，b，c，d分别代表了上下左右的边界大小
a,b,c,d=100,100,100,100

#指定填充的模式
replicate=cv2.copyMakeBorder(im,a,b,c,d,borderType=cv2.BORDER_REPLICATE)#复制最边缘像素
reflect=cv2.copyMakeBorder(im,a,b,c,d,borderType=cv2.BORDER_REFLECT)#反射边缘的像素
reflect101=cv2.copyMakeBorder(im,a,b,c,d,borderType=cv2.BORDER_REFLECT_101)#反射边缘的像素
wrap=cv2.copyMakeBorder(im,a,b,c,d,borderType=cv2.BORDER_WRAP)#外包装法，重复图像
constant=cv2.copyMakeBorder(im,a,b,c,d,borderType=cv2.BORDER_CONSTANT,value=[0,0,255])#常数位填充

#用subplot画出图像进行比较
plt.subplot(2,3,1),plt.imshow(im),plt.title('ORIGINAL')
plt.subplot(2,3,2),plt.imshow(replicate),plt.title('replicate')
plt.subplot(2,3,3),plt.imshow(reflect),plt.title('reflect')
plt.subplot(2,3,4),plt.imshow(reflect101),plt.title('reflect101')
plt.subplot(2,3,5),plt.imshow(wrap),plt.title('wrap')
plt.subplot(2,3,6),plt.imshow(constant),plt.title('constant')
plt.show()


