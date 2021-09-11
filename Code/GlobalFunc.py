# GlobalFunc.py

from FileNameList import MODULE_FILE

# 保证单个数字输入的合法性，返回数字字符串
def ensureNum(number, tips, limit = 0):
    while True:
        if number == '0':
            return '0'
        try:
            number = int(number)
            if limit == 0:
                if 0 < number:
                    return str(number)
            else:
                if 0 < number <= limit:
                    return str(number)
            number = input(tips)
        except:
            number = input(tips)

# 检测日期输入合法性，返回日期字符串
def ensureDate(date):
    while True:
        if date == '0':
            return '0'
        try:
            date = strptime(ddl, '%Y/%m/%d')
            return date
        except:
            date = input('请输入正确格式的日期：')

# 保证多项选择的合法性，返回序号的int类型列表
def ensureMulChoice(choice, length):
    while True:
        if choice == '0':
            return []
        choice_list_str = choice.split('/')
        ensure = True
        for c in choice_list_str:
            try:
                c = int(c)
                if c <= 0 or c > length:
                    ensure = False
                    break
                else:
                    continue
            except:
                ensure = False
                break
        if ensure == False:
            choice = input('请输入正确的序号：')
        else:
            break
    # 将字符串列表转换为排列好的整数列表
    choice_list_int = []
    for choice in choice_list_str:
        choice = int(choice)
        choice_list_int.append(choice)
    choice_list_int.sort(reverse=True)
    return choice_list_int

# 检测可选模块是否开启，返回bool
def checkModuleOn(module_name):
    # 从文件中获取信息
    try:
        module_file = open(MODULE_FILE, 'r', encoding='UTF-8')
        module_list = module_file.readlines()
        module_file.close()
    except:
        return False
    # 检测文件中信息
    for module in module_list:
        name_in_file = module.split(',')[0]
        if name_in_file == module_name:
            module_status = module.split(',')[2].strip('\n')
            if module_status == '1':
                return True
    return False