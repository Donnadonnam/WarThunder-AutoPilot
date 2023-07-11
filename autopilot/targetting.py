import pyautogui
import time
import pydirectinput

def find(Ukraine):
    while True:
        try:  
            time.sleep(20) 
            x,y = pyautogui.locateCenterOnScreen('Untitled.png',confidence=0.5,grayscale=True,region=(615,152,700,500))
            pydirectinput.click(x, y,button='left')
            
            print(x,y)
        except Exception as e:
            print(e)          
find(Ukraine=StopAsyncIteration)
