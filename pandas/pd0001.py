import numpy as np
import pandas as pd

mydataset = {
  'sites': ["Google", "Runoob", "Wiki"],
  'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print('-----------------------------------------------------------------------')
dates=pd.date_range('20210423',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['q','w','e','r'])
print(df)
print('----------------------------选择数据-------------------------------')
print(df['q'])
print(df.q)

print('---------------------------按索引--------------------------------')
print(df[0:3])
print(df['20210424':'20210426'])

print('------------------------------按行--------------------------------')
print(df.loc['20210425'])
print(df.loc[:,['q','w']])
print(df.loc['20210423':'20210426','q':'e'])
print('-----------------------------按位置-----------------------------------')
print(df.iloc[3,1])#4行2列
print(df.iloc[3:5,0:3])#类似于切片
print(df.iloc[[1,3,5],1:3])
print(df.iloc[[1,3,5],[0,2,3]])#就很人性化
print('-----------------------------按条件----------------------------------')
print(df[df.q>8])
