# Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
#                     - x=34; y=-30 -> 4
#                     - x=2; y=4-> 1
#                     - x=-34; y=-30 -> 3

def is_int(coordName):
    try:
        coordinate = int(input(f'Введидте координату отличную от 0 {coordName} '))
    except:
        print("Неверное значение")
        return is_int(coordName)
    if coordinate == 0:
        print('Введите значение отличное от 0')
        return is_int(coordName)
    else:
        return coordinate

def get_point():
    x = is_int('X')
    y = is_int('Y')
    return [x, y]

point = get_point()

if point[0] > 0 and point[1] > 0:
    print(f'Точка ({point[0]}, {point[1]}) находится в I четверти')
if point[0] < 0 and point[1] > 0:
    print(f'Точка ({point[0]}, {point[1]}) находится в II четверти')
if point[0] < 0 and point[1] < 0:
    print(f'Точка ({point[0]}, {point[1]}) находится в III четверти')
if point[0] > 0 and point[1] < 0:
    print(f'Точка ({point[0]}, {point[1]}) находится в IV четверти')