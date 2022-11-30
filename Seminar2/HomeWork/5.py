# Реализуйте алгоритм нахождения рандомного числа.
# (Не используя библиотеки связанные с рандомом)
from datetime import datetime

def myRandom(a = -30, b = 30):
    return int((datetime.now().timestamp() % 1) * (b - a) + a)

print(myRandom())

# a = int(input('Введите левую границу '))
# b = int(input('Введите правую границу '))
# print(myRandom(a, b))