import pyautogui
import keyboard
import time

def click():
    while True:
        if keyboard.is_pressed("q"):
            pyautogui.click()
            time.sleep(0.1)

if __name__ == "__main__":
    click()