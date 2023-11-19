import sys
import requests
import time
import asyncio
from pynput import mouse
# input_value = sys.argv[1]




def on_click(x, y, button, pressed):
    if not pressed:
        print(f"released {button}", flush=True )
    if button == button.right:
        return False



# Collect events until released
with mouse.Listener(
        on_click=on_click,
        ) as listener:
    listener.join()

