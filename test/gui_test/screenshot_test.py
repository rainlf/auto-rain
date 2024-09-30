import pyautogui
from PIL import ImageGrab

screenshot1 = ImageGrab.grab()
screenshot1.save('screenshot1.png')

screenshot2 = pyautogui.screenshot()
screenshot2.save('screenshot2.png')

screenshot3 = pyautogui.screenshot()
screenshot3 = screenshot3.convert('RGB')
screenshot3.save('screenshot3.png')
