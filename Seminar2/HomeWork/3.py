# Задайте список из n чисел последовательности
# (1 + (1/n))^n и выведите на экран их сумму.
#
#     *Пример:*
#
#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 36.9}

def sets1(n):
    d = {key: round((1+(1/key))**key, 2) for key in range(1, n+1)}
    return f'dict = {d}\nsum(dict) = {sum(d.values())}'



print(sets1(int(input('Введите целое N '))))