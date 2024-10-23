import threading

import keyboard

running = False


def listen_stop():
    global running
    keyboard.wait('F10')
    print("F10 pressed, stop...")
    running = False


def open_switch() -> threading.Thread:
    global running
    running = True
    stop = threading.Thread(target=listen_stop)
    stop.start()
    print("Process started, Press 10 to stop")
    return stop
