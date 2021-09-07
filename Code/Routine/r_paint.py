# r_paint.py

import time
from paint_init import *
from Routine import r_io

def paint_routine():
    # 绘制标题
    r_title_size = TITLE_FONT.getsize('今日任务')
    r_title_location = (WIN_WIDTH / 8 * 3 - r_title_size[0] / 2, WIN_HEIGHT * 3 / 16)
    DRAW.text(r_title_location, '今日任务', TITLE_COLOR, TITLE_FONT)
    # 绘制任务
    try:
        r_file = open(r_io.ROUTINE_FILE, 'r', encoding='UTF-8')
    except:
        return
    r_mission_h = WIN_HEIGHT / 4
    count = 0
    for r in r_file.readlines():
        # 判断任务是否被完成
        if r[0] == '0':
            # 判断是否在时间周期内
            timegap = time.time() - time.mktime(time.strptime(r.split(',')[1], '%Y/%m/%d'))
            if timegap % (3600 * 24 * int(r.split(',')[3])) < 3600 * 24:
                mission = r.split(',')[2]
                r_mission_size = MISSION_FONT.getsize(mission)[0]
                r_mission_w = WIN_WIDTH / 8 * 3 - r_mission_size / 2
                DRAW.text((r_mission_w, r_mission_h), mission, MISSION_COLOR, MISSION_FONT)
                r_mission_h += WIN_HEIGHT / 27 # 控制行距
                count += 1
                if count >= 15:
                    break
    r_file.close()
