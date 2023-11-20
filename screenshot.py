import pygetwindow
import time
import os
import pyautogui
import PIL
from datetime import datetime
from PIL import Image

x,y = pyautogui.size()
if not os.path.exists("saved\\screenshots\\"): 
    os.makedirs("saved\\screenshots\\") 
path = 'saved\\screenshots\\'
log_path = 'saved\\'
with open(os.path.join(log_path, "logs.txt"), 'r+') as logs:
    previous_logs = logs.read()
    
    window = pyautogui.getWindowsWithTitle("Flash Browser")
    if len(window) != 1:
        print("[ERR] Could not recognize FlashBrowser")
    else:
        window = window[0]
        # print(window.isActive)
        if window.isActive:
            left, top = window.topleft
            right, bottom = window.bottomright
            box = (left+10,  top, right-10, bottom)
            img_name = str(datetime.now().strftime("%d_%m_%Y-%H_%M_%S"))
            imageRef = path + img_name + ".png"
            p = pyautogui.screenshot(imageRef)
            im = Image.open(imageRef)
            im = im.crop(box)
            im.save(imageRef)
            print('screenshot saved')
            log = f"[{str(datetime.now().strftime("%H:%M:%S"))}] screenshot saved\n"
            logs.write(log)
            
