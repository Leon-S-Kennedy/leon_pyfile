#丢失数据处理
import numpy as np
import pandas as pd

dates=pd.date_range('20210423',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['q','w','e','r'])
print('-----------------------------------------------------------------')
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
#print(df.dropna(axis=0,how='any'))# =0按行、=1按列，丢掉含nan的行默认为nay
'''
how={'any','all'}行内所有数据为nan才会丢掉
how='all'行内所有数据为nan才会丢掉
'''
print(df.fillna(value=0))
print(df.isnull())
print(np.any(df.isnull())==True)#判断是否存在一个nan的值
