# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
#
#     *Пример:*
#
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
import random


def get_polynomial(k):
    koef = [random.randint(1, 100) for i in range(k+1)]
    res = f'{koef[0]}*x^{k}'
    for i in range(1, len(koef)):
        k -= 1
        if koef[i] != 0:
            if k == 1:
                res = res + f' + {koef[i]}*x'
            elif k != 0:
                res = res + f' + {koef[i]}*x^{k}'
            else:
                res = res +f' + {koef[i]}'
    return f'{res} = 0'

def fileWrite(n, f_name):
    if n:
        with open(f_name, 'w') as data:
            data.write(n)


# Чтение из файла
def readFile(f_name):
    with open(f_name, 'r') as data:
        line = [line for line in data]
    return line

f_name = '4_example.txt'
k = int(input("Введит k "))
polynom = get_polynomial(k)
print('Сгенерировали выражение')
print(polynom)
print('Записываем в файл')
fileWrite(polynom, f_name)

print('Читаем из файла')
print(readFile(f_name))