# Напишите программу,
# которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

def multiPara(lst):
    even = lambda x : 0 if x == 0 else 1
    length = len(lst)
    return [lst[i]*lst[length-i-1]\
            for i in range(length//2+even(even(length%2)))]

# Нечетное len()
print(multiPara([2, 3, 4, 5, 6]))
# Четное len()
print(multiPara([2, 3, 5, 6]))