#merge合并
import numpy as np
import pandas as pd
left=pd.DataFrame({'a':['a0','a1','a2','a3'],
                   'b':['b0','b1','b2','b3'],
                    'C':['C0','C1','C2','C3']
                   })
right=pd.DataFrame({'d':['d0','d1','d2','d3'],
                   'e':['e0','e1','e2','e3'],
                    'C':['C0','C1','C2','C3']
                   })
print(left)
print(right)
print('------------------------------------------------------------------')
res=pd.merge(left,right,on='C')#基于c合并两个dataframe,merge默认是inner
print(res)
print('-----------------------------------------------------------------')

'''
对于有两个columns合并时
'''
left1=pd.DataFrame({'a':['a0','a1','a2','a3'],
                   'b':['b0','b1','b2','b3'],
                    'C':['C0','C1','C2','C3'],
                    'd':['d0','d1','d2','d3']
                   })
right1=pd.DataFrame({'d':['d0','d1','d2','d3'],
                   'e':['e0','e1','e2','e3'],
                    'C':['C0','C1','C2','C3']
                   })
print(left1)
print(right1)
res1=pd.merge(left1,right1,on=['C','d'])
print(res1)
print('-------------------------index合并---------------------------------')
left2=pd.DataFrame({'a':['a0','a1','a2','a3'],
                   'b':['b0','b1','b2','b3'],},
                   index=['K0','K1','K2','K3']
                   )
right2=pd.DataFrame({'d':['d0','d1','d2','d3'],
                    'C':['C0','C1','C2','C3']},
                    index=['K2','K3','K4','K5']
                    )
print(left2)
print(right2)
res1=pd.merge(left2,right2,left_index=True,right_index=True,how='outer')
print(res1)
print('-------------------------------------------------------------------')