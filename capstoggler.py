from pynput.keyboard import Key, Controller
import time
keyboard=Controller()
def toggle():
    timeout=time.time()+30
    while True:
        keyboard.press(Key.caps_lock)
        time.sleep(0.1)
        keyboard.release(Key.caps_lock)
        if time.time()>timeout:
            break
toggle()
