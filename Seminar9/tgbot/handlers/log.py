# Файл содержит методы записи логов в файл
import datetime as dt


f_name = ''
cure_time = ''


# Инициализация текущей даты для записи в лог
def init_args():
    global f_name
    global cure_time
    date = dt.datetime.now()
    f_name = f'{date.strftime("%d-%m-%y")}.txt'
    cure_time = date.strftime("%H:%M:%S")


# Формирует строку для записи
def line_generator(cure_time, lines_string):
    return f'{cure_time} {lines_string}\n'


def log_write(f_name, n):
    if n:
        with open(f_name, 'a') as data:
            data.write(n)

