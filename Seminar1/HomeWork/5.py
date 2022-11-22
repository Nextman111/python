# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
#
# Пример:
#
#                 - A (3,6); B (2,1) -> 5,09
#                 - A (7,-5); B (1,-1) -> 7,21
import math


def is_float(coordName):
    try:
        coordinate = float(input(f'Введидте координату {coordName} '))
    except:
        print("Неверное значение")
        return is_int(coordName)
    return coordinate

def point(pointName):
    print(f'Точка {pointName}: ')
    return [is_float('X'), is_float('Y')]

pointA = point('A')
pointB = point('B')
lineAB = math.sqrt((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)

print(f'Расстояние между точками А {pointA} и B {pointB} равно {lineAB}')