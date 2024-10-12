import time
import webbrowser

import pyautogui
import pyperclip
from cnocr import CnOcr

ocr = CnOcr(
    det_model_name='ch_PP-OCRv3_det',
    rec_model_name='densenet_lite_136-gru',
)


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
    screenshot = pyautogui.screenshot()
    out = ocr.ocr(screenshot)
    for line in out:
        content = line['text']
        if text == content:
            x = line['position'][0][0]
            y = line['position'][0][1]
            width = line['position'][1][0] - x
            height = line['position'][3][1] - y
            x, y = pyautogui.center(x, y, width, height)
            pyautogui.click(x, y)


def click_img(img: str, confidence: float = 0.8):
    x, y, width, height = pyautogui.locateOnScreen(img, confidence=confidence)
    x, y = pyautogui.center(x, y, width, height)
    pyautogui.click(x, y)
