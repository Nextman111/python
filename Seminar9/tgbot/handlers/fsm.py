from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from . import complex as cmplx
from . import rational as rational
from . import log as log


def result_calc(calc_type, argument1, argument2, action) -> str:
    calc = None
    match calc_type:
        case 'комплексный':
            calc = cmplx
        case 'рациональный':
            calc = rational

    argument1 = calc.str_to_argument(argument1)
    argument2 = calc.str_to_argument(argument2)

    res = None

    print(argument1)
    print(argument2)
    print(action)

    match action:
        case '+':
            res = calc.sum(argument1, argument2)
        case '-':
            res = calc.divide(argument1, argument2)
        case '*':
            res = calc.multiple(argument1, argument2)
        case '/':
            res = calc.difference(argument1, argument2)

    result = calc.output(res)

    log.init_args()
    log_line = log.line_generator(log.cure_time,
                                  log.print_result(calc.output(argument1),
                                                   calc.output(argument2),
                                                   action,
                                                   result)
                                  )
    log.log_write(log.f_name, log_line)

    return result


calc_type =['рациональный', 'комплексный']
action = {'+', '-', '*', '/'}


class CalculatorStates(StatesGroup):
    """
    Список состояний бота, для выбора типа калькулятора,
    ввода аргументов и действия над ними
    """
    calc_type = State()
    argument1 = State()
    argument2 = State()
    action = State()


async def calc_start(message: types.Message, state: FSMContext):
    # Создаем клавиатуру с возможными вариантами выбора типа калькулятора
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Передаем названия кнопок
    for type_name in calc_type:
        keyboard.add(type_name)

    # Отправляем сообщение пользователю, и как параметр клавиатуру
    await message.answer("Выберите тип калькулятора:", reply_markup=keyboard)
    # Устанавливаем состояние выбора типа калькулятора (calc_type)
    await state.set_state(CalculatorStates.calc_type.state)


async def waiting_calc_type(message: types.Message, state: FSMContext):
    # Проверка ввода
    if message.text.lower() not in calc_type:
        await message.answer("Выберите тип калькулятора:")
        return

    # Проверка прошла
    # Задаем значение полю состояния
    await state.update_data(calc_type=message.text.lower())

    # Меняем состояние на новое (argument1) и ожидаем ввода аргумента
    await state.set_state(CalculatorStates.argument1.state)
    await message.answer("Введите аргумент 1:", reply_markup=types.ReplyKeyboardRemove())


async def waiting_argument1(message: types.Message, state: FSMContext):
    # Задаем значение полю состояния
    await state.update_data(argument1=message.text.lower())

    # Меняем состояние на новое и ожидаем ввода аргумента
    await state.set_state(CalculatorStates.argument2.state)
    await message.answer("Введите аргумент 2:")


async def waiting_argument2(message: types.Message, state: FSMContext):
    await state.update_data(argument2=message.text.lower())

    # Меняем состояние на новое и ожидаем ввода аргумента
    await state.set_state(CalculatorStates.action.state)

    # Создаем клавиатуру с возможными вариантами выбора действия
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in action:
        keyboard.add(i)
    await message.answer("Выберите действие:", reply_markup=keyboard)


async def waiting_action(message: types.Message, state: FSMContext):
    # Проверка ввода
    if message.text not in action:
        await message.answer("Выберите действие:")
        return

    # Проверка прошла
    # Задаем значение полю состояния
    await state.update_data(action=message.text)

    variable_data = await state.get_data()
    res = ''

    for key, val in variable_data.items():
        res += f'{key} = {val}\n'

    await message.answer(res, reply_markup=types.ReplyKeyboardRemove())

    await message.answer(result_calc(variable_data['calc_type'],
                                     variable_data['argument1'],
                                     variable_data['argument2'],
                                     variable_data['action']))

    # Выходим из режима FMS
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(calc_start, commands='calc', state='*')
    dp.register_message_handler(waiting_calc_type, state=CalculatorStates.calc_type)
    dp.register_message_handler(waiting_argument1, state=CalculatorStates.argument1)
    dp.register_message_handler(waiting_argument2, state=CalculatorStates.argument2)
    dp.register_message_handler(waiting_action, state=CalculatorStates.action)

