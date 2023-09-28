from aiogram.utils import executor
from bot_init import dp, bot
import handlers.fsm as fsm
import handlers.general as general
# Регистрация обработчиков сообщений

# dp.register_message_handler(hd.command_handler, commands=commands_list)
fsm.register_handlers(dp=dp)
general.register_handlers(dp=dp)

if __name__ == '__main__':
    print('Starting bot')
    executor.start_polling(dp,)

