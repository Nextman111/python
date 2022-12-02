# Напишите программу,
# которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

# 1
def decimalToBinary1(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n//2
    return binary

# 2
def decimalToBinary2(n):
    return bin(n)[2:]


n = int(input('Введите число: '))
print(decimalToBinary1(n))
print(decimalToBinary2(n))