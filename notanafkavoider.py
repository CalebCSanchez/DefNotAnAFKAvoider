from pynput.keyboard import Key, Controller
import random
import time
list1 = [60, 317, 273, 186,  543] 
keyboard = Controller()
key = "esc"
input("Press any Key to start")
while (True):
    
    keyboard.press(key)
    keyboard.press(key)
    time.sleep(random.choice(list1))
