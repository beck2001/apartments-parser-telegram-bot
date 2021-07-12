from aiogram import Dispatcher, types


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "начать работу с ботом"),
            types.BotCommand("help", "вывести это сообщение с подсказками")
        ]
    )
