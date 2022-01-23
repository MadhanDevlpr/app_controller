import pyautogui as pg # * for hotkeys
import time # * for some interval between actions
import os # * for running commands


# * object for Windows 10 & 11
# ! This may not work on Windows 7 or below.

class device: 
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
        os.system('control')
    def minimize_all(self): #  WIN + M
        pg.hotkey('win','m')
    def open_start(self): #  WIN
        pg.press('win')
    def open_activity_center(self): #  WIN + A
        pg.hotkey('win','a')
    def open_file_explorer(self): #  WIN + E
        pg.hotkey('win','e')
    def createNew_desktop(self): #  WIN + CTRL + D
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
    def print_page(self): #  ctrl  + p
        pg.hotkey('ctrl','p')
    def save(self): # ctrl + s
        pg.hotkey('ctrl','s')
    def save_as(self): # ctrl + shift + s
        pg.hotkey('ctrl','shift','s')
    def open_calculator(self):
        os.system('calc')
    def open_iexpress(self):
        os.system('iexpress')
    def open_hardware_wiz(self):
        os.system('hdwwiz')
    def open_admintools(self):
        os.system('control admintools')
    def bluetooth_transfer(self):
        os.system('fsquirt')
    def open_characterMap(self):
        os.system('charmap')
    def keyboard_properties(self):
        os.system('control keyboard')
    def mouse_properties(self):
        os.system('control mouse')
    def net_connections(self):
        os.system('control netconnections')
    def open_notepad(self):
        os.system('notepad')
    def open_keyboard(self):
        os.system('osk')
    def remote_dekstop(self):
        os.system('mstsc')
    def open_features(self):
        os.system('optionalfeatures')
    def open_magnifier(self):
        os.system('magnify')
    def open_wordpad(self):
        os.system('write')
    def run_command(self,command_value):
        os.system(command_value)
    def git_add(self,files):
        os.system(f'git add {files}')
    def git_commit(self,message):
        os.system(f'git commit -m "{message}"')
    def git_pull(self):
        os.system('git pull')
    def git_push(self, branch): # Name of branch is required
        os.system(f'git push origin {branch}')
    def git_status(self):
        os.system('git status')
    def open_cmd(self):
        os.system('start')
        os.system('cd %USERPROFILE%')
    def trace(self,address):
        os.system(f'tracert {address}')
    