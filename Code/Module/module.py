# module.py

from GlobalFunc import checkModuleOn
from FileNameList import MODULE_FILE
from Module.Timetable import timetable
from os import system

# 定义模块名称及位置属性
# 位置属性符号含义：“_”代表底部，“|”代表侧面
MODULE_MENU = {'timetable' : ('课程表', '_', 'timetable.timetable_menu()')}

# 重置模块开启状态，将其全部关闭，用于模块状态文件被删除时
def reset_status():
    m_file = open(MODULE_FILE, 'w', encoding='UTF-8')
    for module in MODULE_MENU.keys():
        m_file.write('{},{},0\n'.format(module, MODULE_MENU[module][1]))
    m_file.close()

# 切换模块开启状态
def m_switch(module_name, status):
    # 从文件中获取信息
    try:
        module_file = open(MODULE_FILE, 'r', encoding='UTF-8')
        module_list = module_file.readlines()
        module_file.close()
        # 检测文件中信息
        for i in range(len(module_list)):
            module = module_list[i]
            name_in_file = module.split(',')[0]
            if name_in_file == module_name:
                temp = module[:-2]
                module = temp + status + '\n'
                module_list[i] = module
                break
        # 重新写入文件
        m_file = open(MODULE_FILE, 'w', encoding='UTF-8')
        for module in module_list:
            m_file.write(module)
        m_file.close()
    except:
        reset_status()
        if status == '1':
            m_switch(module_name, status)

# 打印菜单
def printModuleMenu(m_status_on, m_status_off):
    print('请选择所要使用的模块：')
    i = 1
    for module in m_status_on:
        print('{}. {}'.format(i, module[0]))
        i += 1
    for module in m_status_off:
        print('{}. {}（未开启）'.format(i, module[0]))
        i += 1
    print('0. 返回主菜单')

# 可选模块管理菜单
def module_menu():
    timetable.timetable_menu()
    # 读入模块信息，判断模块是否开启
    m_status_on = []
    m_status_off = []
    try:
        m_file = open(MODULE_FILE, 'r', encoding='UTF-8')
        m_list = m_file.readlines()
        m_file.close()
        for i in range(len(m_list)):
            if m_list[i].split(',')[2] == '1\n':
                m_status_on.append(MODULE_MENU[m_list[i].split(',')[0]])
            else:
                m_status_off.append(MODULE_MENU[m_list[i].split(',')[0]])
    except:
        for module in MODULE_MENU.values():
             m_status_off.append(module)
        reset_status()
    # 按顺序排列功能函数
    m_func = []
    for module in m_status_on:
        m_func.append(module[2])
    for module in m_status_off:
        m_func.append(module[2])
    # 获取输入
    choice = 0
    while True:
        system('cls')
        printModuleMenu(m_status_on, m_status_off)
        if choice == '':
            print('请输入正确的模块代号：')
        choice = input()
        try:
            if choice == '0':
                break
            else:
                eval(m_func[int(choice) - 1])
        except:
            choice = ''

if __name__ == '__main__':
    module_menu()
