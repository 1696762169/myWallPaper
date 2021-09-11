# timetable.py

from GlobalFunc import ensureMulChoice
from os import system

LESSON_FILE = r'Module\Timetable\lesson.txt'
TIMETABAL_FILE = r'Module\Timetable\timetable.txt'

# 读入文件中的课程，返回包含文件每一行的列表
def lesson_in():
    try:
        lesson_file = open(LESSON_FILE, 'r', encoding='UTF-8')
        lesson_list = lesson_file.readlines()
        lesson_file.close()
        return lesson_list
    except:
        return []

# 打印所有课程名
def printLesson(lesson_list):
    # 判断课程名是否有重复
    lesson_dict = {}
    for lesson in lesson_list:
        lesson_name = lesson.split(',')[0]
        if lesson_name not in lesson_dict.keys():
            lesson_dict[lesson_name] = False
        else:
            lesson_dict[lesson_name] = True
    # 打印课程名
    for i in range(len(lesson_list)):
        lesson_name = lesson_list[i].split(',')[0]
        lesson_room = lesson_list[i].split(',')[1]
        if lesson_dict[lesson_name]:
            print('{}. {}（{}）'.format(i + 1, lesson_name, lesson_room))
        else:
            print('{}. {}'.format(i + 1, lesson_name))
        i += 1

# 设置课程
def lesson_set():
    pass

# 添加课程
def lesson_create():
    # 获取课程名
    lesson_name = input('请输入课程名称（输入0返回）：')
    if lesson_name == '0':
        return
    # 获取上课地点
    lesson_room = input('请输入上课地点（输入0返回）：')
    if lesson_room == '0':
        return
    # 写入文件
    lesson_file = open(LESSON_FILE, 'a', encoding='UTF-8')
    lesson_file.write('{},{}\n'.format(lesson_name, lesson_room))
    lesson_file.close()

# 删除课程
def lesson_delete():
    # 读入文件
    lesson_list = lesson_in()
    print('请选择所要删除的课程，可用“/”分隔多个序号：')
    printLesson(lesson_list)
    choice = input()
    # 检测输入合法性
    lesson_len = len(lesson_list)
    choice_list_str = ensureMulChoice(choice, lesson_len)
    if choice_list_str == []:
        return
    # 更新文件


# 打印课程表管理菜单
def printTimetableMenu():
    system('cls')
    print('请选择课程表管理功能：')
    print('1. 设置课程时间')
    print('2. 创建课程')
    print('3. 删除课程')
    print('0. 返回上级菜单')

# 课程表管理菜单
def timetable_menu():
    choice == '0'
    while True:
        printTimetableMenu()
        if choice == '':
            print('请输入正确的功能代号：')
        choice = input()
        if choice == '1':
            lesson_set()
        elif choice == '2':
            lesson_create()
        elif choice == '3':
            lesson_delete()
        elif choice == '0':
            return
        else:
            choice = ''

