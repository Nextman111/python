# Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных.

# Алгоритм выполнен в ASCII варианте по этому дешифрация чисел будет не возможна.


def algorithmRLE(data):
    rle = []
    for line in data:
        print(f'{line} Исходная')
        rleLine = parseToRLE(line)
        rle.append(rleLine)
        print(f'{rleLine} Зашифрованая')
        parseToStr = parseRLEToSTR(rleLine)
        print(f'{parseToStr} Дешифрованая')
        print(f'Исходная строка равна строке после дешифрации {parseToStr == line}')
    return rle


def parseToRLE(str):
    res = ''
    tmp = ''
    count = 0
    l = len(str)
    for i in range(l):
        if i < l - 1:
            if str[i] == str[i+1]:
                if count < 0:
                    res = f'{res}{count}{tmp}'
                    tmp = ''
                    count = 0
                count += 1
            elif str[i] != str[i+1]:
                if count > 0:
                    res = f'{res}{count+1}{str[i]}'
                    count = 0
                else:
                    tmp = f'{tmp}{str[i]}'
                    count -= 1
        elif str[i] == str[i-1]:
            res = f'{res}{count + 1}{str[i]}'
        else:
            res = f'{res}{count-1}{tmp}{str[i]}'
    return res


def parseRLEToSTR(rle):
    res = ''
    num = ''
    tmp = ''
    for i in range(len(rle)):
        if num == '' and rle[i] == '-':
            num = rle[i]
        elif rle[i].isdigit():
            num = f'{num}{rle[i]}'
        elif num != '' and int(num) > 0:
            res = f'{res}{rle[i] * int(num)}'
            num = ''
        elif num != '' and int(num) < 0:
            tmp = f'{tmp}{rle[i]}'
            if i == len(rle)-1 or rle[i+1].isdigit() or rle[i+1] == '-':
                res = f'{res}{tmp}'
                num = ''
                tmp = ''
    return res


file1 = ['jkguyfyggtdrduyhuyghhjghgjhyt']
file2 = ['aaszcrrgrtggxccv', 'dasdasdgggh']

algorithmRLE(file1)
print()
algorithmRLE(file2)
