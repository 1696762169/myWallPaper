# GlobalFunc.py

# 检测多项选择的合法性
def ensureMulChoice(choice, length):
    while True:
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
            if choice == '0':
                return []
        else:
            break
    return choice_list_str