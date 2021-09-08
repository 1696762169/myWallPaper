# event.py

from time import strptime
from Event import e_io

# 创建长期任务
def e_create():
    # 输入任务
    mission = input('请输入单次任务内容：')
    # 输入截止日期
    ddl = input('请输入截止日期，格式为“年/月/日”：')
    # 检测输入合法性
    while True:
        try:
            date = strptime(ddl, '%Y/%m/%d')
            break
        except:
            ddl = input('请输入正确格式的日期：')
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
    while True:
        choice_list_str = choice.split('/')
        ensure = True
        for c in choice_list_str:
            try:
                c = int(c)
                if c <= 0 or c> len(event_list):
                    ensure = False
                    break
                else:
                    continue
            except:
                ensure = False
                break
        if ensure == False:
            choice = input('请输入正确的序号：')
        else:
            break
    # 删除列表中的对象
    choice_list_int = []
    for choice in choice_list_str:
        choice = int(choice)
        choice_list_int.append(choice)
    choice_list_int.sort(reverse=True)
    for event in choice_list_int:
        del event_list[event - 1]
    # 重新写入
    e_file = open(e_io.EVENT_FILE, 'w', encoding='UTF-8')
    e_file.close()
    for e_line in event_list:
        e_io.e_out_old(e_line)