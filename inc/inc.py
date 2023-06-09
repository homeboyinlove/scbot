import mss
import numpy as np
import pytesseract
from PIL import Image
import cv2
import time

def screen():
    with mss.mss() as sct:
        # Grab the data for name
        name_monitor = {"top": 515, "left": 1235, "width": 275, "height": 25}
        name_sct_img = sct.grab(name_monitor)
        name_img = Image.frombytes("RGB", name_sct_img.size, name_sct_img.bgra, "raw", "BGRX")
        # Grab the data for price
        price_monitor = {"top": 525, "left": 1660, "width": 185, "height": 50}
        price_sct_img = sct.grab(price_monitor)
        price_img = Image.frombytes("RGB", price_sct_img.size, price_sct_img.bgra, "raw", "BGRX")
    return name_img, price_img

def screen_name(name_img):
    img = cv2.cvtColor(np.array(name_img), cv2.COLOR_RGB2BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    custom_config = r'--oem 3 --psm 6'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    name = pytesseract.image_to_string(img, lang='rus+eng', config=custom_config)
    return name.strip()

def screen_price(price_img):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    price = pytesseract.image_to_string(price_img, lang='rus')
    return price.strip()

s = time.time()
func()
print(time.time() - s)