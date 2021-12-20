import prettytable as pt
def show_ticket(row_num):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        lst=[f'\33[0;33m第{i+1}行\33[m','\33[0;33m有票\33[m','\33[0;33m有票\33[m','\33[0;33m有票\33[m','\33[0;33m有票\33[m',
             '\33[0;33m有票\33[m']
        tb.add_row(lst)
    print(tb)

def order_ticket(row_num,row,column):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        if int(row)==i+1:
            lst = [f'\33[0;33m第{i + 1}行\33[m', '\33[0;33m有票\33[m', '\33[0;33m有票\33[m', '\33[0;33m有票\33[m',
                   '\33[0;33m有票\33[m', '\33[0;33m有票\33[m']
            lst[int(column)]='已售'
            tb.add_row(lst)
        else:
            lst = [f'\33[0;33m第{i + 1}行\33[m', '\33[0;33m有票\33[m', '\33[0;33m有票\33[m', '\33[0;33m有票\33[m',
                   '\33[0;33m有票\33[m','\33[0;33m有票\33[m']
            tb.add_row(lst)
    print(tb)
if __name__ == '__main__':
    row_num=13
    show_ticket(row_num)
    choose = input('请输入选择的座位号如第五行第三列请输入13，5：')
    try:
        row, column = choose.split(',')
    except:
        print('请重新输入！！！')
    order_ticket(row_num,row,column)
