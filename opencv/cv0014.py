#傅里叶变换
import numpy as np
import cv2
import matplotlib.pyplot as plt
im=cv2.imread('src00001.png',0)
#转换成float32形式
im_float32=np.float32(im)
dft=cv2.dft(im_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)
#得到灰度图能表示的形式
magnitude_spectrum1=20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

img=cv2.imread('dest00001.png',0)
#转换成float32形式
img_float32=np.float32(img)
dft2=cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift2=np.fft.fftshift(dft2)
#得到灰度图能表示的形式
magnitude_spectrum2=20*np.log(cv2.magnitude(dft_shift2[:,:,0],dft_shift2[:,:,1]))

plt.figure(1)
plt.subplot(221),plt.imshow(im,cmap='gray'),plt.title('input image1'),plt.axis('off')
plt.subplot(222),plt.imshow(magnitude_spectrum1,cmap='gray'),plt.title('magnitude_spectrum1'),plt.axis('off')
plt.subplot(223),plt.imshow(img,cmap='gray'),plt.title('input image2'),plt.axis('off')
plt.subplot(224),plt.imshow(magnitude_spectrum2,cmap='gray'),plt.title('magnitude_spectrum2'),plt.axis('off')

plt.show()

# #低通滤波
#
# #掩膜的生成（低通滤波）
# rows,cols=im.shape
# crows,ccols=int(rows/2),int(cols/2)#取中点
# mask=np.zeros((rows,cols,2),np.uint8)
# mask[crows-30:crows+30,ccols-30:ccols+30]=1#得到一个边长为60的值为1的窗口（边框是图像大小）
# #idft
# fshift=dft_shift*mask
# f_ishift=np.fft.ifftshift(fshift)#平移回去
#
# img_back=cv2.idft(f_ishift)
# #得到灰度图能表示的形式
# im_back=cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
#
# plt.figure(2)
# plt.subplot(121),plt.imshow(im,cmap='gray'),plt.title('input image'),plt.axis('off')
# plt.subplot(122),plt.imshow(im_back,cmap='gray'),plt.title('result'),plt.axis('off')
#
# '''
# 由此可见图像变模糊了，低通滤波器的作用就是滤除高频成分，即轮廓边界之类的
# '''
#
#
# #高通滤波器
# rows,cols=im.shape
# crows,ccols=int(rows/2),int(cols/2)#取中点
# mask=np.ones((rows,cols,2),np.uint8)
# mask[crows-30:crows+30,ccols-30:ccols+30]=0#得到一个边长为60的值为0的窗口（边框是图像大小）
# #idft
# fshift=dft_shift*mask
# f_ishift=np.fft.ifftshift(fshift)#平移回去
#
# img_back=cv2.idft(f_ishift)
# #得到灰度图能表示的形式
# im_back=cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
#
# plt.figure(3)
# plt.subplot(121),plt.imshow(im,cmap='gray'),plt.title('input image'),plt.axis('off')
# plt.subplot(122),plt.imshow(im_back,cmap='gray'),plt.title('Result'),plt.axis('off')
# plt.show()
# '''
# 只保留高频，图像的细节增强了。
# '''