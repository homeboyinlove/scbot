from aiogram import Dispatcher

from data.config import admin_id


async def on_startup_notify(dp: Dispatcher):
    for admin in admin_id:
        await dp.bot.send_message(admin, "Бот запущен и готов к работе")
