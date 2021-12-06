#python中常用的内置模块

#sys    是与python解释器及其环境操作相关的标准库
import  sys
print(sys.getsizeof(24))#获得对象的所占内存的大小（字节）
print(sys.getsizeof(True))
print(sys.getsizeof('李博文'))

#time   提供与时间相关的各种函数的标准库
import time
print(time.time())
print(time.localtime(time.time()))#将输入的时间转换成本地时间

#os     提供了访问操作系统服务功能的标准库
#calendar   提供了与日期相关的各种函数的标准库
#urllib     用来读取来自网上(服务器)的数据标准库
import urllib.request
print(urllib.request.urlopen('http://www.baidu.com'))
#json   用于使用JSON序列化和反序列化对象
#re     用于在字符串中执行正则表达式匹配和替换
#math   提供标准算术运算函数的标准库
#decimal    用于精确控制运算精度、有效数位和四舍五入操作的十进制运算
#logging    提供了灵活的记录事件、错误、警告和调试信息等日志信息的功能
