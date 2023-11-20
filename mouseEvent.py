from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

import json
# input_value = sys.argv[1]
is_mouse_event: bool = False

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
            # print(button)
            if msg == settings['macroName']:
                print(f"macro triggered", flush=True )

def on_release(key):
    msg = format(key.char)
    # print(msg, settings['macroName'])
    if msg == settings['macroName']:
        print("macro triggered", flush=True)
    if msg == "\x03":
        exit()
        
keyboard_listener = KeyboardListener(on_release=on_release)
mouse_listener = MouseListener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()


    
