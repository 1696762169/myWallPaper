# e_io.py

from FilePathList import EVENT_FILE
import time

# 获取文件内容，返回包含文件每一行的列表
def e_in():
    event_list = []
    try:
        e_file = open(EVENT_FILE, 'r', encoding='UTF-8')
        event_list = e_file.readlines()
        return event_list
    except:
        return event_list

# 向文件中写入一个新的event，需要输入两个string
def e_out_new(mission, ddl):
    # 决定新任务插入位置
    event_list = e_in()
    ddl_time = time.mktime(time.strptime(ddl, '%Y/%m/%d'))
    for i in range(len(event_list)):
        e_time = event_list[i].strip('\n').split(',')[1]
        if ddl_time < time.mktime(time.strptime(e_time, '%Y/%m/%d')):
            event_list.insert(i, '{},{}\n'.format(mission, ddl))
            break
    else:
        event_list.append('{},{}\n'.format(mission, ddl))
    # 重新写入文件
    e_file = open(EVENT_FILE, 'w', encoding='UTF-8')
    for e in event_list:
        e_file.write(e)
    e_file.close()

# 向文件中写入一个旧的event，需要输入一行文件
def e_out_old(e_line):
    e_file = open(EVENT_FILE, 'a', encoding='UTF-8')
    e_file.write(e_line)
    e_file.close()
    pass