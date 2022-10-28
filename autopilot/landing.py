import pyautogui
import time
import pydirectinput

print('Shift now')
time.sleep(5)
pyautogui.scroll(-2500) 
while True:
    pydirectinput.press('w',presses=60)
    pydirectinput.press('b',presses=200)
    break
