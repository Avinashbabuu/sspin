from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.utils import executor
from aiogram.fsm.storage.memory import MemoryStorage
import config

from handlers import start, spin, balance, refer, withdraw, admin, ui

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

start.register_handlers(dp)
spin.register_handlers(dp)
balance.register_handlers(dp)
refer.register_handlers(dp)
withdraw.register_handlers(dp)
admin.register_handlers(dp)
ui.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)