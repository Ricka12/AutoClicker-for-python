from pynput.mouse import Button, Controller
import time
import keyboard 
def autoClick():
    mouse = Controller()
    def click_pynput():
        mouse.position = (mouse.position[0], mouse.position[1])
        mouse.click(Button.left)
    while True:
        time.sleep(0.1)
        click_pynput()
        if keyboard.is_pressed('f5'): #press f5 to stop clicking
            break
keyboard.add_hotkey('f6', autoClick) #press f6 to strart clicking
keyboard.wait('esc + shift') #press shift + esc to stop program
