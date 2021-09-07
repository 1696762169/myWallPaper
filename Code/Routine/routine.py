# routine.py

from Routine import r_io
import time

# 创建周期任务
def r_create():
    # 获取输入
    mission = input('请输入周期任务的内容：')
    cycle = input('请输入周期任务的周期：')
    # 检测输入合法性
    while True:
        try:
            int(cycle)
            if cycle > 0:
                break
            else:
                cycle = input('请输入正确的周期：')
        except:
            cycle = input('请输入正确的周期：')
    # 写入文件
    r_io.r_out_new(mission, cycle)

# 标记周期任务已完成
def r_finish():
    # 获取文件内容
    routine_list = r_io.r_in()
    # 判断文件是否为空
    if routine_list == []:
        input('没有周期任务，按回车继续')
        return
    # 打印可标记的选项
    index = 1
    j = 0
    routine_dict = {}
    print('请选择已完成的周期任务序号：')
    for r in routine_list:
        # 判断任务是否被完成
        if r[0] == '0':
            # 判断是否在时间周期内
            timegap = time.time() - time.mktime(time.strptime(r.split(',')[1], '%Y/%m/%d'))
            if timegap % (3600 * 24 * int(r.split(',')[3])) < 3600 * 24:
                mission = r.split(',')[2]
                print('{}. {}'.format(index, mission))
                routine_dict[index] = j
                index += 1
        j += 1
    choice = input()
    # 检测输入合法性
    while True:
        try:
            choice = int(choice)
            if choice <= 0 or choice > len(routine_list):
                choice = input('请输入正确的序号：')
            else:
                break
        except:
            choice = input('请输入正确的序号：')
    # 标记列表中的对象
    r_temp = routine_list[routine_dict[choice]][1:]
    r_temp = '1' + r_temp
    routine_list[routine_dict[choice]] = r_temp
    # 重新写入
    r_file = open(r_io.ROUTINE_FILE, 'w', encoding='UTF-8')
    r_file.close()
    for r_line in routine_list:
        r_io.r_out_old(r_line)

# 删除周期任务
def r_delete():
    # 获取文件内容
    routine_list = r_io.r_in()
    # 判断文件是否为空
    if routine_list == []:
        input('没有周期任务，按回车继续')
        return
    # 打印可删除的选项
    i = 1
    print('请选择所要删除的周期任务序号：')
    for r in routine_list:
        mission = r.split(',')[2]
        print('{}. {}'.format(i, mission))
        i += 1
    choice = input()
    # 检测输入合法性
    while True:
        try:
            choice = int(choice)
            if choice <= 0 or choice > len(routine_list):
                choice = input('请输入正确的序号：')
            else:
                break
        except:
            choice = input('请输入正确的序号：')
    # 删除列表中的对象
    del routine_list[choice - 1]
    # 重新写入
    r_file = open(r_io.ROUTINE_FILE, 'w', encoding='UTF-8')
    r_file.close()
    for r_line in routine_list:
        r_io.r_out_old(r_line)

if __name__ == '__main__':
    # r_create()
    # r_delete()
    pass