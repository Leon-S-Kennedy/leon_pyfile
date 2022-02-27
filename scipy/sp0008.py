#图像处理
import PIL.Image as pl
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

f=misc.face()#导入图片的三维数组形式
print(f,type(f),f.shape)

plt.figure()#打开一个图片窗口
plt.imshow(f)#将三维数组绘制成图片

'''
使用PIL.Image将三维数组形式的图片保存成图片
不用matplotlib的原因是会产生坐标轴并且会有空白
'''
img0=pl.fromarray(f)
#img0.show()
img=img0.convert('RGB')
img.save('face.png')

# plt.figure(2)
# im=plt.imread('pikapika.png')
# plt.imshow(im)
# pika_array=np.array(im)
# print(pika_array.shape)
plt.show()


