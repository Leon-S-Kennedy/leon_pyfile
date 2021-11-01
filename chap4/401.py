#列表文件的查询操作
#列表的索引
#通过list[索引]来获取列表中的元素
d=['a','b',12,]
print(d[0],d[-1])#从左往右是从零开始，从右往左是从-1开始
#获取列表中指定元素的索引
#通过list.index()获取list中指定的元素的索引
a=['hello','world',98,'hello']
print(a.index('hello'))#如果列表之中存在N多个相同的元素，只返回第一个元素的索引
#print(a.index('python'))ValueError: 'python' is not in list
#print(a.index('hello',1,3))ValueError: 'hello' is not in list
print(a.index('hello',1,4))#从start到stop是含start不含stop

