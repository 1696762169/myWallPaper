# event.py

from GlobalFunc import ensureDate, ensureMulChoice
from FilePathList import EVENT_FILE
from Event import e_io
from time import strptime

# 创建长期任务
def e_create():
    # 输入任务
    mission = input('请输入单次任务内容：')
    # 输入截止日期
    ddl = input('请输入截止日期，格式为“年/月/日”：')
    # 检测输入合法性
    ddl = ensureDate(ddl)
    if ddl == '0':
        return
    # 写入文件
    e_io.e_out_new(mission, ddl)

# 删除长期任务
def e_delete():
    # 获取文件内容
    event_list = e_io.e_in()
    # 判断文件是否为空
    if event_list == []:
        input('没有单次任务，按回车退出')
        return
    # 打印可删除的选项
    i = 1
    print('请选择所要删除的单次任务序号，可用“/”分隔多个序号：')
    for e in event_list:
        mission = e.split(',')[0]
        print('{}. {}'.format(i, mission))
        i += 1
    choice = input()
    # 检测输入合法性
    e_len = len(event_list)
    choice_list_int = ensureMulChoice(choice, e_len)
    if choice_list_int == []:
        return
    # 删除列表中的对象
    for choice_int in choice_list_int:
        del event_list[choice_int - 1]
    # 重新写入
    e_file = open(EVENT_FILE, 'w', encoding='UTF-8')
    e_file.close()
    for e_line in event_list:
        e_io.e_out_old(e_line)