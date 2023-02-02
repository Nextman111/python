# модуль для действий над рациональными числами
import re


# Инициализация выражений
def init_args():
    return input_args('1'), input_args('2')


# Ввод аргумента
def input_args(n):
    return str_to_argument(input(f'Введите аргумент {n} '))


def message():
    print('Действия над рациональные числами ')


# Метод принимает строку и возвращает массив в виде списка чисел
def str_to_argument(s):
    res = []
    if re.findall(r'[-]?\d/[-]?\d', s):
        res = fraction_to_rational(s, sep='/')
    elif re.findall(r'[-]?\d[,][ ][-]?\d', s):
        res = fraction_to_rational(s, sep=', ')
    elif re.findall(r'[-]?\d[.,]\d?', s):
        res = decimal_to_rational(s)
    elif re.findall(r'[-]?\d', s):
        res = int_to_rational(s)
    elif s == '':
        res = fraction_zero()
    return res


# Целое в дробное
def int_to_rational(s):
    return [int(s), 1]


# Пустое в дробное
def fraction_zero():
    return [0, 1]


# Из дроби в десятичный вид
def fraction_to_decimal(rtn):
    return rtn[0]/rtn[1]


# Из дроби в консоль
def output(rtn):
    return f'{rtn[0]}/{rtn[1]}'


# Сокращение дроби
def fraction_reduction(rtn):
    if rtn[0] < 0 and rtn[1] < 0 or rtn[1] < 0:
        rtn[1] *= -1
        rtn[0] *= -1
    for i in range(2, 10):
        while rtn[0] % i == 0 and rtn[1] % i == 0:
            rtn[0] /= i
            rtn[1] /= i
    return list(map(int, rtn))


# Из дроби список числитель знаменатель
def fraction_to_rational(s, sep):
    return fraction_reduction(list(map(int, s.split(sep))))


# Из десятичного в список числитель знаменатель
def decimal_to_rational(s):
    s = s.replace(',', '.')
    res = [
        int(s.replace('.', '')),
        10 ** len(s[s.index('.')+1:]) if s[s.index('.')+1] != ' ' else 1
    ]
    return fraction_reduction(res)


# Метод возвращает сумму
def sum(rtl1, rtl2):
    a, b = rtl1
    c, d = rtl2
    return fraction_reduction([a*d + c*b, b*d])


# Метод возвращает разность
def difference(rtl1, rtl2):
    a, b = rtl1
    c, d = rtl2
    return fraction_reduction([a*d - c*b, b*d])


# Метод возвращает произведение
def multiple(rtl1, rtl2):
    a, b = rtl1
    c, d = rtl2
    return fraction_reduction([a*c, b*d])


# Метод возвращает результат деления
def divide(rtl1, rtl2):
    a, b = rtl1
    c, d = rtl2
    return fraction_reduction([a*d, b*c])

