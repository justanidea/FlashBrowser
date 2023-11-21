import os
import pyautogui
from datetime import datetime
from PIL import Image
import dxcam
#value to check : 0 210 255   (935 971)
class Screenshot():
    def __init__(self) -> None:
        self.camera = dxcam.create()
        if not os.path.exists("saved\\screenshots\\"): 
            os.makedirs("saved\\screenshots\\") 
        self.path = 'saved\\screenshots\\'
        self.log_path = 'saved\\'
        
    def take_screenshot(self):   
        with open(os.path.join(self.log_path, "logs.txt"), 'r+') as logs:
            previous_logs = logs.read()
            window = pyautogui.getWindowsWithTitle("Flash Browser")
            if len(window) < 1:
                print("[ERR] Could not recognize FlashBrowser")
            else:
                window = window[0]
                if window.isActive:
                    left, top = window.topleft
                    right, bottom = window.bottomright
                    box = (left+10,  top, right-10, bottom)
                    max_width, max_height = pyautogui.size()
                    x = int(max_width * 0.338671875)
                    x2 = int(max_width * 0.365234375)
                    y = int(max_height * 0.65)
                    r,g,b = pyautogui.pixel(x, y)
                    popup = False
                    if g != 210:
                        r,g,b = pyautogui.pixel(x2, y)
                        if g == 210:
                            popup = True
                    else: 
                        popup = True
                    if popup == True:
                        img_name = str(datetime.now().strftime("%d_%m_%Y-%H_%M_%S"))
                        imageRef = self.path + img_name + ".png"
                        im_array = self.camera.grab()
                        end = datetime.strptime(datetime.now().strftime("%H:%M:%S:%f"), "%H:%M:%S:%f") 
                        im = Image.fromarray(im_array)
                        
                        im = im.crop(box)
                        im.save(imageRef)
                        log = f"[{str(datetime.now().strftime('%H:%M:%S'))}] screenshot saved\n"
                        logs.write(log)
                        return end
                    else:
                        log = f"[{str(datetime.now().strftime('%H:%M:%S'))}] ERR: no popup could be isolated\n"
                        end = datetime.strptime(datetime.now().strftime("%H:%M:%S:%f"), "%H:%M:%S:%f") 
                        logs.write(log)
                        return end
                    
