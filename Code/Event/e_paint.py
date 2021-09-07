# e_paint.py

from paint_init import *
from Event import e_io

def paint_event():
    # 绘制标题
    e_title_size = TITLE_FONT.getsize('长期任务')
    e_title_location = (WIN_WIDTH / 8 * 5 - e_title_size[0] / 2, WIN_HEIGHT * 3 / 16)
    DRAW.text(e_title_location, '长期任务', TITLE_COLOR, TITLE_FONT)
    # 绘制任务
    try:
        e_file = open(e_io.EVENT_FILE, 'r', encoding='UTF-8')
        e_mission_h = WIN_HEIGHT / 4
        count = 0
        for e in e_file.readlines():
            mission = e.split(',')[0]
            e_mission_size = MISSION_FONT.getsize(mission)[0]
            e_mission_w = WIN_WIDTH / 8 * 5 - e_mission_size / 2
            DRAW.text((e_mission_w, e_mission_h), mission, MISSION_COLOR, MISSION_FONT)
            e_mission_h += WIN_HEIGHT / 27  # 控制行距
            count += 1
            if count >= 15:
                break
        e_file.close()
    except:
        pass