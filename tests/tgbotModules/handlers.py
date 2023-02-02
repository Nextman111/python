from aiogram import types


async def echo_send(message: types.Message):
    await message.answer(message.text)

