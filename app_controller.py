import pyautogui as pg # * for hotkeys
import time # * for some interval between actions
import os # * for running commands


# * object for Windows 10 & 11
# ! This may not work on Windows 7 or below.

class windows_controller: 
    def __init__(self):
        pass
    def cmd_color(self,value):  #  can be used to change the color of a console based program
        if value == None:
            os.system('color')
        else:
            os.system(f"color {value}")
    def clear_cmd(self):  #  clears the cmd and makes a fresh clean look
        os.system('cls')
    def open_settings(self): #  WIN + I
        pg.hotkey('win','i')
    def open_cpanel(self): #  Opens with RUN
        pg.hotkey('win','r')
        time.sleep(2)
        pg.write('control')
        time.sleep(2)
        pg.press('enter')
    def open_cmd(self): #  Opens with RUN
        pg.hotkey('win','r')
        time.sleep(2)
        pg.write('cmd')
        time.sleep(2)
        pg.press('enter')
    def minimize_all(self): #  WIN + M
        pg.hotkey('win','m')
    def open_start(self): #  WIN
        pg.press('win')
    def open_activity_center(self): #  WIN + A
        pg.hotkey('win','a')
    def open_file_explorer(self): #  WIN + E
        pg.hotkey('win','e')
    def create_desktop(self): #  WIN + CTRL + D
        pg.hotkey('win','ctrl','d')
    def shutdown(self): #  ALT + F4 & ENTER
        os.system('shutdown /s')
    def restart(self): #  ALT + F4 & ENTER
        os.system('shutdown /r')
    def fullscreen(self): #  F11 / fn + f11
        pg.press('f11')
    def open_task_manager(self): #  CTRL + SHIFT + C
        pg.hotkey('ctrl','shift','c')
    def open_search(self): #  WIN + S
        pg.hotkey('win','s')
    def open_xbox(self): #  WIN + G
        pg.hotkey('win','g')
    def open_run(self): #  WIN + R
        pg.hotkey('win','r')
    def new_tab(self): #  CTRL + T
        pg.hotkey('ctrl','t')
    def print(self): #  ctrl  + p
        pg.hotkey('ctrl','p')
    def save(self): # ctrl + s
        pg.hotkey('ctrl','s')
    def save_as(self): # ctrl + shift + s
        pg.hotkey('ctrl','shift','s')
    def alert(self,value_str,title):
        pg.alert(text=value_str,title=title)



# ! Currently this is not supported for Linux, Unix and Mac computers..