import os

filename = 'student.txt'


def menum():
    print('==============================学生信息管理系统==============================')
    print('----------------------------------主菜单----------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查询学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生人数')
    print('\t\t\t\t\t\t7.显示学生信息')
    print('\t\t\t\t\t\t0.退出')


def save(lst):
    students_txt = open(filename, 'a+', encoding='utf-8')
    for item in lst:
        students_txt.write(str(item) + '\n')
    students_txt.close()


def show_st(lst):
    if len(lst) == 0:
        print('没有查询到该学生的信息！！！')
        return
    else:
        for_title = '{:^8}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        print(for_title.format('id', 'name', 'math', 'chinese', 'english', 'sum'))
        format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        for item in lst:
            print(format_data.format(item.get('id'),
                                     item.get('name'),
                                     item.get('math'),
                                     item.get('chinese'),
                                     item.get('english'),
                                     int(item.get('math')) + int(item.get('chinese')) + int(item.get('english'))))


def f1():
    student_list = []
    while True:
        id = input('请输入学号：')
        if id:
            pass
        else:
            print('请按规定输入')
            continue
        name = input('请输入姓名：')
        if name:
            pass
        else:
            print('请按规定输入')
            continue
        try:
            math = float(input('请输入数学成绩：'))
            chinese = float(input('请输入语文成绩：'))
            english = float(input('请输入英语成绩：'))
        except:
            print('请输入有效的成绩')
            continue
        student = {'id': id, 'name': name, 'math': math, 'chinese': chinese, 'english': english, }
        student_list.append(student)
        answer = input('继续输入请按y？:')
        if answer == 'y' or answer == "Y":
            continue
        else:
            break
    save(student_list)
    print('信息录入完毕！')


def f2():
    st_q = []
    id = ''
    name = ''
    while True:
        if os.path.exists(filename):
            mode = input('请输入查找方式，按id查找请按1，按姓名查找请按2：')
            if mode == '1':
                id = input('请输入学生的id：')
            elif mode == '2':
                name = input('请输入学生的姓名：')
            else:
                print('请正确输入！')
                continue
            with open(filename, 'r', encoding='utf-8')as file:
                st = file.readlines()
                for i in st:
                    d = dict(eval(i))
                    if id != '':
                        if d['id'] == id:
                            st_q.append(d)
                    else:
                        if d['name'] == name:
                            st_q.append(d)
            show_st(st_q)
            st_q.clear()
            answer = input('继续查询请按y:')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                return
        else:
            print('请先录入学生信息！')
            return


def f3():
    while True:
        del_id = input('请输入要删除的学生的id:')
        if del_id == '':
            print('请按要求输入！')
            continue
        else:
            flag = False  # 米奇妙妙屋
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8')as file:
                    st_old = file.readlines()
            else:
                st_old = []
            if st_old:
                with open(filename, 'w', encoding='utf-8')as rwf:
                    for item in st_old:
                        d = dict(eval(item))
                        if d['id'] == del_id:
                            flag = True
                        else:
                            rwf.write(str(d) + '\n')
            else:
                print('学生信息还未录入，请先输入学生信息！')
                break
        if flag:
            print('id为{0}的学生信息已被删除'.format(del_id))
        else:
            print('没有找到该学生的信息')
        f7()
        answer = input('继续删除请按y')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break


def f4():
    while True:
        st_id = input('请输入要修改的学生的id:')
        if st_id == '':
            print('请按要求输入！')
            continue
        else:
            break
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8')as file:
            st_old = file.readlines()
    else:
        return
    with open(filename, 'w', encoding='utf-8')as wrf:
        flag = True
        for item in st_old:
            d = dict(eval(item))
            if d['id'] == st_id:
                print('找到该学生的信息可以修改')
                d['name'] = input('请重新输入姓名：')
                while True:
                    try:
                        d['math'] = float(input('请重新输入数学成绩：'))
                        d['chinese'] = float(input('请重新输入语文成绩：'))
                        d['english'] = float(input('请重新输入英语成绩：'))
                    except:
                        print('请重新输入')
                    else:
                        break
                wrf.write(str(d) + '\n')
                print('该生信息修改成功')
                flag = False
            else:
                wrf.write(str(d) + '\n')
        if flag:
            print('没有找到该生信息')
        answer = input('继续修改请按y:')
        if answer == 'y' or answer == 'Y':
            f4()


def f5():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8')as file:
            st_lst = file.readlines()
            st_new = []
            for i in st_lst:
                d = dict(eval(i))
                st_new.append(d)
    else:
        return
    sort = input('按1选择升序排列，按2选择降序排列：')
    if sort == '1':
        sort_bool = False
    elif sort == '2':
        sort_bool = True
    else:
        print('请按要求输入！')
        f5()
    mode = input('请选择排序方式1.math,2.chinese,3.english,4.sum')
    if mode == '1':
        st_new.sort(key=lambda x: int(x['math']), reverse=sort_bool)
    elif mode == '2':
        st_new.sort(key=lambda x: int(x['chinese']), reverse=sort_bool)
    elif mode == '3':
        st_new.sort(key=lambda x: int(x['english']), reverse=sort_bool)
    elif mode == '4':
        st_new.sort(key=lambda x: int(x['math']) + int(x['chinese']) + int(x['english']), reverse=sort_bool)
    else:
        print('你的输入有误，请重新输入')
        f5()
    show_st(st_new)
    answer = input('继续查看请按y')
    if answer == 'y' or answer == 'Y':
        f5()


def f6():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8')as file:
            st = file.readlines()
            if st:
                print(f'共有学生{len(st)}人！')
            else:
                print('还没有录入学生')
    else:
        print('请先录入学生信息！')


def f7():
    st_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8')as file:
            st = file.readlines()
            for i in st:
                st_lst.append(eval(i))
            if st_lst:
                show_st(st_lst)
                answer = input('继续查看请按y')
                if answer == 'y' or answer == 'Y':
                    f7()
            else:
                print('请先录入学生信息！')
    else:
        print('请先录入学生信息！')


def main():
    while True:
        menum()
        try:
            choice = int(input('请选择需要的服务:'))
            if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
                if choice == 0:
                    answer = input('确定退出请输入y:')
                    if answer == 'y' or answer == 'Y':
                        print('感谢使用！！！')
                        break
                    else:
                        continue
                elif choice == 1:
                    f1()
                elif choice == 2:
                    f2()
                elif choice == 3:
                    f3()
                elif choice == 4:
                    f4()
                elif choice == 5:
                    f5()
                elif choice == 6:
                    f6()
                elif choice == 7:
                    f7()
        except ValueError:
            print('请按要求输入!')


if __name__ == '__main__':
    main()
