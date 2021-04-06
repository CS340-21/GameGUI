from tkinter import *


root = Tk()
root.geometry("800x500")
root.title("Tasks to be Completed")
numItems = 0
checklist = []

# it SHOULD delete everything that was checked...not yet working right
def removeAll(warning):
    global numItems
    for i in reversed(range(len(checklist))):
        if checklist[i].var.get() == 1:
            checklist[i].c.destroy()
            checklist.pop(i)
            numItems -= 1
            continue
    warning.destroy()

# A warning pops up before deletion
def removeEntry():
    warning = Tk()
    l   = Label(warning, text="Are you sure you want to remove the selected entry(s)?").grid(row=0, column = 1)
    no  = Button(warning, text="No", padx=100, command=warning.destroy).grid(row=1, column=2)
    yes = Button(warning, text="Yes", padx=100, command=lambda: removeAll(warning)).grid(row=1, column=0)

def editEntry():
    editWindow = Tk()
    editWindow.geometry("200x200")
    indices = []
    numChecked = 0
    for i in checklist:
        if i.var.get() == 1:
            l = Label(editWindow, text=i.c.cget("text")).grid(row=numChecked, column=0)
            e = Entry(editWindow).grid(row=numChecked, column=1)
            numChecked += 1

# This allows the user to push the edit button
# ONLY when there is a box checked
def enableEdit():
    for i in checklist:
        if i.var.get() == 1:
            editButton.config(state=NORMAL)
            removeButton.config(state=NORMAL)
            break
        editButton.config(state=DISABLED)
        removeButton.config(state=DISABLED)

# Currently stores an individual checkbox, will later store dates
class entry():

    def __init__(self, item):
        self.var = IntVar()
        self.c = Checkbutton(root, variable=self.var, text=item, command=enableEdit)


def pushToList(item):
    global numItems
    global checklist

    # prints new item to main window as long as something was typed in
    if item != "":
        checklist.append(entry(item))
        checklist[numItems].c.grid(row=numItems, column=1)
    # remove congratulatory message if new work is added
        if numItems == 0:
            noWork.destroy()
        numItems += 1

# Opens a new window for the user to input a task
def addItem():
    itemEntry = Tk()
    itemEntry.geometry("250x100")
    e = Entry(itemEntry)
    e.grid(row=0, column=3)
    # Button must be pushed after item is entered
    confirm = Button(itemEntry, text='Add Item', command=lambda: pushToList(e.get())).grid(row=2, column=5)
    close = Button(itemEntry, text="Close", command=itemEntry.destroy).grid(row=2, column=6)

# If there are no tasks left, print a congratulations
if numItems == 0:
    noWork = Label(root, text="You've finished all of your work. Great job!")
    noWork.grid(row=0, column=0)

# If user pushes this button, they can add a new entry to the list
newEntry = Button(root, text="New Entry", padx=50, command=addItem)
newEntry.grid(row=8, column=3)

# This button allows you to edit an entry
editButton = Button(root, text="Edit Entry(s)", padx=50, state=DISABLED, command=editEntry)
editButton.grid(row=8, column=2)

removeButton = Button(root, text="Remove Entry(s)", padx=50, state=DISABLED, command=removeEntry)
removeButton.grid(row=8, column=1)

root.mainloop()
