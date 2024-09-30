import pyautogui

def write(data: str) -> bool:
    """
    输入数据
    :param data:
    :return:
    """
    pyautogui.write(data)
