# e_io.py
import time

EVENT_FILE = 'Event\\event.txt'

# 获取文件内容，返回包含文件每一行的列表
def e_in():
    event_list = []
    try:
        e_file = open(EVENT_FILE, 'r')
        event_list = e_file.readlines()
        return event_list
    except:
        return event_list

# 向文件中写入一个新的event，需要输入两个string
def e_out_new(mission, ddl):
    e_file = open(EVENT_FILE, 'a')
    e_file.write('{},{}'.format(mission, ddl))
    e_file.close()

# 向文件中写入一个旧的event，需要输入一行文件
def e_out_old(e_line):
    e_file = open(EVENT_FILE, 'a')
    e_file.write(e_line)
    e_file.close()
    pass