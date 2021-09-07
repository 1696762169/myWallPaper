# e_io.py
import time

class e_obj(object):
    def __init__(self, mission, ddl):
        self.mission = mission
        self.ddl = ddl

EVENT_FILE = 'event.txt'

def e_in():
    pass

# 向文件中写入一个新的event，需要输入两个string
def e_out_new(mission, ddl):
    e_file = open(EVENT_FILE, 'a')
    e_file.write('{},{}'.format(mission, ddl))
    e_file.close()


def e_out_old():
    pass