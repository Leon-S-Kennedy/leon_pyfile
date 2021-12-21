import time
def show_info():
    print('输入提示数字，执行相应操作：0.退出1.查看登录日志')
def write_log(user):
    with open('log.txt','a',encoding='utf-8')as file:
        s=f'用户名{user},登陆时间{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}'
        file.write(s)
        file.write('\n')
def read_info():
    with open('log.txt','r',encoding='utf-8')as fl:
        while True:
            line=fl.readline()
            if line=='':
                break
            else:
                print(line)
if __name__ == '__main__':
    print(time.time())
    print(time.localtime(time.time()))
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
    user=input('请输入用户名：')
    pwd=input('请输入密码：')
    if user=='admin'and pwd=='password':
        print('登录成功')
        write_log(user)
        show_info()
        num=int(input('请输入操作数：'))
        while True:
            if num==0:
                print('退出成功')
                break
            elif num==1:
                print('查看登录日志')
                read_info()
                num=int(input('请输入操作数：'))
            else:
                print('您的操作有误！！！')
                show_info()
                num=int(input('请输入操作数：'))
    else:
        print('用户名或密码错误！！')