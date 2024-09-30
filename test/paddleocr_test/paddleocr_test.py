import pyautogui
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr
import numpy as np


def orc_for_img():
    # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
    # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    img_path = './ch.jpg'
    result = ocr.ocr(img_path, cls=True)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)
    # 绘制结果
    result = result[0]
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')


def orc_for_screenshot():
    text = "文本"
    # Initialize PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    # Capture a screenshot
    screenshot = pyautogui.screenshot()
    # Convert the screenshot to a format compatible with PaddleOCR
    screenshot = screenshot.convert('RGB')
    # 将PIL图像转换为numpy数组
    image_np = np.array(screenshot)

    # 使用OCR模型进行文本检测和识别
    result = ocr.ocr(image_np, cls=True)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)

    # 查找匹配的文本及其位置
    for line in result:
        for item in line:
            if isinstance(item, dict) and 'text' in item and item['text'] == text:
                # 返回找到的文本框的坐标
                box = item['bbox']
                print("Text found at:", box)
    print("Text not found")


orc_for_screenshot()
