import os
import pyautogui
from datetime import datetime
from PIL import Image
import dxcam

class Screenshot():
    def __init__(self) -> None:
        self.camera = dxcam.create()
        if not os.path.exists("saved\\screenshots\\"): 
            os.makedirs("saved\\screenshots\\") 
        self.path = 'saved\\screenshots\\'
        self.log_path = 'saved\\'
        
    def take_screenshot(self):   
        with open(os.path.join(self.log_path, "logs.txt"), 'r+') as logs:
            window = pyautogui.getWindowsWithTitle("Flash Browser")
            if len(window) != 1:
                print("[ERR] Could not recognize FlashBrowser")
            else:
                window = window[0]
                if window.isActive:
                    left, top = window.topleft
                    right, bottom = window.bottomright
                    box = (left+10,  top, right-10, bottom)
                    img_name = str(datetime.now().strftime("%d_%m_%Y-%H_%M_%S"))
                    imageRef = self.path + img_name + ".png"
                    im_array = self.camera.grab()
                    end =datetime.strptime(datetime.now().strftime("%H:%M:%S:%f"), "%H:%M:%S:%f") 
                    im = Image.fromarray(im_array)
                    im = im.crop(box)
                    im.save(imageRef)
                    log = f"[{str(datetime.now().strftime('%H:%M:%S'))}] screenshot saved\n"
                    logs.write(log)
                    return end
                    
