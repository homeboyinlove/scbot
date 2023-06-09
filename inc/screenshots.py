import mss.tools
import pytesseract
from PIL import Image
import cv2
import time

def screen(monitor):
    with mss.mss() as sct:
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        return output


def screen_name():
    monitor = {"top": 515, "left": 1235, "width": 275, "height": 25}
    screen(monitor)
    img = cv2.imread(r'sct-515x1235_275x25.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    custom_config = r'--oem 3 --psm 6'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    name = pytesseract.image_to_string(img, lang='rus+eng', config=custom_config)
    return name.strip()


def screen_price():
    monitor = {"top": 525, "left": 1660, "width": 185, "height": 50}
    screen(monitor)
    img = Image.open('sct-525x1660_185x50.png')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    price = pytesseract.image_to_string(img, lang='rus')
    return price.strip()

# while True:
#     print(screen_name())