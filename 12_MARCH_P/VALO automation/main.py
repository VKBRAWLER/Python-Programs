import keyboard
import time
import mouse
def press_key(key):
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)
def long_press_key(key, time = 1):
    keyboard.press(key)
    time.sleep(time)
    keyboard.release(key)
def sqrAFK():
    while(1):
        time.sleep(10)
        press_key('a')
        press_key('s')
        press_key('w')
        press_key('d')
def agentSelect():
        agentloc = 707
        mouse.move(agentloc, 919, absolute=True, duration=0.1)
        time.sleep(0.5)
        mouse.click('left')
        agentloc += 85
        mouse.move(agentloc, 919, absolute=True, duration=0.1)
        time.sleep(0.5)
        mouse.click('left')
        agentloc += 85
        mouse.move(agentloc, 919, absolute=True, duration=0.1)
        time.sleep(0.5)
        mouse.click('left')
        agentloc += 85
        mouse.move(agentloc, 919, absolute=True, duration=0.1)
        time.sleep(0.5)
        mouse.click('left')
        agentloc += 85
        mouse.move(agentloc, 919, absolute=True, duration=0.1)
        time.sleep(0.5)
        mouse.click('left')
        mouse.move(960, 732, absolute=True, duration=0.1) # lock in
        mouse.click('left')
def startNewGame():
        mouse.move(1030, 30, absolute=True, duration=0.1)
        time.sleep(0.5)
        mouse.click('left')
        mouse.move(930, 987, absolute=True, duration=0.1)
        time.sleep(0.5)
        mouse.click('left')
def move():   
        for i in range(5):
            keyboard.press('w')
            time.sleep(3)
            keyboard.release('w')
            keyboard.press('s')
            time.sleep(0.5)
            keyboard.release('s')
            if (i % 2 == 0):
                keyboard.press('a')
                time.sleep(3)
                keyboard.release('a')
            else:
                keyboard.press('d')
                time.sleep(3)
                keyboard.release('d')
        time.sleep(3)
        keyboard.press('space')
        keyboard.release('space')
def msg():
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.write('I am a AI bot, under development. Please ignore me. and don\'t report plzz :)')
    time.sleep(0.1)
    keyboard.press_and_release('enter')
num = 1
time.sleep(5)
while(1):
    print("Trigger " + str(num))
    move()
    startNewGame()
    move()
    agentSelect()
    msg()
    num += 1