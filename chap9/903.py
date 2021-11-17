#python中的异常处理机制
#traceback模块
import traceback
try:
    print('------------------------------')
    print(1/0)
except:
    traceback.print_exc()
