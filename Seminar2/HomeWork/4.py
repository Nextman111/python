# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

# Создадим список
def getListN(n):
    return [i for i in range(-abs(n), abs(n)+1)]

# Создадим файл с позициями. Позиция включится в список рандомно.
# Исключим индекс n, чтобы не попасть на значение  0.
def fileNew(n, f_name):
    if n != 0:
        with open(f_name, 'w') as data:
            r = [f'{i}\n' for i in range(n*2) if random.randint(0, 1) and i != n]
            data.writelines(r)

# Чтение из файла
def readFile(f_name):
    with open(f_name, 'r') as data:
        line = [int(line) for line in data]
    return line

def multList(lst, indexLst):
    mult = 1
    for i in indexLst:
        mult *=lst[i]
    return mult

n = int(input('Введите N '))
lst = getListN(n)
print(f'Список сформирован {lst}')
f_name = 'file_for_4.txt'
fileNew(n, f_name)
f_data = readFile(f_name)
print(f'Файл перезаписан. Индексы для умножения элементов {f_data}')
mult = multList(lst, f_data)
print(f'Произведение элементов списка по индексам из файла равно {mult}')