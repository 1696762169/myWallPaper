# timetable_paint.py

from GlobalFunc import CHINA_TIME
from FilePathList import TIMETABAL_FILE, SEMESTER_FILE
from paint_init import *
import time

# 未设置学期开始时间或当日无课时绘制提示
def paint_tips(tips):
    empty_size = TITLE_FONT.getsize(tips)
    empty_location = (WIN_WIDTH / 2 - empty_size[0] / 2, WIN_HEIGHT / 8 * 7 - empty_size[1] / 2)
    DRAW.text(empty_location, tips, TITLE_COLOR, TITLE_FONT)

# 计算当前的周数
def calWeekNum():
    try:
        semester_file = open(SEMESTER_FILE, 'r', encoding='UTF-8')
        start = semester_file.read()
        start_time = time.mktime(time.strptime(start, '%Y/%m/%d'))
        semester_file.close()
    except:
        return 0
    timegap = time.time() - start_time
    weekNum = int(timegap / (3600 * 24 * 7)) + 1
    return weekNum

# 绘制日期信息
def paint_date(weekNum, date):
    date_dict = {0: '一', 1: '二', 2: '三', 3: '四', 4: '五', 5: '六', 6: '日', }
    week_text = '第{}周'.format(weekNum)
    date_text = '周{}'.format(date_dict[date])
    text_height = SMALL_FONT.getsize(week_text)[1]
    week_location = WIN_WIDTH / 4, WIN_HEIGHT / 8 * 7 - text_height
    date_location = WIN_WIDTH / 4, WIN_HEIGHT / 8 * 7.1
    DRAW.text(week_location, week_text, NORMAL_COLOR, SMALL_FONT)
    DRAW.text(date_location, date_text, NORMAL_COLOR, SMALL_FONT)

# 绘制一门课程
def paint_lesson(clock, name, room):
    clock_dict = {'1':'8:00', '2':'10:00', '3':'13:30', '4':'15:30', '5':'19:00'}
    paint_w = WIN_WIDTH / 12 * (int(clock) + 3) + WIN_WIDTH / 24
    # 绘制时间
    clock_size = SMALL_FONT.getsize(clock_dict[clock])
    clock_location = (paint_w - clock_size[0] / 2, WIN_HEIGHT / 16 * 13.2)
    DRAW.text(clock_location, clock_dict[clock], NORMAL_COLOR, SMALL_FONT)
    # 绘制课程名称
    name_size = SMALL_FONT.getsize(name)
    name_location = (paint_w - name_size[0] / 2, clock_location[1] + clock_size[1] * 1.3)
    DRAW.text(name_location, name, NORMAL_COLOR, SMALL_FONT)
    # 绘制教室
    room_size = SMALL_FONT.getsize(room)
    room_location = (paint_w - room_size[0] / 2, name_location[1] + name_size[1] * 1.3)
    DRAW.text(room_location, room, NORMAL_COLOR, SMALL_FONT)

def paint_timetable():
    # 获取周数
    weekNum = calWeekNum()
    if weekNum == 0:
        paint_tips('未设置学期开始时间')
        return
    # 绘制日期信息
    date = time.gmtime(CHINA_TIME).tm_wday
    paint_date(weekNum, date)
    # 读入课程表文件信息
    try:
        timetable_file = open(TIMETABAL_FILE, 'r', encoding='UTF-8')
        lesson_list = timetable_file.readlines()
        timetable_file.close()
    except:
        paint_tips('今日无课')
        return
    # 绘制课程
    noLesson = True
    for lesson in lesson_list:
        # 判断本周是否需要该课程
        lesson_fre = lesson.split(',')[0]
        if ((lesson_fre == '2' and weekNum % 2 == 0) or
            (lesson_fre == '3' and weekNum % 2 == 1)):
            continue
        # 判断今日是否需要该课程
        lesson_date = lesson.split(',')[1]
        if int(lesson_date) != date + 1:
            continue
        # 绘制该课程
        noLesson = False
        lesson_clock = lesson.split(',')[2]
        lesson_name = lesson.split(',')[3]
        lesson_room = lesson.split(',')[4].strip('\n')
        paint_lesson(lesson_clock, lesson_name, lesson_room)
    if noLesson:
        paint_tips('今日无课')