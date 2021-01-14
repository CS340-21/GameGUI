import pyautogui as auto
import PySimpleGUI as sg
import time

x, y = auto.size()
print(x)
print(y)

MAX_ROWS = 2
MAX_COL = 3
board = [[1 for j in range(MAX_COL)] for i in range(MAX_ROWS)]
layout = [[sg.Button(size=(20, 10), button_color=('red', 'green'), key=(i,j)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
window = sg.Window(title="6q-Interface", layout=layout)  # margins=(1200 ,1000)).read()

# print(window)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    else:
        window[event].update(button_color=("green", "red"))
        window = window.refresh()
        time.sleep(.5)
        window[event].update(button_color=("red", "green"))
        window = window.refresh()

window.close()
