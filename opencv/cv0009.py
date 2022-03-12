#图像金字塔
#高斯金字塔：向下采样（缩小）
#          向上采样(放大)
import cv2
import numpy as np
'''
用向下采样缩小图片
'''
im=cv2.imread(r'D:\pythonFile\pywork\scipy\face.png')
down=cv2.pyrDown(im)
print(down.shape)
cv2.imshow('down',down)
cv2.waitKey(0)
cv2.destroyAllWindows()
