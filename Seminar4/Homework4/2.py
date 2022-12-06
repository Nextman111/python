# Задайте натуральное число N.
# Напишите программу, которая составит список
# простых множителей числа N.

def multList(n):
    d = 2
    res = []
    while n > 1:
        if n%d == 0:
            res.append(d)
            n = n/d
        else:
            d = d+1
    return res

n = int(input("Введите натуральное N "))
print(multList(n))
