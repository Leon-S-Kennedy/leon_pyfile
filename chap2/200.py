#程序的组织结构
#程序的顺序结构
print("------程序开始------")
print('首先把冰箱门打开')
print('把大象装进冰箱')
print('把冰箱门关上')
print('------程序结束-----')

#对象的布尔值
#python一切皆对象，所有对象都有bool值使用bool()获取布尔值
print("以下对象的布尔值为False")
print(bool(False))
print(bool(0),bool(0.0))
print(bool(None))
print(bool(""))
print(bool([]),bool(list()))#空列表
print(bool(()),bool(tuple()))#空元组
print(bool({}),bool(dict()))#空字典
print(bool(set()))#空集合
print('剩下的布尔值都是Ture', bool("剩下的布尔值都是Ture"))
