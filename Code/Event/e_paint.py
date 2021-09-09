# e_paint.py

from paint_init import *
from Event import e_io

def paint_event():
    # 绘制标题
    e_title_size = TITLE_FONT.getsize('待办任务')
    e_title_location = (WIN_WIDTH / 8 * 5 - e_title_size[0] / 2, WIN_HEIGHT * 2.5 / 16)
    DRAW.text(e_title_location, '待办任务', TITLE_COLOR, TITLE_FONT)
    # 绘制任务
    try:
        e_file = open(e_io.EVENT_FILE, 'r', encoding='UTF-8')
        e_mission_h = WIN_HEIGHT / 4
        count = 0
        e_list = e_file.readlines()
        # 设置行距
        if len(e_list) <= 9:
            e_linegap = WIN_HEIGHT / 16
        elif len(e_list) <= 15:
            e_linegap = WIN_HEIGHT / 16 * 9 / len(e_list)
        else:
            e_linegap = WIN_HEIGHT / 27
        # 开始绘制
        for e in e_list:
            mission = e.split(',')[0]
            date = e.split(',')[1].strip('\n').split('/')
            mission = '{}    {}月{}日'.format(mission, date[1], date[2])
            e_mission_size = MISSION_FONT.getsize(mission)[0]
            e_mission_w = WIN_WIDTH / 8 * 5 - e_mission_size / 2
            DRAW.text((e_mission_w, e_mission_h), mission, MISSION_COLOR, MISSION_FONT)
            e_mission_h += e_linegap
            count += 1
            if count >= 15:
                break
        e_file.close()
    except:
        pass