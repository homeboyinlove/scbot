from set_bot_commands import set_default_commands


async def on_startup(dp):
    from notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers.users.echo import dp

    executor.start_polling(dp, on_startup=on_startup)
