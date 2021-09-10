# project.py

import time

PROJECT_FILE = r'Project\project.txt'

# 更新长期项目进度
def p_update():
    # 检测是否有长期项目，若有则读入信息
    try:
        p_file = open(PROJECT_FILE, 'r', encoding='UTF-8')
        p = p_file.readline()
        p_contain = p.split(',')
        if len(p_contain) != 5:
            input('没有长期项目，按回车返回')
            return
        p_file.close()
    except:
        input('没有长期项目，按回车返回')
        return
    # 获取输入
    mission_num = p_contain[3]
    done_num = p_contain[4]
    update_num = input('当前进度：{}/{}，请输入新的进度：'.format(done_num, mission_num))
    if update_num == '0':
        return
    # 检测输入合法性
    while True:
        try:
            update_num = int(update_num)
            if 0 <= update_num <= int(mission_num):
                break
            else:
                update_num = input('请输入正确的进度：')
                if update_num == '0':
                    return
        except:
            update_num = input('请输入正确的进度：')
            if update_num == '0':
                return
    # 写入文件
    p_contain[4] = str(update_num)
    p_file = open(PROJECT_FILE, 'w', encoding='UTF-8')
    for i in range(4):
        p_file.write(p_contain[i] + ',')
    p_file.write(p_contain[4])
    p_file.close()

# 创建长期项目
def p_create():
    # 获取项目名
    name = input('请输入项目名称：')
    # 获取项目完成时间
    ddl = input('请输入预计完成天数或截止日期，格式位“年/月/日”：')
    if ddl == '0':
        return
    # 检测输入合法性
    while True:
        try:
            ddl = int(ddl)
            if ddl > 0:
                ddl_type = 0
                break
            else:
                ddl = input('请输入正确的完成天数或截止日期：')
                if ddl == '0':
                    return
        except:
            try:
                p_gmtime = time.strptime(ddl, '%Y/%m/%d')
                ddl_time = time.mktime(p_gmtime)
                if ddl_time > time.time():
                    ddl_type = 1
                    break
                else:
                    ddl = input('请输入正确的完成天数或截止日期：')
                    if ddl == '0':
                        return
            except:
                ddl = input('请输入正确的完成天数或截止日期：')
                if ddl == '0':
                    return
    # 获取需要完成的任务数
    mission_num = input('请输入项目总进度数量：')
    if mission_num == '0':
        return
    # 检测数据合法性
    while True:
        try:
            mission_num = int(mission_num)
            if mission_num > 0:
                break
            else:
                mission_num = input('请输入正确的任务数')
                if mission_num == '0':
                    return
        except:
            mission_num = input('请输入正确的任务数')
            if mission_num == '0':
                return
    # 生成数据
    start_time = str(int(time.time()))
    if ddl_type == 0:
        ddl_time = str(int(time.time() + ddl * 3600 * 24))
    else:
        ddl_time = str(int(time.mktime(time.strptime(ddl, '%Y/%m/%d'))))
    mission_num = str(mission_num)
    # 写入文件
    p_file = open(PROJECT_FILE, 'w', encoding='UTF-8')
    p_file.write('{},{},{},{},{}'.format(name, start_time, ddl_time, mission_num, '0'))
    p_file.close()
    input('创建成功！按回车返回')

# 删除长期项目
def p_delete():
    try:
        p_file = open(PROJECT_FILE, 'r', encoding='UTF-8')
        p_file.close()
    except:
        input('没有长期任务，按回车返回')
        return
    ensure = input('请输入“确认”来确认删除长期项目：')
    if ensure == '确认':
        p_file = open(PROJECT_FILE, 'w', encoding='UTF-8')
        p_file.close()
        input('删除成功！按回车返回')

# 检测是否有长期项目
def p_exist():
    try:
        p_file = open(PROJECT_FILE, 'r', encoding='UTF-8')
        p = p_file.readline()
        p_file.close()
        p_contain = p.split(',')
        if len(p_contain) != 5:
            return False
        else:
            return True
    except:
        return False

# 长期项目创建/删除
def p_manage(p_isExist):
    if p_isExist:
        p_delete()
    else:
        p_create()