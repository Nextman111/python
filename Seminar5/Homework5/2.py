# Создайте программу для игры в ""Крестики-нолики"".
import os
import random

def menu():
    os.system('cls')
    print('Игра в Крестики - нолики')
    menu = {1: 'Игра: Игрок против игрока',
            2: 'Игра: Игрок против бота',
            4: 'Правила игры'}

    for el, val in menu.items():
        print(f'{el} {val}')

    gameMode = 0
    while not(1 <= gameMode <= 3):
        gameMode = int(input('Выберите действие из списка '))
    if gameMode == 3:
        rules()
    else:
        return game(gameMode)


def game(gameMode, tableCandys = 2021, maxCandys = 28):
    table = newTable()
    os.system('cls')
    printTable(table)
    player = ''

    if gameMode == 1:
        player = 'Player1' if random.randint(0,1) == 0 else 'Player2'
    if gameMode == 2:
        player = 'Player'

    while tableCandys > 0:

        print(f'Ход игрока {player} ')
        if player not in 'Bot':
            moveX, moveY = playerMove(table)
            table[moveX - 1][moveY - 1] = 'X' if player == 'Player2' else '0'
        else:
            moveX, moveY = bot(table)
            table[moveX - 1][moveY - 1] = 'X'

        os.system('cls')
        printTable(table)

        check = checkTable(table)
        if check == 1:
            print(f'Победил игрок {player} ')
            input('Для возврата в меню нажмите Enter ')
            return menu()
        elif check == -1:
            print('Ничья!')
            input('Для возврата в меню нажмите Enter ')
            return menu()

        if gameMode == 1:
            player = 'Player1' if player == 'Player2' else 'Player2'
        if gameMode == 2:
            player = 'Player' if player == 'Bot' else 'Bot'

    return menu()


def bot(table):
    moveX = random.randint(1, 3)
    moveY = random.randint(1, 3)
    if table[moveX - 1][moveY - 1] != '-':
        print('Клетка уже заполнена ')
        return bot(table)
    else:
        return moveX, moveY

def checkTable(table):
    res = False
    if (table[0][0] == table[0][1] == table[0][2] and table[0][0] != '-') or\
       (table[1][0] == table[1][1] == table[1][2] and table[1][0] != '-') or\
       (table[2][0] == table[2][1] == table[2][2] and table[2][0] != '-') or\
       (table[0][0] == table[1][1] == table[2][2] and table[0][0] != '-') or\
       (table[2][0] == table[1][1] == table[0][2] and table[2][0] != '-') or\
       (table[0][0] == table[1][0] == table[2][0] and table[0][0] != '-') or\
       (table[0][1] == table[1][1] == table[2][1] and table[0][1] != '-') or\
       (table[0][2] == table[1][2] == table[2][2] and table[0][2] != '-'):
        res = 1
    elif table[0].count('-') == table[1].count('-') == table[2].count('-') == 0:
        res = -1
    return res


def playerMove(table):
    moveX = tryInputInt('X')
    moveY = tryInputInt('Y')
    if table[moveX-1][moveY-1] != '-':
        print('Клетка уже заполнена ')
        return playerMove(table)
    else:
        return moveX, moveY


def tryInputInt(coord):
    x = 0
    while not (1 <= x <= 3):
        try:
            x = int(input(f'Введите координату по {coord} '))
        except:
            print("Неверное значение")
            return tryInputInt(coord)
    return x

def rules():
    os.system('cls')
    print('Правила игры:\n\
    Игроки по очереди ставят X или O.\n\
    Побеждает игрок первым в заполнивший своим символом 3 клетки подряд.\n\
    По горизонтали, либо по вертикали, либо по диагонали.\n')
    input('Для возврата в меню нажмите Enter ')
    return menu()

def newTable():
    return [["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]]

def printTable(table):
    for i in table:
        print('|'.join(i))


menu()

# table = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0]]
# for i in table:
#     print(i)