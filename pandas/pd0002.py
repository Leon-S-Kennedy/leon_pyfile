#设置值
import numpy as np
import pandas as pd

dates=pd.date_range('20210423',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['q','w','e','r'])
print('-----------------------------------------------------------------')
df.iloc[2,2]=1111
df.loc['20210424','q']=2222#注意loc和iloc的区别
df[df.q<3]=0#q小于3的行为True,该行元素变为0
print(df)
df['t']=0
df['y']=np.nan
print(df)
df['u']=pd.Series(list(range(6)),index=pd.date_range('20210425',periods=6))
print(df)
