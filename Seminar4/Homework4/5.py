# Даны два файла,
# в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# (одинаковый размер уравнений)*



file1 = '5_example.txt'
file2 = '5.1_example.txt'

# Чтение из файла
def readFile(f_name):
    with open(f_name, 'r') as data:
        line = [line for line in data]
    return line

def fileWrite(n, f_name):
    if n:
        with open(f_name, 'w') as data:
            data.write(n)

def parsePolynomial(x):
    koef = x[:-4].split(' + ')
    return [int(koef[i][:-4]) if i < len(koef)-2 else
            int((koef[i][:-2]) if i == len(koef) - 2 else int(koef[i]))
            for i in range(len(koef))]


def sumPolynomial(x):
    return [sum(i) for i in zip(*x)]

def get_polynomial(koef):
    k = len(koef)
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

polynomial1 = readFile(file1)[0]
polynomial2 = readFile(file2)[0]
print(polynomial1)
print(polynomial2)
polynoms = parsePolynomial(polynomial1), parsePolynomial(polynomial2)
sumPolynom = get_polynomial(sumPolynomial((polynoms)))
print(sumPolynom)
fileWrite(sumPolynom,'5_sum_polynom.txt')