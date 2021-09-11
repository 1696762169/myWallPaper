# lesson_manage.py

from GlobalFunc import ensureNum, ensureMulChoice
from FileNameList import LESSON_FILE

# 读入文件中的课程，返回包含文件每一行的列表
def lesson_in():
    try:
        lesson_file = open(LESSON_FILE, 'r', encoding='UTF-8')
        lesson_list = lesson_file.readlines()
        lesson_file.close()
        return lesson_list
    except:
        return []

# 打印所有课程名
def printLesson(lesson_list):
    # 判断课程名是否有重复
    lesson_dict = {}
    for lesson in lesson_list:
        lesson_name = lesson.split(',')[0]
        if lesson_name not in lesson_dict.keys():
            lesson_dict[lesson_name] = False
        else:
            lesson_dict[lesson_name] = True
    # 打印课程名
    for i in range(len(lesson_list)):
        lesson_name = lesson_list[i].split(',')[0]
        lesson_room = lesson_list[i].split(',')[1]
        if lesson_dict[lesson_name]:
            print('{}. {}（{}）'.format(i + 1, lesson_name, lesson_room.strip('\n')))
        else:
            print('{}. {}'.format(i + 1, lesson_name))
        i += 1

# 添加课程
def lesson_create():
    # 获取课程名
    lesson_name = input('请输入课程名称（输入0返回）：')
    if lesson_name == '0':
        return
    # 获取上课地点
    lesson_room = input('请输入上课地点（输入0返回）：')
    if lesson_room == '0':
        return
    # 写入文件
    lesson_file = open(LESSON_FILE, 'a', encoding='UTF-8')
    lesson_file.write('{},{}\n'.format(lesson_name, lesson_room))
    lesson_file.close()

# 删除课程
def lesson_delete():
    # 读入文件
    lesson_list = lesson_in()
    if lesson_list == []:
        input('没有课程，按回车返回')
        return
    # 获取输入
    print('请选择所要删除的课程，可用“/”分隔多个序号：')
    printLesson(lesson_list)
    choice = input()
    # 检测输入合法性
    lesson_len = len(lesson_list)
    choice_list_int = ensureMulChoice(choice, lesson_len)
    if choice_list_int == []:
        return
    # 删除列表中的对象
    for choice_int in choice_list_int:
        del lesson_list[choice_int - 1]
    # 重新写入文件
    lesson_file = open(LESSON_FILE, 'w', encoding='UTF-8')
    for lesson_line in lesson_list:
        lesson_file.write(lesson_line)
    lesson_file.close()