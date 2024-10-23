"""
@author rain
@date 9/4/2024 3:00 PM
"""

import threading
import time

import keyboard
import pyautogui

running = True


def listen_stop():
    global running
    keyboard.wait('F10')
    print("F10 pressed, stop...")
    running = False


def touch_fish():
    while running:
        pyautogui.click(200, 200)
        time.sleep(1)
        pyautogui.click(200, 400)
        time.sleep(1)
        pyautogui.click(400, 400)
        time.sleep(1)
        pyautogui.click(400, 200)
        time.sleep(1)


def run_task():
    stop = threading.Thread(target=listen_stop)
    stop.start()
    print("Process started, Press 10 to stop")
    touch_fish()
    stop.join()


if __name__ == '__main__':
    run_task()
