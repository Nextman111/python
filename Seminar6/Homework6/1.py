# Напишите программу вычисления арифметического выражения
# заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#
# Пример:
# 2 + 2 => 4;
# 1 + 2 * 3 => 7;
# 11 - 2 * 3 => -5;


def tryParseToInt(i):
    try:
        i = int(i)
    except:
        pass
    return i


def parseExpresson(expression):
    exp = [tryParseToInt(i) for i in expression.split()]
    while len(exp) > 1:
        if '*' and '/' in exp:
            if exp.index('*') < exp.index('/'):
                index = exp.index('*')
                exp[index - 1] *= exp.pop(index + 1)
                exp.pop(index)
            else:
                index = exp.index('/')
                exp[index - 1] /= exp.pop(index + 1)
                exp.pop(index)
        if '/' in exp:
            index = exp.index('/')
            exp[index - 1] /= exp.pop(index + 1)
            exp.pop(index)
        elif '*' in exp:
            index = exp.index('*')
            exp[index - 1] *= exp.pop(index + 1)
            exp.pop(index)
        elif '-' in exp:
            index = exp.index('-')
            exp[index - 1] -= exp.pop(index + 1)
            exp.pop(index)
        elif '+' in exp:
            index = exp.index('+')
            exp[index - 1] += exp.pop(index + 1)
            exp.pop(index)

    return exp[0]


expression1 = '2 + 2'
expression2 = '1 + 2 * 3 - 1 + 2 * 3'
expression3 = '11 - 2 - 23'
expression4 = '3 * 2 + 4 - 12 / 6 * 4 + 2 * 3'

print(f'{expression1} = {parseExpresson(expression1)}')
print(f'{expression2} = {parseExpresson(expression2)}')
print(f'{expression3} = {parseExpresson(expression3)}')
print(f'{expression4} = {parseExpresson(expression4)}')
