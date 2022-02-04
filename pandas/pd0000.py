import numpy as np
import pandas as pd

s=pd.Series([1,3,6,np.nan,44,1])
print(s)

date=pd.date_range('20210423',periods=6)
print(date)

df=pd.DataFrame(np.random.randn(6,4),index=date,columns=['a','b','c','d'])
print(df)

df1=pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)

df2=pd.DataFrame({'a':pd.Timestamp('20210423'),
                  'b':pd.Series(1.,index=list(range(4)),dtype='float32'),
                  'c':np.array([3]*4,dtype='int32'),
                  'd':pd.Categorical(['test','train','test','train',])
                  })
print(df2)
print(df2.dtypes)
#得到行的名字和列的名字，其中index为行，columns为列
print(df2.index)
print(df2.columns)

print(df2.values)
print(df2.describe())

print(df2.T)

print(df1.sort_index(axis=0,ascending=False))

