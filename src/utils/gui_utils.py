import time
import webbrowser

import pyautogui
import pyperclip


def open_url(url: str):
    """
    打开网址
    """
    webbrowser.open(url)


def write(value: str):
    """
    输入文字
    pyautogui 不支持中文, 改用 pyperclip 实现
    pyautogui.write(value)
    """
    pyperclip.copy(value)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')


def click(x: int, y: int):
    """
    鼠标点击
    """
    pyautogui.click(x, y)


def click_text(text: str):
    pass


def click_img(img: str, confidence: float = 0.8):
    x, y, width, height = pyautogui.locateOnScreen(img, confidence=confidence)
    x, y = pyautogui.center(x, y, width, height)
    pyautogui.click(x, y)
