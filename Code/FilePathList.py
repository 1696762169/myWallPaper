# FilePathList.py

import os.path

# 生成存放文件的目录
Todo_path = os.path.abspath('Todo.py')
superior_path = ''
dir_list = Todo_path.split('\\')
for path in dir_list[:-2]:
    superior_path += path
    superior_path += '\\'
FILE_DIR = superior_path + 'File\\'
ASSET_DIR = superior_path + 'Assets\\'

# 刷新记录
UPDATE_FILE = FILE_DIR + r'update.txt'

# 周期任务记录文件
ROUTINE_FILE = FILE_DIR + r'routine.txt'

# 单次任务记录文件
EVENT_FILE = FILE_DIR + r'event.txt'

# 长期项目记录文件
PROJECT_FILE = FILE_DIR + r'project.txt'

# 可选模块状态与打印位置记录文件
MODULE_FILE = FILE_DIR + r'Module\ModuleStatus.txt'

# 可选模块文件
# 课程表模块文件
TIMETABAL_FILE = FILE_DIR + r'Module\Timetable\timetable.txt'
LESSON_FILE = FILE_DIR + r'Module\Timetable\lesson.txt'
SEMESTER_FILE = FILE_DIR + r'Module\Timetable\semester.txt'

if __name__ == '__main__':
    p = r'D:/myWallPaper\Code/Todo.py'
    # print(p)
    # print(normpath(p))
    print(ROUTINE_FILE)