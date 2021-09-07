# r_paint.py

from paint_init import *
from Routine import r_io

def paint_routine():
    # 绘制标题
    r_title_size = TITLE_FONT.getsize('今日任务')
    r_title_location = (WIN_WIDTH / 8 * 3 - r_title_size[0] / 2, WIN_HEIGHT * 3 / 16)
    DRAW.text(r_title_location, '今日任务', TITLE_COLOR, TITLE_FONT)
    # 绘制任务
    with open(r_io.ROUTINE_FILE, 'r', encoding='UTF-8') as r_file:
        r_mission_h = WIN_HEIGHT / 4
        count = 0
        for r in r_file.readlines():
            mission = r.split(',')[2]
            r_mission_size = MISSION_FONT.getsize(mission)[0]
            r_mission_w = WIN_WIDTH / 8 * 3 - r_mission_size / 2
            DRAW.text((r_mission_w, r_mission_h), mission, MISSION_COLOR, MISSION_FONT)
            r_mission_h += WIN_HEIGHT / 27 # 控制行距
            count += 1
            if count >= 15:
                break
        r_file.close()