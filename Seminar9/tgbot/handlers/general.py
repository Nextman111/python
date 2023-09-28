from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import Message, ReplyKeyboardRemove


async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Я умею считать рациональные и комплексные числа.\
        \nдля начала используй команду /calc\nдля отмены команду /cancel",
        reply_markup=types.ReplyKeyboardRemove()
    )


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Все отменено\n начните заново /calc", reply_markup=types.ReplyKeyboardRemove())


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start', 'help'], state='*')
    dp.register_message_handler(cmd_cancel, commands='cancel', state='*')
