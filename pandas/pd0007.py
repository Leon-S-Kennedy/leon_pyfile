import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
series的绘制
'''

data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data=data.cumsum()
#plt.figure(0),data.plot(),plt.show()

'''
data的绘制
'''
data1=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=['A','B','C','D'])
data1=data1.cumsum()
#data1.plot(),plt.show()
ax1=data1.plot.scatter(x='A',y='B',color='DarkBlue',label='class_1')
data1.plot.scatter(x='A',y='C',color='DarkGreen',label='class_2',ax=ax1)
plt.show()
