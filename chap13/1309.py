#os模块的walk方法(递归遍历所有文件)
import os
path=os.getcwd()
list1=os.walk(path)
for a,b,c in list1:#a指目录路径，b指目录名称，c指文件名称
    '''    
    print(a)
    print(b)
    print(c)
    print('--------------------这是一条分割线--------------------')
    '''

#分析：a是路径，不含文件所以下一步不用遍历a,b是目录名称可能含有子目录或文件，需要遍历，c是指文件名，一定要遍历
    #for b1 in b:
        #print(os.path.join(a,b1))#将文件路径和目录名连接起来
    for c1 in c:
        print(os.path.join(a,c1))#把文件路径和文件名连接起来
    print('---------------------------------------------------------------')