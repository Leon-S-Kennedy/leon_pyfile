#列出指定目录下的所有文件
import os
path=os.getcwd()
list1=os.listdir(path)
for flnm in list1:
    if flnm.endswith('.py'):
        print(flnm)


