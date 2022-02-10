#合并
import pandas as pd
import numpy as np
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
'''
concat合并
'''
#上下合并
res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)#0表示竖向合并，1表示横向合并
print(res)#如果没有ignore_index=True可以看到索引并没有合并，一般会添加ignore_index=True
print('-------------------------------------------------------------------------')

'''
join
'''
#不指定join='inner'合并时没有指定的值会被nan掉，默认是outer表示会被nan掉
df4=pd.DataFrame(np.ones((3,4))*1,columns=['e','b','c','d'])
result=pd.concat([df1,df4],join='inner',ignore_index=True)
print(result)
print('-------------------------------------------------------------------------------')
'''
append合并
'''
#如果没有ignore_index=True可以看到索引并没有合并，一般会添加ignore_index=True
res2=df1.append([df2,df2],ignore_index=True)
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(res2)
print('-------------------------------------------------------------------------------')
res3=res2.append(s1,ignore_index=True)
print(res3)
