import pyautogui
import utils.file_utils as file_utils

from utils.log_utils import log


def write(data: str) -> bool:
    pyautogui.write(data)
    return True


def click(*img: str, confidence: float = 0.8) -> bool:
    image: str = file_utils.get_assert_file_path(*img)
    try:
        x, y, width, height = pyautogui.locateOnScreen(image, confidence=confidence)
        x, y = pyautogui.center((x, y, width, height))
        log.debug(f"click {x}.{y}")
        pyautogui.click(x, y, interval=0.3)
        return True
    except Exception as e:
        # log.warning(f"image not found: {image}")
        return False

