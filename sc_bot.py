import mss.tools
import pytesseract
from PIL import Image
import cv2
import json
import serial
import time
import pyautogui

arduino = serial.Serial('COM3', 115200, timeout=0)
pyautogui.FAILSAFE=False


time.sleep(5)
def screen(monitor):
    with mss.mss() as sct:
        # monitor = {"top": 525, "left": 1235, "width": 600, "height": 35}
        # monitor = {"top": 525, "left": 1235, "width": 275, "height": 25}
        # monitor = {"top": 525, "left": 1660, "width": 185, "height": 50}

        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        return output


def main():
    with open("sc_prices.json", encoding="utf-8") as file:
        sc_prices = json.load(file)
    print(sc_prices)
    while True:
        pyautogui.moveTo(x=1798, y=440)
        arduino.write(b'C1')  # отправка команды клика на ардуино
        time.sleep(1)


        monitor = {"top": 515, "left": 1235, "width": 275, "height": 25}
        screen(monitor)
        img = cv2.imread(r'sct-515x1235_275x25.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        custom_config = r'--oem 3 --psm 6'
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        name = pytesseract.image_to_string(img, lang='rus+eng', config=custom_config)
        name_final = name.strip()
        print(name_final)

        monitor = {"top": 525, "left": 1660, "width": 185, "height": 50}
        screen(monitor)
        img = Image.open('sct-525x1660_185x50.png')
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        price = pytesseract.image_to_string(img, lang='rus')
        word = price.strip()
        if word != '':
            hlp = ''
            for i in word:
                if i.isdigit():
                    hlp += i
            price_final = int(hlp)
            print(int(hlp))
            if name_final in sc_prices.keys():
                print('yes')
                if price_final <= int(sc_prices[name_final]):
                    pyautogui.moveTo(x=1732, y=540)
                    arduino.write(b'C1')
                    arduino.flush()
                    time.sleep(0.1)
                    pyautogui.moveTo(x=1765, y=586)
                    arduino.write(b'C1')
                    arduino.flush()
                    time.sleep(0.1)
                    print('True')
            else:
                print('no')

        else:
            print(word)


if __name__ == "__main__":
    main()