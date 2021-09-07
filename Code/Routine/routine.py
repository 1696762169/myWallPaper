# routine.py

from Routine import r_io

# 创建周期任务
def r_create():
    # 获取输入
    mission = input('请输入周期任务的内容：')
    cycle = input('请输入周期任务的周期：')
    # 检测输入合法性
    while True:
        try:
            int(cycle)
            break
        except:
            cycle = input('请输入正确的周期：')
    # 写入文件
    r_io.r_out_new(mission, cycle)

# 删除周期任务
def r_delete():
    # 获取文件内容
    routine_list = r_io.r_in()
    # 打印可删除的选项
    i = 1
    print('请选择所要删除的周期任务序号：')
    for r in routine_list:
        print('{}. {}'.format(i, r.mission))
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
    r_file = open(r_io.ROUTINE_FILE, 'w')
    r_file.close()
    for r in routine_list:
        r_io.r_out_old(r)

if __name__ == '__main__':
    # r_create()
    # r_delete()
    pass