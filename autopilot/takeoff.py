import time
import pyautogui

print('Shift now')
time.sleep(20)
pyautogui.scroll(2500) 

pyautogui.mouseUp() #This differs from plane to plane, while lighter planes like the MiG-21 would take off with this command, heavier ones would need something like this

# pyautogui.mouseUp(x=850,y=300) #To get a proper push from the ground incase of heavier planes
