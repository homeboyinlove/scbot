from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile
from filters.private_chat import IsPrivate
from data.config import admin_id
from inc.screenshots import screen_name, screen_price
from loader import sc_prices, dp
from aiogram.utils.markdown import hbold
import serial
import pyautogui
import time

@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start_deeplink(message: types.Message):

    arduino = serial.Serial('COM3', 115200, timeout=0)

    while True:
        pyautogui.moveTo(x=1798, y=440)
        arduino.write(b'C1')  # отправка команды клика на ардуино
        time.sleep(0.7)

        screen_name()
        screen_price()
        name = screen_name()
        word = screen_price()
        if word != '':
            hlp = ''
            for i in word:
                if i.isdigit():
                    hlp += i
            price_final = int(hlp)

            if name in sc_prices.keys() and price_final <= int(sc_prices[name]):
                pyautogui.moveTo(x=1732, y=540)
                arduino.write(b'C1')
                arduino.flush()
                time.sleep(0.05)
                pyautogui.moveTo(x=1765, y=586)
                arduino.write(b'C1')
                arduino.flush()
                time.sleep(1)
                text = f"{hbold('Название: ')} {name}\n" \
                       f"{hbold('Цена: ')} {str(price_final)}\n" \
                       f"{hbold('--------------------')}"
                for admin in admin_id:
                    await dp.bot.send_message(admin, text)
                    # photo = InputFile("sct-515x1235_275x25.png")
                    # await bot.send_photo(admin, photo= photo)
                    # photo = InputFile("sct-525x1660_185x50.png")
                    # await bot.send_photo(admin, photo=photo)
                    # await dp.bot.send_message(admin, "--------------------------")