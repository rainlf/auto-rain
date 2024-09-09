"""
@author rain
@date 9/4/2024 3:00 PM
"""

import threading
import time

import keyboard
import pyautogui


running = False


def listen_start():
    global running
    keyboard.wait('F9')
    running = True


def listen_stop():
    global running
    keyboard.wait('F10')
    running = False


def main():
    start = threading.Thread(target=listen_start)
    stop = threading.Thread(target=listen_stop)
    start.start()
    stop.start()

    print("Press F9 to start")
    start.join()
    print("Process started, Press 10 to stop")
    while running:
        pyautogui.click(200, 200)
        time.sleep(1)
        pyautogui.click(200, 400)
        time.sleep(1)
        pyautogui.click(400, 400)
        time.sleep(1)
        pyautogui.click(400, 200)
        time.sleep(1)

    stop.join()


if __name__ == '__main__':
    main()
