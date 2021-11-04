#字典生成式
a=['a','b','c','d','e','f']
b=['1','2','3','4']
c={a.upper():b for a,b in zip(a,b)}#使用zip(a,b)打包，以元素少的那个列表为基准
print(c)
#可以类比列表的生成式

