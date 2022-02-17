#k均值
import scipy.cluster.vq as vq
import numpy as np

data = np.vstack((np.random.rand(100,3) + np.array([.5,.5,.5]),np.random.rand(100,3)))
print(data,data.shape)
'''
生成了一个200行3列的一个数组，前100行的数在0.5到1.5之间，后100行在0到1之间
'''
wdata=vq.whiten(data)

centroids,_=vq.kmeans(wdata,3)
print(centroids)

clx, dist = vq.vq(data, centroids)
print(clx,len(clx))
