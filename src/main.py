from tkinter import *
import panas as pd
import pickle

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
        

class dateTime():
    def __init__(self, month, day, year, hour, minute):
        self.month = month
        self.day = day
        self.year = year
        self.hour = hour
        self.minute = minute

# Currently stores an individual checkbox, will later store dates
class entry():

    def __init__(self, item):
        self.var = IntVar()
        self.textstr = item
        self.dateTime = None
        self.c = Checkbutton(root, variable=self.var, text=item, command=enableEdit)

        
# may not need this, waiting to run to check functionality
def init_dates(month, day, year, hour, minute):
    try:
        mo = month.get()
        print(mo)
    except:
        mo = None
    try:
        d = day.get()
    except:
        d = None
    try:
        y = year.get()
    except:
        y = None
    try:
        h = hour.get()
    except:
        h = None
    try:
        mi = minute.get()
    except:
        mi = None

    return mo, d, y, h, mi

        
def pushToList(item, month, day, year, hour, minute):
    global numItems
    global checklist
    
    # prints new item to main window as long as something was typed in
    if item != "":
        e = entry(item)
        e.dateTime = dateTime(month, day, year, hour, minute)
        checklist.append(e)
        checklist[numItems].c.grid(row=numItems, column=1)
        dateLabel = Label(root, text=month + "/" + day + "/" + year + " " + hour + ":" + minute)
        dateLabel.grid(row=numItems, column=2)
    # remove congratulatory message if new work is added
        if numItems == 0:
            noWork.destroy()
        numItems += 1

# Opens a new window for the user to input a task
def addItem():
    itemEntry = Tk()
    itemEntry.geometry("400x400")
    eLabel = Label(itemEntry, text="Task:").grid(row=0, column=0)
    e = Entry(itemEntry)
    e.grid(row=0, column=1)
    monthLabel = Label(itemEntry, text="Month:").grid(row=2, column=0)
    month = Entry(itemEntry)
    month.grid(row=2, column=1)
    dayLabel = Label(itemEntry, text="Day:").grid(row=3, column=0)
    day = Entry(itemEntry)
    day.grid(row=3, column=1)
    yearLabel = Label(itemEntry, text="Year:").grid(row=4, column=0)
    year = Entry(itemEntry)
    year.grid(row=4, column=1)
    hourLabel = Label(itemEntry, text="Hour:").grid(row=5, column=0)
    hour = Entry(itemEntry)
    hour.grid(row=5, column=1)
    minLabel = Label(itemEntry, text="Minute:").grid(row=6, column=0)
    minute = Entry(itemEntry)
    minute.grid(row=6, column=1) 
    # Button must be pushed after item is entered
    confirm = Button(itemEntry, text='Add Item', command=lambda: pushToList(e.get(), month.get(),
    day.get(), year.get(), hour.get(), minute.get())).grid(row=7, column=0)
    close = Button(itemEntry, text="Close", command=itemEntry.destroy).grid(row=7, column=1)

    
def loadTasks():
    df = pd.read_pickle('pickled.dat')
    if not df.empty:
        print("Not empty")
        
def saveTasks():
    df = pd.DataFrame(columns=['task', 'month', 'day', 'year', 'hour', 'minute'])
    
    for i in checklist:
        df = df.append([{'task': i.textStr, 'month': i.dateTime.month, 'day': i.dateTime.day, 'year': i.dateTime.year,
                         'hour': i.dateTime.hour, 'minute': i.dateTime.minute}])
    
    df.to_pickle('pickled.dat')


loadTasks()

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

saveTasks()
