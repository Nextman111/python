# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#
# Пример:
#
#                 - 6 -> да
#                 - 7 -> да
#                 - 1 -> нет

def parseToDayOfTheWeak():
    day = input('Введидте число дня недели ')
    if day.isdigit() and (0 < int(day) < 8):
        return int(day)
    else:
        print('Неверное значение, введите число от 1 до 7')
        return parseToDayOfTheWeak()

if parseToDayOfTheWeak() > 5:
    print("Выходной")
else:
    print("Рабочий")