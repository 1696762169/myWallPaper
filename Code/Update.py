# Update.py

import time
import paint
import Routine

# 中国时间戳
CHINA_TIME = time.time() + 3600 * 8
UPDATE_FILE = r'update.txt'

# 用于判断是否执行刷新操作，返回bool值
def updateAllow():
    try:
        u_file = open(UPDATE_FILE, 'r+', encoding='UTF-8')
        timegap = time.time() - time.mktime(time.strptime(u_file.readline(), '%Y/%m/%d'))
        if timegap > 3600 * 24:
            u_file.write(time.strftime('%Y/%m/%d', time.gmtime(CHINA_TIME)))
            u_file.close()
            return True
        else:
            u_file.close()
            return False
    except:
        u_file = open(UPDATE_FILE, 'w', encoding='UTF-8')
        u_file.write(time.strftime('%Y/%m/%d', time.gmtime(CHINA_TIME)))
        u_file.close()
        return True

# 执行刷新操作
def update():
    # 将所有周期任务设为未完成
    routine_list = Routine.r_io.r_in()
    for i in range(len(routine_list)):
        r_temp = routine_list[i][1:]
        r_temp = '0' + r_temp
        routine_list[i] = r_temp
    r_file = open(Routine.r_io.ROUTINE_FILE, 'w', encoding='UTF-8')
    for r in routine_list:
        r_file.write(r)
    r_file.close()
    # 刷新壁纸
    paint.generateWallpaper()
    paint.setWallpaper()

def main():
    allowed = updateAllow()
    if allowed:
        # print(1)
        update()

if __name__ == '__main__':
    # update()
    main()