# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""
#
import os
import random


def rules():
    os.system('cls')
    print('Правила игры:\n\
    На столе лежит 2021 конфета.\n\
    Играют два игрока делая ход друг после друга.\n\
    Первый ход определяется жеребьёвкой.\n\
    За один ход можно забрать не более чем 28 конфет.\n\
    Все конфеты оппонента достаются сделавшему последний ход.\n')
    input('Для возврата в меню нажмите Enter ')
    return menu()

def menu():
    os.system('cls')
    print('Игра в конфетки')
    menu = {1: 'Игра: Игрок против игрока',
            2: 'Игра: Игрок против бота',
            3: 'Игра: Игрок против супер бота',
            4: 'Правила игры'}

    for el, val in menu.items():
        print(f'{el} {val}')

    gameMode = 0
    while not(1 <= gameMode <= 4):
        gameMode = int(input('Выберите действие из списка '))
    if gameMode == 4:
        rules()
    else:
        return game(gameMode)

def game(gameMode, tableCandys = 100, maxCandys = 28):
    player = ''
    if gameMode == 1:
        player = 'Player1' if random.randint(0,1) == 0 else 'Player2'
    if gameMode == 2:
        player = 'Player'
    while tableCandys > 0:
        # os.system('cls')
        print(f'На Столе {tableCandys}, можно взять  не более {maxCandys}')
        move = 0
        print(f'Ход игрока {player} ')
        if player not in ['Bot', 'SuperBot']:
            move = tryInputInt(maxCandys)
        elif player == 'Bot':
            move = bot(maxCandys)
            print(move)
        elif player == 'SuperBot':
            move = SuperBot(tableCandys, maxCandys)
            print(move)
        tableCandys -= move
        if tableCandys <= 0:
            print(f'Победил игрок {player} ')
            input('Для возврата в меню нажмите Enter ')
        if gameMode == 1:
            player = 'Player1' if player == 'Player2' else 'Player2'
        if gameMode == 2:
            player = 'Player' if player == 'Bot' else 'Bot'
        if gameMode == 3:
            player = 'Player' if player == 'SuperBot' else 'SuperBot'
    return menu()


def bot(maxCandys):
    return random.randint(1, maxCandys)


def tryInputInt(maxCandys):
    x = 0
    while not (1 <= x <= maxCandys):
        try:
            x = int(input(f'Введите число от 1 до {maxCandys} '))
        except:
            print("Неверное значение")
            return tryInputInt(maxCandys)
    return x


def SuperBot(tableCandys, maxCandys):
    return tableCandys % (maxCandys + 1)

menu()
