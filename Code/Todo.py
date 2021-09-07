# Todo.py

from os import system
from sys import exit
from Routine import *
from Event import *
import paint

func_list = [('routine.r_create()','创建周期任务'),
             ('event.e_create()','创建单次任务'),
             ('routine.r_delete()','删除周期任务'),
             ('event.e_delete()','删除单次任务'),
             ('','启用可选模块'),
             ('','停用可选模块'),]

def printMenu():
    print('===此处应有欢迎语===')
    i = 1
    for func in func_list:
        print('{}. {}'.format(i,func[1]))
        i += 1
    print('0. 退出程序')

def main():
    choice = 0
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
                eval(func_list[int(choice) - 1][0])
        except:
            choice = ''
        system('cls')

if __name__ == '__main__':
    # from random import randint
    # for i in range(20):
    #     r_io.r_out_new('测试{}'.format(randint(0, 999999)), randint(0, 99))
    #     e_io.e_out_new('测试{}'.format(randint(0, 999999)), '{}/{}/{}'.format(randint(2000,2021), randint(1, 12), randint(1, 30)))
    main()