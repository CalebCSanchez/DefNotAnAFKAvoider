from pynput.keyboard import Controller, Key, Listener
import random
import keyboard
import time
import sys

with open('file_path', 'w') as file:
    file.write('hello world !')


# pressed = False

# def on_release(key):
#     if key == Key.enter:
#         return False

# def on_press(key):
#     if key == Key.enter:
#         return True

# with Listener(on_press=on_press, on_release=on_release) as listener:
#     yn = input("enter something")
#     listener.join()
#     while(pressed):
#         quit_key = keyboard.read_key()
#     print(quit_key)


# def wait_for_enter_to_be_up():
#     while True:
#         if keyboard.is_pressed('enter'): 
#             continue
#         break

def esc_is_pressed():
        for i in range(4):
            yn = input('WARNING: Esc can be used, but a quit key must be remapped.\nAre you sure you want to use the ESC key(y/n)?\n')
            # wait_for_enter_to_be_up()
            time.sleep(1) #I literally can't figure out how to stop it from capturing the enter in the input field and nobody seems to be helping python sucks
            if len(yn) == 0:
                print('Please type y or n')
                continue
            if yn[0] == 'y' or yn[0] == 'Y':
                print("Type the key you want to use to quit the program:")
                quit_key = keyboard.read_key() 
                if quit_key == 'esc':
                    print('wait a second....')
                    continue
                afk_key = 'esc'
                break
            elif yn[0] == 'n' or yn[0] == 'N':
                quit_key = 'esc'
                afk_key = 'NaN'
                break
            print('Please type y or n')
        if i == 3:
                print('Bruh...')
                sys.exit()
        return quit_key, afk_key          

print(esc_is_pressed())


# def not_an_afk_avoider():
#     list1 = [60, 317, 273, 186,  543] 
#     keyboard_controller = pynkeyboard.Controller()
#     quitkey = 'esc'
#     afk_key = 'w'
#     try:
#         print("Press a key to use (aka up arrow, w, ESC):")
#         if keyboard.is_pressed('esc'):
            
                
#             # if quitkey[0] == 'y' or 'Y':
#             # sys.exit()
#             # elif quitkey[0] == 'n' or 'N':
#             # break
#             # print('please type yes or no')
#         key = keyboard.read_key()
#     except:
#         print('invalid function')

    # while True:
    # if keyboard.is_pressed('esc'):
    # break
    # keyboard_controller.press(key)
    # keyboard_controller.press(key)
    # time.sleep(random.choice(list1))
