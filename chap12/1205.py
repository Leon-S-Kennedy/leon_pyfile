#python中第三方模块的使用
import schedule
import time
def job():
    print('wdnmd')
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
