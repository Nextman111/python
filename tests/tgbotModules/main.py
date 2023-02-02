from aiogram.utils import executor
from bot_init import dp
import handlers as hd

dp.register_message_handler(hd.echo_send)

executor.start_polling(dp, skip_updates=True)
