from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data import config

bot = Bot(token=config.TOKEN)
storage = MemoryStorage()
# storage = RedisStorage2()
dp = Dispatcher(bot=bot, storage=storage)
