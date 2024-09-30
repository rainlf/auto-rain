import pyautogui
from cnocr import CnOcr

"""
Demo 站点: https://huggingface.co/spaces/breezedeus/CnOCR-Demo
检测模型文件所在的根目录: C:\\Users\\Rain\\AppData\\Roaming\\cnstd
识别模型文件所在的根目录: C:\\Users\\Rain\\AppData\\Roaming\\cnocr
"""


def test_screenshot():
    screenshot = pyautogui.screenshot()
    ocr = CnOcr(
        det_model_name='ch_PP-OCRv3_det',
        rec_model_name='densenet_lite_136-gru',
    )
    out = ocr.ocr(screenshot)
    print(out)


test_screenshot()
