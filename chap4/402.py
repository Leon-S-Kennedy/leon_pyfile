#获取列表的多个元素（切片操作）
a=[0,1,2,3,4,5,6,7,8,9]
print(a[1:6:1])
'''注意与list[索引]来获取列表中的元素相区分开来
list[star,stop,step]其中含start不含stop
'''
b=a[1:6:1]
print('原列表',id(a))
print('切片列表',id(b))
print(a[1:6:1],a[1:6:],a[1:6])#step的默认值为1
print(a[1:6:2])
print(a[:6:2])#start省略时，其默认值为0
print(a[1::2])#stop省略时，其默认到最后

#当step为负数时(可以理解为向前切片)
print(a[::-1])
print(a[7::-1])
print(a[:0:-1])
