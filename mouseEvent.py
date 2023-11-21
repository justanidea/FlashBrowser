from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from screenshot import Screenshot
import json
from datetime import datetime
# input_value = sys.argv[1]
is_mouse_event: bool = False
scr = Screenshot()
path = 'preferences.json'
with open(path, 'r') as settings:
    settings = json.load(settings)
    if "Mouse" in settings['macroName']:
        # print("mouse key detected:" + settings['macroName'])
        is_mouse_event = True
        match settings['macro']:
            case 0:
                settings['macroName'] = "Button.left"
            case 1:
                settings['macroName'] = "Button.center"
            case 2:
                settings['macroName'] = "Button.right"
            case 3:
                settings['macroName'] = "Button.x1"
            case 4:
                settings['macroName'] = "Button.x2"
    else:
        # print("keyboard key detected:" + settings['macroName'])
        pass



def on_click(x, y, button, pressed):
    if is_mouse_event == True:
        if not pressed:
            msg = format(button)
            if msg == settings['macroName']:
                take_screenshot()

def on_release(key):
    msg = format(key.char)
    if msg == settings['macroName']:
        take_screenshot()
    if msg == "\x03":
        exit()

def take_screenshot():
    start =datetime.strptime(datetime.now().strftime("%H:%M:%S:%f"), "%H:%M:%S:%f")  
    print("macro triggered", flush=True)
    end = scr.take_screenshot()
    delta = end - start
    print(f"screenshot made after {delta} seconds", flush=True)
    
keyboard_listener = KeyboardListener(on_press=on_release)
mouse_listener = MouseListener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()


    
