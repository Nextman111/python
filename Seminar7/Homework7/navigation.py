# Модуль навигации по калькулятору
import input_output as io
import os
import complex as complex
import rational as rational
import log as log


def navigation():
    os.system('cls')
    print('Выберите режим калькулятора :')

    menu_ = menu()
    io.print_menu(menu_)

    selected_menu = io.try_input_int(menu_.keys(), 'Введите номер режима ')

    if selected_menu:
        os.system('cls')
        run_mode(selected_menu)


def menu():
    return {1: ('Рациональные числа', rational),
            2: ('Комплексные числа', complex)
            }


def obj_menu(obj):
    return {1: ('Сумма', obj.sum, '+'),
            2: ('Разность', obj.difference, '-'),
            3: ('Произведение', obj.multiple, '*'),
            4: ('Деление', obj.divide, '/')
            }


def run_mode(selected):
    obj = menu()[selected][1]
    obj.message()
    args = obj.init_args()

    obj_actions = io.print_menu(obj_menu(obj))
    operation = io.try_input_int(obj_actions.keys(), 'Введите номер действия ')

    result = obj_actions[operation][1](*args)
    action = obj_actions[operation][2]

    result_args = tuple(map(obj.output, [*args, result]))
    result_line = io.print_result(result_args, action)

    log.init_args()
    log_line = log.line_generator(log.cure_time, result_line)
    log.log_write(log.f_name, log_line)

    input('Нажмите Enter чтобы вернуться в меню')
    navigation()
