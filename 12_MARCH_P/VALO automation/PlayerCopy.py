import mouse
import time
import keyboard
time.sleep(1)
keyboard.press('b')
keyboard.release('b')
mouse.move(200, 0, absolute=False, duration=0.1)
mouse.click('left')