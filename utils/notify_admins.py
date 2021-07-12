import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            # when bot is launched notify admins about it
            await dp.bot.send_message(chat_id=admin, text=f"Бот запущен и готов к работе")
        except Exception as err:
            logging.error(err)

