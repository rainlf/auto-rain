import pyautogui
from cnocr import CnOcr

"""
Demo 站点: https://huggingface.co/spaces/breezedeus/CnOCR-Demo
检测模型文件所在的根目录: C:\\Users\\Rain\\AppData\\Roaming\\cnstd
识别模型文件所在的根目录: C:\\Users\\Rain\\AppData\\Roaming\\cnocr
"""

ocr = CnOcr(
    det_model_name='ch_PP-OCRv3_det',
    rec_model_name='densenet_lite_136-gru',
)


def test_screenshot():
    screenshot = pyautogui.screenshot()
    out = ocr.ocr(screenshot)
    for line in out:
        text = line['text']
        x = line['position'][0][0]
        y = line['position'][0][1]
        width = line['position'][1][0] - x
        height = line['position'][3][1] - y
        print(text, x, y, width, height)


test_screenshot()
