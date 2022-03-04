#读取视频
import cv2
import numpy as np
import matplotlib.pyplot as plt
vc=cv2.VideoCapture('makabaka.mp4')
#判断视频文件是否被读取
if vc.isOpened():
    op,frame=vc.read()
else:
    op=False

#遍历每一帧，进行处理然后输出显示
while op:
    ret,frame=vc.read()
    if frame is None:
        break
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('result',gray)
        if cv2.waitKey(10) & 0xFF==27:#设定播放速度和终止键为esc(10表示一帧停留的时间)
            break
    else:
        break
vc.release()
cv2.destroyAllWindows()

