# Модуль содержит методы ввода\вывода


def try_input_int(keys, message):
    try:
        i = int(input(message))
    except:
        print('Целое число ')
        return try_input_int(keys, message)

    if i in keys:
        # print('Выберите значение из списка ')
        return i
    else:
        return try_input_int(keys, message)


def print_menu(d):
    for i, v in d.items():
        print(f'{i} - {v[0]}')
    return d


def print_result(args, action):
    res = f'{args[0]} {action} {args[1]} = {args[2]}'
    print(res)
    return res
