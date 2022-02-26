import PIL.Image as pl
im=pl.open("D:\pythonFile\pywork\chap13\pika.jpg")
im.save('pikapika.png')
im2=open('pikapika.png')
new_im=im.convert('L')
#new_im.show()
print(im.size)

#filter方法
from PIL import ImageFilter
bluF = im.filter(ImageFilter.BLUR)#均值滤波
conF = im.filter(ImageFilter.CONTOUR)#找轮廓
edgeF = im.filter(ImageFilter.FIND_EDGES)#边缘检测
# bluF.show()
# conF.show()
# edgeF.show()

#split方法
r,g,b = im.split()#返回rgb三个通道的图像
#b.show()

#eval方法
'''
使用变量function对应的函数（该函数应该有一个参数）处理变量image所代表图像中的每一个像素点。
如果变量image所代表图像有多个通道，那变量function对应的函数作用于每一个通道。
注意：变量function对每个像素只处理一次，所以不能使用随机组件和其他生成器。
'''
def fun1(x):
    return x * 0.3
def fun2(y):
    return y * 2.0
im_eval1 = pl.eval(im, fun1)
im_eval2 = pl.eval(im, fun2)
# im_eval1.show()
# im_eval2.show()
