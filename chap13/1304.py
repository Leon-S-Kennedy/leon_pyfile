#with语句（上下文管理器）
#   with语句可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确的关闭，以此达到释放资源的目的
with open('a.txt','r')as file:#open('a.txt','r')称为上下文表达式这句话的对象称为上下文管理器
    print(file.read())
#不用手动关闭，免得造成资源的浪费
