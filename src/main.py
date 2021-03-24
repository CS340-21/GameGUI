from tkinter import *

root = Tk()
root.geometry("500x500")
numItems = 0
checklist = []

def pushToList(item):
    global numItems
    global checklist
    # prints new item to main window as long as something was typed in
    if item != "":
        var = IntVar()
        c = Checkbutton(root, text=item, variable=var)
        checklist.append(c)
        checklist[numItems].grid(row=numItems, column=1)
    # remove congratulatory message if new work is added
        if numItems == 0:
            noWork.destroy()
        numItems += 1

# Opens a new window for the user to input a task
def addItem():
    itemEntry = Tk()
    itemEntry.geometry("200x100")
    e = Entry(itemEntry)
    e.grid(row=0, column=3)
    # Button must be pushed after item is entered
    confirm = Button(itemEntry, text='Add Item', command=lambda: pushToList(e.get()))
    confirm.grid(row=2, column=5)


# If there are no tasks left, print a congratulations
if numItems == 0:
    noWork = Label(root, text="You've finished all of your work. Great job!")
    noWork.grid(row=0, column=3)

# If user pushes this button, they can add a new entry to the list
newEntry = Button(root, text="New Entry", padx=50, command=addItem)
newEntry.grid(row=8, column=8)

# This button allows you to edit an entry
editEntry = Button(root, text="Edit Entry", padx=50)
for i in checklist:
    print(i.var.get())
    if i.var.get() == 1:
        editEntry.grid(row=8, column=6)


root.mainloop()
