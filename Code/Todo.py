# Todo.py

from os import system
from sys import exit
from time import time

from Routine import *
from Event import *
from Project import *
from Module import module
import paint

# 判断长期项目是否存在，以便生成菜单
p_isExist = project.p_exist()

MAIN_MENU = [('routine.r_create()', '创建周期任务'),
             ('event.e_create()','创建单次任务'),
             ('routine.r_finish()', '标记周期任务已完成'),
             ('routine.r_delete()','删除周期任务'),
             ('event.e_delete()','删除单次任务'),
             ('project.p_update()','长期项目进度更新'),
             ('project.p_manage(p_isExist)','删除长期项目' if p_isExist else '创建长期项目'),
             ('module.module_menu()','可选模块菜单'),
             ('','设置')]

def printMenu():
    print('===此处应有欢迎语===')
    i = 1
    for func in MAIN_MENU:
        print('{}. {}'.format(i,func[1]))
        i += 1
    print('0. 退出程序')

def main():
    choice = '0'
    while True:
        printMenu()
        if choice == '':
            print('请输入正确的功能代号：')
        choice = input()
        try:
            if choice == '0':
                paint.generateWallpaper()
                paint.setWallpaper()
                break
            else:
                eval(MAIN_MENU[int(choice) - 1][0])
        except:
            choice = ''
        system('cls')

if __name__ == '__main__':
    # 添加随机测试数据
    # from random import randint
    # for i in range(20):
    #     # r_io.r_out_new('测试{}'.format(randint(0, 999999)), randint(0, 99))
    #     e_io.e_out_new('测试{}'.format(randint(0, 999999)), '{}/{}/{}'.format(2021, randint(1, 12), randint(1, 30)))

    # paint.generateWallpaper()
    # paint.setWallpaper()
    # routine.r_create()
    # routine.r_finish()
    # routine.r_delete()
    # event.e_delete()
    # project.project_menu()
    # module.module_menu()

    main()