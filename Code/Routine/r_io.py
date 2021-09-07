# r_io.py

import time

ROUTINE_FILE = 'Routine\\routine.txt'

# 读取文档中的所有routine，并返回一个包含文件每一行的列表
def r_in():
    routine_list = []
    try:
        r_file = open(ROUTINE_FILE, 'r')
        routine_list = r_file.readlines()
        r_file.close()
        return routine_list
    except:
        return routine_list

# 向文档中写入一条新routine，需要传入两个string
def r_out_new(mission, cycle):
    r_file = open(ROUTINE_FILE, 'a')
    start = str(time.time())
    r_file.write('0,{},{},{}\n'.format(start, mission, cycle))
    r_file.close()

# 向文档中写入一条已经存在的routine，需要传入文件中的一行
def r_out_old(r_line):
    r_file = open(ROUTINE_FILE, 'a')
    r_file.write(r_line)
    r_file.close()

if __name__ == '__main__':
    # import random
    # for i in range(20):
    #     r_out_new('测试{}'.format(random.randint(0,99)),random.randint(0,99))
    # r_in()
    pass