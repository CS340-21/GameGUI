import pyautogui as auto
import PySimpleGUI as sg
import pandas as pd
import time
import csv

x, y = auto.size()
print(x)
print(y)

# Create a dictionary of all possible row and column values to loop through all possible options

MAX_ROWS = 2
MAX_COL = 2

print(x/MAX_COL)
print(y/MAX_ROWS)

df = pd.DataFrame()

board = [[1 for j in range(MAX_COL)] for i in range(MAX_ROWS)]
layout = [[sg.Button(size=(int(x/8/MAX_COL), int(y/17/MAX_ROWS)), button_color=('red', 'green'), key=(i,j)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
window = sg.Window(title="6q-Interface", size=(x, y), layout=layout)  # margins=(1200 ,1000)).read()

# print(window)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    else:
        window[event].update(button_color=('green', 'red'))
        window = window.refresh()
        time.sleep(.5)
        window[event].update(button_color=('red', 'green'))
        window = window.refresh()

        df = df.append([[MAX_ROWS, MAX_COL, event, None]], ignore_index=True)

headers = ['Max Rows', 'Max Cols', 'Block', 'Image']
df.columns = headers

file = 'block_test_results.csv'
df.to_csv(file, na_rep='-', header=True, index=False)

print(df)
window.close()
