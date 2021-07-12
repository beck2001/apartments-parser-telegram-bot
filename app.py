import logging
from aiogram import Dispatcher, executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher: Dispatcher):
    # set default commands
    await set_default_commands(dispatcher)

    # notify admins about bot
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, on_startup=on_startup, skip_updates=True)

