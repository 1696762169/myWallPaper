# r_io.py

import time

ROUTINE_FILE = 'routine.txt'

class r_obj(object):
    def __init__(self, done, start, mission = '', cycle = ''):
        self.done = done
        self.start = start
        self.mission = mission
        self.cycle = cycle

# 读取文档中的所有routine，并返回一个包含r_obj对象的列表
def r_in():
    try:
        r_file = open(ROUTINE_FILE, 'r')
        routine_list = []
        for line in r_file.readlines():
            attrs = line.split(',')
            r = r_obj(attrs[0], attrs[1], attrs[2], attrs[3])
            routine_list.append(r)
        r_file.close()
        return routine_list
    except:
        routine_list = []
        return routine_list

# 向文档中写入一条新routine，需要传入两个string
def r_out_new(mission, cycle):
    r_file = open(ROUTINE_FILE, 'a')
    start = str(time.time())
    r_file.write('0,{},{},{}\n'.format(start, mission, cycle))
    r_file.close()

# 向文档中写入一条已经存在的routine，需要传入一个r_obj对象
def r_out_old(r):
    r_file = open(ROUTINE_FILE, 'a')
    r_file.write('{},{},{},{}'.format(r.done, r.start, r.mission, r.cycle))
    r_file.close()

if __name__ == '__main__':
    # import random
    # for i in range(20):
    #     r_out_new('测试{}'.format(random.randint(0,99)),random.randint(0,99))
    # r_in()
    pass