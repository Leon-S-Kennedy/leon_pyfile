#图像阈值
import cv2
import matplotlib.pyplot as plt
'''
ret,dst=cv2.thresold(src,thres,maxval,type)
其返回值是一个元组，后一个元素才是需要的输出图像
dst                         输出图像
src                         输入图像，通常来说是灰度图
thresh                      阈值
maxval                      一个参数
type                        二值化操作类型
cv2.THRESH_BINARY           超过部分取maxval，其他取0
cv2.THRESH_BINARY_INV       前一个的反转
cv2.THRESH_TRUNC            大于阈值设为阈值，其他不变
cv2.THRESH_TOZERO           大于阈值不改变，其他设为0
cv2.THRESH_TOZERO_INV       前一个的反转
'''
im0=cv2.imread('face_gray.png')
ret1,im1=cv2.threshold(im0,127,255,cv2.THRESH_BINARY)
ret2,im2=cv2.threshold(im0,127,255,cv2.THRESH_BINARY_INV)
ret3,im3=cv2.threshold(im0,127,255,cv2.THRESH_TRUNC)
ret4,im4=cv2.threshold(im0,127,255,cv2.THRESH_TOZERO)
ret5,im5=cv2.threshold(im0,127,255,cv2.THRESH_TOZERO_INV)

#使用for循环实现subplot
titles=['original','binary','binary_inv','trunc','tozero','tozero_inv']
images=[im0,im1,im2,im3,im4,im5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.axis('off')
plt.show()
