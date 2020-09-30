import pyautogui
from time import sleep
import pyfiglet

words = "12345678910"

sleep(1)
for word in words:
    pyautogui.typewrite(words)
    pyautogui.press("enter")

    print(word)
