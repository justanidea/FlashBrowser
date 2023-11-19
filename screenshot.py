import pygetwindow
import time
import os
import pyautogui
import PIL
from datetime import datetime
from PIL import Image


x,y = pyautogui.size()
print(f"width={x}\theight={y}")
path = 'screenshots\\'
window = pyautogui.getWindowsWithTitle("Flash Browser")
if len(window) != 1:
    print("[ERR] Could not recognize FlashBrowser")
else:
    window = window[0]
    window.activate()
    print(window.isActive)
    left, top = window.topleft
    right, bottom = window.bottomright
    box = (left+10,  top, right-10, bottom)
    print(box)
    img_name = str(datetime.now().strftime("%d_%m_%Y-%H_%M_%S"))
    print(img_name)
    imageRef = path + img_name + ".png"
    print(imageRef)
    p = pyautogui.screenshot(imageRef)
    im = Image.open(imageRef)
    im = im.crop(box)
    im.save(imageRef)

