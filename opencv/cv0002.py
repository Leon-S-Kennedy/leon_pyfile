#图像截取
import cv2
import numpy as np
import matplotlib.pyplot as plt
im=cv2.imread('face_gray.png')
im1=im[0:200,:]
#cv2.imshow('capture',im1)
#cv2.waitKey(0)

#颜色通道提取
im2=cv2.imread(r'D:\pythonFile\pywork\scipy\face.png')
b,g,r=cv2.split(im2)
print(b,type(b),b.shape)
def blue(im):
    copy_im=im.copy()
    copy_im[:,:,1]=0
    copy_im[:,:,2]=0
    cv2.imshow('blue',copy_im)
    cv2.waitKey(0)
def green(im):
    copy_im=im.copy()
    copy_im[:,:,0]=0
    copy_im[:,:,2]=0
    cv2.imshow('green',copy_im)
    cv2.waitKey(0)
def red(im):
    copy_im=im.copy()
    copy_im[:,:,0]=0
    copy_im[:,:,1]=0
    cv2.imshow('red',copy_im)
    cv2.waitKey(0)
blue(im2)
green(im2)
red(im2)