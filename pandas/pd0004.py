#pd导入导出
import pandas as pd
import numpy as np
data=pd.read_csv('students.csv')
print(data)#默认会加上索引
data.iloc[0,0]=0
print(data)
data.to_pickle('st.pickle')
