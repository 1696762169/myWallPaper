# timetable_manage.py

from GlobalFunc import ensureNum
from FilePathList import TIMETABAL_FILE
import Module.Timetable.lesson_manage

# 选择课程表中的时间，返回字符串列表：[单双周代号，日期代号，上课时间代号]
def time_choice():
    time_list = []
    # 获取单双周输入
    print('请选择课程的上课频率：')
    print('1. 每周')
    print('2. 单周')
    print('3. 双周')
    odd_even = input()
    # 检测输入合法性
    odd_even = ensureNum(odd_even, '请输入正确的上课频率代号：', 3)
    if odd_even == '0':
        return []
    time_list.append(odd_even)
    # 获取星期几输入
    print('请选择上课日期（数字1-7表示星期一至星期日）：')
    week_day = input()
    # 检测数据合法性
    week_day = ensureNum(week_day, '请输入数字1-7：', 7)
    if week_day == '0':
        return []
    time_list.append(week_day)
    # 获取上课时间输入
    print('请选择开始上课时间：')
    print('1. 8:00')
    print('2. 10:00')
    print('3. 13:30')
    print('4. 15:30')
    print('5. 19:00')
    clock = input()
    # 检测数据合法性
    clock = ensureNum(clock, '请选择正确的上课时间：', 5)
    if clock == '0':
        return []
    time_list.append(clock)
    return time_list

# 设置课程
def timetable_set():
    # 读入文件
    lesson_list = Module.Timetable.lesson_manage.lesson_in()
    if lesson_list == []:
        input('没有课程，按回车返回')
        return
    # 获取课程序号输入
    print('请选择所要设置的课程：')
    Module.Timetable.lesson_manage.printLesson(lesson_list)
    lesson_num = input()
    # 检测输入合法性
    lesson_len = len(lesson_list)
    lesson_num = ensureNum(lesson_num, '请输入正确的课程代号：', lesson_len)
    if lesson_num == '0':
        return
    # 获取上课时间输入
    time_list = time_choice()
    if time_list == []:
        return
    # 写入文件
    timetable_file = open(TIMETABAL_FILE, 'a', encoding='UTF-8')
    for i in range(3):
        timetable_file.write(time_list[i] + ',')
    timetable_file.write(lesson_list[int(lesson_num)  - 1])
    timetable_file.close()

# 清除课程表内容
def timetable_clear():
    # 获取输入
    time_list = time_choice()
    if time_list == []:
        return
    # 获取课程表记录
    try:
        timetable_file = open(TIMETABAL_FILE, 'r', encoding='UTF-8')
        record_list = timetable_file.readlines()
        timetable_file.close()
    except:
        return
    # 查找课程表记录并删除
    clear_time = ''
    for t in time_list:
        clear_time += t
        clear_time += ','
    for i in range(len(record_list)):
        if record_list[i][:6] == clear_time:
            del record_list[i]
            # 重新写入文件
            timetable_file = open(TIMETABAL_FILE, 'w', encoding='UTF-8')
            for record in record_list:
                timetable_file.write(record)
            timetable_file.close()
            break