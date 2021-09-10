# p_paint.py

from Project import project
from paint_init import *
import time

# 绘制没有长期项目时的提示
def drawNoProject():
    p_title_size = TITLE_FONT.getsize('没有长期项目')
    p_title_location = (WIN_WIDTH / 2 - p_title_size[0] / 2, WIN_HEIGHT / 16)
    DRAW.text(p_title_location, '没有长期项目', TITLE_COLOR, TITLE_FONT)

def paint_project():
    # 判断是否存在长期项目，并读取信息
    try:
        p_file = open(project.PROJECT_FILE, 'r', encoding='UTF-8')
        p = p_file.readline()
        p_contain = p.split(',')
        if len(p_contain) != 5:
            drawNoProject()
            return
        p_file.close()
    except:
        drawNoProject()
        return
    # 绘制项目名
    p_name_location = (WIN_WIDTH / 4, WIN_HEIGHT / 100)
    DRAW.text(p_name_location, '项目名称：{}'.format(p_contain[0]), NORMAL_COLOR, SMALL_FONT)
    # 绘制截止时间
    ddl_date = time.strftime('%Y/%m/%d', time.gmtime(int(p_contain[2])))
    p_ddl_size = SMALL_FONT.getsize('截止时间：{}'.format(ddl_date))
    p_ddl_location = (WIN_WIDTH / 4 * 3 - p_ddl_size[0], WIN_HEIGHT / 100)
    DRAW.text(p_ddl_location, '截止时间：{}'.format(ddl_date), NORMAL_COLOR, SMALL_FONT)
    # 绘制项目进度文字
    p_done_location = (WIN_WIDTH / 4, WIN_HEIGHT / 100 * 6)
    p_done_size = SMALL_FONT.getsize('项目进度：')
    DRAW.text(p_done_location, '项目进度：', NORMAL_COLOR, SMALL_FONT)
    # 绘制项目进度
    p_done_x = WIN_WIDTH / 4 + p_done_size[0]
    p_done_y = WIN_HEIGHT / 100 * 6 + p_done_size[1] / 3
    p_done_length = (WIN_WIDTH / 2 - p_done_size[0] * 2) * int(p_contain[4]) / int(p_contain[3])
    p_done_width = p_done_size[1] / 3 * 2
    p_done_rec = (p_done_x, p_done_y, p_done_x + p_done_length, p_done_y + p_done_width)
    DRAW.rectangle(p_done_rec, PROJECT_COLOR)
    # 绘制时间进度文字
    p_time_location = (WIN_WIDTH / 4, WIN_HEIGHT / 100 * 11)
    p_time_size = SMALL_FONT.getsize('时间进度：')
    DRAW.text(p_time_location, '时间进度：', NORMAL_COLOR, SMALL_FONT)
    # 绘制时间进度
    p_time_x = WIN_WIDTH / 4 + p_time_size[0]
    p_time_y = WIN_HEIGHT / 100 * 11 + p_time_size[1] / 3
    time_passed = time.time() - int(p_contain[1])
    time_total = int(p_contain[2]) - int(p_contain[1])
    if time_passed <= time_total:
        p_time_length = (WIN_WIDTH / 2 - p_time_size[0] * 2) * time_passed / time_total
    else:
        p_time_length = (WIN_WIDTH / 2 - p_time_size[0] * 2)
    p_time_width = p_time_size[1] / 3 * 2
    p_time_rec = (p_time_x, p_time_y, p_time_x + p_time_length, p_time_y + p_time_width)
    DRAW.rectangle(p_time_rec, TIME_COLOR)
