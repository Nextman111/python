# модуль для действий над комплексными числами


# Инициализация выражений
def init_args():
    return input_args('1'), input_args('2')


# Ввод аргумента
def input_args(n):
    return str_to_argument(input(f'Введите аргумент {n} '))


def message():
    print('Действия над комплексными числами ')


# Метод преобразует строковое выражение комплексного числа
# в формат для расчета:
def str_to_argument(s):
    cur = ''
    res = []
    for i in s:
        if i == '-' and cur == '':
            cur = i
        elif (i == ',' or i == '.')\
                and len(cur) > 0 \
                and cur != '-' \
                and not ',' in cur:
            cur += '.'
        elif i.isdigit():
            cur += i
        elif not i.isdigit() and len(cur) > 0 and cur != '-':
            res.append(float(cur))
            cur = ''
    return res


# Метод преобразует комплексное число в строку
def output(cmplx, round_=5):
    return f'{round(cmplx[0],round_)}{"+" if cmplx[1] > 0 else "-"}{round(cmplx[1],round_)}i'


# Сопряженное
# Метод получает число и возвращает сопряженное ему число
def complex_conjugate(cmplx):
    cmplx[1] *= -1
    return cmplx


# Метод возвращает сумму пары комплексных чисел
def sum(cmplx1, cmplx2):
    a, b = cmplx1
    c, d = cmplx2
    return [a+c, b+d]


# Метод возвращает разность пары комплексных чисел
def difference(cmplx1, cmplx2):
    a, b = cmplx1
    c, d = cmplx2
    return [a-c, b-d]


# Метод возвращает произведение пары комплексных чисел
def multiple(cmplx1, cmplx2):
    a, b = cmplx1
    c, d = cmplx2
    return [a*c-b*d, b*c + a*d]


# Метод возвращает результат деления пары комплексных чисел
def divide(cmplx1, cmplx2):
    a, b = cmplx1
    c, d = cmplx2
    z = c**2 + d**2
    return [(a*c+b*d)/z, (b*c-a*d)/z]
