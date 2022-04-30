import pyautogui as pg # * for hotkeys
import time # * for some interval between actions
import os # * for running commands


# * object for control over Linux

class device:
    def __init__(self):
        pass
    def open_notifications(self): #  WIN + M
        pg.hotkey('win','m')
    def open_activities(self): #  WIN
        pg.press('win')
    def switch_desktop(self): #  WIN + CTRL + D
        pg.hotkey('win','ctrl','d')
    def fullscreen(self): #  F11 / fn + f11
        pg.press('f11')
    def new_tab(self): #  CTRL + T
        pg.hotkey('ctrl','t')
    def print_page(self): #  ctrl  + p
        pg.hotkey('ctrl','p')
    def save(self): # ctrl + s
        pg.hotkey('ctrl','s')
    def save_as(self): # ctrl + shift + s
        pg.hotkey('ctrl','shift','s')
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
    def trace(self,web_url):
        os.system(f'tracert {web_url}')
    def ping(self,url):
        os.system(f'ping {url}')
