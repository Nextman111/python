from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from bot_init import bot, dp


class CalculatorStates(StatesGroup):
    calc_type = State()
    argument1 = State()
    argument2 = State()
    action = State()


async def command_calc_type(message: types.Message, state: FSMContext):
    await message.answer('Выберите режим калькулятора\n')

    async with state.proxy() as data:
        data['calc_type'] = message.text
    await CalculatorStates.calc_type.set()

    await CalculatorStates.next()


async def command_argument1(message: types.Message, state: FSMContext):
    await message.answer('Введите первый аргумент\n')
    # await CalculatorStates.argument1.set()

    async with state.proxy() as data:
        data['argument1'] = message.text

    await CalculatorStates.next()


async def command_argument2(message: types.Message, state: FSMContext):
    await message.answer('Введите второй аргумент\n')
    # await CalculatorStates.argument2.set()

    async with state.proxy() as data:
        data['argument2'] = message.text

    await CalculatorStates.next()


async def command_action(message: types.Message, state: FSMContext):
    await message.answer('Выберите действие\n')
    # await CalculatorStates.action.set()

    async with state.proxy() as data:
        data['action'] = message.text

    await state.finish()
