from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)


dp.register_message_handler(echo_send)

executor.start_polling(dp, skip_updates=True)
