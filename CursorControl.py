import pyautogui

print(pyautogui.position())
x, y = pyautogui.position()

pyautogui.dragTo(x+100, y+100, duration=5)