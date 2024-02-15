import webbrowser
import pyautogui
import win32api
import win32con
import keyboard
import random
import time

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(random.randint(10, 30) / 1000)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

EXIT_KEY = 'q'  # interrupt the process by pressing this key (we cant use mouse)
URL = 'https://gameforge.com/en-US/littlegames/magic-piano-tiles'
positions = [  # positions of lanes to be checked
    (430, 500),
    (490, 500),
    (560, 500),
    (650, 500)
]

webbrowser.open(URL)
input('Press <enter> when the page is loaded completely...')
time.sleep(2)

while not keyboard.is_pressed(EXIT_KEY):
    for x, y in positions:
        if not pyautogui.pixel(x, y)[2]:  # if the pixel was black
            click(x, y)
