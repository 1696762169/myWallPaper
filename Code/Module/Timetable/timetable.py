# timetable.py

from GlobalFunc import checkModuleOn
from Module.Timetable.timetable_manage import timetable_set, timetable_clear, semester_set
from Module.Timetable.lesson_manage import lesson_create, lesson_delete
from os import system

TIMETABLE_NAME = 'timetable'
TIMETABLE_MENU = [('timetable_set()','添加课程表内容'),
                  ('timetable_clear()','清除课程表内容'),
                  ('lesson_create()','创建课程'),
                  ('lesson_delete()','删除课程'),
                  ('semester_set()','设置学期开始日期')]

# 打印课程表管理菜单
def printTimetableMenu():
    system('cls')
    print('请选择所要使用的课程表功能：')
    i = 0
    j = 0
    module_on = checkModuleOn(TIMETABLE_NAME)
    if not module_on:
        print('1. 开启课程表模块')
        j += 1
    for k in range(len(TIMETABLE_MENU)):
        print('{}. {}'.format(i + j + 1, TIMETABLE_MENU[i][1]))
        i += 1
    if module_on:
        print(str(i + 1) + '. 停用课程表模块')
    print('0. 返回上级菜单')

# 课程表管理菜单
def timetable_menu():
    from Module.module import m_switch
    choice = '0'
    while True:
        module_on = checkModuleOn(TIMETABLE_NAME)
        i = (0 if module_on else 1)
        printTimetableMenu()
        if choice == '':
            print('请输入正确的功能代号：')
        choice = input()
        if choice == '0':
            return
        # 开启模块
        if choice == '1' and not module_on:
            m_switch(TIMETABLE_NAME, '1')
            continue
        # 关闭模块
        if choice == str(len(TIMETABLE_MENU) + 1) and module_on:
            m_switch(TIMETABLE_NAME, '0')
            continue
        # 执行功能
        try:
            eval(TIMETABLE_MENU[int(choice) - i - 1][0])
        except:
            choice = ''

